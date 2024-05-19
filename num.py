# import google.generativeai as genai
# import streamlit as st
# import base64
# import os

# # Set your Google API key directly in the script
# API_KEY = "AIzaSyAdHm4Xvp2n6-nV_Yx9lf3EHpdKPFcE3to"

# # Configure the Gen AI SDK
# genai.configure(api_key=API_KEY)

# # Initialize Gemini Pro model
# model = genai.GenerativeModel("gemini-pro")
# chat = model.start_chat(history=[])

# # Function to get Gemini response


# def get_gemini_response(question, num_questions, difficulty):
#     question_prompt = f"{question} mcq {difficulty}"
#     response = chat.send_message(question_prompt, stream=True)
#     generated_questions = []
#     for chunk in response:
#         if len(generated_questions) == num_questions:
#             break
#         generated_questions.append(chunk.text.strip())
#     return generated_questions

# # Read and encode the image


# def get_base64_image(image_path):
#     with open(image_path, "rb") as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode()
#     return encoded_string


# # Path to your image
# image_path = "background.jpg"

# # Get the base64 string
# base64_image = get_base64_image(image_path)

# # Set page title and add decorations
# st.set_page_config(page_title="MCQ Generator using LLM")

# # CSS for background gradient and styling
# st.markdown(
#     f"""
#     <style>
#         body {{
#             background: linear-gradient(120deg, #f6d365 0%, #fda085 100%);
#             background-attachment: fixed;
#             color: #333;
#             font-family: 'Arial', sans-serif;
#         }}
#         .main {{
#             background-color: rgba(255, 255, 255, 0.9);
#             padding: 20px;
#             border-radius: 15px;
#             margin: 20px;
#             box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
#         }}
#         h1 {{
#             color: #4A90E2;
#             text-align: center;
#         }}
#         h2 {{
#             color: #333;
#             text-align: center;
#         }}
#         p {{
#             font-size: 18px;
#             text-align: center;
#         }}
#         .highlight {{
#             background-color: #f0f8ff;
#             padding: 10px;
#             border-radius: 10px;
#             margin-bottom: 20px;
#         }}
#         .center {{
#             display: flex;
#             justify-content: center;
#             align-items: center;
#         }}
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# # Initialize Streamlit app
# st.title("MCQ Generator using Large Language Model")
# st.markdown(
#     """
#     <div class="main">
#         <h1>Generate Multiple Choice Questions</h1>
#         <p>Welcome to MCQ Generator using Large Language Model (LLM). Enter your question below and select the difficulty level
#         to generate multiple choice questions. You can specify the number of questions you want to generate.</p>
#     </div>
#     """,
#     unsafe_allow_html=True
# )

# # Initialize session state for chat history if it doesn't exist
# if 'chat_history' not in st.session_state:
#     st.session_state['chat_history'] = []

# # Input field for user question
# input_question = st.text_input("Enter your question here:", key="input")

# # Prompt for number of questions
# num_questions = st.number_input(
#     "Number of Questions", min_value=1, max_value=10, value=5)

# # Slider for difficulty level
# difficulty_level = st.select_slider(
#     "Select Difficulty Level:",
#     options=["Easy", "Medium", "Hard"]
# )

# # Button to ask the question
# submit_button = st.button("Generate MCQs")

# # Process user input and display response
# if submit_button and input_question:
#     response = get_gemini_response(
#         input_question, num_questions, difficulty_level.lower())
#     # Add user query and response to session state chat history
#     st.session_state['chat_history'].append(("You", input_question))
#     st.subheader("Generated Multiple Choice Questions:")
#     # Display generated questions
#     for i, question in enumerate(response):
#         st.write(f"**Question {i + 1}:**\n{question}\n")
#         st.session_state['chat_history'].append(
#             ("Bot", f"Question {i + 1}:\n{question}"))
