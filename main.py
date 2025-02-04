# cd desktop/sesac_study/포트폴리오
import streamlit as st
from project import intro, alter_credit, math_teacher, happy_dog_map, certi, resume

st.set_page_config(page_title = "이진우 포트폴리오입니다.", page_icon = ":sunglasses:")

# 네비게이션 로고, 기본 로고
st.logo(image="images/horizontal_blue.png", 
        icon_image="images/icon_blue.png")

# 연도, 상단 탭 CSS
css = '''
<style>
    /* --------- 연도버튼 ---------- */
    .stButtonGroup [data-baseweb="button-group"] button [data-testid="stMarkdownContainer"] p {
    font-size: 17px;         /* 텍스트 크기 조정 */
    font-weight : bold;
    padding: 10px 0px;       /* 버튼의 패딩 조정 */
    height: 45px;            /* 버튼의 높이 */
    width : 40px;
    }
    [data-baseweb="button-group"] {
    column-gap: 0.4rem; /* 버튼 간격 */
    }
    [kind="pills"] {
    border-radius : 8px; /* 둥근 모서리 */
    }
    [kind="pillsActive"] {
    border-radius: 8px; /* 활성화된 버튼에도 동일한 둥근 모서리 */
    }


    /* ---------- 상단탭 ---------*/
    [data-baseweb="tab-highlight"] {
    height: 0.16rem;        /* 빨간줄 */
    }
    [data-baseweb="tab-border"] {
    margin-top: 0.8px;      /* 회색줄 */
    }
    .stTabs [data-baseweb="tab-list"] {
    display: flex;          /* 플렉스 컨테이너 설정 */
    gap: 1.6rem;            /* 탭 간 간격 조정 */
    }
    .stTabs [data-baseweb="tab-list"] button [data-testid="stMarkdownContainer"] p {
    font-size: 1.1rem;      /* 탭 글씨 크기 */
    font-weight: normal;    /* 기본 상태 */
    }
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] [data-testid="stMarkdownContainer"] p {
    font-weight: bold;      /* 활성화된 탭글씨 볼드 처리 */
    }

    
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

    /* 프로젝트 제목 */
    [id="5118a375"] {
    margin-top: 0 !important;
    padding-top: 0 !important;
    }

    /* 프로젝트 제목 상단 [주제] */
    .st-emotion-cache-1b3332t {
    margin-top: 10px;  /* 위쪽 여백 */
    margin-bottom: 10px; /* 아래쪽 여백 */
    font-size: 25px;
    font-weight: bold;
    color:rgb(126, 123, 123);
    }

    /* ------- 깃허브 -------- */
    .stLinkButton {
    display: flex;
    justify-content: flex-end; /* 가로 방향 오른쪽 끝 정렬 */
    }
    .st-emotion-cache-1mcbg9u.e16zdaao0 {
    background-color: #000000; /* 배경색 */
    color: white;             /* 글자색 */  

    border: none;       /* 기본 테두리 제거 */
    outline: none;      /* 외곽선 제거 */
    }
    .st-emotion-cache-1mcbg9u.e16zdaao0:hover {
    outline: none; /* 호버 시 외곽선 제거 */
    border: none;  /* 호버 시 테두리 제거 */
    }
    .st-emotion-cache-1mcbg9u.e16zdaao0:focus,
    .st-emotion-cache-1mcbg9u.e16zdaao0:active {
    outline: none;      /* 포커스 시 외곽선 제거 */
    border: none;       /* 포커스 시 테두리 제거 */
    color: white;       /* 글자색 흰색 유지 */
    background-color: #000000; /* 배경색 유지 */
    }
</style>
'''
st.markdown(css, unsafe_allow_html=True)



# state 초기화 / 연도 생성 / 네비게이션 생성
options = ["2023", "2024", "2025"]
year = st.pills("a", options, selection_mode="single", default="2025", label_visibility="hidden") # collapsed, visible
year = year or "2025"

# 자기소개
intro = st.Page(intro.intro, title="소개", icon=":material/person:")
resume = st.Page(resume.resume, title="이력사항", icon=":material/license:")
certi = st.Page(certi.certi, title="경력사항", icon=":material/lab_profile:")

# 프로젝트  
alter_credit_scording = st.Page(alter_credit.alter_project, title="대안 신용 평가", icon=":material/credit_card:", default=True)
math_teacher = st.Page(math_teacher.math_project, title="나만의 수학 선생님 만들기", icon=":material/function:", default=True)
happy_dog_map = st.Page(happy_dog_map.happy_project, title="강아지 행복 지도", icon=":material/notification_important:", default=True)

# 프로젝트 리스트
project_list = {
    "2025": [alter_credit_scording],
    "2024": [math_teacher],
    "2023": [happy_dog_map],
}

page_dict = {
    "자기소개": [intro, resume, certi],
    f"{year}년 프로젝트": project_list.get(year, []),  # year에 해당하는 프로젝트만 선택
}

# 유효한 year 값 확인 후 프로젝트 리스트 구성
if year not in options:
    year = "2025"  # 기본값 설정

page = st.navigation(page_dict)
page.run()

# 프로젝트 선택하지 않으면 연도 숨기기
if page.title in ['소개', '이력사항','경력사항']:
    st.markdown("<style>[data-testid='stButtonGroup'] {display: none;}</style>", unsafe_allow_html=True)
else:
    st.markdown("<style>[data-testid='stButtonGroup'] {display: block;}</style>", unsafe_allow_html=True)


# /* 호버 확대 */
# [data-testid="stHorizontalBlock"] img {
# transition: transform 0.3s ease;
# }
# [data-testid="stHorizontalBlock"] img:hover {
# transform: scale(1.8); /* 확대 크기*/
# position: relative;
# z-index: 9999;
# }