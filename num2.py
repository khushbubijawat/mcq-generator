import streamlit as st
import google.generativeai as genai
import base64

# Set your Google API key directly in the script
API_KEY = "AIzaSyAdHm4Xvp2n6-nV_Yx9lf3EHpdKPFcE3to"

# Configure the Gen AI SDK
genai.configure(api_key=API_KEY)

# Initialize Gemini Pro model
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

# Function to get Gemini response


def get_gemini_response(question, num_questions, difficulty):
    question_prompt = f"{question} mcq {difficulty}"
    response = chat.send_message(question_prompt, stream=True)
    generated_questions = []
    for chunk in response:
        if len(generated_questions) == num_questions:
            break
        generated_questions.append(chunk.text.strip())
    return generated_questions

# Read and encode the image


def get_base64_image(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string


# Path to your image
image_path = "background.jpg"

# Get the base64 string
base64_image = get_base64_image(image_path)

# Set page configuration
st.set_page_config(page_title="MCQ Generator",
                   page_icon=":books:", layout="wide")

# CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: rgba(255, 255, 255, 0.9);
        padding: 20px;
        border-radius: 15px;
        margin: 20px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    h1 {
        color: #4A90E2;
        text-align: center;
    }
    h2 {
        color: #333;
        text-align: center;
    }
    p {
        font-size: 18px;
        text-align: center;
    }
    .title {
        font-size: 2.5em;
        font-weight: bold;
        color: #000000;
        text-align: center;
        margin-bottom: 0.5em;
    }
    .subheader {
        font-size: 1.5em;
        color: #333;
        margin-bottom: 1em;
    }
    .question {
        font-weight: bold;
        margin-top: 1em;
    }
    .answer {
        color: #007BFF;
        margin-bottom: 0.5em;
    }
    .sidebar .sidebar-content {
        text-align: center;
    }
    .sidebar .sidebar-content img {
        max-width: 80%;
        border-radius: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Initialize Streamlit app
st.markdown('<div class="title">MCQ Generator</div>', unsafe_allow_html=True)
st.markdown(
    """
    <div class="main">
        <h1>Generate Multiple Choice Questions</h1>
        <p>Welcome to MCQ Generator using Large Language Model (LLM). Enter your question below and select the difficulty level 
        to generate multiple choice questions. You can specify the number of questions you want to generate.</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar for additional features
with st.sidebar:
    st.markdown('<div class="sidebar-content">', unsafe_allow_html=True)
    st.image(image_path, caption="MCQ Generator")
    st.write(
        "Use this app to generate multiple-choice questions (MCQs) based on your input.")
    st.write("Powered by MBM University.")
    st.markdown('</div>', unsafe_allow_html=True)

# Initialize session state for chat history if it doesn't exist
if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

# Input field for user question
input_question = st.text_input("Input: ", key="input")

# Slider for number of questions
num_questions = st.slider("Number of Questions",
                          min_value=1, max_value=10, value=5)

# Initialize difficulty level in session state if it doesn't exist
if 'difficulty_level' not in st.session_state:
    st.session_state['difficulty_level'] = "easy"

# Buttons for difficulty level
col1, col2, col3 = st.columns(3)

with col1:
    if st.button("Easy"):
        st.session_state['difficulty_level'] = "easy"
with col2:
    if st.button("Medium"):
        st.session_state['difficulty_level'] = "medium"
with col3:
    if st.button("Hard"):
        st.session_state['difficulty_level'] = "hard"

# Process user input and display response
if input_question:
    response = get_gemini_response(
        input_question, num_questions, st.session_state['difficulty_level'])
    # Add user query and response to session state chat history
    st.session_state['chat_history'].append(("You", input_question))
    st.markdown('<div class="subheader">The Response is:</div>',
                unsafe_allow_html=True)
    # Display each generated question
    for i, question in enumerate(response):
        st.write(f"Question {i + 1}:\n{question}")
        st.session_state['chat_history'].append(
            ("Bot", f"Question {i + 1}:\n{question}"))
