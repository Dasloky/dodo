import streamlit as st
from datetime import date
import time
import random

# הגדרות דף
st.set_page_config(page_title="עבור עידודו ❤️", page_icon="❤️", layout="wide")

# ניהול State
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'current_reason' not in st.session_state:
    st.session_state.current_reason = None
if 'last_page' not in st.session_state:
    st.session_state.last_page = "הפינה של עידודו ❤️"

# --- CSS עם אנימציית לבבות ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');

:root {
    --soft-cream: #FFF9F5; 
    --warm-text: #432818;  
    --accent-pink: #ffb5a7;
    --card-bg: #ffffff;
}

html, body, .main {
    direction: rtl;
    text-align: right;
    font-family: 'Assistant', sans-serif;
    background-color: var(--soft-cream);
    color: var(--warm-text);
}

.cute-card {
    background: var(--card-bg);
    padding: 20px;
    border-radius: 20px;
    border: 1px solid #f8ad9d;
    text-align: center;
    box-shadow: 0 4px 12px rgba(248, 173, 157, 0.15);
    margin-bottom: 15px;
}

.cute-card h3 {
    color: #f08080 !important;
    margin-bottom: 5px;
    font-size: 32px;
}

.cute-card p {
    color: var(--warm-text) !important;
    font-size: 18px;
    margin: 0;
}

@keyframes hearts-fall {
    0% { top: -10%; transform: translateX(0) rotate(0deg); opacity: 1; }
    100% { top: 100%; transform: translateX(20px) rotate(360deg); opacity: 0; }
}

.heart-particle {
    position: fixed;
    color: #ffb5a7;
    font-size: 24px;
    user-select: none;
    pointer-events: none;
    z-index: 9999;
    animation: hearts-fall 3s linear forwards;
}
</style>
""", unsafe_allow_html=True)

def trigger_hearts():
    heart_html = ""
    for i in range(20):
        left = random.randint(0, 95)
        delay = random.uniform(0, 2)
        heart_html += f'<div class="heart-particle" style="left:{left}%; animation-delay:{delay}s;">❤️</div>'
    st.markdown(heart_html, unsafe_allow_html=True)

# לוגיקת תאריכים
START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# --- ניווט עליון (2 עמודים בלבד) ---
st.write("### היי עידודו 👋")
page = st.selectbox(
    "לאן נטייל?",
    ["הפינה של עידודו ❤️", "קיר זיכרונות 📸"],
    label_visibility="visible"
)

# איפוס במעבר בין הדפים
if page != st.session_state.last_page:
    st.session_state.last_page = page
    st.rerun()

st.divider()

# --- עמוד 1: הפינה המאוחדת (1, 2, 4) ---
if page == "הפינה של עידודו ❤️":
    st.title("הפינה שלנו ❤️")
    st.balloons()
    
    # חלק 1: הסטטיסטיקות (עמוד 1 הישן)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="cute-card"><h3>{days_together}</h3><p>ימים שאנחנו ביחד</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="cute-card"><h3>8</h3><p>שנים של חברות אמת</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="cute-card"><h3>∞</h3><p>כמות המחשבות שלי עליך</p></div>', unsafe_allow_html=True)
    
    st.write("---")
    
    # חלק 2: סיבות לחייך (עמוד 2 הישן)
    st.subheader("למה אתה העידודו שלי? ✨")
    reasons = [
        "בגלל החיוך שגורם לי לשכוח מהכל",
        "בגלל שאתה תמיד יודע מה להגיד כשקשה",
        "בגלל הדרך שבה אתה מצחיק אותי עד דמעות",
        "בגלל 8 שנים של חברות שהיא הבית שלי",
        "בגלל שאתה פשוט... אתה.",
        "בגלל המבט הזה ששמור רק לי",
        "בגלל שאתה החבר הכי טוב שיכולתי לבקש"
    ]
    
    if st.button("לחץ כאן למשהו קטן וטוב ✨"):
        st.session_state.current_reason = random.choice(reasons)
        trigger_hearts()
    
    if st.session_state.current_reason:
        st.markdown(f'<div class="cute-card"><h3>💖</h3><p>{st.session_state.current_reason}</p></div>', unsafe_allow_html=True)

    st.write("---")

    # חלק 3: הכספת והמכתב (עמוד 4 הישן)
    st.subheader("כספת הלב 🔒")
    target_clicks = 2
    
    if st.session_state.clicks < target_clicks:
        st.write("כדי לפתוח את המכתב הסודי, צריך למלא את מדד האהבה.")
        progress = st.session_state.clicks / target_clicks
        st.progress(progress)
        
        if st.button("שלח אהבה ❤️"):
            st.session_state.clicks += 1
            st.rerun()
    else:
        st.success("הכספת נפתחה! ❤️")
        st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 15px; border: 1px dashed #f08080; color: #432818; line-height: 1.6; text-align: center;">
        <b>עידודו שלי,</b><br><br>
        אחרי 8 שנים, אני פשוט רוצה להגיד תודה על מי שאתה.<br>
        תודה שאתה תמיד שם, מצחיק, מקשיב ואוהב.<br><br>
        אני אוהבת אותך המון,<br>
        <b>נאנה</b>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("לנעול מחדש? 🔐"):
            st.session_state.clicks = 0
            st.rerun()

# --- עמוד 2: קיר זיכרונות (עמוד 3 הישן - ללא שינוי) ---
elif page == "קיר זיכרונות 📸":
    st.title("הזיכרונות שלנו 📸")
    
    TOTAL_PHOTOS = 27  
    
    placeholder = st.empty()
    
    if 'photo_order' not in st.session_state:
        st.session_state.photo_order = list(range(1, TOTAL_PHOTOS + 1))
        random.shuffle(st.session_state.photo_order)
        
    for num in st.session_state.photo_order:
        img_path = f"Image_{num}.jpg"
        with placeholder.container():         
            try:
                st.image(img_path, use_container_width=True)
                st.markdown(f"<p style='text-align:center; margin-top:10px;'>רגע מתוק #{num}</p>", unsafe_allow_html=True)
            except:
                st.write(f"מחכה לתמונה הבאה... ({num})")            
            
            time.sleep(4)
            
    if st.button("סיבוב נוסף?"):
        random.shuffle(st.session_state.photo_order)
        st.rerun()
