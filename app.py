import streamlit as st
from PIL import Image
import numpy as np
import io

from utils import convert_raw_to_rgb
from style_transfer import apply_histogram_match

st.title("📸 StyleMatch – Match Your RAW Photos to Your Edited Style")

ref_file = st.file_uploader("Upload your EDITED JPG (Reference Image)", type=["jpg", "jpeg"])
raw_file = st.file_uploader("Upload your RAW file", type=["cr2", "nef", "arw", "dng"])

if ref_file and raw_file:
    ref_img = Image.open(ref_file).convert("RGB")
    raw_rgb = convert_raw_to_rgb(raw_file)

    ref_resized = ref_img.resize((raw_rgb.shape[1], raw_rgb.shape[0]))
    ref_np = np.array(ref_resized)

    result = apply_histogram_match(raw_rgb, ref_np)

    st.image(result, caption="Edited Output", use_column_width=True)
    result_img = Image.fromarray(result)
    buf = io.BytesIO()
    result_img.save(buf, format="JPEG")
    byte_im = buf.getvalue()
    st.download_button("Download Result", byte_im, file_name="styled_result.jpg", mime="image/jpeg")