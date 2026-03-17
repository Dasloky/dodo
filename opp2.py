import streamlit as st
from datetime import date
import random

# הגדרות דף
st.set_page_config(page_title="עבור עידודו ❤️", page_icon="❤️", layout="wide")

# ניהול State - חשוב מאוד לשמירת נתונים במעבר דפים
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'current_reason' not in st.session_state:
    st.session_state.current_reason = None
if 'last_page' not in st.session_state:
    st.session_state.last_page = "הפינה של עידודו ❤️"
if 'photo_order' not in st.session_state:
    # אתחול הגלריה
    TOTAL_PHOTOS = 27
    st.session_state.photo_order = list(range(1, TOTAL_PHOTOS + 1))
    random.shuffle(st.session_state.photo_order)
if 'current_photo_idx' not in st.session_state:
    st.session_state.current_photo_idx = 0

# --- CSS עם אנימציית לבבות ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');

:root {
    --soft-cream: #FFF9F5; 
    --warm-text: #432818;  
    --accent-pink: #ffb5a7;
}

html, body, [data-testid="stAppViewContainer"] {
    direction: rtl;
    text-align: right;
    font-family: 'Assistant', sans-serif;
    background-color: var(--soft-cream);
    color: var(--warm-text);
}

.cute-card {
    background: white;
    padding: 25px;
    border-radius: 20px;
    border: 1px solid #f8ad9d;
    text-align: center;
    box-shadow: 0 4px 12px rgba(248, 173, 157, 0.15);
    margin-bottom: 20px;
}

.cute-card h3 {
    color: #f08080 !important;
    font-size: 32px;
    margin: 0;
}

.cute-card p {
    font-size: 18px;
    margin: 10px 0 0 0;
}

/* אנימציית לבבות */
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
    heart_html = "".join([
        f'<div class="heart-particle" style="left:{random.randint(0, 95)}%; animation-delay:{random.uniform(0, 2)}s;">❤️</div>'
        for _ in range(20)
    ])
    st.markdown(heart_html, unsafe_allow_html=True)

# לוגיקת תאריכים
START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# --- תפריט ניווט ---
st.write("### היי עידודו 👋")
page = st.selectbox("לאן נטייל?", ["הפינה של עידודו ❤️", "קיר זיכרונות 📸"])

# איפוס מוחלט במעבר בין דפים למניעת באגים
if page != st.session_state.last_page:
    st.session_state.last_page = page
    st.rerun()

st.divider()

# ==========================================
# עמוד 1: הפינה של עידודו (הכל מאוחד)
# ==========================================
if page == "הפינה של עידודו ❤️":
    st.title("הפינה שלנו ❤️")
    
    # 1. כרטיסיות מספרים
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="cute-card"><h3>{days_together}</h3><p>ימים שאנחנו ביחד</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="cute-card"><h3>8</h3><p>שנים של חברות אמת</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="cute-card"><h3>∞</h3><p>כמות המחשבות שלי עליך</p></div>', unsafe_allow_html=True)
    
    st.divider()
    
    # 2. סיבות לחייך
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

    st.divider()

    # 3. כספת הלב
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
        trigger_hearts()
        st.markdown("""
        <div style="background: white; padding: 25px; border-radius: 15px; border: 2px dashed #f08080; text-align: center; line-height: 1.6;">
            <b>עידודו שלי,</b><br><br>
            אחרי 8 שנים, אני פשוט רוצה להגיד תודה על מי שאתה.<br>
            תודה שאתה תמיד שם, מצחיק, מקשיב ואוהב.<br><br>
            אני אוהבת אותך המון,<br>
            <b>נאנה</b>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("") # מרווח קטן
        if st.button("לנעול מחדש? 🔐"):
            st.session_state.clicks = 0
            st.rerun()

# ==========================================
# עמוד 2: קיר זיכרונות
# ==========================================
elif page == "קיר זיכרונות 📸":
    st.title("הזיכרונות שלנו 📸")
    
    # משיכת התמונה הנוכחית לפי האינדקס
    current_num = st.session_state.photo_order[st.session_state.current_photo_idx]
    img_path = f"Image_{current_num}.jpg"
    
    # הצגת התמונה
    try:
        st.image(img_path, use_container_width=True)
        st.markdown(f"<p style='text-align:center; font-size:18px;'>רגע מתוק #{current_num}</p>", unsafe_allow_html=True)
    except:
        st.warning(f"מחכה לתמונה הבאה... (לא מצאתי את הקובץ: Image_{current_num}.jpg)")
    
    st.write("") # מרווח
    
    # כפתור מעבר לתמונה הבאה (ממורכז)
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("לתמונה הבאה 📸", use_container_width=True):
            # מקדם את האינדקס באחד, ואם הגענו לסוף - חוזר להתחלה
            st.session_state.current_photo_idx = (st.session_state.current_photo_idx + 1) % len(st.session_state.photo_order)
            st.rerun()
            
    # כפתור לערבוב מחדש של הגלריה
    if st.button("ערבב תמונות מחדש 🔀"):
        random.shuffle(st.session_state.photo_order)
        st.session_state.current_photo_idx = 0
        st.rerun()
