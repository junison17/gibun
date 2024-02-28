import streamlit as st
import openai

def generate_poem(prompt: str) -> str:
    # OpenAI API 키 불러오기
    openai.api_key = st.secrets["api_key"]

    # Generate content using GPT-4
    response = openai.Completion.create(
        engine="gpt-4",  # GPT-4로 업데이트
        prompt=prompt + " 원태연 시인의 시처럼",
        max_tokens=2048,
        temperature=0.4,
        top_p=1.0,  # GPT-4 사용시에 적합한 파라미터로 조정
        frequency_penalty=0.5,  # GPT-4에 맞게 추가된 파라미터
        presence_penalty=0.5,  # GPT-4에 맞게 추가된 파라미터
    )

    return response.choices[0].text.strip()


def generate_image(prompt: str) -> str:
    # Generate image using the latest DALL-E model
    response = openai.Image.create(
        model="dall-e-latest",  # DALL-E의 최신 버전으로 가정하여 업데이트
        prompt=prompt,
        size="1024x1024",
        n=1,
    )

    return response.data[0].url

# 사용자 입력 받기
prompt = st.text_input('당신의 기분을 입력하세요')

if st.button('Generate Text and Image'):
    poem = generate_poem(prompt)
    image_url = generate_image(prompt)
    st.image(image_url, caption='Generated Image')
    st.write(poem)
