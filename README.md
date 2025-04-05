# Karunya_Project-X

# AI Powered Personal Tutor (vLearn)

## Overview
vLearn is an AI-powered personal tutor that leverages advanced machine learning techniques to deliver tailored learning experiences. The name "vLearn" stands for "Virtual Learning" and also reflects the concept of "We Learn" collaboratively. Our project, vLearn, adapts courses to each learner's capabilities by generating customized multiple-choice questions (MCQs) using our fine-tuned T5 model.

## Features
- **Personalized Learning:** Tailors MCQs to each learner’s strengths and weaknesses.
- **Adaptive Course Content:** Dynamically adjusts course material based on performance.
- **Collaborative Platform:** Encourages interaction and shared learning experiences.

## Tech Stack & Components

### Frontend
- **React.js**  
  Download: [React Official Website](https://reactjs.org/)

### Backend
- **Node.js**  
  Download: [Node.js Official Download](https://nodejs.org/en/download/)

### Database
- **MongoDB**  
  Download: [MongoDB Community Download](https://www.mongodb.com/try/download/community)

### Development Environment
- **Visual Studio Code**  
  Download: [Visual Studio Code](https://code.visualstudio.com/download)

### Model Training
- **Python Programming**  
  Download: [Python Downloads](https://www.python.org/downloads/)
- **T5 Model:** Fine-tuned on our custom dataset for generating MCQs.

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Klassy01/Karunya_Project-X.git
cd your-repo
```

### 2. Frontend Setup
- Navigate to the frontend directory:
  ```bash
  cd frontend
  ```
- Install dependencies:
  ```bash
  npm install
  ```
- Start the development server:
  ```bash
  npm start
  ```

### 3. Backend Setup
- Navigate to the backend directory:
  ```bash
  cd ../backend
  ```
- Install dependencies:
  ```bash
  npm install
  ```
- Start the server:
  ```bash
  node server.js
  ```

### 4. Database Setup
- Install MongoDB from the [MongoDB Community Download](https://www.mongodb.com/try/download/community) and follow the installation instructions.
- Update your backend configuration with the MongoDB connection string.

### 5. Model Training
- Install Python from the [Python Downloads](https://www.python.org/downloads/).
- Create a virtual environment and install required packages:
  ```bash
  python -m venv venv
  source venv/bin/activate  # For Windows: venv\Scripts\activate
  pip install -r requirements.txt
  ```
- Train the T5 model with your dataset:
  ```bash
  python train_model.py
  ```


# AI Powered Personal Tutor (vLearn) - Project Workflow

This document outlines the complete implementation steps and architecture of the **vLearn** project — an AI-powered personalized tutor system designed to deliver adaptive learning experiences based on a learner's performance.

---

## 1. Frontend Development

**Technologies Used:**  
- React.js  
- Node.js

### Steps:
- Designed the user interface using **React.js**, offering a smooth and interactive experience.
- Implemented features like course selection, assessments, and progress tracking.
- React components dynamically load content such as courses, quizzes, and module statuses.
- The frontend communicates with the backend via API calls for data fetch and submission.
- **Node.js** serves as the backend runtime environment to build APIs for course retrieval, MCQ generation, user management, etc.

---

## 2. Course Generation

**Source:**  
- Open-source educational materials and curated topic outlines.

### Steps:
- Collected information from reliable sources like GitHub repositories, MOOCs, and documentation.
- Structured the collected data into six primary modules for each subject.
- Each module contains 5–6 subtopics, making the content manageable and learner-friendly.
- Content was written in `.md` files for easy formatting, readability, and storage in MongoDB.

---

## 3. Dataset Generation (MCQs)

### Steps:
- Manually and programmatically generated MCQs based on the course content.
- Categorized the questions into three difficulty levels: **Basic**, **Intermediate**, and **Advanced**.
- Ensured a variety of question styles including factual, conceptual, and application-based.
- Saved the dataset in structured JSON format to be used for model fine-tuning.

---

## 4. Model Fine-Tuning (T5)

**Model Used:**  
- T5 (Text-to-Text Transfer Transformer)
- ollama model of Deepseek-r1:7b(For the personal chatbot)

### Steps:
1. Loaded the pre-trained T5 model using the `transformers` library from Hugging Face.
2. Preprocessed the MCQ dataset to match the T5 input-output format.
   - Input: Text passages or key points.
   - Output: MCQs in question-answer format.
3. Split the dataset into training and validation sets.
4. Used GPU-based training environment for faster fine-tuning.
5. Trained the model using a learning rate scheduler, early stopping, and evaluation metrics.
6. Saved the fine-tuned model for deployment.

---

## 5. Integration: Model + Frontend + Backend

**Database:** MongoDB  
**Tools:** Mongoose (for MongoDB), Express.js, REST APIs

### Steps:
- Deployed the model as a Flask or FastAPI service.
- Created API endpoints for MCQ generation based on course/module input.
- Frontend sends user data and course context to the backend.
- Backend forwards the request to the model and receives generated MCQs.
- MongoDB stores:
  - Course `.md` files
  - User progress and scores
  - Generated MCQs per user
- Used MongoDB Atlas (cloud-based cluster) for seamless integration and scalability.

---

## 6. Additional Features

### Chatbot Support
- Integrated **DeepSeek R1 7B** model using Ollama for natural language conversations.
- Used for:
  - Answering course-related doubts
  - Providing motivational and study tips
  - Guiding through the course content

### AI Assistant
- AI suggests personalized study plans based on learner's performance.
- Adaptive MCQs to improve weak areas identified by the system.

---

## 7. Future Scope

### a. Community Learning
- Integrate discussion forums or chat groups for learners to collaborate.
- Peer-to-peer help and shared resources.

### b. Video Lessons
- Add curated video lessons for each module.
- Improve comprehension with visual content.

### c. Adaptive Courses
- Use learner's quiz performance to dynamically alter course difficulty.
- Introduce personalized learning paths.

### d. Coding Tests and Interactive Games
- Include real-time coding environments for hands-on practice.
- Develop interactive quizzes and games to make learning fun and effective.

---

## 8. Model Optimization with OpenVINO IR

**Framework:** OpenVINO Toolkit (Intel)

### Purpose:
To optimize the performance of the fine-tuned T5 model for deployment on edge devices or in resource-constrained environments.

### Steps:
1. Converted the fine-tuned T5 model to **ONNX** format using `transformers` and `onnxruntime`.
2. Used **OpenVINO Model Optimizer** to convert the ONNX model to **Intermediate Representation (IR)** format.
   - IR includes `.xml` and `.bin` files representing the model structure and weights.
3. Deployed the model using **OpenVINO Inference Engine** for:
   - Faster inference speed
   - Lower latency
   - Efficient CPU usage
4. Integrated OpenVINO runtime into the backend service to serve optimized model predictions.

### Benefits:
- Enhanced performance on Intel hardware (CPUs, VPUs, integrated GPUs)
- Reduced model size and faster load times
- Cost-effective inference on low-resource machines

---

## Conclusion

The **vLearn** project offers a comprehensive, scalable, and intelligent solution for personalized education. With adaptive content, automated assessments, and chatbot assistance, it redefines how students learn and engage with educational material.


## Team
**Karunya_Project_x**

- Aparna J
- David Jayaraj A
- Jerwin Titus D

## For more info Contact
 Email - aparna6024@gmail.com
 Phone - +91 9176398947
