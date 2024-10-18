from dotenv import load_dotenv
import os
import streamlit as st

st.title("Drunk A.I Assistant")

role_alloted=st.text_input("Enter Your A.I Role")
Temperature=st.slider("Temperature",min_value=0.1,max_value=1.0,step=0.05)
Input_Box=st.text_input("Enter Your Query")


os.environ['LANGCHAIN_API_KEY']=os.getenv('LANGCHAIN_API_KEY')
os.environ['LANGCHAIN_TRACING_V2']='true'
os.environ['LANGCHAIN_PROJECT']=os.getenv('LANGCHAIN_PROJECT')

groq_api_key=os.getenv('GROQ_API_KEY')

from langchain_core.prompts import ChatPromptTemplate
Base_Prompt="Reply adequately to the query sought as per the role alloted. {role_alloted}"
prompt=ChatPromptTemplate.from_messages([
    ('system',Base_Prompt),
    ('user',"{input}")

])

from langchain_groq import ChatGroq
Groq_Model=ChatGroq(model='gemma2-9b-It',api_key=groq_api_key,temperature=Temperature)

from langchain_core.output_parsers import StrOutputParser
Parser=StrOutputParser()

chain=prompt|Groq_Model|Parser
result=chain.invoke({"role_alloted":role_alloted,"input":Input_Box})

st.write(result)


