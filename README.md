# T5-Based Multiple-Choice Question (MCQ) Generator

## Overview

This repository contains a fine-tuned [T5 (Text-to-Text Transfer Transformer)](https://huggingface.co/docs/transformers/model_doc/t5) model designed to generate multiple-choice questions (MCQs) from input text. The model is particularly useful for educators and content creators aiming to automate the creation of assessment items.

## Table of Contents

- [Model Details](#model-details)
  - [Model Description](#model-description)
  - [Model Sources](#model-sources)
- [Usage](#usage)
  - [Installation](#installation)
  - [Generating MCQs](#generating-mcqs)
- [Training Details](#training-details)
  - [Training Data](#training-data)
  - [Training Procedure](#training-procedure)
- [Evaluation](#evaluation)
  - [Testing Data](#testing-data)
  - [Metrics and Results](#metrics-and-results)
- [Limitations and Recommendations](#limitations-and-recommendations)
- [Environmental Impact](#environmental-impact)
- [Citation](#citation)
- [Contact](#contact)

## Model Details

### Model Description

The MCQ Generator is a fine-tuned version of the T5 model, adapted to transform input text into coherent and contextually relevant multiple-choice questions. This adaptation leverages the T5 architecture's text-to-text framework to facilitate educational content creation.

- **Developed by:** [Your Name or Organization]
- **Contact:** [Your Contact Information]
- **Model Type:** Text-to-Text Generation
- **Language:** English
- **License:** [Specify License, e.g., MIT, Apache 2.0]
- **Fine-tuned from:** [Base T5 Model Version, e.g., t5-base]

### Model Sources

- **Repository:** [Link to your model repository]
- **Paper (optional):** [Link to any related publication]
- **Demo (optional):** [Link to an interactive demo]

## Usage

### Installation

To utilize the MCQ Generator, install the necessary Python packages:

```bash
pip install torch transformers streamlit

###Generating MCQs
##Below is an example of how to use the model to generate MCQs:

```python
import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Load the tokenizer and model
model_name = "your-model-repository-id"  # Replace with your model's repository ID
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def generate_mcqs(input_text, num_questions=5):
    input_prompt = f"generate {num_questions} mcqs: {input_text}"
    inputs = tokenizer(input_prompt, return_tensors="pt", max_length=512, truncation=True)
    model.eval()
    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_length=512,
            num_return_sequences=num_questions,
            do_sample=True,
            top_k=50,
            top_p=0.95,
            temperature=0.8
        )
    questions = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]
    return questions

# Streamlit UI
st.title("Java Programming MCQ Generator")

# Sample input text for Java programming
sample_input = (
    "Java is a high-level, class-based, object-oriented programming language that is designed "
    "to have as few implementation dependencies as possible. It is intended to let application "
    "developers write once, run anywhere (WORA), meaning that compiled Java code can run on all "
    "platforms that support Java without the need for recompilation. Java applications are typically "
    "compiled to bytecode that can run on any Java virtual machine (JVM) regardless of the underlying "
    "computer architecture."
)

# Text area for user input
input_text = st.text_area("Enter the text for MCQ generation:", sample_input, height=200)

# Slider to select the number of MCQs to generate
num_questions = st.slider("Number of MCQs to generate:", min_value=1, max_value=10, value=5)

if st.button("Generate MCQs"):
    if input_text.strip():
        with st.spinner("Generating MCQs..."):
            mcqs = generate_mcqs(input_text, num_questions)
            for idx, mcq in enumerate(mcqs, 1):
                st.subheader(f"MCQ {idx}")
                lines = mcq.strip().split('\n')
                for line in lines:
                    if line.startswith("Question:"):
                        st.write(f"**{line}**")
                    elif line.startswith(("A.", "B.", "C.", "D.")):
                        st.write(line)
                    elif line.startswith("Answer:"):
                        st.success(line)
    else:
        st.warning("Please enter some text to generate MCQs.")
```python
## Training Details

### Training Data

The model was fine-tuned on a dataset comprising educational texts and corresponding multiple-choice questions across various subjects, ensuring a broad understanding of different topics.

### Training Procedure

The fine-tuning process involved:

- **Preprocessing:** Formatting input texts with prompts indicating MCQ generation tasks.

- **Hyperparameters:**
  - **Batch size:** [Specify batch size]
  - **Learning rate:** [Specify learning rate]
  - **Number of epochs:** [Specify number of epochs]

- **Optimization:** Utilized [Optimizer Name, e.g., AdamW] with appropriate learning rate scheduling.

## Evaluation

### Testing Data

The model was evaluated using a separate dataset containing educational texts and expert-crafted MCQs to assess its performance.

### Metrics and Results

Evaluation metrics included:

- **BLEU Score:** [Insert score]
- **ROUGE Score:** [Insert score]
- **Human Evaluation:** [Summarize findings, e.g., "80% of generated questions were deemed appropriate by experts."]

## Limitations and Recommendations

While the model aims to generate relevant MCQs, users should be aware of potential biases and limitations:

- **Biases:** Outputs may reflect biases present in the training data. It's essential to review generated questions for cultural, gender, or other biases.

- **Accuracy:** The model may occasionally produce questions that are ambiguous or not entirely aligned with the input text.

- **Context Limitation:** The model's understanding is based solely on the provided input text and does not incorporate external knowledge beyond its training data.

**Recommendations:**

- Manually review and edit generated MCQs to ensure clarity and relevance.

- Be cautious of potential biases and strive to create inclusive and fair assessment items.

- Test the model's outputs across diverse topics to gauge its performance and limitations.

## Drive Link For Model
https://drive.google.com/file/d/1lU0FfmVBCMJcf-_r4uJNB1EoTCQc9OqG/view?usp=drive_link
