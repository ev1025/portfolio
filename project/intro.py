import streamlit as st
import pandas as pd

def intro():
    st.markdown("<h2 style='color:#37818E;'> 끊임없는 변화에도 잘 적응하는 데이터 분석가</h2><br>", unsafe_allow_html=True)
    # st.markdown("<hr style='border: 1px solid #CECCCC'>", unsafe_allow_html=True)

    col1, col2 = st.columns([2,2]) 
    with col1:
        st.image('images/intro2.jpg',width=400)
        # st.write("사진")

    with col2:
        st.markdown("<br>", unsafe_allow_html=True)

        st.markdown("""
        <style>
            .spacer { margin-bottom: 30px; } /* 줄 간격 조정 */
            a { color: #8F8F8F !important; } /* 링크 색상 변경 */
        </style>
        ##### **🙂 이름** : <span style ='color:#8F8F8F;'> 이진우</span>

        <div class="spacer"></div>
                                  
        ##### **📱 전화번호** : <a href="tel:01096953199">010-9695-3199</a>

        <div class="spacer"></div>

        ##### **📨 이메일** : <a href="mailto:eg2874@naver.com">eg2874@naver.com</a>

        <div class="spacer"></div>

        ##### 📂 **깃허브** : <a href="https://github.com/ev1025">보러가기</a>

        <div class="spacer"></div>

        ##### 🙇 **자기소개서** : <a href="https://cheddar-alphabet-bb9.notion.site/4745bdcb258949e1939b50a87690292c?pvs=4">보러가기</a> 

        """, unsafe_allow_html=True)
    

    # st.markdown("<hr style='border: 1px solid #CECCCC'>", unsafe_allow_html=True)
    # st.markdown("<br><br>", unsafe_allow_html=True)

    # st.markdown("<h3 style='color:#37818E;'> 기술 스택 </h3>", unsafe_allow_html=True)

    col3, col4, col5 = st.columns([1,1,1]) 

    with col3:
        st.image('images/python.png',width=150) 
        st.markdown("<br>", unsafe_allow_html=True) 
        st.markdown("- **Langchain**을 활용한 **RAG**구현", unsafe_allow_html=True) 
        st.markdown("- **Chat-GPT**, **HuggingFace** 모델 파인튜닝", unsafe_allow_html=True) 
        st.markdown("- **Streamlit**, **Chainlit**을 활용한 대시보드 설계", unsafe_allow_html=True) 
        st.markdown("- **Scikit-learn**, **Tensorflow** 활용 머신러닝", unsafe_allow_html=True) 

    with col4:
        st.image('images/mysql.png',width=150)
        st.markdown("<br>", unsafe_allow_html=True) 
        st.markdown("- **조인**과 **서브 쿼리**를 이용한 데이터 추출 및 **RDBMS 관리**", unsafe_allow_html=True) 

    with col5:
        st.image('images/tableau.png',width=150)
        st.markdown("<br>", unsafe_allow_html=True) 
        st.markdown("- **KPI** 및 실무에 필요한 **Interative Dashboard** 작성", unsafe_allow_html=True) 


# Create a clickable email link using markdown

# Create a clickable phone number link using markdown
