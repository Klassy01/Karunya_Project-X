import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import HomePage from "./components/HomePage/HomePage";
import CoursePage from "./components/CoursePage/CoursePage";
import StartPage from "./components/StartPage/StartPage";
import QuizPage from "./components/QuizPage/QuizPage";
import AboutPage from "./components/AboutPage/AboutPage";
import ContactPage from "./components/ContactPage/ContactPage";
import LessonPage from "./components/LessonPage/LessonPage";
import ModuleCheck from "./components/ModuleCheck/ModuleCheck"; 
import Sidebar from "./components/Sidebar/Sidebar";
import Navbar from "./components/Navbar/Navbar";
import Chatbot from "./components/Chatbot/chatbot";
import "./App.css";

function App() {
  return (
    <Router>
      <div className="app-container">
        <Routes>
          <Route path="/" element={<Layout showChatbot={true}><HomePage /></Layout>} />
          <Route path="/courses" element={<Layout showChatbot={true}><CoursePage /></Layout>} />
          <Route path="/start" element={<Layout showChatbot={true}><StartPage /></Layout>} />
          <Route path="/quiz" element={<NoLayout><QuizPage /></NoLayout>} />
          <Route path="/about" element={<Layout showChatbot={true}><AboutPage /></Layout>} />
          <Route path="/contact" element={<Layout showChatbot={true}><ContactPage /></Layout>} />
          <Route path="/lesson" element={<Layout showChatbot={true}><LessonPage /></Layout>} />
          <Route path="/module-check" element={<NoLayout><ModuleCheck /></NoLayout>} /> {/* ✅ NEW ROUTE */}
        </Routes>
      </div>
    </Router>
  );
}

// Layout Component (Includes Navbar, Sidebar, and optionally Chatbot)
function Layout({ children, showChatbot }) {
  return (
    <div className="main-layout">
      <Navbar />
      <Sidebar />
      <div className="page-content">{children}</div>
      {showChatbot && <Chatbot />}
    </div>
  );
}

// NoLayout Component (For Pages Without Navbar, Sidebar, and Chatbot)
function NoLayout({ children }) {
  return <div className="no-layout">{children}</div>;
}

export default App;
