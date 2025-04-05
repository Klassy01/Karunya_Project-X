import React, { useEffect, useState } from "react";
import { useSearchParams, useNavigate } from "react-router-dom";
import axios from "axios";
import "./QuizPage.css";

function QuizPage() {
  const [searchParams] = useSearchParams();
  const navigate = useNavigate();

  const [selectedCourse] = useState(searchParams.get("course") || "Java");
  const [questions, setQuestions] = useState([]);
  const [selectedAnswers, setSelectedAnswers] = useState({});
  const [loading, setLoading] = useState(true);
  const [score, setScore] = useState(null);
  const [category, setCategory] = useState("");
  const [grade, setGrade] = useState("");

  // Fetch quiz questions when component mounts
  useEffect(() => {
    setLoading(true);
    axios
      .post("http://localhost:5001/generate-mcq", { course: selectedCourse })
      .then((response) => {
        setQuestions(response.data.questions);
        setLoading(false);
      })
      .catch((error) => {
        console.error("Error fetching questions:", error);
        setLoading(false);
      });
  }, [selectedCourse]);

  // Handle answer selection
  const handleAnswerSelect = (questionIndex, selectedOption) => {
    setSelectedAnswers({ ...selectedAnswers, [questionIndex]: selectedOption });
  };

  // Handle submit
  const handleSubmit = () => {
    let correctCount = 0;
    questions.forEach((question, index) => {
      if (selectedAnswers[index] === question.correct) correctCount += 1;
    });

    setScore(correctCount);

    const level =
      correctCount <= 4
        ? "Beginner"
        : correctCount <= 7
        ? "Intermediate"
        : "Advanced";

    setCategory(level);

    // Set grade based on performance
    const gradeCalc = (score) => {
      if (score === questions.length) return "A+";
      if (score >= questions.length * 0.8) return "A";
      if (score >= questions.length * 0.6) return "B";
      if (score >= questions.length * 0.4) return "C";
      return "D";
    };

    const finalGrade = gradeCalc(correctCount);
    setGrade(finalGrade);

    // Redirect after 3 seconds
    setTimeout(() => {
      navigate(`/lesson?course=${selectedCourse}&level=${level}`);
    }, 3000);
  };

  return (
    <div className="quiz-container">
      <h2>Quiz for {selectedCourse}</h2>

      {loading ? (
        <p className="loading-text">Loading questions...</p>
      ) : (
        <div>
          {questions.map((question, index) => (
            <div key={index} className="question-card">
              <p>
                {index + 1}. {question.text}
              </p>
              {question.options.map((option) => (
                <label key={option} className="option-label">
                  <input
                    type="radio"
                    name={`question-${index}`}
                    value={option}
                    checked={selectedAnswers[index] === option}
                    onChange={() => handleAnswerSelect(index, option)}
                  />
                  {option}
                </label>
              ))}
            </div>
          ))}

          <button onClick={handleSubmit} className="submit-button">
            Submit Quiz
          </button>

          {score !== null && (
            <div className="score-section">
              <h3>Your Score: {score} / {questions.length}</h3>
              <p className={`category ${category.toLowerCase()}`}>
                Skill Level: {category}
              </p>
              <p className="grade">🎓 Grade: <strong>{grade}</strong></p>
              <p>Redirecting you to the {category} course in 3 seconds...</p>
            </div>
          )}
        </div>
      )}
    </div>
  );
}

export default QuizPage;
