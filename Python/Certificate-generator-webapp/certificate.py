import cv2
import os
import base64
import streamlit as st
import numpy
import sys
from PIL import Image, ImageDraw
font = cv2.FONT_HERSHEY_SIMPLEX
fontScale = 3
activities = ["Get certificate","About"]
st.sidebar.image("pics//apricus.png")
choice=st.sidebar.selectbox("Select Activty",activities)


def get_binary_file_downloader_html(bin_file, file_label='File'):
    with open(bin_file, 'rb') as f:
        data = f.read()
    bin_str = base64.b64encode(data).decode()
    href = f'<a href="data:application/octet-stream;base64,{bin_str}" download="{os.path.basename(bin_file)}">Download {file_label}</a>'
    return href
def annotate(name):
    certi = cv2.imread("pics\\img.png")
    original = cv2.putText(certi, name, (710, 790),font,   fontScale, (0, 0, 0), thickness=5)
    cv2.imwrite("output/Certificate.jpg",original)


    if st.button("View certificate"):
        st.image(original, caption=None, width=350, use_column_width=None, clamp=False, channels='BGR',output_format='PNG')
        st.markdown(get_binary_file_downloader_html ('output\\original.jpg', 'Certificate'), unsafe_allow_html=True)

if choice =="Get certificate":
    st.title("Get Your Certificate")
    img=cv2.imread('C:\\Users\\Admin\Desktop\\github\\certificates_streamlit\\pics\\apricus.png')
    na=st.text_input('Enter your name')
    annotate(na)
    #st.markdown(get_binary_file_downloader_html(original, 'Picture'), unsafe_allow_html=True)


if choice =="About":
    st.subheader("Cerficate App")
    st.markdown("</> with ❤ by Apricus" )
    st.markdown("follow us on instagram 😃 (https://instagram.com/apricus_vjit?utm_medium=copy_link)")

