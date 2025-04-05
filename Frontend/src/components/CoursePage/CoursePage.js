import React from "react";
import { useNavigate } from "react-router-dom";
import "./CoursePage.css";
import pythonLogo from "../../assets/python.png"; 
import javaLogo from "../../assets/java.png";

const CoursePage = () => {
  const navigate = useNavigate();

  const handleCourseSelect = (course) => {
    navigate(`/start?course=${encodeURIComponent(course)}`);
  };

  const popularCourses = [
    { name: "Python", image: pythonLogo, desc: "Learn Python for AI & Data Science." },
    { name: "Java", image: javaLogo, desc: "Master Java for Software Development." },
  ];

  return (
    <div className="course-container">
      <h2 className="popular-title">🔥 Popular Courses</h2>
      <div className="popular-courses">
        {popularCourses.map((course) => (
          <div 
            key={course.name} 
            className="course-card" 
            onClick={() => handleCourseSelect(course.name)}
            role="button"
            tabIndex={0}
            onKeyPress={(e) => e.key === 'Enter' && handleCourseSelect(course.name)}
          >
            <img src={course.image} alt={`${course.name} course`} />
            <h3>{course.name}</h3>
            <p>{course.desc}</p>
          </div>
        ))}
      </div>
    </div>
  );
};

export default CoursePage;
