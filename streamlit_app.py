import streamlit as st
#st.set_page_config(layout="wide")
from openai import AzureOpenAI
import os
#from dotenv import load_dotenv
#load_dotenv()
# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
  api_key= os.getenv("AZURE_OPENAI_API_KEY"),
  api_version="2024-05-01-preview"
)

def get_patient_response(doctor_input, client):
    messages = [
                {
                    "role": "user",
                    #"content": f"you have just be diagnosed stage 4 cancer and you are so upset and have suicidal thoughts. this is a medical consultation with a doctor. this is what he said: {doctor_input} \n\n---\n\n reply to the doctor's message in a conversational manner and keep things short",
                    "content": f"you are a {personality} patient being called to meet a doctor at Sengkang Hospital for this medical appointment session, about your diagnosis results. you tend to suspect the diagnosis results and the doctor's medical decisions, and have the urge to speak with a supervisor. this is what he said: {doctor_input} \n\n---\n\n now respond to the doctor in this conversation, keep your reponse conversational:",
                }
            ]
    response = client.chat.completions.create(
                model="us-east-gpt-4o-mini-2024-07-18",
                messages=messages,
                stream=False,
            )
    return response.choices[0].message.content

def reset_conversation():
  st.session_state.messages = []

st.title("EmpathBot")

personality = st.selectbox(
    "Patient's personality",
    ("Passive", "Needy", "Aggressive"),
)

patient_chat, judge = st.columns(2, gap="large")

with patient_chat:
    messages = st.container(height=600)
    with messages:
        convo_log = ""
        for message in st.session_state.messages:
            convo_log += message["role"] + ": " + message["content"]
            with st.chat_message(message["role"]):
                st.markdown(message["content"])
            
    if patient_chat_input := st.chat_input("Enter message here...", key="patient_chat"):
        st.session_state.messages.append({"role": "Doctor", "content": patient_chat_input})
        patient_response = get_patient_response(convo_log + patient_chat_input, client)
        st.session_state.messages.append({"role": "Patient", "content": patient_response})
        messages.chat_message("Doctor").write(patient_chat_input)
        messages.chat_message("Patient").write(patient_response)

#with judge:
#    messages = st.container(height=300)
#    if judge_input := st.chat_input("Enter message here...", key="judge"):
#        messages.chat_message("user").write(judge_input)
#        messages.chat_message("assistant").write(f"Echo: {judge_input}")
with judge:
    col1, col2 = st.columns(2)
    with col1:
        eval = st.button("Evaluate", type="primary")
        
    with col2:
        reset = st.button("Reset", type="secondary", on_click=reset_conversation)
    if eval:
        
        def get_answer_from_model(document, client):
            messages = [
                {
                    "role": "user",
                    "content": f"Here's a conversation between a patient and a doctor: {document} \n\n---\n\n give a professional comment to the doctor's performance, in less than 200 words:",
                }
            ]
            response = client.chat.completions.create(
                model="us-east-gpt-4o-mini-2024-07-18",
                messages=messages,
                stream=False,
            )
            return response.choices[0].message.content

        # Generate an answer using the OpenAI API.
        convo_log = ""
        for message in st.session_state.messages:
            convo_log += message["role"] + ": " + message["content"]
        
        answer = get_answer_from_model(convo_log, client)

        # Display the answer in the Streamlit app.
        st.markdown(answer, unsafe_allow_html=True)
    #if reset:
    #    st.write("Click 'Evaluate' to check AI's comments")
    #    st.session_state.messages = []