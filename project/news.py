import streamlit as st

def news_project():
    st.markdown("<h3 style='color: #8F8F8F; font-weight: bold;'>[Streamlit 대시보드]</h3>", unsafe_allow_html=True)
    st.title('크롤링 데이터를 활용한 실시간 토픽 모델링(LDA) 및 주식 차트 분석')
    st.link_button("Github", "https://github.com/ev1025/News_Crawling_Dashboard")

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


