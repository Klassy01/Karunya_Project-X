import React, { useState } from "react";
import Sidebar from "../Sidebar/Sidebar";
import Navbar from "../Navbar/Navbar";
import "./HomePage.css";

const HomePage = () => {
  const [isOpen, setIsOpen] = useState(false);

  return (
    <div className="homepage">
      {/* ✅ Navbar at the top */}
      <Navbar setIsOpen={setIsOpen} />

      {/* ✅ Sidebar (toggles correctly) */}
      <Sidebar isOpen={isOpen} setIsOpen={setIsOpen} />

      {/* ✅ Main Content */}
      <div className="content">
        <h1>Welcome to V Learn 🎓</h1>
        <p>Your personalized learning platform.</p>
      </div>
    </div>
  );
};

export default HomePage;
