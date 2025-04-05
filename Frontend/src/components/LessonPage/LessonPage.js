import React, { useState, useEffect, useMemo } from "react";
import { useSearchParams, useNavigate, useLocation } from "react-router-dom";
import "./LessonPage.css";

function LessonPage() {
  const [searchParams] = useSearchParams();
  const location = useLocation();
  const navigate = useNavigate();

  const course = location.state?.course || searchParams.get("course") || "Unknown Course";
  const level = location.state?.level || searchParams.get("level") || "Unknown Level";
  const initialIndex = location.state?.moduleIndex || 0;

  const [moduleIndex] = useState(initialIndex); // Removed unused setModuleIndex
  const [content, setContent] = useState("Loading content...");

  const modulePaths = useMemo(() => {
    const courseLower = course.toLowerCase();
    const levelLower = level.toLowerCase();

    if (courseLower === "java") {
      if (levelLower === "beginner") {
        return [
          "/courses/Basic_java_course_Module 1.txt",
          "/courses/Basic_java_course_Module 2.txt",
          "/courses/Basic_java_course_Module 3.txt",
          "/courses/Basic_java_course_Module 4.txt",
          "/courses/Basic_java_course_Module 5.txt",
          "/courses/Basic_java_course_Module 6.txt",
        ];
      } else if (levelLower === "intermediate") {
        return [
          "/courses/intermediate_java_course_Module 1.txt",
          "/courses/intermediate_java_course_Module 2.txt",
          "/courses/intermediate_java_course_Module 3.txt",
          "/courses/intermediate_java_course_Module 4.txt",
          "/courses/intermediate_java_course_Module 5.txt",
          "/courses/intermediate_java_course_Module 6.txt",
        ];
      } else if (levelLower === "advanced") {
        return [
          "/courses/advanced_java_course_Module1.txt",
          "/courses/advanced_java_course_Module2.txt",
          "/courses/advanced_java_course_Module3.txt",
          "/courses/advanced_java_course_Module4.txt",
          "/courses/advanced_java_course_Module5.txt",
          "/courses/advanced_java_course_Module6.txt",
        ];
      }
    } else if (courseLower === "python") {
      if (levelLower === "beginner") {
        return ["/courses/Basic_python_course.txt"];
      } else if (levelLower === "intermediate") {
        return ["/courses/intermediate_python_course.txt"];
      } else if (levelLower === "advanced") {
        return ["/courses/advanced_python_course.txt"];
      }
    }

    return [];
  }, [course, level]);

  useEffect(() => {
    if (modulePaths.length === 0 || moduleIndex >= modulePaths.length) {
      setContent("No more content or invalid course/level.");
      return;
    }

    const filePath = modulePaths[moduleIndex];
    fetch(process.env.PUBLIC_URL + filePath)
      .then((response) => {
        if (!response.ok) throw new Error(`HTTP error! Status: ${response.status}`);
        return response.text();
      })
      .then((data) => {
        setContent(data);
      })
      .catch((error) => {
        console.error("Error loading course content:", error);
        setContent("Error loading content. Please try again later.");
      });
  }, [moduleIndex, modulePaths]); // ✅ Include memoized modulePaths

  const handleNext = () => {
    navigate("/module-check", {
      state: {
        course,
        level,
        moduleIndex,
      },
    });
  };

  return (
    <div className="course-container">
      <h1>Welcome to {course} Course</h1>
      <h2>Level: {level}</h2>
      <p>This is your starting point. Let's get learning! 🚀</p>

      {moduleIndex < modulePaths.length && (
        <div className="lesson-card">
          <h3>Lesson {moduleIndex + 1}: Module {moduleIndex + 1}</h3>
          <p>Start learning the basics of {course} at the {level} level.</p>
          <pre className="lesson-content">{content}</pre>
          <button onClick={handleNext}>Take Quiz</button>
        </div>
      )}

      {moduleIndex >= modulePaths.length && (
        <div className="completion-message">
          <h2>🎉 Congratulations! You've completed all modules.</h2>
        </div>
      )}
    </div>
  );
}

export default LessonPage;
