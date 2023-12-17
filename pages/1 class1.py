import streamlit as st
from PIL import Image
import numpy as np

st.title("1차시. 빛의 삼원색과 빛의 합성")
st.subheader("")
st.subheader("학습 목표", divider='violet')
st.markdown("1. 빛의 합성으로 영상 장치에서 다양한 색이 표현되는 원리를 설명할 수 있다.")
st.divider()

st.subheader("점묘화를 가까이서 볼 때와 멀리서 볼 때 왜 다르게 보일까?", divider='violet')
image = Image.open("./images/A_Sunday_on_La_Grande_Jatte.jpg")
st.image(image)
st.markdown("조르주 쇠라의 그랑드자트 섬의 일요일 오후")
st.divider()

video_file = open('./videos/다양하게 보이는 색(생생개념영상).mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.divider()

st.subheader("탐구1. 스마트 기기에서 다양한 색이 표현되는 원리", divider='violet')
video_file = open('./videos/스마트 기기에서 다양한 색이 표현되는 원리(실험영상).mp4', 'rb')
video_bytes = video_file.read()
st.video(video_bytes)
st.markdown('##### **다음 과정에 따라 실험해 봅시다.**')
st.markdown(" 1. 확대경을 컴퓨터에 연결한다.")
st.markdown(" 2. RGB 슬라이드바를 조절하여 점묘화를 빨간색으로 바꾼다.")
st.markdown(" 3. 빨간색 화면 부분에 확대경을 대고 관찰하고 학습지에 사인펜으로 그린다.")
st.markdown(" 4. RGB 슬라이드바를 다시 조절하여 초록색, 파란색, 자홍색, 노란색, 청록색으로 바꾼다.")
st.markdown(" 5. 색이 나타난 화면 부분에 확대경을 대고 관찰하고 학습지에 사인펜으로 그린다.")
st.markdown(" 5. 스마트 기기에서 다양한 색이 어떻게 표현되는지 토의해본다.")
st.divider()
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

st.subheader("개념 1. 빛의 삼원색", divider='violet')
st.markdown("여러 가지 색을 표현하는 기본이 되는 빛")
st.markdown("빨간색, 초록색, 파란색")
st.divider()
st.subheader("개념 2. 빛의 합성", divider='violet')
st.markdown("두 가지 이상의 색의 빛을 합하여 다른 색의 빛을 얻는 것")
image = Image.open("./images/빛의 합성.png")
st.image(image)
st.divider()
st.subheader("개념 3. 영상 장치에서 다양한 색을 표현하는 원리", divider='violet')
st.markdown("각 화소에서 빨간색, 초록색, 파란색을 켜거나 꺼서 나오는 색이 합성되기 때문이다.")
st.divider()
st.subheader("개념 4. 빛의 합성 이용", divider='violet')
image = Image.open("./images/빛의 합성 이용.png")
st.image(image)
st.divider()
