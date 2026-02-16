import os
import json
import random
import requests
import datetime

# --- CONFIGURATION ---
VIDEO_FOLDER = "videos"
HISTORY_FILE = "history.json"
TELEGRAM_BOT_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")
WEBHOOK_URL = os.environ.get("WEBHOOK_URL")

# Yahan maine image se dekh kar aapka exact Repo Name daal diya hai
GITHUB_REPO = "Automation8248/offernix-page-" 
BRANCH_NAME = "main"

# --- DATA GRID (Pre-saved Titles & Captions) ---

# List 1: Titles (Har bar inme se koi ek randomly select hoga)
TITLES_GRID = [
    "Facts That Will Change The Way You See The World",
    "Science Explained In The Simplest Way Possible",
    "You Won’t Believe This Is Actually Real Science",
    "Hidden Facts Nobody Talks About",
    "The Truth Behind What We See Every Day",
    "Mind-Blowing Facts You Should Know Today",
    "Things Science Finally Explained",
    "Reality Is Stranger Than You Think",
    "The World Works Differently Than You Imagine",
    "The Logic Behind Everyday Life",
    "What Really Happens Around You",
    "Secrets Of Nature Finally Revealed",
    "This Will Make You Question Reality",
    "Facts That Sound Fake But Are True",
    "Science Facts You Can’t Unlearn",
    "The Hidden Rules Of The Universe",
    "What Nobody Taught You In School",
    "Real Facts That Feel Impossible",
    "Everyday Things Explained By Science",
    "The Mystery Behind Common Things",
    "Why This Actually Happens",
    "Explained In 60 Seconds",
    "You See This Daily But Never Noticed",
    "Science Behind The Ordinary",
    "The Most Interesting Knowledge Today",
    "Facts That Will Blow Your Mind",
    "The Secret Life Of Everything",
    "Simple Science That Feels Like Magic",
    "Truths We Ignore Every Day",
    "Reality vs What You Think",
    "Things You Didn’t Know Exist",
    "The Real Reason Behind It",
    "This Changes Everything",
    "The Science Of Everyday Life",
    "Your Brain Will Love This",
    "One Minute Knowledge Boost",
    "What Actually Happens",
    "The Hidden Side Of Reality",
    "Things You Never Questioned",
    "The Most Interesting Explanation Ever",
    "Science Made Easy",
    "The Truth Is More Interesting Than Fiction",
    "This Knowledge Is Powerful",
    "Why The World Works Like This",
    "The Secret Mechanics Of Life",
    "Facts That Feel Illegal To Know",
    "The Unknown Side Of Common Things",
    "Stop Scrolling & Learn This",
    "The Most Useful Facts Today",
    "Knowledge You’ll Remember Forever",
    "The Universe Is Weird",
    "Reality Is Not What It Seems",
    "Understanding The World Better",
    "This Is How It Really Works",
    "You’ve Been Thinking Wrong",
    "Science Reveals The Truth",
    "Amazing Facts In Under A Minute",
    "The Smartest Thing You’ll Watch Today",
    "Real Knowledge In Simple Words",
    "Science That Feels Unreal",
    "The Most Fascinating Truths",
    "Watch This Before Sleeping",
    "Curiosity Solved",
    "Everything Has A Reason",
    "This Is Not A Coincidence",
    "Things Explained Clearly",
    "The World Is Smarter Than Us",
    "The Logic Of Nature",
    "Real Facts No One Tells",
    "The Science Behind The Scenes",
    "Learn Something New Today",
    "The Ultimate Knowledge Dose",
    "Facts Worth Knowing",
    "Science Is Beautiful",
    "A Short Video With Big Knowledge",
    "How Reality Actually Functions",
    "You Didn’t Notice This",
    "The Hidden Pattern Of Life",
    "This Makes Perfect Sense",
    "Knowledge In Its Purest Form",
    "Explained Like Never Before",
    "Everything Connects Somehow",
    "Your Perspective Will Change",
    "Things Are Not Random",
    "Small Facts Big Meaning",
    "Understanding Reality Better",
    "The Amazing Truth",
    "Knowledge Everyone Should Have",
    "The World Is Full Of Secrets",
    "Curiosity Answered",
    "This Will Surprise You",
    "Facts You Can’t Ignore",
    "Science Behind The Mystery",
    "How Nature Tricks Us",
    "Real Information No Clickbait",
    "The Explanation You Needed",
    "A New Way To See Things",
    "Think About This",
    "The Logic Behind The Mystery",
    "Everything Happens For A Reason",
    "What Science Discovered",
    "Truth Hidden In Plain Sight",
    "The Unknown Reality",
    "Simple Yet Powerful Knowledge",
    "You Learned Something Today",
    "Curiosity Starts Here",
    "Real Knowledge Only",
    "The World Is More Interesting Than You Think",
    "Everyday Mysteries Solved",
    "This Will Make Sense Now",
    "Facts That Feel Like Fiction",
    "The Power Of Understanding",
    "Think Smarter Not Harder",
    "One Idea That Changes Everything",
    "Reality Explained Clearly",
    "This Is Pure Science",
    "Knowledge Without Complication",
    "Learn This In One Minute",
    "The Most Valuable Information Today",
    "Smart People Will Love This"
]



