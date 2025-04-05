from transformers import T5Tokenizer, T5ForConditionalGeneration

# Load the model and tokenizer from the Hub
model = T5ForConditionalGeneration.from_pretrained("jerwinTitus/t5_mcq_model")
tokenizer = T5Tokenizer.from_pretrained("jerwinTitus/t5_mcq_model")

# Prepare your input
input_text = "generate mcq: Your input text here"
inputs = tokenizer(input_text, return_tensors="pt", max_length=512, truncation=True)

# Generate MCQ
model.eval()  # Set the model to evaluation mode
outputs = model.generate(**inputs, max_length=256)
generated_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
print(generated_text)
