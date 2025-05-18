from transformers import pipeline

classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)

def detect_bias(text: str):
    labels = ["neutral", "slightly biased", "strongly biased"]
    return classifier(text, labels)


# This function uses the Hugging Face Transformers library to create a zero-shot classification
# pipeline with the BART model. The detect_bias function takes a text input and classifies it 
# into one of three labels: "neutral", "slightly biased", or "strongly biased". The function
# returns the classification result, which includes the labels and their corresponding scores.