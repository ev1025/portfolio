import streamlit as st

def alter_project():
    st.text('[대안 신용 평가]')
    st.title('서울시민통신데이터를 이용한 신용카드 연체 여부 예측')
    st.link_button("Github", "https://github.com/ev1025/Alternative-Credit-Scoring")

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


