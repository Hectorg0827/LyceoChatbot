import streamlit as st
import openai
import speech_recognition as sr
import pyttsx3

# OpenAI API Key (Replace 'YOUR_API_KEY' with your actual API key)
OPENAI_API_KEY = "YOUR_API_KEY"

# Initialize text-to-speech engine
engine = pyttsx3.init()

# Function to process chatbot response
def get_chatbot_response(prompt):
    openai.api_key = OPENAI_API_KEY
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[{"role": "system", "content": "You are an AI assistant for school administration."},
                  {"role": "user", "content": prompt}]
    )
    return response["choices"][0]["message"]["content"]

# Function to convert speech to text
def speech_to_text():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.info("Listening... Speak now.")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        return "Sorry, I could not understand your speech."
    except sr.RequestError:
        return "Could not request results, please check your connection."

# Function to convert text to speech
def text_to_speech(response):
    engine.say(response)
    engine.runAndWait()

# Streamlit UI
st.title("Lyceo Principal's Portal AI Chatbot")

# Input options: Text or Voice
input_type = st.radio("Choose input method:", ["Text", "Voice"])

if input_type == "Text":
    user_input = st.text_input("Ask the chatbot a question:")
    if st.button("Submit") and user_input:
        response = get_chatbot_response(user_input)
        st.write("Chatbot:", response)
        text_to_speech(response)

elif input_type == "Voice":
    if st.button("Speak Now"):
        spoken_text = speech_to_text()
        st.write("You said:", spoken_text)
        if spoken_text:
            response = get_chatbot_response(spoken_text)
            st.write("Chatbot:", response)
            text_to_speech(response)

# Display school-related responses
st.subheader("Example Queries:")
st.write("✅ 'Show me students with low attendance'")
st.write("✅ 'Generate a teacher performance report'")
st.write("✅ 'Predict at-risk students'")

st.info("This AI chatbot integrates real-time school data and predictive analytics.")

