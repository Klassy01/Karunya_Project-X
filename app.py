import streamlit as st
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

# Load the fine-tuned model and tokenizer
model_name = "t5_mcq_model"  # Replace with your model's name or path
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

def generate_mcqs(input_text, num_questions=5):
    """
    Generate multiple-choice questions based on the input text.

    Args:
        input_text (str): The input text for MCQ generation.
        num_questions (int): Number of MCQs to generate.

    Returns:
        list: A list of generated MCQs.
    """
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
st.title("MCQ Generator")

# Text area for user input
input_text = st.text_area("Enter the text for MCQ generation:", height=200)

# Slider to select the number of MCQs to generate
num_questions = st.slider("Number of MCQs to generate:", min_value=1, max_value=10, value=5)

if st.button("Generate MCQs"):
    if input_text.strip():
        with st.spinner("Generating MCQs..."):
            mcqs = generate_mcqs(input_text, num_questions)
            for idx, mcq in enumerate(mcqs, 1):
                st.subheader(f"MCQ {idx}")
                st.write(mcq)
    else:
        st.warning("Please enter some text to generate MCQs.")