# List 2: Captions (Har bar inme se koi ek randomly select hoga)
CAPTIONS_GRID = [
    "Knowledge you didn’t know you needed.",
    "Small fact, big meaning.",
    "Learn something new today.",
    "The world is more interesting than it looks.",
    "Reality explained simply.",
    "Now this makes sense.",
    "One minute smarter.",
    "Curiosity satisfied.",
    "You won’t forget this.",
    "Simple but powerful knowledge.",
    "Understanding made easy.",
    "The truth behind everyday life.",
    "Smart facts daily.",
    "Keep learning, keep growing.",
    "Science is everywhere.",
    "Things finally explained.",
    "Think about this.",
    "Hidden truth revealed.",
    "Not magic, just science.",
    "Knowledge = power.",
    "Your daily brain upgrade.",
    "This changes perspective.",
    "Learn • Understand • Remember",
    "Facts that matter.",
    "Now you know.",
    "Tiny lesson for today.",
    "Curiosity unlocked.",
    "You learned something valuable.",
    "Stay curious.",
    "The more you know.",
    "Information worth sharing.",
    "A smarter internet today.",
    "Short video, big knowledge.",
    "Explained in seconds.",
    "Worth your attention.",
    "This is real.",
    "Understand the world better.",
    "Facts over myths.",
    "Mind officially blown.",
    "Knowledge never wastes time.",
    "Learning never stops.",
    "Every day is a learning day.",
    "Your brain will thank you.",
    "Save this for later.",
    "Share knowledge, spread curiosity.",
    "Smart people watch this.",
    "You didn’t notice this before.",
    "Keep your mind active.",
    "Truth hidden in plain sight.",
    "Just science doing its job.",
    "Something new every day.",
    "Now life makes more sense.",
    "Think deeper.",
    "Observe carefully.",
    "Reality is fascinating.",
    "Short but meaningful.",
    "Daily dose of facts.",
    "You’re smarter than yesterday.",
    "This was interesting.",
    "Knowledge unlocked.",
    "Worth remembering.",
    "Curiosity never fails.",
    "More facts coming soon.",
    "Stay informed.",
    "Learn fast.",
    "Simple explanation matters.",
    "The world explained briefly.",
    "Knowledge in 10 seconds.",
    "Smart scrolling approved.",
    "You came for a reason.",
    "Understand don’t just watch.",
    "Now you see differently.",
    "One concept at a time.",
    "Facts make life clearer.",
    "This is useful knowledge.",
    "Your mind just leveled up.",
    "Observe the world smarter.",
    "Brain food.",
    "Quick learning moment.",
    "Think smarter today.",
    "That’s interesting, right?",
    "More knowledge ahead.",
    "Save and learn later.",
    "Education made simple.",
    "The logic of reality.",
    "Learning is addictive.",
    "Information matters.",
    "Smart content only.",
    "Worth your time.",
    "Science makes sense.",
    "Expand your mind.",
    "The explanation you needed.",
    "Now everything connects.",
    "Useful fact today.",
    "Knowledge never gets old.",
    "Understanding is powerful.",
    "Curiosity wins again.",
    "Simple knowledge everyday.",
    "Short learning break.",
    "Your daily fact dose.",
    "Watch, learn, repeat."
]



