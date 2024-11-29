import streamlit as st
from google_vision_ocr import process_image_with_google_vision
from text_cleaner import clean_and_format_text
import os

# Constants
OUTPUT_DIR = "assets/outputs/"


# Configure Google Vision API credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = st.secrets["google_cloud_service_key"]

# Configure Streamlit app
st.set_page_config(page_title="📝 Handwritten OCR Analyzer", layout="wide", initial_sidebar_state="expanded")

# Header
st.title("📝 Handwritten Text Analysis with Google Vision")
st.markdown("Analyze, clean, and evaluate handwritten text using Google Vision API.")

# Sidebar
st.sidebar.title("📂 Upload Image")
uploaded_file = st.sidebar.file_uploader("Upload a handwriting image", type=["png", "jpg", "jpeg"])

# Ensure output directory exists
os.makedirs(OUTPUT_DIR, exist_ok=True)

# Initialize session state to persist data
if "extracted_text" not in st.session_state:
    st.session_state.extracted_text = None
if "cleaned_text" not in st.session_state:
    st.session_state.cleaned_text = None
if "confidence_score" not in st.session_state:
    st.session_state.confidence_score = None

# Process uploaded image
if uploaded_file:
    # Save uploaded file locally
    image_path = os.path.join(OUTPUT_DIR, uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    # Display uploaded image
    st.image(image_path, caption="Uploaded Image", use_container_width=True)

if st.button("Analyze Text"):
    with st.spinner("🔍 Analyzing handwriting..."):
        try:
            # Perform OCR with Google Vision
            extracted_text, confidence_score, _ = process_image_with_google_vision(image_path, OUTPUT_DIR)

            # Check if text was extracted
            if not extracted_text.strip():
                st.warning("⚠️ No text detected. Try uploading a clearer image.")
                st.stop  # Correctly placed inside the block

            # Clean and format the extracted text
            cleaned_text = clean_and_format_text(extracted_text)

            # Save results in session state
            st.session_state.extracted_text = extracted_text
            st.session_state.cleaned_text = cleaned_text
            st.session_state.confidence_score = confidence_score

            # Feedback
            st.success("✅ Processing Completed!")

        except FileNotFoundError:
            st.error("❌ Uploaded file could not be found. Please try again.")
        except Exception as e:
            st.error(f"❌ An error occurred: {e}")

# Display results
if st.session_state.cleaned_text:
    # Extracted and cleaned text
    st.subheader("📋 Extracted and Cleaned Text")
    st.text_area("Cleaned Text", st.session_state.cleaned_text, height=300)

    # Confidence score
    st.subheader("📊 Confidence Score")
    st.metric("Confidence Score", f"{st.session_state.confidence_score:.2f}%")

    # Download buttons
    st.download_button(
        label="📥 Download Cleaned Text",
        data=st.session_state.cleaned_text,
        file_name="cleaned_text.txt",
        mime="text/plain",
    )
    st.download_button(
        label="📥 Download Confidence Score",
        data=f"Confidence Score: {st.session_state.confidence_score:.2f}%",
        file_name="confidence_score.txt",
        mime="text/plain",
    )

# Instructions for new users
if not uploaded_file:
    st.info("📂 Upload a handwriting image to start the analysis.")

# Footer
st.markdown(
    """
    ---
    ### ℹ️ Note:
    - This tool uses Google Vision OCR for handwriting analysis.
    - When API confidence values are missing, a proxy confidence score is calculated.
    - Ensure valid API credentials are configured for the Google Vision service.
    """
)