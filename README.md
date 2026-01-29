# GenAI-Powered Job Recommender System

This project is an AI-powered job recommender system that helps users find relevant job opportunities based on their resume. The application analyzes the user's resume, provides a summary of their skills and experience, identifies skill gaps, suggests a career roadmap, and fetches job listings from LinkedIn and Naukri.

## Features

-   **Resume Analysis:** Extracts text from a PDF resume and provides a comprehensive analysis.
-   **AI-Powered Insights:** Uses a Large Language Model (LLM) to:
    -   Summarize the resume.
    -   Identify skill gaps and areas for improvement.
    -   Generate a career roadmap with suggestions for skills to learn and certifications to obtain.
-   **Job Recommendations:** Fetches job listings from LinkedIn and Naukri based on the user's profile.
-   **Web Interface:** A user-friendly web interface built with Streamlit.

## How it Works

1.  **Resume Upload:** The user uploads their resume in PDF format through the Streamlit web interface.
2.  **Text Extraction:** The application extracts the text from the PDF using PyMuPDF.
3.  **AI Analysis:** The extracted text is sent to the Groq API (using a Llama 3.3 70B model) to generate a resume summary, identify skill gaps, and create a career roadmap. The LLM is also used to extract relevant keywords for a job search.
4.  **Job Scraping:** The application uses the Apify API to search for jobs on LinkedIn and Naukri using the keywords extracted in the previous step.
5.  **Display Results:** The resume analysis and job recommendations are displayed to the user.

## Technologies Used

-   **Frontend:** [Streamlit](https://streamlit.io/)
-   **Backend:** [Python](https://www.python.org/)
-   **AI/LLM:** [Groq API](https://groq.com/) (Llama 3.3 70B model)
-   **Job Scraping:** [Apify API](https://apify.com/)
-   **PDF Processing:** [PyMuPDF](https://pymupdf.readthedocs.io/)
-   **Configuration:** [python-dotenv](https://pypi.org/project/python-dotenv/)

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/GenAI-Powered-Job-Recommender-System.git
    cd GenAI-Powered-Job-Recommender-System
    ```

2.  **Create a virtual environment and activate it:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows, use `.venv\Scripts\activate`
    ```

3.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Configuration

This project requires API keys for Groq and Apify.

1.  Create a `.env` file in the root of the project.
2.  Add your API keys to the `.env` file as follows:

    ```
    GROQ_API_KEY="your-groq-api-key"
    APIFY_API_TOKEN="your-apify-api-token"
    ```

3.  Replace `"your-groq-api-key"` and `"your-apify-api-token"` with your actual API keys.

## Usage

1.  Make sure your virtual environment is activated.
2.  Run the Streamlit application:

    ```bash
    streamlit run app.py
    ```

3.  Open your web browser and navigate to the URL provided by Streamlit (usually `http://localhost:8501`).
4.  Upload your resume and get your job recommendations!
