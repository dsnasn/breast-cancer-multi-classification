import streamlit as st
from PIL import Image
from utils import load_models, preprocess_image, hierarchical_predict

# 设置页面标题和布局
st.set_page_config(page_title="Breast Cancer Diagnosis", layout="wide")

# 自定义页面样式
st.markdown(
    """
    <style>
    body {
        background-color: #fdfdfd;
    }
    .main-title {
        font-size: 2.5rem;
        color: #e91e63;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-title {
        font-size: 1.2rem;
        color: #555;
        text-align: center;
        margin-bottom: 20px;
    }
    .result-card {
        background-color: #f5f5f5;
        border: 2px solid #e91e63;
        border-radius: 10px;
        padding: 20px;
        text-align: center;
        margin-top: 20px;
    }
    .result-card h3 {
        margin: 0;
    }
    .result-card p {
        font-size: 1.1rem;
        margin: 10px 0 0 0;
    }
    .disclaimer {
        margin-top: 20px;
        color: #555;
        font-size: 1rem;
        text-align: center;
        border-top: 1px solid #ddd;
        padding-top: 10px;
    }
    .subtype-table {
        margin: 20px 0;
        text-align: left;
    }
    table {
        width: 100%;
        border-collapse: collapse;
    }
    th, td {
        border: 1px solid #ddd;
        padding: 8px;
    }
    th {
        background-color: #e91e63;
        color: white;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 页面头部
st.markdown('<div class="main-title">Breast Cancer Histopathology Diagnosis</div>', unsafe_allow_html=True)
st.markdown('<div class="sub-title">Upload a histopathology image to diagnose it as Benign or Malignant, and determine its subtype.</div>', unsafe_allow_html=True)

# 子类型说明表格
st.markdown(
    """
    <div class="subtype-table">
        <table>
            <tr>
                <th>Classification</th>
                <th>Subtype</th>
            </tr>
            <tr>
                <td><strong>Benign</strong></td>
                <td>Adenosis, Fibroadenoma, Phyllodes Tumor, Tubular Adenoma</td>
            </tr>
            <tr>
                <td><strong>Malignant</strong></td>
                <td>Ductal Carcinoma, Lobular Carcinoma, Mucinous Carcinoma, Papillary Carcinoma</td>
            </tr>
        </table>
    </div>
    """,
    unsafe_allow_html=True,
)

# 加载模型
with st.spinner("Loading Models..."):
    binary_model, benign_model, malignant_model = load_models()
st.sidebar.success("Models Loaded!")

# 上传图片
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    # 显示上传的图片
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_container_width=False, width=300, output_format="auto")

    # 图片预处理和分类
    processed_image = preprocess_image(image)
    binary_result, subtype_result = hierarchical_predict(processed_image, binary_model, benign_model, malignant_model)

    # 子类型映射
    benign_subtypes = ["Adenosis", "Fibroadenoma", "Phyllodes Tumor", "Tubular Adenoma"]
    malignant_subtypes = ["Ductal Carcinoma", "Lobular Carcinoma", "Mucinous Carcinoma", "Papillary Carcinoma"]

    if binary_result == "Benign":
        subtype_name = benign_subtypes[int(subtype_result.split(":")[-1].strip())]
        color = "green"
    else:
        subtype_name = malignant_subtypes[int(subtype_result.split(":")[-1].strip())]
        color = "red"

    # 显示结果（放在图片下方）
    st.markdown(
        f"""
        <div class="result-card">
            <h3 style="color: {color};">Binary Classification Result: {binary_result}</h3>
            <p>Subtype Classification Result: <strong>{subtype_name}</strong></p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    # 显示声明
    st.markdown(
        """
        <div class="disclaimer">
            <p><strong>Note:</strong> The diagnosis result provided by this application is for reference purposes only. Please consult a qualified medical professional for accurate diagnosis and further evaluation.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )
