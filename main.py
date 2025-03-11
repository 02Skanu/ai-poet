from dotenv import load_dotenv
import os
import streamlit as st
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

# 내가 입력한 프롬프트에 이어서 말을 완성하는 모델
# from langchain_openai import OpenAI
# llm = OpenAI(openai_api_key=api_key)
# prompt = "내가 좋아하는 동물은"
# result = llm.invoke(prompt)
# print(result)

st.title("인공지능 시인")
# 내가 입력한 프롬프트에 답변을 하는 채팅 모델
from langchain_openai.chat_models import ChatOpenAI

chat_model = ChatOpenAI(openai_api_key=api_key)

contents = st.text_input('시의 주제를 제시해주세요.')

if st.button('시 작성 요청하기'):
    with st.spinner('시 작성 중...'):

        result = chat_model.invoke(contents + "에 대한 시를 써줘")
        st.write(result.content)

