# Handwritten OCR Analyzer

The **Handwritten OCR Analyzer** is a web-based application that uses Google Vision API to analyze and clean handwritten text. The application offers features such as confidence scoring for text recognition and text cleaning for better usability.

---

## Live Demo

👉 [Try the App Here](https://ocr-application-7rbymnbumoadzbksmu4wes.streamlit.app/)

---

## Features

- **Text Extraction**: Extract handwritten text using Google Vision API.
- **Text Cleaning**: Automatically clean and format the extracted text.
- **Confidence Scoring**: Calculate API confidence or proxy confidence scores.
- **User-Friendly Interface**: Upload images and analyze them instantly.
- **Download Options**: Save cleaned text and confidence score for further use.

---

## Steps to Build the Application

### 1. **Setup the Development Environment**

#### Prerequisites
- **Python 3.7 or later** installed.
- A Google Cloud account with **Vision API** enabled.
- **Streamlit** for creating the web application.

#### Instructions

1. Clone the repository:
   ```bash
   git clone https://github.com/rishxyz/OCR-Application.git
   cd ocr-application
2. Create a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Windows, use: venv\Scripts\activate
3. Install the dependencies:   
    ```bash
    pip install -r requirements.txt
4. 	Obtain your Google Cloud Vision API Key:
	-	Log in to the Google Cloud Console.
	-	Create a new service account under your project.
	-	Assign the necessary roles (e.g., Vision API Admin).
	-	Download the JSON key file.
5.	Set up Streamlit Secrets to securely store your API key:
	-	Create a secrets.toml file in the root directory with the following structure:
    ```bash
    [google_cloud_service_key]
    type = "service_account"
    project_id = "your_project_id"
    private_key_id = "your_private_key_id"
    private_key = "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n"
    client_email = "your_client_email"
    client_id = "your_client_id"
    auth_uri = "https://accounts.google.com/o/oauth2/auth"
    token_uri = "https://oauth2.googleapis.com/token"
    auth_provider_x509_cert_url = "https://www.googleapis.com/oauth2/v1/certs"
    client_x509_cert_url = "your_client_x509_cert_url"

    
### 2. **Run the Application Locally**
1.  Activate your virtual environment:
    ```bash 
    source venv/bin/activate  # For Windows: venv\Scripts\activate
2. Run the Streamlit application:
    ```bash
    streamlit run app.py
3. 	Open the application in your browser:
    -	Local URL: http://localhost:8501



### 3. **Deployment on Streamlit Cloud**
Steps for Deployment:

1.	Push your code to a public GitHub repository.
2.	Add the repository to your Streamlit Cloud workspace:
	-	Log in to Streamlit Cloud.
	-	Create a new app and link it to your GitHub repository.
3.	Configure Secrets:
	-	Go to the “Secrets” tab in the Streamlit Cloud app settings.
	-	Add your google_cloud_service_key in the same TOML format as above.
4.	Deploy the app and use the provided URL.

---



### **Known Issues and Troubleshooting**


1.	Error: Invalid API Key
	-	Ensure your secrets.toml file or Streamlit Cloud secrets are correctly configured.
	-	Verify that the Google Cloud Vision API is enabled in your project.
2.	Image Upload Issues
	-	Only .png, .jpg, and .jpeg files are supported.
	-	Check the image size; overly large images might fail to process.
3.	Low Confidence Scores
	-	Use higher-quality images for better recognition.
	-	Ensure the text is not obstructed or overly stylized.

---
## **Future Improvements

-	Add support for multiple languages in OCR processing.
-  Enhance confidence scoring using AI-based post-processing.
-	Improve UI design for better user experience.


---
## License

This project is licensed under the MIT License.

---
## Contact

For questions or feedback, please contact:
-	Name: Rishika Chowdary
-   Email: rishikachowdary.alla@unh.edu
- 	GitHub: rishxyz






