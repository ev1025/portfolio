import streamlit as st

def math_project():
    st.text('[gemma 파인 튜닝]')
    st.title('LLM를 이용한 나만의 수학 선생님 만들기')
    st.link_button("Github", "https://github.com/ev1025/gemma_sprint")

    tabs = st.tabs(["분석 개요","데이터 분석", "모델 훈련", "모델 평가", '결과'])

    with tabs[0]:   
        st.write('개요')
    
    with tabs[1]:   
        st.write('전처리')

    with tabs[2]:
        st.write('모델 훈련')

    with tabs[3]:
        st.write('모델 평가')

    with tabs[4]:
        st.write('훈련 결과')