# List 3: Fixed Hashtags (Ye har video me SAME rahega)
FIXED_HASHTAGS = """
.
.
.
.
.
#facts #science #didyouknow #mindblowing #interestingfacts #amazingfacts #sciencefacts #knowledge #learnsomethingnew #education #howthingswork #explained #universe #spacefacts #psychologyfacts #brainfacts #dailyfacts #viral #trending #fyp #explorepage #reels #shorts #youtubeshorts #shortvideo #viralshorts #trendingreels #ytshorts #educationalvideo #factvideo """
# Isse AFFILIATE_HASHTAGS se badal kar INSTA_HASHTAGS kar diya hai
INSTA_HASHTAGS = """
.
.
.
.
"#facts #sciencefacts #didyouknow #mindblowingfacts #learnsomethingnew"
"""

# --- HELPER FUNCTIONS ---

def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []
    with open(HISTORY_FILE, 'r') as f:
        return json.load(f)

def save_history(data):
    with open(HISTORY_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# --- MAIN LOGIC ---

def run_automation():
    # 1. DELETE OLD FILES (15 Days Logic)
    history = load_history()
    today = datetime.date.today()
    new_history = []
    
    print("Checking for expired videos...")
    for entry in history:
        sent_date = datetime.date.fromisoformat(entry['date_sent'])
        days_diff = (today - sent_date).days
        
        file_path = os.path.join(VIDEO_FOLDER, entry['filename'])
        
        if days_diff >= 15:
            if os.path.exists(file_path):
                os.remove(file_path)
                print(f"DELETED EXPIRED: {entry['filename']}")
        else:
            new_history.append(entry)
    
    save_history(new_history)
    history = new_history 

    # 2. PICK NEW VIDEO
    if not os.path.exists(VIDEO_FOLDER):
        os.makedirs(VIDEO_FOLDER)
        
    all_videos = [f for f in os.listdir(VIDEO_FOLDER) if f.lower().endswith(('.mp4', '.mov', '.mkv'))]
    sent_filenames = [entry['filename'] for entry in history]
    
    available_videos = [v for v in all_videos if v not in sent_filenames]
    
    if not available_videos:
        print("No new videos to send.")
        return

    video_to_send = random.choice(available_videos)
    video_path = os.path.join(VIDEO_FOLDER, video_to_send)
    
    print(f"Selected Video File: {video_to_send}")

    # 3. RANDOM SELECTION (Grid System)
    selected_title = random.choice(TITLES_GRID)
    selected_caption = random.choice(CAPTIONS_GRID)
    
    # Combine content
    full_telegram_caption = f"{selected_title}\n\n{selected_caption}\n{FIXED_HASHTAGS}"
    
    print(f"Generated Title: {selected_title}")
    print(f"Generated Caption: {selected_caption}")

    # 4. SEND TO TELEGRAM
    if TELEGRAM_BOT_TOKEN and TELEGRAM_CHAT_ID:
        print("Sending to Telegram...")
        with open(video_path, 'rb') as video_file:
            url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendVideo"
            payload = {
                'chat_id': TELEGRAM_CHAT_ID, 
                'caption': full_telegram_caption
            }
            files = {'video': video_file}
            try:
                requests.post(url, data=payload, files=files)
            except Exception as e:
                print(f"Telegram Error: {e}")

    # 5. SEND TO WEBHOOK
    if WEBHOOK_URL:
        print("Sending to Webhook...")
        # URL construction with your specific repo name
        raw_video_url = f"https://raw.githubusercontent.com/{GITHUB_REPO}/{BRANCH_NAME}/{VIDEO_FOLDER}/{video_to_send}"
        # Encode spaces if any
        raw_video_url = raw_video_url.replace(" ", "%20")
        
        webhook_data = {
            "video_url": raw_video_url,
            "title": selected_title,
            "caption": selected_caption,
            "hashtags": FIXED_HASHTAGS,
            "insta_hashtags": INSTA_HASHTAGS, # Make.com mein isi naam se field aayegi
            "source": "AffiliateBot"
        }
        try:
            requests.post(WEBHOOK_URL, json=webhook_data)
            print(f"Webhook Sent: {raw_video_url}")
        except Exception as e:
            print(f"Webhook Error: {e}")

    # 6. UPDATE HISTORY
    new_history.append({
        "filename": video_to_send,
        "date_sent": today.isoformat()
    })
    save_history(new_history)
    print("Automation Complete.")

if __name__ == "__main__":
    run_automation()
