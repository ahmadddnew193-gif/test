import streamlit as st


if "player_count" not in st.session_state:
    st.session_state.vis = []
    st.session_state.plr = []

st.set_page_config(page_title="Camera Test", layout="wide")
st.title("📸 Camera & Audio Test")



cam = st.camera_input("Take a photo")
audio = st.audio_input("audio")

if cam:
    st.success("Photo captured!")
    st.download_button("Download Photo", data=cam.read(), file_name="photo.png")

