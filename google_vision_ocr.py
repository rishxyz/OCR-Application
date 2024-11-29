from google.cloud import vision
import io
from text_cleaner import clean_and_format_text
from utils import calculate_average_confidence, calculate_proxy_confidence, draw_bounding_boxes

def detect_text_google(image_path):
    """
    Detect text in an image using Google Cloud Vision API.
    """
    client = vision.ImageAnnotatorClient()

    try:
        with io.open(image_path, 'rb') as image_file:
            content = image_file.read()

        image = vision.Image(content=content)
        response = client.text_detection(image=image)

        if response.error.message:
            raise Exception(f"Google Vision API Error: {response.error.message}")

        # Filter annotations with valid descriptions
        text_annotations = response.text_annotations
        if not text_annotations:
            print("No text annotations found.")
            return []

        return [annotation for annotation in text_annotations if annotation.description]

    except Exception as e:
        print(f"Error during text detection: {e}")
        return []


def process_image_with_google_vision(image_path, output_dir):
   
    print("Processing image with Google Cloud Vision...")
    detected_text = detect_text_google(image_path)

    if detected_text:
        # Filter annotations and handle None descriptions safely
        valid_annotations = [annotation for annotation in detected_text if annotation.description]

        if not valid_annotations:
            print("No valid text annotations found.")
            return "", 0.0, None

        # DEBUG: Log valid annotations
        print(f"Valid annotations count: {len(valid_annotations)}")

        # Extract raw text safely
        raw_text = " ".join(str(annotation.description) for annotation in valid_annotations if annotation.description)
        print("\nRaw Extracted Text:")
        print(f"{raw_text}\n(Type: {type(raw_text)})")

        # Clean and format text
        try:
            cleaned_text = clean_and_format_text(raw_text)
        except Exception as e:
            raise ValueError(f"Error in text cleaning: {e}")

        print("\nCleaned and Formatted Text:")
        print(f"{cleaned_text}\n(Type: {type(cleaned_text)})")

        # Calculate confidence score
        try:
            if hasattr(valid_annotations[0], "confidence") and valid_annotations[0].confidence > 0:
                confidence_score = calculate_average_confidence(valid_annotations)
            else:
                confidence_score = calculate_proxy_confidence(raw_text)
        except Exception as e:
            raise ValueError(f"Error in confidence calculation: {e}")

        print(f"\nConfidence Score: {confidence_score:.2f}%")

        # Draw bounding boxes and save the annotated image
        try:
            annotated_image_path = draw_bounding_boxes(image_path, valid_annotations, output_dir)
        except Exception as e:
            raise ValueError(f"Error in bounding box generation: {e}")

        print(f"Annotated image saved as '{annotated_image_path}'")
        return cleaned_text, confidence_score, annotated_image_path

    else:
        print("No text detected.")
        return "", 0.0, None