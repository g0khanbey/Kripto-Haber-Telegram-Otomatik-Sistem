# 📰 Kripto Haber Telegram Otomatik Sistem

Bu proje, **Cryptopanic** haber API'sinden en güncel kripto para haberlerini çekerek, bunları belirlediğiniz bir **Telegram kanalında otomatik olarak paylaşan** Python tabanlı bir bottur.

## 🚀 Özellikler

- Cryptopanic API üzerinden en son kripto haberlerini çeker.
- Daha önce gönderilmiş haberle karşılaştırır, farklıysa otomatik olarak gönderir.
- Haber içeriğini `.txt` dosyalarına kaydeder.
- Telegram kanalına otomatik olarak yeni haber gönderir.
- `/start`, `/site`, ve `/youtube` gibi Telegram komutlarını destekler.
- 10 saniyede bir yeni haber kontrolü yapılır.

## 📁 Dosya Açıklamaları

### `main.py`

Telegram botunun çalıştığı ana dosyadır:

- `token.txt` dosyasından bot token’ını okur.
- Telegram komutlarını karşılar (`/start`, `/site`, `/youtube`).
- 10 saniyelik aralıklarla haber kontrolü yapar.
- Yeni bir haber tespit edildiğinde içeriğini `son_haber.txt` dosyasına yazar.
- Daha önceki içerikle karşılaştırır (`kontrol.txt`).
- Yeni ise belirlenen Telegram kanalına gönderir.

#### Kullanılan Modüller:
```python
import requests
import time
import telegram.ext
import telegram  
from telegram.ext import Updater, CommandHandler
