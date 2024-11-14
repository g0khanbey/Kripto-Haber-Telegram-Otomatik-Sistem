import requests
import time

# Cryptopanic API URL'si
api_url = "https://cryptopanic.com/api/v1/posts/?auth_token=345b58e07de1eabf54bcc8317cc27f6903928a7b&kind=news"

# Son alınan haber bilgisini tutmak için bir değişken
last_post_id = None

while True:
    # API'ye istek yap
    response = requests.get(api_url)

    # İstek başarılı mı kontrol et
    if response.status_code == 200:
        data = response.json()
        latest_post = data["results"][0]  # En son haber bilgisi
        
        # Eğer son alınan haber bilgisi ile aynı değilse, yeni haber var demektir
        if last_post_id != latest_post["id"]:
            last_post_id = latest_post["id"]
            
            title = latest_post["title"]
            published_at = latest_post["published_at"]
            url = latest_post["url"]
            
            # Eğer içerik almak istiyorsanız, içeriğin anahtar adını burada belirtin
            content = latest_post.get("content", "İçerik bulunmuyor.")
            
            with open("son_haber.txt", "w", encoding="utf-8") as file:
                file.write(f"Başlık: {title}\n")
                file.write(f"Yayın Tarihi: {published_at}\n")
                file.write(f"URL: {url}\n")
                file.write(f"İçerik: {content}\n")
            print("Yeni haber alındı.")
    else:
        print("API isteği başarısız oldu.")
    
    # 10 saniye bekle
    time.sleep(10)
