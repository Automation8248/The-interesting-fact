import os
import requests

# GitHub Secrets
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.getenv("TELEGRAM_CHAT_ID")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")

VIDEO_DIR = "videos"

def upload_to_catbox(file_path):
    url = "https://catbox.moe/user/api.php"
    data = {"reqtype": "fileupload"}
    with open(file_path, "rb") as f:
        files = {"fileToUpload": f}
        response = requests.post(url, data=data, files=files)
    return response.text

def main():
    if not os.path.exists(VIDEO_DIR):
        print("Folder nahi mila")
        return

    # वीडियो फाइल्स की लिस्ट लेना
    video_files = sorted([f for f in os.listdir(VIDEO_DIR) if f.lower().endswith(('.mp4', '.mkv', '.mov'))])
    
    if not video_files:
        print("Koi video bacha nahi hai")
        return

    video_to_process = video_files[0]
    file_path = os.path.join(VIDEO_DIR, video_to_process)

    try:
        # Catbox पर अपलोड (Webhook के लिए लिंक)
        catbox_video_link = upload_to_catbox(file_path)
        
        # SEO Hashtags (सिर्फ Telegram के लिए)
        seo_hashtags = "#trending #viral #foryou #explore #instagram #reels #video #tiktok #fyp"

        # --- TELEGRAM FORMAT ---
        # इसमें वीडियो फाइल + डॉट्स + हैशटैग रहेंगे
        tg_caption = (
            f"New video post\n"
            f".\n"
            f".\n"
            f".\n"
            f".\n"
            f".\n"
            f"{seo_hashtags}"
        )

        # --- WEBHOOK FORMAT ---
        # इसमें सिर्फ वीडियो लिंक और कैप्शन रहेगा (No Dots, No Hashtags)
        webhook_content = f"{catbox_video_link}\nNew video post"

        # 1. Telegram पर डायरेक्ट वीडियो फाइल भेजना
        if BOT_TOKEN and CHAT_ID:
            tg_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
            with open(file_path, "rb") as video:
                requests.post(tg_url, files={"video": video}, data={"chat_id": CHAT_ID, "caption": tg_caption})

        # 2. Webhook पर सिर्फ लिंक और कैप्शन भेजना
        if WEBHOOK_URL:
            requests.post(WEBHOOK_URL, json={"content": webhook_content})

        # 3. सिर्फ इस्तेमाल हुई फाइल को डिलीट करना
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"Success: {video_to_process} post ho gaya aur file delete kar di gayi.")

    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
