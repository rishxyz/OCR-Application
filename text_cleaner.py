import re
from spellchecker import SpellChecker

def clean_and_format_text(raw_text):
    """
    Cleans and formats extracted text for improved readability.
    Handles generic text without relying on specific questions.
    """
    if not raw_text:  # Handle None or empty text
        return ""

    spell = SpellChecker()

    # Split the text safely, handling potential NoneType issues
    words = raw_text.split()
    
    # Correct typos and ensure words are valid strings
    corrected_words = [
        spell.correction(word) if word and word not in spell and word.isalpha() else word
        for word in words
    ]
    
    # Filter out None values in corrected_words
    corrected_words = [word if word else "" for word in corrected_words]

    # Rejoin words into a single text
    cleaned_text = " ".join(corrected_words)

    # Remove repeated words
    cleaned_text = re.sub(r'\b(\w+)( \1\b)+', r'\1', cleaned_text)


    cleaned_text = cleaned_text.replace("•", "\n•")
    cleaned_text = re.sub(r"(?<!\d)\. ", ".\n", cleaned_text)  # Avoid breaking decimal numbers like 9.8
    cleaned_text = re.sub(r"(?<!\w)([A-Z][a-z]+( [A-Z][a-z]+)*)", r"\n\1\n", cleaned_text)

    # Remove extra spaces
    cleaned_text = re.sub(r'\s+', ' ', cleaned_text).strip()
    return cleaned_text