# Breast Cancer Histopathology Diagnosis  

| Benign Classification         | Malignant Classification         |
|-------------------------------|-----------------------------------|
| ![Benign GIF](test%20results/benign.gif) | ![Malignant GIF](test%20results/malignant.gif) |

> A web-based application for diagnosing breast cancer histopathology images as **Benign** or **Malignant** and identifying specific subtypes using advanced deep learning models.

---

## 📋 Features
- **Real-Time Classification**: Analyze histopathology images to classify them as **Benign** or **Malignant** and further identify their subtypes.  
  This provides detailed insights into the nature of the uploaded image.
- **Interactive Interface**: Upload histopathology images and receive instant predictions in a clean, intuitive interface.  
  Results are displayed with subtype names to enhance interpretability for users.
- **Educational Purpose**: Designed for educational purposes to demonstrate the potential of deep learning in medical imaging.  
  Note: This tool is not intended for clinical use.

---

## Subtype Classification

The application supports the following classifications and subtypes:

| **Classification** | **Subtype**                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| **Benign**          | Adenosis, Fibroadenoma, Phyllodes Tumor, Tubular Adenoma                   |
| **Malignant**       | Ductal Carcinoma, Lobular Carcinoma, Mucinous Carcinoma, Papillary Carcinoma |

---

## 🛠️ Quick Start
### Install Dependencies
Run the following command to install all required libraries:
```bash
pip install -r requirements.txt
```
### Download Model Files
This project requires pre-trained model files to function properly.
**Note**: The model files are not included in the repository.
Please contact the author to obtain the necessary model files.
### Run Locally
After downloading the model files and placing them in the `models/` directory, launch the Streamlit application:
```bash
streamlit run main.py
```

---

## ⚠️ Disclaimer
The diagnosis results provided by this application are for reference purposes only.
Please consult a qualified medical professional for accurate diagnosis and further evaluation.

---

## 📂 Project Structure
```bash
breast-cancer-multi-classification/
│
├── test results/         # GIFs for demonstration
├── models/
├── main.py               # Main Streamlit application
├── utils.py
├── requirements.txt      
└── README.md             
```

---

## 🧰 Technology Stack

- **Frontend**: Streamlit
- **Backend**: TensorFlow/Keras
- **Visualization**: Streamlit Components

---




