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
    try:
        with open(file_path, "rb") as f:
            files = {"fileToUpload": f}
            response = requests.post(url, data=data, files=files, timeout=30)
        if response.status_code == 200:
            return response.text
        return None
    except Exception as e:
        print(f"Catbox Upload Error: {e}")
        return None

def main():
    if not os.path.exists(VIDEO_DIR):
        print("Folder nahi mila")
        return

    # Files ki list (Alphabetical order)
    video_files = sorted([f for f in os.listdir(VIDEO_DIR) if f.lower().endswith(('.mp4', '.mkv', '.mov'))])
    
    if not video_files:
        print("Koi video bacha nahi hai")
        return

    # Pehli video file (Content)
    video_to_process = video_files[0]
    file_path = os.path.join(VIDEO_DIR, video_to_process)
    
    # Title extraction
    clean_title = os.path.splitext(video_to_process)[0]

    # Catbox Video Link generate karna
    catbox_url = upload_to_catbox(file_path)

    if catbox_url:
        # SEO Hashtags
        seo_hashtags = "#trending #viral #foryou #explore #instagram #reels #video #tiktok #fyp"

        # --- TELEGRAM FORMAT (Direct Video File, No hashtags) ---
        tg_caption = (
            f"New video post\n"
            f".\n"
            f".\n"
            f".\n"
            f".\n"
            f".\n"
            f"Daily Update"
        )

        # --- WEBHOOK CAPTION (Caption + Hashtags) ---
        # Jaisa aapne kaha: Ismein caption aur # dono rahenge
        full_webhook_caption = f"New video post\n{seo_hashtags}"

        # 1. Telegram par direct video file bhejna
        if BOT_TOKEN and CHAT_ID:
            try:
                tg_url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendVideo"
                with open(file_path, "rb") as video:
                    requests.post(tg_url, files={"video": video}, data={"chat_id": CHAT_ID, "caption": tg_caption}, timeout=30)
                print("Telegram send success.")
            except Exception as tg_err:
                print(f"Telegram Failed: {tg_err}")

        # 2. Webhook for Make.com (URL = Catbox Link)
        if WEBHOOK_URL:
            try:
                # 'url' field mein catbox video link jayega
                # 'caption' field mein text aur # dono jayenge
                payload = {
                    "url": catbox_url, 
                    "title": clean_title, 
                    "caption": full_webhook_caption
                }
                requests.post(WEBHOOK_URL, json=payload, timeout=10)
                print("Webhook send success.")
            except Exception as web_err:
                print(f"Webhook Failed: {web_err}")
        else:
            print("Warning: Webhook URL missing.")

        # 3. Sirf wahi file delete karna jo use hui hai
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"File {video_to_process} deleted.")

        print(f"Workflow Complete! Link used: {catbox_url}")
    else:
        print("Catbox Upload Failed.")

if __name__ == "__main__":
    main()
