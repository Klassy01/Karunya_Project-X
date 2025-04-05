import React from "react";
import "./Navbar.css";
import logo from "../../assets/logo.png";

const Navbar = ({ setIsOpen }) => {
  return (
    <nav className="navbar">
      <div className="left-section">
        <button className="menu-btn" onClick={() => setIsOpen(true)}>
          ☰
        </button>
        <img src={logo} alt="V Learn Logo" className="logo" />
      </div>
      <h1 className="nav-title">V Learn</h1>
    </nav>
  );
};

export default Navbar;
