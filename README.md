# 📈 Crypto Forecast App

![Language](https://img.shields.io/badge/language-TypeScript-blue) ![Backend](https://img.shields.io/badge/backend-Python-yellow) ![Docker](https://img.shields.io/badge/docker-supported-2496ED) ![License](https://img.shields.io/badge/license-MIT-green)

Bu proje, kripto para piyasalarındaki geçmiş verileri analiz ederek makine öğrenmesi yöntemleriyle gelecek fiyat tahminleri sunan bir web uygulamasıdır. Modern bir **Client-Server** mimarisine sahiptir ve **Docker** ile kolayca dağıtılabilir.

## 🚀 Proje Hakkında

Uygulama, kullanıcıların Bitcoin, Ethereum gibi popüler kripto paraların geçmiş performanslarını incelemesine ve Python tabanlı tahmin modelleri sayesinde olası gelecek trendlerini görüntülemesine olanak tanır.

**Temel Özellikler:**
* 📊 **Veri Görselleştirme:** Kripto para verilerinin interaktif grafiklerle sunumu.
* 🤖 **Fiyat Tahmini:** Python (Scikit-learn/Pandas) kullanılarak oluşturulan tahmin modelleri.
* ⚡ **Modern Arayüz:** TypeScript ve React tabanlı hızlı kullanıcı deneyimi.
* 🐳 **Docker Desteği:** Tek komutla tüm ortamın (Frontend + Backend) ayağa kaldırılması.

## 🛠️ Teknolojiler

Proje iki ana katmandan oluşmaktadır:

### 1. Client (Frontend)
* **Dil:** TypeScript
* **Framework:** React (veya Next.js)
* **Stil:** CSS / Tailwind
* **İletişim:** REST API

### 2. Server (Backend)
* **Dil:** Python
* **Framework:** Flask / FastAPI
* **Veri Analizi:** Pandas, NumPy
* **ML Kütüphaneleri:** Scikit-learn (Tahmin algoritmaları için)

## 📂 Proje Yapısı

```bash
crypto-forecast-app/
├── client/          # TypeScript tabanlı Frontend uygulaması
├── server/          # Python tabanlı Backend ve Tahmin API'si
├── docker-compose.yml # Konteyner orkestrasyon dosyası
└── README.md
```

## ⚙️ Kurulum ve Çalıştırma

Projeyi çalıştırmanın en kolay yolu **Docker** kullanmaktır.

### Seçenek 1: Docker ile Çalıştırma (Önerilen)

1. **Projeyi klonlayın:**
   ```bash
   git clone [https://github.com/furkanozturk06/crypto-forecast-app.git](https://github.com/furkanozturk06/crypto-forecast-app.git)
   cd crypto-forecast-app
   
## 👨‍💻 Geliştirici
Furkan Öztürk

GitHub: @furkanozturk06
