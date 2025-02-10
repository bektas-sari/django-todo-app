# ✅ Django To-Do App

Bu proje, Django kullanarak geliştirilmiş **modern ve şık bir To-Do (Görev Listesi) uygulamasıdır**. Kullanıcılar görev ekleyebilir, tamamlayabilir ve silebilir. **Bootstrap 5 ve JavaScript animasyonları** ile dinamik bir deneyim sunar.

## 🚀 Özellikler
- 🏃 **Yeni görev ekleme (fade-in animasyonlu)**
- ✅ **Görev tamamlama (yeşil parlama efekti)**
- ❌ **Görev silme (fade-out animasyonlu)**
- 🎨 **Bootstrap ile modern ve mobil uyumlu tasarım**
- 🔄 **Hafif ve hızlı, veritabanı destekli**

## 📌 Kurulum ve Çalıştırma

### 1️⃣ Depoyu Klonla
```
git clone https://github.com/bektas-sari/django-todo-app.git
cd django-todo-app
```

### 2️⃣ Sanal Ortamı Başlat ve Gerekli Kütüphaneleri Yükle
```
python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate  # Windows
pip install -r requirements.txt
```

### 3️⃣ Veritabanını Ayarla ve Sunucuyu Çalıştır
```
python manage.py migrate
python manage.py createsuperuser  # (Opsiyonel, admin paneli için)
python manage.py runserver
```

Şimdi tarayıcıda şu adrese git: http://127.0.0.1:8000/

📜 Kullanılan Teknolojiler
* Python 3, Django
* Bootstrap 5, JavaScript
* SQLite (Django default database)

🔥 Katkıda Bulunma
1 - Fork yaparak projeyi kendi hesabınıza kopyalayın.
2 - Yeni bir branch oluşturun
```
git checkout -b yeni-ozellik
```
3 - Değişiklikleri yapın ve commit edin:
```
git commit -m "Yeni özellik eklendi"

```
4 - Değişiklikleri kendi GitHub reposunuza gönderin:
```
git push origin yeni-ozellik
```
5 - Pull Request (PR) gönderin! 🎉

📩 İletişim
Bir hata bildirimi veya geliştirme öneriniz varsa, issue açabilir veya bana GitHub üzerinden ulaşabilirsiniz.

MIT Lisansı © 2025 Bektas SARI
