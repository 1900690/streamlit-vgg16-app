import streamlit as st
from PIL import Image
from classify import predict

st.title("アップロードした画像を解析します")

uploaded_file = st.file_uploader("画像を選択してください...", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='画像をアップロードしています', use_column_width=True)
    st.write("")
    st.write("分析中です...")
    label = predict(uploaded_file)
    st.write('%s (%.2f%%)' % (label[1], label[2]*100))