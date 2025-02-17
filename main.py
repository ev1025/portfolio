# cd desktop/sesac_study/포트폴리오
import streamlit as st
from project import intro, alter_credit, math_teacher, happy_dog_map, luvd, resume, news

st.set_page_config(page_title = "이진우 포트폴리오입니다.", page_icon = ":sunglasses:")

# 네비게이션 로고, 기본 로고
st.logo(image="images/logo.png", 
        icon_image="images/icon_blue.png")


# 연도, 상단 탭 CSS
css = '''
<style>
    /* --------- 네비게이션 --------- */
    [data-testid="stNavSectionHeader"] {
        font-size: 1rem;    /* 헤더  */
        color: #666666;
    }
    .st-emotion-cache-6tkfeg {
        font-size: 1.1rem;  /* 링크 */
        font-weight: 400;
        color: #888888;
    }
    .st-emotion-cache-xtjyj5 {
        font-size: 1.1rem;  /* 활성화 링크 */
        display: flex;
        color: #272727;
    }
    [data-testid="stIconMaterial"] {
        font-size: 20px;    /* 아이콘 크기 */
    }
    [data-testid="stSidebarNavLink"] span {
    margin-right: 7px;      /* 아이콘과 텍스트 사이의 여백 */
    }

    
    /* -------- 본문 상단 --------  */
    h1 {
    padding-top: 0.1rem; /* 제목 여백 제거 */
    padding-bottom: 0.3rem; /* 제목 여백 제거 */
    }
    [data-testid='stVerticalBlock'] {
    gap : 0.3rem;
    }
    .st-emotion-cache-mptgkq.exotz4b0 {
    color :#888888;
    font-size : 19px;
    font-weight: bold;
    margin-top: 15px;
    }
    .stButton {
    position: relative;
    z-index: 999;
    }
    div.stButton > button:first-child {
    margin-left: auto;
    display: block;
    position: relative;
    bottom: 20px;
    right: 20px;
    }

    /* 프로젝트 제목 여백*/
    h1 {
    margin-top: 0 !important;
    padding-top: 0 !important;
    }

    /* 프로젝트 제목 상단 [주제] */
    .st-emotion-cache-1b3332t {
    margin-top: 10px;  /* 위쪽 여백 */
    font-size: 25px;
    font-weight: bold;
    color:rgb(126, 123, 123);
    }

    /* ------- 깃허브 버튼 -------- */
    .stLinkButton {
        display: flex;
        justify-content: flex-end; /* 가로 방향 오른쪽 끝 정렬 */
    }

    .st-emotion-cache-1mcbg9u.efj1jhq2 {
        background-color: #000000; /* 배경색 */
        color: #FFFFFF;            /* 글자색 */

        border: none;       /* 기본 테두리 제거 */
        outline: none;      /* 외곽선 제거 */
    }
    .st-emotion-cache-1mcbg9u.efj1jhq2 p,
    .st-emotion-cache-1mcbg9u.efj1jhq2 p:focus,
    .st-emotion-cache-1mcbg9u.efj1jhq2 p:active {
        color: white; /* 글자색 */
        font-weight: bold;
    }
    
    .st-emotion-cache-1mcbg9u.efj1jhq2:active,
    .st-emotion-cache-1mcbg9u.efj1jhq2:hover, {
        outline: none; /* 호버 시 외곽선 제거 */
        border: none;  /* 호버 시 테두리 제거 */
    }
    
    /* ------- 프로필 이미지 중앙 정렬 -------- */
    [data-testid="stFullScreenFrame"]{
    display: flex;
    justify-content: center;
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)

# # 상단 연도 버튼
# options = ["2023", "2024", "2025"]
# year = st.pills("a", options, selection_mode="single", default="2025", label_visibility="hidden") # collapsed, visible
# year = year or "2025"

# project_list = {
#     "2025": [alter_credit_scording, news],
#     "2024": [math_teacher,luvd],
#     "2023": [happy_dog_map],
# }

# 자기소개
intro = st.Page(intro.intro, title="소개", icon=":material/person:", default=True)
resume = st.Page(resume.resume, title="이력사항", icon=":material/license:")
luvd = st.Page(luvd.performance, title="경력사항", icon=":material/insert_chart:")

# 프로젝트  
alter_credit_scording = st.Page(alter_credit.alter_project, title="대안 신용 평가", icon=":material/credit_card:")
news = st.Page(news.news_project, title="실시간 뉴스 토픽 분석", icon=":material/newsmode:")
math_teacher = st.Page(math_teacher.math_project, title="나만의 수학 선생님 만들기", icon=":material/function:")
happy_dog_map = st.Page(happy_dog_map.happy_project, title="강아지 행복 지도", icon=":material/pets:")


# 사이드바 프로필 사진, 이름
st.sidebar.image("images/me.jpg", width=170)
st.sidebar.markdown("<h3 style='font-weight: bold; text-align: center;'>데이터 분석가 이진우</h3>", unsafe_allow_html=True)

page_dict = {
    "자기소개" : [intro, resume, luvd],
    "프로젝트" : [alter_credit_scording, news, math_teacher, happy_dog_map]
    # f"{year}년 활동": project_list.get(year, []),  # year에 해당하는 프로젝트만 선택
}

page = st.navigation(page_dict)
page.run()

# # 프로젝트 선택하지 않으면 연도 숨기기
# if page.title in ['소개', '이력사항']:
#     st.markdown("<style>[data-testid='stButtonGroup'] {display: none;}</style>", unsafe_allow_html=True)
# else:
#     st.markdown("<style>[data-testid='stButtonGroup'] {display: block;}</style>", unsafe_allow_html=True)

    

# /* 호버 확대 */
# [data-testid="stHorizontalBlock"] img {
# transition: transform 0.3s ease;
# }
# [data-testid="stHorizontalBlock"] img:hover {
# transform: scale(1.8); /* 확대 크기*/
# position: relative;
# z-index: 9999;
# }

