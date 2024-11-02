from flask import Flask, request, render_template
from keras.models import load_model
import numpy as np
from tensorflow.keras.preprocessing import image
import os  # Bu satırı ekleyin

app = Flask(__name__)

# Modeli yükle
model = load_model('C:\\Users\\halil\\OneDrive\\Masaüstü\\AI proje\\mango_leaf_disease_model.h5')



# Hastalık bilgileri (daha önce sağladığınız bilgiler)
disease_info = {
    'Anthracnose': {
        'description': 'Anthracnose: Yapraklarda koyu lekeler oluşturan mantar hastalığıdır.',
        'cause': 'Sıcak ve nemli havalarda yayılır.',
        'treatment': 'Fungisit uygulamaları ve hastalıklı yaprakların temizlenmesi.'
    },
    'Bacterial Canker': {
        'description': 'Bacterial Canker: Yapraklarda su lekeleri ve çürüme yapar.',
        'cause': 'Bakteriyel enfeksiyonlar nedeniyle ortaya çıkar.',
        'treatment': 'Bakterisit uygulamaları ve hastalıklı kısımların kesilmesi.'
    },
    'Cutting Weevil': {
        'description': 'Cutting Weevil: Yaprakları delip beslenen böceklerdir.',
        'cause': 'Böceklerin zararlılığı nedeniyle yapraklar zarar görür.',
        'treatment': 'Zararlı böcekler için insektisit kullanımı.'
    },
    'Die Back': {
        'description': 'Die Back: Dal ve yaprakların kurumasına neden olan bir hastalıktır.',
        'cause': 'Çevresel stresler ve patojenler nedeniyle gelişir.',
        'treatment': 'Köklendirme ve kuruyan kısımların kesilmesi.'
    },
    'Gall Midge': {
        'description': 'Gall Midge: Yapraklarda şişkinlik ve deformasyonlar oluşturur.',
        'cause': 'Böceklerin larvaları yaprak içinde beslenir.',
        'treatment': 'İlaçlama ve zarar gören yaprakların temizlenmesi.'
    },
    'Healthy': {
        'description': 'Healthy: Sağlıklı mango yaprakları.',
        'cause': 'Doğru bakım ve sağlıklı koşullar.',
        'treatment': 'Düzenli sulama ve gübreleme.'
    },
    'Powdery Mildew': {
        'description': 'Powdery Mildew: Yapraklarda beyaz toz benzeri mantar görünümü oluşturur.',
        'cause': 'Hava koşullarındaki aşırı nem.',
        'treatment': 'Fungisit uygulamaları ve iyi hava sirkülasyonu sağlama.'
    },
    'Sooty Mould': {
        'description': 'Sooty Mould: Yapraklarda siyah toz görünümü oluşturur.',
        'cause': 'Saklama böcekleri tarafından üretilen yapışkan maddeler.',
        'treatment': 'Böcek kontrolü ve iyi bakım.'
    }
}

# 'uploads' klasörünü kontrol et ve oluştur
if not os.path.exists('uploads'):
    os.makedirs('uploads')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'file' not in request.files:
        return 'Dosya yok'

    file = request.files['file']
    if file.filename == '':
        return 'Dosya seçilmedi'

    # Görüntüyü yükle
    img_path = f'uploads/{file.filename}'  # Dosyayı uygun bir dizine kaydet
    file.save(img_path)

    # Görüntüyü işleme
    img = image.load_img(img_path, target_size=(224, 224))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)

    # Tahmin yap
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions)

    # Sınıf ismini al
    class_names = ['Anthracnose', 'Bacterial Canker', 'Cutting Weevil', 'Die Back', 'Gall Midge', 'Healthy', 'Powdery Mildew', 'Sooty Mould']
    predicted_class = class_names[predicted_class_index]

    # Hastalık bilgilerini al
    disease_description = disease_info[predicted_class]['description']
    disease_cause = disease_info[predicted_class]['cause']
    disease_treatment = disease_info[predicted_class]['treatment']

    return render_template('result.html', 
                           predicted_class=predicted_class, 
                           disease_description=disease_description, 
                           disease_cause=disease_cause, 
                           disease_treatment=disease_treatment)

if __name__ == '__main__':
    app.run(debug=True)

import numpy as np
from keras.models import load_model
from keras.preprocessing import image

# Modelinizi yükleyin
model = load_model('C:\\Users\\halil\\OneDrive\\Masaüstü\\AI proje\\mango_leaf_disease_model.h5')



# Test etmek istediğiniz resmin yolunu belirtin
img_path = 'path_to_your_image.jpg'  # Burayı güncelleyin

# Resmi yükleyin ve modelin girdi boyutuna uygun hale getirin
img = image.load_img(img_path, target_size=(224, 224))  # Modelinizin beklediği boyut
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)

# Tahmin yapın
predictions = model.predict(img_array)
predicted_class = np.argmax(predictions[0])  # Tahmin edilen sınıfı alın

# Sınıf isimlerinizi buraya ekleyin
class_names = ['Anthracnose', 'Bacterial Canker', 'Cutting Weevil', 'Die Back', 'Gall Midge', 'Healthy', 'Powdery Mildew', 'Sooty Mould']

print(f'Tahmin edilen sınıf: {class_names[predicted_class]}')