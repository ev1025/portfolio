import streamlit as st

def performance():
    st.text('[Funel분석을 통한 성과 개선]')
    st.title('고객 이용 페이지 개선을 통한 서비스 이용 수 2배 증가')

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
