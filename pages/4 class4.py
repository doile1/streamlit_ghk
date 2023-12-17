import os
import streamlit as st
from PIL import Image

st.title("4차시. 점묘화 감상하기")
st.subheader("")
st.subheader("학습 목표", divider='violet')
st.markdown(" 4. 빛의 원리를 생각하며 점묘화를 감상할 수 있다.")
st.divider()

st.subheader("활동2. 점묘화 감상하기", divider='violet')
st.markdown("내가 그린 점묘화를 업로드하고 우리반의 점묘화를 보고 감상문을 써봅시다.")
st.divider()

myname = st.text_input('이름을 입력해주세요.')
if myname is None or myname == '':
    st.warning('이름을 입력하세요.')
else:
    st.success('이름 입력 완료')

# 파일 저장하는 함수 정의
def save_uploaded_file(directory, file):
    if not os.path.exists(directory):
        os.makedirs(directory)

    with open(os.path.join(directory, file.name),'wb') as f: 
        f.write(file.getbuffer())
        
    return st.success('파일 업로드 완료')
    
paintingfile = st.file_uploader('점묘화 그림 파일 업로드하기')

# 제출 버튼
image_folder = os.getcwd() + '/images2'

# 'images2' 디렉토리가 존재하는지 확인하고, 없다면 생성합니다.
if not os.path.exists(image_folder):
    os.makedirs(image_folder)

# 제출 버튼이 눌렸을 때만 파일 리스트를 가져옵니다.
if st.button('점묘화 갤러리 만들기', use_container_width = True):
    if paintingfile is None:
        st.warning('파일을 업로드하세요.')
    elif myname is None or myname == '':
        st.warning('이름을 입력하세요.')
    else:
        filename = myname + '.jpg'
        paintingfile.name = filename
        save_uploaded_file('images2', paintingfile)

        files = os.listdir(image_folder)
        image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
        my_range = range(len(image_files))

st.divider()


st.subheader('점묘화 갤러리', divider='rainbow')
# 그래프 모음집 업데이트
cols = st.columns(3)

image_folder = os.getcwd() + '/images2'
files = os.listdir(image_folder)
image_files = [f for f in files if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
#print(image_files)
my_range = range(len(image_files))

for i in my_range:
    with cols[i % 3]:
        st.image('images2' + '/' + image_files[int(i)], caption = image_files[int(i)])

st.divider()

st.subheader('감상문 작성', divider='rainbow')
# 학생의 감상문 입력 받기
student_result = st.text_input("**감상문을 써주세요.**")
# 학생의 감상문 보여주기
if st.button('감상문 제출'):
    st.write(f"**'{student_result}'** 라고 감상했군요! 수고했어요.")

st.divider()