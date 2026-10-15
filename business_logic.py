import os, glob
from dotenv import load_dotenv
from groq import Groq

# --- Groq Key لینا - یہ آپ کی پرانی والی لائنیں ہیں، ڈیلیٹ نہیں کیں ---
load_dotenv()
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
try:
    import streamlit as st
    if not GROQ_API_KEY:
        GROQ_API_KEY = st.secrets.get("GROQ_API_KEY")
except:
    pass

client = Groq(api_key=GROQ_API_KEY) if GROQ_API_KEY else None

# --- آپ کا سارا ڈیٹا - یہ بھی پورا رکھا ہے ---
TRAINER_DATA_TEXT = """
Company: Warrior Queen - Female Fitness by Zainab Khan
Trainer: Zainab Khan - Karate Black Belt, Certified Trainer, 8+ years experience
Location: Inaam Martial Arts Academy, Karachi + Personal Home Training Thrice a Week (ghar par bhi hoti hai)
CONTACT:
WhatsApp: 0333-5029001
Instagram: @ZK_Warrior_28
Fcebook: Zainab Khan

Services:
1. Girls Karate & Self Defense
2. Kickboxing - Self Defense + Safety + Full Body Fitness
3. Mobility Training
4. Muscle Building
5. Joint / Muscle / Haddi / Ghutna / Kamar Pain Recovery
6. Personal Home Training
Fees:
Free Trial Group = FREE,
Paid One-on-One Trial = Rs 3000,
Private Female Strength Group = Rs 15,000/month,
Girls Karate Group = Rs 10,000/month,
One-on-One Personal (1 Hour, Thrice a Week, ghar par bhi) = Rs 35,000/month
Age: 5-15 Karate, 16-25 Karate+Kickboxing, 26-35 Kickboxing+Strength, 35+ Personal One-on-One + Mobility
Contact: WhatsApp, Instagram: warrior.queen.zainab
"""

# --- ماڈل یہاں لگا ہوا ہے - یہی وہ جگہ ہے جس کا آپ پوچھ رہی تھیں ---
def handle_user_query(sawal):
    if not client:
        return {"message": "Groq API Key nahi lagi,.env file check karein"}

    prompt = f"""
    Tum Zainab Khan ho, Warrior Queen Trainer ho. Sirf neeche diye gaye DATA se jawab do.
    Jawab hamesha Roman Urdu me, izzat dar aur friendly lehje me do.
    DATA: {TRAINER_DATA_TEXT}
    User ka sawal: {sawal}
    """

    try:
        completion = client.chat.completions.create(
            model="openai/gpt-oss-20b",
            messages=[
                {"role": "system", "content": "Tum Zainab Khan ho, Warrior Queen trainer."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3
        )
        jawab = completion.choices[0].message.content
        return {"message": jawab}
    except Exception as e:
        return {"message": f"Groq Error: {e}"}

# --- آپ کا پرانا image wala function bhi rakha hai ---
def get_trainer_images():
    image_files = []
    for ext in ("*.jpg", "*.jpeg", "*.png", "*.webp"):
        image_files.extend(glob.glob(f"images/{ext}"))
        image_files.extend(glob.glob(ext))
    return image_files