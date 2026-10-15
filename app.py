import streamlit as st
import os
import glob
from business_logic import get_trainer_images, handle_user_query

st.set_page_config(page_title="WARRIOR QUEEN", layout="wide")

# --- 1. GALLERY UPAR ---
st.subheader("Gallery")
pics = get_trainer_images()
pics = [p for p in pics if os.path.exists(p)]

if len(pics) < 4:
    for ext in ["*.jpg", "*.jpeg", "*.png", "*.JPG"]:
        for f in glob.glob(ext):
            if f not in pics:
                pics.append(f)

if pics:
    cols = st.columns(4)
    for i in range(min(4, len(pics))):
        with cols[i]:
            st.image(pics[i], width=200)

st.divider()

# --- 2. NEECHE INFO ---
left, right = st.columns([1, 2])

with left:
    st.subheader("Trainer Links")
    st.write("**Zainab Khan - Warrior Queen**")
    st.write("Inaam Martial Arts, Karachi")
    st.markdown("---")
    st.markdown("📱 WhatsApp: 0333-5029001")
    st.markdown("📸 Instagram: ZK_Warrior_28")
    st.markdown("📘 Facebook: Zainab Khan")
    st.link_button("📌 Pin Location", "https://maps.google.com")

with right:
    st.title("WARRIOR QUEEN - Trainer Info")
    st.write("Personal Training, Self Defense & Fitness")

    q = st.text_input("Sawal likhein.....", placeholder="Fees kya hai?")

    if q:
        ans = handle_user_query(q)
        msg = ans.get("message", ans) if isinstance(ans, dict) else ans

        # Fees wala ganda dict theek karna
        if isinstance(msg, dict) and "free_trial" in msg:
            st.success("Fees ki tafseel:")
            st.write(f"**Free Trial:** {msg.get('free_trial')}")
            st.write(f"**Paid Trial:** {msg.get('paid_trial')}")
            st.write("**Group Classes:**")
            for g in msg.get('group_classes', []):
                st.write(f"- {g}")
            st.write(f"**One on One:** {msg.get('one_on_one')}")
        else:
            st.info(msg)