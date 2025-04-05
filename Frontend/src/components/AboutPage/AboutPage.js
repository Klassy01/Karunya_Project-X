import "./AboutPage.css";
import logo from "../../assets/logo.png"; 

function AboutPage() {
  return (
    <div className="about-container">
      <div className="about-content">
        <img src={logo} alt="Company Logo" className="about-logo" />
        <h1>About Our Learning Platform</h1>
        <p>
          <strong>VLearn</strong> – The name <strong>VLearn</strong> represents the idea that "<strong>V Learn – We Learn</strong>",  
          emphasizing "collaborative learning" where knowledge is shared and cultivated together.  
          Additionally, <strong>VLearn</strong> symbolizes "Virtual Learning", embracing technology  
          to provide seamless, interactive, and accessible education for all.
        </p>
        <p>
          Welcome to <strong>VLearn</strong>, where education meets innovation! 
          Our platform is designed to revolutionize the way you learn, offering 
          interactive courses in various domains like Programming, AI, Data Science, 
          and more.
        </p>
        <p>
          At VLearn, we believe in "personalized, adaptive learning experiences". 
          Our AI-powered tutor helps you understand complex concepts through 
          "interactive quizzes, hands-on projects, and real-world examples".
        </p>
        <p>
          Whether you’re a beginner or an advanced learner, VLearn offers a structured 
          pathway to success. Join thousands of learners and master new skills at your own pace!
        </p>
      </div>
    </div>
  );
}

export default AboutPage;
