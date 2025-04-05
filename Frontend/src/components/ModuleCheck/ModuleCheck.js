import React from "react";
import { useLocation, useNavigate } from "react-router-dom";

function ModuleCheck() {
  const location = useLocation();
  const navigate = useNavigate();
  const { course, level, moduleIndex } = location.state || {};

  const handlePass = () => {
    navigate("/lesson", {
      state: {
        course,
        level,
        moduleIndex: moduleIndex + 1,
      },
    });
  };

  return (
    <div className="quiz-card">
      <h2>Quiz for Module {moduleIndex + 1}</h2>
      <p><strong>Course:</strong> {course}</p>
      <p><strong>Level:</strong> {level}</p>
      <p><strong>Question:</strong> Is this course awesome? 😄</p>
      <button onClick={handlePass}>Yes, pass me!</button>
    </div>
  );
}

export default ModuleCheck;
