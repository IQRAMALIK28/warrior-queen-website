import streamlit as st

st.set_page_config(page_title="Warrior Queen Zainab Khan", layout="wide")

st.markdown("""
<style>
/* tasveeron ko barabar karne ke liye */
[data-testid="stImage"] img {
    height: 400px !important;
    object-fit: cover !important;
    border-radius: 15px;
}
</style>
<div style="background: linear-gradient(90deg, #FF416C, #FF4B2B); padding:25px; border-radius:15px; text-align:center; color:white;">
<h1>👑 Warrior Queen Zainab Khan 👑</h1>
<p>5th World Champion | Riyadh 2025 | Karachi, Pakistan</p>
<p>Online Classes + Private Classes Available</p>
</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns(3)
with col1:
    st.image("zainab_khan_1.jpg", use_container_width=True)
with col2:
    st.image("zainab_khan_2.jpg", use_container_width=True)
with col3:
    st.image("zainab_khan_3.jpg", use_container_width=True)

st.write("---")

left, right = st.columns([1, 2])

with left:
    st.subheader("📍 Contact Karein")
    st.write("📱 +92 335 5029001")
    st.write("📍 Iman Martial Art Academy, Gizri Ave, Karachi")
    st.write("📸 Instagram: zx-warrior23")
    st.write("📘 Facebook: Zainab Khan")
    st.write("📧 warriorqueenzainab@gmail.com")
    st.link_button("📲 WhatsApp", "https://wa.me/923355029001", use_container_width=True)

with right:
    st.header("Warrior Queen - Official Website")
    st.write("Warrior Queen Zainab Khan - World Champion 2025 from Karachi")
    
    st.subheader("🏅 Credentials")
    st.write("""
    - World Champion Martial Artist - Gold Medalist 2025
    - Head Female Coach at Iman Martial Arts Academy
    - Founder: Warrior Queen By Zainab Khan
    - Black Belt in Karate & Taekwondo
    - Certified Self Defense Instructor
    - 5+ Years Experience
    """)
    
    st.subheader("💪 Services - Hamari Khidmat")
    st.write("""
    - Womens Self Defense
    - Girls & Kids Martial Arts
    - Private Classes Available (One-on-One)
    - Online Training Available - All Pakistan
    - Personal Fitness, Kickboxing, Karate & Taekwondo
    """)
    st.success("✅ Online Classes Available - All Pakistan")
    st.warning("✅ Private Classes Available")