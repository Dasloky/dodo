import streamlit as st
from datetime import date
import time
import random

# הגדרות דף
st.set_page_config(page_title="עבור עידודו ❤️", page_icon="❤️", layout="wide")

# --- ניהול State ---
if 'clicks' not in st.session_state:
    st.session_state.clicks = 0
if 'current_reason' not in st.session_state:
    st.session_state.current_reason = None
# שינוי עמוד ברירת המחדל לקיר זיכרונות
if 'last_page' not in st.session_state:
    st.session_state.last_page = "קיר זיכרונות 📸"
if 'balloons_fired' not in st.session_state:
    st.session_state.balloons_fired = False

# --- CSS נקי ומיושר לימין ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');

/* הגדרות צבעים וגופנים */
html, body, [data-testid="stAppViewContainer"] {
    direction: rtl;
    text-align: right;
    font-family: 'Assistant', sans-serif;
    background-color: #F8F9FA; 
    color: #333333;
}

/* הצמדת כל הכותרות לימין */
h1, h2, h3, h4, h5, h6, p, label, .stMarkdown div {
    text-align: right !important;
    direction: rtl !important;
}

/* עיצוב כרטיסיות הנתונים */
.cute-card {
    background: white;
    padding: 20px;
    border-radius: 15px;
    border: 1px solid #E0E0E0;
    box-shadow: 0 2px 8px rgba(0,0,0,0.05);
    margin-bottom: 15px;
}

.cute-card h3 {
    color: #D63384 !important;
    font-size: 32px;
    margin: 0;
    text-align: center !important; /* מספרים נשארים במרכז הכרטיס */
}

.cute-card p {
    text-align: center !important; /* טקסט תחתון בכרטיס נשאר במרכז */
}

/* אנימציית לבבות */
.heart-particle {
    position: fixed;
    color: #D63384;
    font-size: 24px;
    user-select: none;
    pointer-events: none;
    z-index: 9999;
    animation: hearts-fall 3s linear forwards;
}

@keyframes hearts-fall {
    0% { top: -10%; transform: translateX(0) rotate(0deg); opacity: 1; }
    100% { top: 100%; transform: translateX(20px) rotate(360deg); opacity: 0; }
}

/* יישור כפתורים לימין */
.stButton>button {
    display: block;
    margin-right: 0;
    margin-left: auto;
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

# --- תפריט ניווט (קיר זיכרונות מופיע ראשון) ---
st.write("### היי עידודו 👋")
current_page = st.selectbox("לאן נטייל?", ["קיר זיכרונות 📸", "הפינה של עידודו ❤️"], key="nav_bar")

# --- מנגנון האיפוס במעבר דפים ---
if current_page != st.session_state.last_page:
    st.session_state.clicks = 0
    st.session_state.current_reason = None
    st.session_state.balloons_fired = False
    st.session_state.last_page = current_page
    st.rerun()

st.divider()

# ==========================================
# עמוד 1: קיר זיכרונות (עכשיו העמוד הראשי)
# ==========================================
if current_page == "קיר זיכרונות 📸":
    st.title("הזיכרונות שלנו 📸")
    
    TOTAL_PHOTOS = 27
    if 'photo_order' not in st.session_state:
        st.session_state.photo_order = list(range(1, TOTAL_PHOTOS + 1))
        random.shuffle(st.session_state.photo_order)
    
    placeholder = st.empty()
    
    for num in st.session_state.photo_order:
        # עצירה בטוחה אם מעבירים דף
        if st.session_state.nav_bar != "קיר זיכרונות 📸":
            break
            
        with placeholder.container():
            img_path = f"Image_{num}.jpg"
            try:
                st.image(img_path, use_container_width=True)
                st.markdown(f"<h4 style='text-align:right; color:#D63384;'>רגע מתוק #{num}</h4>", unsafe_allow_html=True)
            except:
                st.info("טוען רגע יפה...")
        
        # המתנה של 4 שניות עם בדיקת יציאה מהדף כל שנייה
        for _ in range(4):
            time.sleep(1)
            if st.session_bar != "קיר זיכרונות 📸": # בדיקה כפולה למניעת תקיעה
                st.rerun()
    
    # ערבוב מחדש בסיום הלולאה
    random.shuffle(st.session_state.photo_order)
    st.rerun()

# ==========================================
# עמוד 2: הפינה של עידודו
# ==========================================
elif current_page == "הפינה של עידודו ❤️":
    # בלונים קופצים פעם אחת בכניסה לדף זה
    if not st.session_state.balloons_fired:
        st.balloons()
        st.session_state.balloons_fired = True
        
    st.title("הפינה שלנו ❤️")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="cute-card"><h3>{max(0, days_together)}</h3><p>ימים שאנחנו ביחד</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="cute-card"><h3>8</h3><p>שנים של חברות אמת</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="cute-card"><h3>∞</h3><p>כמות המחשבות שלי עליך</p></div>', unsafe_allow_html=True)
    
    st.divider()
    
    st.subheader("למה אתה העידודו שלי? ✨")
    reasons = [
        "בגלל החיוך שגורם לי לשכוח מהכל",
        "בגלל שאתה תמיד יודע מה להגיד כשקשה",
        "בגלל הדרך שבה אתה מצחיק אותי עד דמעות",
        "בגלל 8 שנים של חברות שהיא הבית שלי",
        "בגלל שאתה פשוט... אתה."
    ]
    
    if st.button("לחץ כאן למשהו קטן וטוב ✨"):
        st.session_state.current_reason = random.choice(reasons)
        trigger_hearts()
    
    if st.session_state.current_reason:
        st.markdown(f'<div class="cute-card"><p style="font-size:20px; margin:0; text-align:right;">{st.session_state.current_reason}</p></div>', unsafe_allow_html=True)

    st.divider()

    st.subheader("כספת הלב 🔒")
    target_clicks = 2
    
    if st.session_state.clicks < target_clicks:
        st.write("כדי לפתוח את המכתב הסודי, צריך למלא את מדד האהבה.")
        st.progress(st.session_state.clicks / target_clicks)
        if st.button("שלח אהבה ❤️"):
            st.session_state.clicks += 1
            st.rerun()
    else:
        st.success("הכספת נפתחה! ❤️")
        st.markdown("""
        <div style="background: white; padding: 25px; border-radius: 15px; border: 1px solid #D63384; text-align: right; line-height: 1.6;">
            <b style="color:#D63384;">עידודו שלי,</b><br><br>
            אחרי 8 שנים, אני פשוט רוצה להגיד תודה על מי שאתה.<br>
            תודה שאתה תמיד שם, מצחיק, מקשיב ואוהב.<br><br>
            אני אוהבת אותך המון,<br>
            <b>נאנה</b>
        </div>
        """, unsafe_allow_html=True)
        if st.button("לנעול מחדש 🔐"):
            st.session_state.clicks = 0
            st.rerun()
