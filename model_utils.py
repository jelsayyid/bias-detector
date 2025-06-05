from transformers import pipeline


_classifier = None


def _get_classifier():
    """Lazily create and return the zero-shot classification pipeline."""
    global _classifier
    if _classifier is None:
        _classifier = pipeline(
            "zero-shot-classification",
            model="facebook/bart-large-mnli",
        )
    return _classifier


def detect_bias(text: str):
    """Classify the given text into bias categories."""
    labels = ["neutral", "slightly biased", "strongly biased"]
    classifier = _get_classifier()
    return classifier(text, labels)


# This function uses the Hugging Face Transformers library to create a zero-shot classification
# pipeline with the BART model. The detect_bias function takes a text input and classifies it 
# into one of three labels: "neutral", "slightly biased", or "strongly biased". The function
# returns the classification result, which includes the labels and their corresponding scores.