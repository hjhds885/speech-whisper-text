import streamlit as st
import cv2
from streamlit_webrtc import VideoTransformerBase, webrtc_streamer

class VideoTransformer(VideoTransformerBase):
    def transform(self, frame):
        # フレームをRGBに変換
        img = frame.to_ndarray(format="bgr")
        # OpenCVで処理を行うことも可能 (例: imgをグレースケールに変換)
        # img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        return img

st.title("Webカメラの認識デモ")

# WebRTCを使用してカメラにアクセス
webrtc_streamer(key="example", video_transformer_factory=VideoTransformer)
