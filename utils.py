import tensorflow as tf
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

# 自定义 L2NormalizeLayer 类
class L2NormalizeLayer(tf.keras.layers.Layer):
    def __init__(self, axis=-1, **kwargs):
        super(L2NormalizeLayer, self).__init__(**kwargs)
        self.axis = axis

    def call(self, inputs):
        return tf.nn.l2_normalize(inputs, axis=self.axis)

    def get_config(self):
        config = super().get_config()
        config.update({'axis': self.axis})
        return config

# 加载模型函数
def load_models():
    binary_model = load_model('models/best_binary_model.h5', custom_objects={'L2NormalizeLayer': L2NormalizeLayer})
    benign_model = load_model('models/best_benign_model.h5', custom_objects={'L2NormalizeLayer': L2NormalizeLayer})
    malignant_model = load_model('models/best_malignant_model.h5', custom_objects={'L2NormalizeLayer': L2NormalizeLayer})
    return binary_model, benign_model, malignant_model

# 图片预处理函数
def preprocess_image(image, target_size=(128, 128)):
    """调整图片大小并归一化"""
    image = image.resize(target_size)  # 调整大小
    image_array = img_to_array(image) / 255.0  # 转换为 NumPy 数组并归一化
    return np.expand_dims(image_array, axis=0)  # 添加批次维度

# 分类预测函数
def hierarchical_predict(image, binary_model, benign_model, malignant_model):
    """使用层级模型进行预测"""
    binary_pred = binary_model.predict(image, verbose=0)
    binary_class = np.argmax(binary_pred, axis=1)[0]  # 二分类类别

    if binary_class == 0:  # 如果是良性
        subtype_pred = benign_model.predict(image, verbose=0)
        subtype_class = np.argmax(subtype_pred, axis=1)[0]
        return "Benign", f"Subtype: {subtype_class}"
    else:  # 如果是恶性
        subtype_pred = malignant_model.predict(image, verbose=0)
        subtype_class = np.argmax(subtype_pred, axis=1)[0]
        return "Malignant", f"Subtype: {subtype_class}"
