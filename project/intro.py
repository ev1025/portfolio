import streamlit as st
import pandas as pd

def intro():
    st.markdown("# 안녕하세요! 적응력 甲 값진우입니다.", unsafe_allow_html=True)
    st.markdown("<hr style='border: 2px solid #37818E;'>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([2,2]) 
    
    with col1:
        st.image('images/intro2.jpg',width=400)

    with col2:
        st.markdown("<h3 style=' color: #37818E;'>언제, 어디서든</h3>", unsafe_allow_html=True)
        st.markdown("##### &nbsp; 끊임없이 변화하고 적응합니다.")
        st.divider()

        st.markdown("""
        <style>
            .spacer { margin-bottom: 20px; } /* 줄 간격 조정 */
            a { color: #8F8F8F !important; } /* 링크 색상 변경 */
        </style>
                
        ##### **📱 전화번호** : <a href="tel:01096953199">010-9695-3199</a>

        <div class="spacer"></div>

        ##### **📨 이메일** : <a href="mailto:eg2874@naver.com">eg2874@naver.com</a>

        <div class="spacer"></div>

        ##### 📂 **깃허브** : <a href="https://github.com/ev1025">보러가기</a>

        <div class="spacer"></div>

        ##### 🙇 **자기소개서** : <a href="https://cheddar-alphabet-bb9.notion.site/4745bdcb258949e1939b50a87690292c?pvs=4">보러가기</a> 

        """, unsafe_allow_html=True)
        st.divider()
# Create a clickable email link using markdown

# Create a clickable phone number link using markdown
