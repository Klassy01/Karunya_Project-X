from transformers import T5Tokenizer, T5ForConditionalGeneration, Trainer, TrainingArguments
from datasets import Dataset
import json

# === Load dataset ===
with open("mcq_dataset_2000.json", "r") as f:
    data = json.load(f)

# === Preprocess data ===
def format_example(item):
    options = item["options"]
    option_labels = ['A', 'B', 'C', 'D']
    formatted_options = "\n".join([f"{label}) {opt}" for label, opt in zip(option_labels, options)])
    correct_index = options.index(item["answer"])
    correct_label = option_labels[correct_index]

    input_text = f"generate mcq: {item['text']}"
    target_text = f"Q: {item['question']}\n{formatted_options}\nAnswer: {correct_label}"

    return {"input_text": input_text, "target_text": target_text}

dataset = [format_example(item) for item in data]
dataset = Dataset.from_list(dataset)

# === Train/test split ===
dataset = dataset.train_test_split(test_size=0.2)
train_data = dataset["train"]
test_data = dataset["test"]

# === Load tokenizer and model ===
model_name = "t5-small"
tokenizer = T5Tokenizer.from_pretrained(model_name)
model = T5ForConditionalGeneration.from_pretrained(model_name)

# === Tokenize ===
def tokenize(example):
    model_inputs = tokenizer(example["input_text"], max_length=512, truncation=True, padding="max_length")
    labels = tokenizer(example["target_text"], max_length=256, truncation=True, padding="max_length")
    model_inputs["labels"] = labels["input_ids"]
    return model_inputs

train_data = train_data.map(tokenize, batched=True, remove_columns=["input_text", "target_text"])
test_data = test_data.map(tokenize, batched=True, remove_columns=["input_text", "target_text"])

# === Training arguments ===
training_args = TrainingArguments(
    output_dir="./t5_mcq_model",
    evaluation_strategy="epoch",
    save_strategy="epoch",
    num_train_epochs=3,
    per_device_train_batch_size=4,
    per_device_eval_batch_size=4,
    logging_dir="./logs",
    weight_decay=0.01,
    logging_steps=10,
    save_total_limit=2
)

# === Trainer ===
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=train_data,
    eval_dataset=test_data,
    tokenizer=tokenizer
)

# === Train ===
trainer.train()

# === Save model and tokenizer ===
model.save_pretrained("./t5_mcq_model")
tokenizer.save_pretrained("./t5_mcq_model")