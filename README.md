# 🎨 Color Picker (with K-Means)

A simple web app built with Streamlit that extracts the **5 most dominant colors** from uploaded image using **K-Means Clustering algorithm**.
---

Access the color picker program by clicking this link https://dominantcolorpicker.streamlit.app/

## 🚀 Features

- 🖼️ Upload any `.jpg`, `.jpeg`, or `.png` image
- 🧠 Color extraction using **K-Means**
- 🎨 Displays **5 dominant colors** with:
  - Live color preview blocks
  - HEX codes (e.g. `#ff5733`)
  - RGB values (e.g. `(255, 87, 51)`)
- 💅 Modern dark-mode UI with hover effects, rounded blocks, and clean layout
- 🧩 No need for `scikit-learn` or other ML packages — perfect for learning how K-Means works under the hood

---

## 🧠 How It Works

Each pixel in the image is treated as a 3D data point (R, G, B). The app:

1. **Resizes** the image for efficiency
2. **Flattens** the pixel array
3. **Initializes** random centroids (colors)
4. **Assigns** each pixel to the nearest centroid (Euclidean distance)
5. **Updates** centroids based on pixel averages
6. Repeats until convergence
