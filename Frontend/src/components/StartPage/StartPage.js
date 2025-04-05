import React, { useState } from "react";
import { useSearchParams, useNavigate } from "react-router-dom";
import { FaBook, FaCompass } from "react-icons/fa";
import logo from "../../assets/logo.png";
import "./StartPage.css";

function OptionCard({ title, description, icon, isSelected, onClick }) {
  return (
    <button onClick={onClick} className={`option ${isSelected ? "selected" : ""}`}>
      <span className="option-icon">{icon}</span>
      <div className="option-text">
        <h3>{title}</h3>
        <p>{description}</p>
      </div>
    </button>
  );
}

function StartPage() {
  const [selected, setSelected] = useState(null);
  const [searchParams] = useSearchParams();
  const selectedCourse = searchParams.get("course");
  const navigate = useNavigate();

  const handleContinue = () => {
    if (!selected) {
      alert("Please select an option!");
      return;
    }

    if (selected === "start") {
      navigate(`/lesson?course=${selectedCourse}&level=Beginner`);
    } else if (selected === "find") {
      navigate(`/quiz?course=${selectedCourse}`);
    }
  };

  return (
    <div className="container">
      <img src={logo} alt="Vlearn" className="mascot" />
      <h2>Now let’s find the best place to start for {selectedCourse}!</h2>

      <OptionCard
        title="Start from scratch"
        description="Take the easiest lesson of the course"
        icon={<FaBook />}
        isSelected={selected === "start"}
        onClick={() => setSelected("start")}
      />

      <OptionCard
        title="Find my level"
        description="Let us recommend where you should start learning"
        icon={<FaCompass />}
        isSelected={selected === "find"}
        onClick={() => setSelected("find")}
      />

      <button className="continue-btn" onClick={handleContinue}>CONTINUE</button>
    </div>
  );
}

export default StartPage;
