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

## 📊 Performance Metrics

The project involves training and evaluating three models (`DenseNet121`) for binary and multi-class classification tasks. The results are as follows:

### Binary Classification (Benign vs. Malignant)
- **Test Accuracy**: **98.36%**
- **Model**: Fine-tuned `DenseNet121`
- **Dataset**: BreakHis (7,909 histopathology images)
- **Training Time**: ~889 seconds
- **Test Confusion Matrix**:

|                  | Predicted Benign | Predicted Malignant |
|------------------|------------------|---------------------|
| **Actual Benign**    | 1,350               | 50                  |
| **Actual Malignant** | 70                 | 1,430                |

### Multi-Class Classification (Benign Subtypes)
- **Test Accuracy**: **95.16%**
- **Classes**: TA, PT, A, F
- **Validation Accuracy**: ~92.11%

### Multi-Class Classification (Malignant Subtypes)
- **Test Accuracy**: **93.97%**
- **Classes**: DC, LC, MC, PC
- **Validation Accuracy**: ~89.90%

---

### Sample Outputs
1. **Input Image**: Histopathology image of suspected malignant tissue  
   **Prediction**: Malignant (Confidence: 97.2%)

2. **Input Image**: Histopathology image of benign tissue  
   **Prediction**: Benign (Confidence: 94.8%)  **Prediction**: Benign (Confidence: 94.8%)

---

### Deployment
The model has been deployed using Streamlit for real-time image uploads and predictions, enabling user-friendly interactions and accessibility.

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

- **Deep Learning Framework**: TensorFlow/Keras
- **Base Model**: DenseNet121 (Pre-trained)
- **Dataset**: [BreaKHis Dataset](https://www.kaggle.com/datasets/ambarish/breakhis?select=BreaKHis_v1)
- **Frontend**: Streamlit




