import streamlit as st
from PIL import Image
import numpy as np
import random

# -----------------------------
# Streamlit Page Configuration
# -----------------------------
st.set_page_config(page_title="Color Picker", layout="centered", page_icon="🎨")
st.title("🎨 Color Picker")
st.markdown(
    "Upload an image to extract the **5 most dominant colors** using a **K-Means clustering algorithm**"
)

# -----------------------------
# Helper: RGB to HEX
# -----------------------------
def rgb_to_hex(rgb):
    return '#%02x%02x%02x' % tuple(rgb)

# -----------------------------
# Manual K-Means Implementation
# -----------------------------
def initialize_centroids(data, k):
    indices = random.sample(range(data.shape[0]), k)
    return data[indices]

def assign_clusters(data, centroids):
    distances = np.linalg.norm(data - centroids[:, np.newaxis], axis=2)
    return np.argmin(distances, axis=0)

def update_centroids(data, labels, k):
    return np.array([
        data[labels == i].mean(axis=0) if np.any(labels == i)
        else data[random.randint(0, data.shape[0]-1)]
        for i in range(k)
    ])

def kmeans_from_scratch(data, k=5, max_iter=100):
    centroids = initialize_centroids(data, k)
    for _ in range(max_iter):
        labels = assign_clusters(data, centroids)
        new_centroids = update_centroids(data, labels, k)
        if np.allclose(centroids, new_centroids):
            break
        centroids = new_centroids
    return np.round(centroids).astype(int)

# -----------------------------
# File Upload
# -----------------------------
uploaded_image = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

if uploaded_image:
    image = Image.open(uploaded_image).convert("RGB")
    st.image(image, caption="Uploaded image", use_container_width=True)

    # Resize and flatten image for faster processing
    image = image.resize((200, 200))
    pixels = np.array(image).reshape(-1, 3)

    with st.spinner("Extracting colors..."):
        dominant_colors = kmeans_from_scratch(pixels, k=5)

    # -----------------------------
    # Display Result
    # -----------------------------
    st.markdown("## 🎨 Dominant Colors")
    cols = st.columns(5)

    for i, color in enumerate(dominant_colors):
        hex_code = rgb_to_hex(color)
        rgb_clean = tuple(int(c) for c in color)
        with cols[i]:
            st.markdown(
                f"<div style='background-color:{hex_code}; height:100px; border-radius:10px'></div>",
                unsafe_allow_html=True
            )
            st.markdown(f"**HEX:** `{hex_code}`")
            st.markdown(f"**RGB:** `{rgb_clean}`")

    st.success("Colors extracted successfully! 🎉")

else:
    st.info("Please upload an image to start.")

# -----------------------------
# Footer
# -----------------------------
st.markdown("---")
st.caption("Built using Streamlit and pure Python K-Means.")
