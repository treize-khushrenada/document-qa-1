import streamlit as st
from openai import AzureOpenAI
import os

client = AzureOpenAI(
  azure_endpoint = os.getenv("AZURE_OPENAI_ENDPOINT"),
  api_key= os.getenv("AZURE_OPENAI_API_KEY"),
  api_version="2024-05-01-preview"
)

patient_chat, judge = st.columns(2)

with patient_chat:
    messages = st.container(height=300)
    if patient_chat_input := st.chat_input("Enter message here...", key="patient_chat"):
        messages.chat_message("user").write(patient_chat_input)
        messages.chat_message("assistant").write(f"Echo: {patient_chat_input}")

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
        reset = st.button("Reset", type="secondary")
    if eval:
        
        def get_answer_from_model(document, client):
            messages = [
                {
                    "role": "user",
                    "content": f"Here's a document: {document} \n\n---\n\n translate it to Bahasa Malaysia. Return directly with the translated output in your answer",
                }
            ]
            response = client.chat.completions.create(
                model="us-east-gpt-4o-mini-2024-07-18",
                messages=messages,
                stream=False,
            )
            return response.choices[0].message.content

        # Generate an answer using the OpenAI API.
        answer = get_answer_from_model("ahahahahah", client)

        # Display the answer in the Streamlit app.
        st.markdown(answer, unsafe_allow_html=True)
    if reset:
        st.write("Click 'Evaluate' to check AI's comments")
