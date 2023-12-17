import streamlit as st
from PIL import Image
import numpy as np

st.title("2차시. 물체의 색이 다르게 보이는 까닭")
st.subheader("")
st.subheader("학습 목표", divider='violet')
st.markdown(" 2. 물체의 색이 빛의 삼원색으로 합성됨을 관찰할 수 있다.")
st.divider()

st.subheader("탐구2. 조명 색에 따른 물체의 색 관찰하기", divider='violet')
#video_file = open('./videos/조명 색에 따른 물체의 색 관찰(실험영상).mp4', 'rb')
#video_bytes = video_file.read()
#st.video(video_bytes)
video_url = 'https://drive.google.com/uc?id=1TsYD9foa4HtuLMvJDSOZJEkvCK8_rj7i'
st.video(video_url)
st.markdown('##### **다음 과정에 따라 실험해 봅시다.**')
st.markdown(" 1. 상자의 옆면에 지름 1cm 정도의 구멍을 뚫은 후 상자 속에 파란색 공을 넣는다.")
st.markdown(" 2. RGB 슬라이드바를 조절하여 점묘화를 파란색으로 바꾼다.")
st.markdown(" 3. 파란색 화면 부분을 상자에 대어 파란색 빛이 상자 속을 비추도록 하고 상자 안을 관찰한다.")
st.markdown(" 4. RGB 슬라이드바를 다시 조절하여 빨간색, 초록색으로 상자 속을 비추고 상자 안을 관찰한다.")
st.markdown(" 5. 스마트 기기 화면의 색에 따라 상자 안 공이 무슨 색으로 보이는지 학습지에 쓴다.")
st.divider()

image = Image.open("./images/A_Sunday_on_La_Grande_Jatte.jpg")
red_channel, green_channel, blue_channel = image.split()
st.image(image)
np_zeros = np.zeros([image.size[1],image.size[0]], dtype=np.uint8)
zeros = Image.fromarray(np_zeros)

col1, col2, col3 = st.columns(3)

with col1:
    st.write("RedChannel")
    shift_r = st.slider("red",-255,255,value=0, step = 1, key="r")
    np_red_channel = np.array(red_channel).astype(int)
    np_red_channel_shift = np.clip(np_red_channel+shift_r, 0, 255)
    red_channel_np = Image.fromarray(np_red_channel_shift.astype('uint8'))
    merged_image = Image.merge("RGB", (red_channel_np, zeros, zeros))
    st.image(merged_image)
    
with col2:
    st.write("GreenChannel")
    shift_g = st.slider("green",-255,255,value=0, step = 1, key="g")
    np_green_channel = np.array(green_channel).astype(int)
    np_green_channel_shift = np.clip(np_green_channel+shift_g, 0, 255)
    green_channel_np = Image.fromarray(np_green_channel_shift.astype('uint8'))
    merged_image = Image.merge("RGB", (zeros, green_channel_np, zeros))
    st.image(merged_image)
    
    
with col3:
    st.write("BlueChannel")
    shift_b = st.slider("blue",-255,255,value=0, step = 1, key="b")
    np_blue_channel = np.array(blue_channel).astype(int)
    np_blue_channel_shift = np.clip(np_blue_channel+shift_b, 0, 255)
    blue_channel_np = Image.fromarray(np_blue_channel_shift.astype('uint8'))
    merged_image = Image.merge("RGB", (zeros, zeros, blue_channel_np))
    st.image(merged_image)
    
    
rgbmerged_image = Image.merge("RGB", (red_channel_np, green_channel_np, blue_channel_np))
st.image(rgbmerged_image)
st.divider()

st.subheader("개념 5. 물체의 색", divider='violet')
#video_file = open('./videos/물체의 색(교과개념자료).mp4', 'rb')
#video_bytes = video_file.read()
#st.video(video_bytes)
video_url = 'https://drive.google.com/uc?id=1j5lpIWUXQ8DOdc0vgkLDh5mfj_dWeVb2'
st.video(video_url)
image = Image.open("./images/물체의 색.png")
st.image(image)
st.markdown("물체의 색은 그 물체가 반사하는 빛의 색이다.")
st.markdown("물체가 빨간색 빛만 반사하면 빨간색으로 보이며,")
st.markdown("물체가 초록색 빛만 반사하면 초록색으로 보인다.")
st.markdown("물체가 반사하는 빛이 없다면 검은색으로 보인다.")
st.divider()

st.subheader("확인 문제", divider='violet')
st.markdown("1. 빛의 삼원색을 쓰시오.")
st.markdown("2. 스마트 기기 화면의 화소에서 (   )과 (   ) 빛을 켜면 노란색으로 표현된다.")
st.markdown("3. 햇빛이 빨간색 빛만 포함하고 있다면 현재 우리 주변 물체의 색이 어떻게 달라질지 설명해 보자.")
st.markdown("4. 점묘화의 원리를 설명해 보자.")
st.divider()
