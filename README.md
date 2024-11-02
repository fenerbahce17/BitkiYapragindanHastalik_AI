Mango bitkisinin yaprağını kullanarak görüntü işleme ile hastalık tespiti  için model oluşturdum.Ve flask ile bu modeli kullanarak hastalığı ve çözümünü gösteren bir websitesi oluşturdum.




Ön Rapor:
1. Proje Tanımı 
Bu projede, mango yapraklarında meydana gelen hastalıkları görüntü verisi üzerinden tespit eden bir yapay zeka modeli geliştirilmiştir. Kullanıcılar, projemiz üzerinden yaprak fotoğraflarını yükleyerek hastalıklı yaprakları tanımlayıp tedavi önerilerine ulaşabilmektedir. Proje, tarımsal hastalıkları erken aşamada tespit ederek verim kaybını azaltmayı ve çiftçilere rehberlik etmeyi amaçlamaktadır.
2. Kullanılan Teknolojiler 
Bu projede Python programlama dili ve Flask web framework’ü kullanılmıştır. Flask, projenin web arayüzünü sağlamakta ve modeli kullanıcı dostu bir şekilde sunmaktadır. Model eğitiminde TensorFlow ve Keras kütüphanelerinden yararlanılmıştır. Görüntü verilerinin işlenmesinde ImageDataGenerator ve Image modülleri kullanılarak veri artırımı yapılmıştır.
3. Veri Kümesi
 Proje kapsamında kullanılan veri kümesi, Kaggle üzerinde yer alan “Mango Leaf Disease Dataset” adlı veri kümesinden alınmıştır. Bu veri kümesi, farklı hastalık türlerini içeren etiketlenmiş yaprak görüntülerinden oluşmaktadır. Toplamda sekiz sınıf yer almaktadır:
•	Anthracnose
•	Bacterial Canker
•	Cutting Weevil
•	Die Back
•	Gall Midge
•	Healthy
•	Powdery Mildew
•	Sooty Mould
4. Kullanılan Algoritmalar ve Modeller 
Proje kapsamında görüntü sınıflandırma işlemi için derin öğrenme modelleri ve optimizasyon teknikleri kullanılmıştır:
a)Derin Öğrenme (Deep Learning) ve Evrişimsel Sinir Ağları (CNN)
Evrişimsel Sinir Ağları (Convolutional Neural Networks - CNN): Bu model türü, özellikle görüntü verisi gibi yüksek boyutlu verilerde başarılıdır. CNN’ler katman katman filtreler uygulayarak, görüntünün kenar, doku ve renk gibi özelliklerini çıkarmaya yarar. İlk katmanlar daha temel özellikleri öğrenirken, son katmanlar daha karmaşık yapıları algılar.
Modelin Katmanları: Çeşitli evrişim (convolution) katmanları, havuzlama (pooling) katmanları ve son olarak yoğun bağlantılı (fully connected) katmanlar eklenerek görüntünün özellikleri çıkarılır. Bu modelde Conv2D, MaxPooling2D, Flatten, Dense gibi katmanlar kullanılmıştır.
Softmax Aktivasyon Fonksiyonu: Çıktı katmanında kullanılan softmax fonksiyonu, sınıf tahminlerini olasılık değerine dönüştürür. Bu sayede model, hastalık sınıfı ile sağlıklı sınıf arasında karar verebilir.
b) Veri Ön İşleme ve Artırma (Data Preprocessing and Augmentation)
Veri Artırma (Data Augmentation): Sınırlı sayıda eğitim verisi olduğunda modelin daha iyi genelleme yapabilmesi için kullanılır. Görüntülerde döndürme, ölçekleme, kırpma, yatay çevirme gibi işlemler yapılarak veri sayısı artırılır. Bu sayede model farklı pozisyonlarda ve ışık koşullarında da doğru tahmin yapabilir.
Ölçekleme (Normalization): Görüntü verilerindeki piksel değerleri genelde 0-255 arasındadır. Bu değerlerin 0 ile 1 arasına ölçeklenmesi, modelin daha hızlı ve verimli öğrenmesini sağlar.
c) Optimizasyon Algoritması: Adam
Adam Optimizasyon Algoritması (Adaptive Moment Estimation): Derin öğrenme modellerinde yaygın olarak kullanılan bir optimizasyon algoritmasıdır. Geri yayılım sırasında modelin ağırlıklarının güncellenmesi için gradyanları kullanır. Adam, öğrenme hızını otomatik olarak ayarlayarak modelin daha hızlı ve stabil bir şekilde optimize edilmesini sağlar.
d) Kayıp Fonksiyonu (Loss Function)
Kategorik Çapraz Entropi (Categorical Cross-Entropy): Bir sınıflandırma problemi olduğu için kullanılan kayıp fonksiyonudur. Modelin doğru tahmin yapabilmesi için tahmin edilen olasılık dağılımını gerçek sınıf dağılımıyla karşılaştırarak hatayı ölçer ve optimizasyon algoritması bu hatayı azaltmaya çalışır.
5. Proje Çıktıları
 Modelin test doğruluğu %90’ın üzerinde elde edilmiş olup gerçek dünya kullanımında performansı izlenmektedir. Web uygulamasına yüklenen görseller, model tarafından sınıflandırılarak kullanıcıya sunulmaktadır. Sonuç sayfasında, tespit edilen hastalık ile ilgili tanım, nedenleri ve tedavi yöntemleri açıklanmaktadır.
6. Sonuç ve Gelecek Çalışmalar 
Bu proje, mango yaprağı hastalıklarını otomatik olarak tespit ederek tarım sektöründe dijitalleşmeye katkı sağlamayı hedeflemektedir. Modelin doğruluğunu artırmak için daha fazla veri toplanarak veya modelin daha gelişmiş versiyonları kullanılarak performans iyileştirilebilir.

