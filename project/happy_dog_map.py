import streamlit as st

def happy_project():
    st.markdown("<h4 style='color: #008080; font-weight: bold;'>[태블로 시각화]</h4>", unsafe_allow_html=True)
    st.subheader("네이버지도 크롤링을 이용한 강아지 행복 지도")
   
    st.markdown("<hr style='border: 1.5px solid #008080;'>", unsafe_allow_html=True)

    col1, col2 = st.columns([4,1])
    with col1:
        st.markdown("""<h5 style=' font-weight: bold;'>
                    프로젝트 기간 : 2023년 4월 5일 ~ 2023년 4월 14일 (10일)</h5>""", unsafe_allow_html=True)
    with col2:
        st.link_button("Github", "https://github.com/ev1025/happy_dog_map")
    st.markdown("""
                
##### 참여인원 : 1인
##### 기여내용
- 프로젝트 기획 및 데이터 수집
- 핵심지표 설정 및 대시보드 제작
                """, unsafe_allow_html=True)
    st.markdown("<hr style='border: 1.5px solid #008080;'>", unsafe_allow_html=True)
    st.markdown(r"""

#### 1. 프로젝트 배경
- 코로나19로 인한 경기 불황속에서도 반려동물 창업에 대한 수요가 급증했다. ([기사 링크](https://news.sktelecom.com/173572))
- 하지만 반려견을 키우는 입장에서 `인터넷 검색`만으로 반려동물 관련 장소에 대한 정보를 얻기 어려웠다.
- 그래서 `반려견과 함께 할 수 있는 장소`에 대한 정보의 부재를 해소하고자 서울특별시의 반려동물 관련 매장 정보를 볼 수 있는 대시보드를 제작했다.

---

#### 2. 기대효과
- `소비자나 예비 창업자`에게 `상권에 대한 정보`를 제공한다.
- 아직은 모호한 `반려동물 상권`에 대한 문화가 정착되는데 일조한다.
- 일일이 매장 상세 정보를 확인하지 않아도 주변에 원하는 장소를 빠르게 찾을 수 있다.

---

#### 3. 데이터 개요
##### 1) 데이터 수집 및 적재
- 본 프로젝트는 네이버지도 크롤링과 공공데이터를 활용하여 진행했다.
- 강아지 동반이 가능한 식당이나 카페에 대한 정보가 명확하게 명시되지 않았었는데 최근 네이버에서 `지역별 강아지동반 식당과 카페 리스트`를 공개하여 그 정보를 크롤링했다.
- 그 외에 `동물병원, 애견미용실, 애견호텔, 애견유치원, 애견간식, 애견용품점` 등의 정보를 `서울특별시의 각 행정구별`로 크롤링하여 수집했다.
- 지표설정을 위해 각 `행정구별 반려동물 등록현황을 공공데이터 포털`을 통해 수집했다.
- 공공데이터는 각 행정구별 갱신 시기가 일치하지 않고, 강아지를 제외한 반려동물이 포함되어 있는 자료로 실제와 다소 차이가 있다.
- 수집한 데이터는 `로컬 Mysql DB`에 적재하였으며 `파이썬으로 정제 및 분석`작업을 거친 뒤 `태블로로 시각화`했다.

<p align="center">
<img src="https://user-images.githubusercontent.com/110000734/231789734-895323c8-9f64-44ef-b20a-83ae08fffc3b.JPG">

<br>
<br>

##### 2) 지표설정
- 업종별 가중치부여 : 병원은 생명과 직결된 시설이기 때문에 0.225 , 반려동물을 위한 시설은 0.125, 반려동물동반 시설은 0.1점으로 도합 1점이 되도록 부여했다.  
- 그 외에 행정구별 반려동물과 시설의 수를 정리했다.
<p align="center">
<img src="https://user-images.githubusercontent.com/110000734/231937930-a63ef46a-d6f2-43e3-a09f-7931cf03a77a.JPG">

<br>
<br>  
                
- 행정구별 업종별 순위부여
  - 할당량 : 행정구별로 `하나의 사업장`이 맡아야 하는 `반려동물 수`   
    $할당량 = \frac{반려동물 수}{시설 수}$   
  - 순위는 `할당량`이 `낮은 순`으로 부여
  - 테마점수 : 각 테마별 해당구의 점수
  - 행정구점수 : 각 행정구의 테마점수를 `총 합산한 점수`
<p align="center">
<img src="https://user-images.githubusercontent.com/110000734/231953302-fb71dd5b-f2b7-452e-b2ec-ca0a9ccdd985.JPG">

---

#### 4. 대시보드 ([링크](https://public.tableau.com/views/_16814577730860/sheet6_1?:language=ko-KR&:display_count=n&:origin=viz_share_link))
##### 1) 전체화면
  - 대시보드에는 서울특별시 전체 강아지 수와 각 행정구별 업종 수, 업종목록을 확인할 수 있다.
  
<p align="center">
<img src="https://user-images.githubusercontent.com/110000734/232397385-dc343f77-215c-45de-b887-f2bc5aae91c1.png">  
  
<br>
<br>
                
  
##### 2) 구 선택
  - 원하는 행정구와 업종을 선택할 수 있다.
  
  - 선택하면 총 개수, 행정구의 업종별 순위와 점수, 가게 목록을 확인할 수 있다.
<p align="center">
<img src="https://user-images.githubusercontent.com/110000734/232402637-9a97ee2f-1311-4131-81f5-6f58ebea874b.jpg">

<br>
<br>

##### 3) 기타 기능
  - 여러 구를 한 번에 선택 할 수 있다.
  
  - 선택한 업종의 총 개수를 확인 할 수 있다.
  
  - 테이블의 목록은 최대 10페이지(100개)까지 확인이 가능
  
  - 테이블의 상호명을 누르면 바로 네이버지도 페이지로 이동
  
  - 오른쪽 위에 표시된 날씨는 선택한 구의 업종점수를 날씨로 표현
    - 85점 이상 : 따듯해요
    - 85점 미만 ~ 60점 이상 : 약간 흐려요
    - 60점 미만 ~ 40점 이상 : 흐려요
    - 40점 미만 : 비와요
<p align="center">
<img src="https://user-images.githubusercontent.com/110000734/232402799-805d9d5a-1761-49d5-bac7-b6c7dc7a66b3.png">

<br>
<br>
  
  - 전체 점수와 마리수에 마우스를 올리시면 순위를 그래프로 확인 할 수 있다.
  
<p align="center">
<img src="https://user-images.githubusercontent.com/110000734/232419648-b62db7a1-e224-4b06-82f9-34fb1f22814a.jpg">




    """, unsafe_allow_html=True)