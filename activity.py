from transformers import pipeline

def classify_text_offline(text):
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)
    return result

if __name__ == "__main__":
    sample_text = "I love using Hugging Face APIs!"
    result = classify_text_offline(sample_text)
    print("Result:", result)
