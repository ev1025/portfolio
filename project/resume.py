import streamlit as st

def resume():
    def make_col(title, date, content):
        col1, col2 = st.columns([1,4]) 
    
        with col1:
            st.markdown(f"<h3 style='color: #37818E;'>{title}</h3>", unsafe_allow_html=True)
            st.write("")
            st.write("")
            for day in date:
                st.markdown(f"<span style='color: #8F8F8F;'>{day}</span>", unsafe_allow_html=True)
                st.write("")
                st.write("")

        with col2: #3DAFE8
            st.markdown("<hr style='border: 2px solid #37818E;'>", unsafe_allow_html=True)
            for con in content:
                st.markdown(f"<span style='color: #060E0F;'>{con}</span>", unsafe_allow_html=True)
                st.write("")
                st.write("")
    make_col('경력사항',
             ["2023.09 ~ 2024.12",],
             ['연애 IT 기업 럽디 그로스마케터 (약 15개월)',])
    st.write("")
    st.write("")    
    make_col('교육활동',
             ["2024.12 ~ 2025.04","2024.07 ~ 2024.10","2023.06 ~ 2023.08","2022.08 ~ 2023.02"],
             ['새싹 캠퍼스 종로 3기 데이터분석 & 서비스 기획 과정 (약 4개월)',
              '2024 구글 머신러닝 부트캠프 수료 (약 4개월)',
              '데이터분석 기반 SNS 마케터 과정 수료 (약 2개월)',
              '코드스테이츠 AI 부트캠프 15기 수료 (약 7개월)'])
    st.write("")
    st.write("")
    make_col('자격사항',
             ["2024.07", "2024.04", "2024.03", "2023.08"],
             ['빅데이터 분석기사',
              'SQL 개발자(SQLD)',
              '데이터분석 준전문가(ADSP)',
              '컴퓨터활용능력 1급'])
    st.write("")
    st.write("")
    make_col('학력사항',
             ["2020.03 ~ 2022.07", "2022.07"],
             ['한양 사이버대학교 (글로벌 경영학, 경영정보학 복수 전공) 수석 졸업','졸업생 대표 성적우수 총장상 수상'])
    