from transformers import AutoModelForCausalLM, AutoTokenizer

# Load the pre-trained Mistral-7B model and its tokenizer
MODEL_NAME = "mistralai/Mistral-7B-v0.1"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)

def generate_response(prompt):
    """Generates a text response given an input prompt using Mistral-7B."""
    inputs = tokenizer(prompt, return_tensors="pt")  # Convert text to tokenized tensor
    outputs = model.generate(**inputs, max_new_tokens=100)  # Generate response
    return tokenizer.decode(outputs[0], skip_special_tokens=True)  # Convert tokens to text

if __name__ == "__main__":
    prompt = "Describe the eligibility criteria for a clinical trial on diabetes."
    print(generate_response(prompt))