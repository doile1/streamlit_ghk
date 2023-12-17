import pandas as pd
from PIL import Image
import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("3차시. 점묘화 그리기")
st.subheader("")
st.subheader("학습 목표", divider='violet')
st.markdown(" 3. 점묘화의 원리를 알고 효과적으로 표현할 수 있다.")
st.divider()

st.subheader("활동1. 점묘화 그리기", divider='violet')
st.markdown("점묘화를 감상한 후 여러 가지 색을 선택하여 점묘화를 그리고 저장해 봅시다.")
st.divider()

col1, col2, col3 = st.columns(3)

with col1:
    image = Image.open("./images/점묘화1.jpg")
    st.image(image)
with col2:
    image = Image.open("./images/점묘화2.jpg")
    st.image(image)
with col3:
    image = Image.open("./images/점묘화3.jpg")
    st.image(image)

st.divider()
# Specify canvas parameters in application
drawing_mode = st.sidebar.selectbox(
    "Drawing tool:", ("point", "freedraw", "line", "rect", "circle", "transform")
)

stroke_width = st.sidebar.slider("Stroke width: ", 1, 25, 3)
if drawing_mode == 'point':
    point_display_radius = st.sidebar.slider("Point display radius: ", 1, 25, 3)
stroke_color = st.sidebar.color_picker("Stroke color hex: ")
bg_color = st.sidebar.color_picker("Background color hex: ", "#eee")
realtime_update = st.sidebar.checkbox("Update in realtime", True)



# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    update_streamlit=realtime_update,
    width=600,
    height=600,
    drawing_mode=drawing_mode,
    point_display_radius=point_display_radius if drawing_mode == 'point' else 0,
    key="canvas",
)

# Do something interesting with the image data and paths
if canvas_result.image_data is not None:
    st.image(canvas_result.image_data)

st.divider()