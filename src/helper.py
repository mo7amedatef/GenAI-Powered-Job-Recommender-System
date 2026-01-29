import os
import fitz # PyMuPDF
from openai import OpenAI



from dotenv import load_dotenv
load_dotenv()


GROQ_API_KEY = os.getenv("GROQ_API_KEY")
client = OpenAI(
    # api_key=OPENAI_API_KEY
    api_key=GROQ_API_KEY
)


def extract_text_from_pdf(uploaded_file):
    """
    Extracts text from a PDF file.
    
    Args:
        uploaded_file (str): The path to the PDF file.
        
    Returns:
        str: The extracted text.
    """
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text



def ask_openai(prompt, max_tokens=500):
    """
    Sends a prompt to the Groq API (Free Tier) and returns the response.
    Args:
        prompt (str): The prompt to send to the OpenAI API.
        model (str): The model to use for the request.
        temperature (float): The temperature for the response.
        
    Returns:
        str: The response from the OpenAI API.
    """
    response = client.chat.completions.create(
        # model= "gpt-4o",
        # Llama 3.3 70B is currently one of the most powerful free models on Groq
        model="llama-3.3-70b-versatile", 
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.5,
        max_tokens=max_tokens
    )

    return response.choices[0].message.content