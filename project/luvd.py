import streamlit as st
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import os
import pandas as pd
import altair as alt

def performance():
    st.markdown("<h3 style='color: #008080; font-weight: bold;'>[퍼널 개선으로 서비스 이용 고객 2배 증가]</h3>", unsafe_allow_html=True)
    st.title('연애 IT 기업 LuvD 그로스 마케터')
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("""<h4 style='color: #7D7D7D; font-weight: bold;'>
                2023년 9월 1일 ~ 2024년 12월 6일 (15개월) </h4>""", unsafe_allow_html=True)
    st.markdown("<hr style='border: 1.5px solid #808080;'>", unsafe_allow_html=True)
    st.markdown("""<h3> 회사 소개</h3>
                <span style = font-size:20px> &nbsp; 이별을 겪은 사람들이 지난 연애와 자신을 되돌아보고 더 나은 사람이 될 수 있도록 솔루션을 주는 연애 IT 기업입니다. 
                실패한 연애를 바로잡고 <strong>헤어진 연인</strong>과 <strong>관계를 회복</strong>하거나 <strong>극복</strong>을 통해 새로운 연애를 시작할 수 있도록 돕습니다. </span>
<br>
<br>
<br>
                """, unsafe_allow_html=True)


    #### 비즈니스 퍼널
    st.markdown("""<h3> 비즈니스 퍼널</h3>
<br>
                """, unsafe_allow_html=True)
    st.image("images/FUNEL2.png",width=700)

    st.divider()
    st.markdown("""<br>
                """, unsafe_allow_html=True)
 
    


    # ---------------------  문제사항 1  ------------------------------------
    st.markdown("""
    ### 문제 사항
    #### 1) 홈페이지 Bounce Rate(즉시 이탈)가 높고 방문자 수 대비 신청서 제출률이 저조
    - 상담 신청을 위해서는 무조건 홈페이지를 방문해야 하는 문제 발견
    - 홈페이지에 방문하지 않고도 상담을 신청할 수 있도록 퍼널을 축소
    - 해당 서비스는 개인의 민감한 정보를 다루기 때문에 신뢰성 있는 페이지 개선에 초점
    - 페이지 개선 이후 상담신청 **전환률 1%** 상승

    <br>       
                """, unsafe_allow_html=True) 
    col1, col2 = st.columns([1,1])
    with col1:
        st.image("images/link_before.png")
        st.markdown("<div style='font-size:15px; text-align: center;'>개선 전</div>", unsafe_allow_html=True)
    with col2:
        st.image("images/link_after.jpg")
        st.markdown("<div style='font-size:15px; text-align: center;'>개선 후</div><br><br><br>", unsafe_allow_html=True)

    st.markdown("<h5 style=' text-align: center;'>퍼널 개선 후 상담신청 전환률</h5>", unsafe_allow_html=True)

    # 한글폰트
    font_path = os.path.join(os.path.dirname(os.path.abspath(os.path.dirname(__file__))),'Fonts','NanumGothicBold.ttf')
    font_prop = fm.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = font_prop.get_name()
    plt.rcParams['axes.unicode_minus'] = False

    data_submit = pd.DataFrame({'개선여부': ['개선 전', '개선 후'], '값': [0.007, 0.017]})
    base = alt.Chart(data_submit)

    bars = base.mark_bar().encode(
        x=alt.X('개선여부:N', axis=alt.Axis(title=None, labelAngle=0)),
        y=alt.Y('값:Q', 
                axis=alt.Axis(
                    title='상담신청(%)',
                    format='%'
                )),
        color=alt.Color('개선여부:N', legend=None),
        tooltip=[
            alt.Tooltip('개선여부:N', title='구분'),
            alt.Tooltip('값:Q', title='상담신청', format='.1%')
        ]
    )

    text = base.mark_text(
        align='center',
        baseline='middle',
        dy=-10,
        fontSize=16
    ).transform_calculate(
        percentage="format(datum.값 * 100, '.1f') + '%'"  
    ).encode(
        x=alt.X('개선여부:N'),
        y=alt.Y('값:Q'),
        text='percentage:N',
        tooltip=[alt.Tooltip('percentage:N', title='상담신청')]
    )

    chart = (bars + text)
    st.altair_chart(chart, use_container_width=True)


    # ---------------------  문제사항 2  ------------------------
    st.markdown("""
<br>  
<br>
                                  
#### 2) 신청서를 제출했지만 견적 상담을 하지 않는 문제
- 신청서를 제출하고 카카오톡 채팅방으로 입장해야 견적 상담을 받을 수 있는 문제 발견
- 신청서 제출 완료 페이지를 개선하여 제출 즉시 카카오톡 채팅방으로 들어올 수 있도록 유도
- 페이지 개선 후 약 **90% 이상**의 고객이 즉시 채팅방으로 입장
           
<br>
<br>
                """, unsafe_allow_html=True) 
    col3, col4 = st.columns([1,1])
    with col3:
        st.image("images/di_before.png")
        st.markdown("<div style='font-size:15px; text-align: center;'>개선 전</div>", unsafe_allow_html=True)

    with col4:
        st.image("images/di_after.png")
        st.markdown("<div style='font-size:15px; text-align: center;'>개선 후</div>", unsafe_allow_html=True)



    # ---------------------  실제 성과 ------------------------
    st.divider() 
    st.markdown("""
<br>  
<br>
    
### 개선 결과
- 추가적인 **마케팅 비용 없이** 결제 전환률을 유지하며 상담 신청자 수를 증가시켜 **2배 이상의 성과** 달성
- 해딩 수치는 실제 수치에 스케일링을 진행하였습니다.
                
<br>
<br>
                """, unsafe_allow_html=True) 
    

    # ---------------------  성과 그래프 ------------------------

    data = {
        "date": [
            "23-01", "23-02", "23-03", "23-04", "23-05", "23-06", "23-07", "23-08", "23-09", "23-10", "23-11", "23-12",
            "24-01", "24-02", "24-03", "24-04", "24-05", "24-06", "24-07", "24-08", "24-09", "24-10"
        ],
        "상담 신청": [34, 33, 34, 35, 32, 32, 32, 31, 29, 27, 26, 36, 40, 44, 49, 53, 51, 54, 50, 51, 50, 52],
        "상담": [15, 16, 17, 16, 15, 14, 14, 16, 15, 13, 15, 21, 21, 23, 27, 28, 25, 22, 26, 26, 25, 28],
        "후속상담": [6, 7, 7, 8, 5, 6, 8, 7, 7, 8, 8, 9, 10, 10, 12, 13, 12, 12, 14, 13, 13, 15]
    }

    # 데이터프레임 생성
    df = pd.DataFrame(data)

    # date를 datetime 형식으로 변환 (x축 정렬을 위해)
    df["date"] = pd.to_datetime(df["date"], format="%y-%m")

    # 데이터를 long format으로 변환
    df_melted = df.melt(id_vars=["date"], var_name="category", value_name="value")

    # 원하는 순서로 범주 정렬
    category_order = ["상담 신청", "상담", "후속상담"]
    df_melted["category"] = pd.Categorical(df_melted["category"], categories=category_order, ordered=True)

    # 색상 설정 (상담 신청 = 연한 파랑, 상담 = 중간 파랑, 후속상담 = 진한 파랑)
    color_scale = alt.Scale(
        domain=category_order,
        range=["#A6CEE3", "#1F78B4", "#08306B"]  # 연한 → 진한 파란색 그라데이션
    )

    # 라인 차트 생성
    vertical_line = alt.Chart(pd.DataFrame({'date': ['2023-11-01']})) \
        .mark_rule(color='#D3D3D3', size=2) \
        .encode(
            x='date:T'
        )

    # 텍스트 추가
    text_on_line = vertical_line.mark_text(
        align='center',
        baseline='alphabetic',
        dy=-10  # 텍스트가 선 위로 올라오게 조정
    ).encode(
        text=alt.value("팀 합류")  # 선 위에 표시할 텍스트
    )

    # 라인 차트 생성
    line_chart = (
        alt.Chart(df_melted)
        .mark_line(point=True)  # 점 추가
        .encode(
            x=alt.X("date:T", title=None),
            y=alt.Y("value:Q", title=None, scale=alt.Scale(zero=False)),  # Y축 제목 제거
            color=alt.Color("category:N", scale=color_scale, title=None),  # 범주 정렬 및 색상 적용
            tooltip=["date:T"]
        )
    )

    # 텍스트 표시 (각 값 위에 표시)
    text = line_chart.mark_text(
        align='center',
        baseline='bottom',
        dy=-5  # 값이 선 위에 표시되도록 조정
    ).encode(
        text='value:Q'
    )

    # Streamlit에서 출력 (라인 차트 + 세로선 + 텍스트)
    st.altair_chart(line_chart + vertical_line + text_on_line + text, use_container_width=True)
