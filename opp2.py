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
if 'last_page' not in st.session_state:
    st.session_state.last_page = "קצת עידו"
if 'balloons_fired' not in st.session_state:
    st.session_state.balloons_fired = False

# הגדרת יעד הלחיצות (כדי להשתמש בו גם בכרטיסיות וגם בכספת)
TARGET_CLICKS = 2

# --- CSS מעוצב עם יישור לימין ---
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

h1, h2, h3, h4, h5, h6, p, label, .stMarkdown div {
    text-align: right !important;
    direction: rtl !important;
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
    text-align: center !important;
}

.cute-card p {
    font-size: 18px;
    margin: 10px 0 0 0;
    text-align: center !important;
}

.stButton>button {
    display: block;
    margin-right: 0;
    margin-left: auto;
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
    heart_html = "".join([
        f'<div class="heart-particle" style="left:{random.randint(0, 95)}%; animation-delay:{random.uniform(0, 2)}s;">❤️</div>'
        for _ in range(20)
    ])
    st.markdown(heart_html, unsafe_allow_html=True)

# לוגיקת תאריכים
START_DATE = date(2026, 1, 1) 
days_together = (date.today() - START_DATE).days

# --- תפריט ניווט ---
st.write("### אתר ממש ממש מגניב")
current_page = st.selectbox("לאן נטייל?", ["קצת עידו", "יש לי להגיד לך משהו"], key="nav_bar")

# איפוס מוחלט במעבר דפים
if current_page != st.session_state.last_page:
    st.session_state.clicks = 0
    st.session_state.current_reason = None
    st.session_state.balloons_fired = False
    st.session_state.last_page = current_page
    st.rerun()

st.divider()

# ==========================================
# עמוד 1: קצת עידו (גלריה)
# ==========================================
if current_page == "קצת עידו":
    st.title("📸")
    
    TOTAL_PHOTOS = 27
    photo_list = list(range(1, TOTAL_PHOTOS + 1))
    random.shuffle(photo_list)
    
    placeholder = st.empty()
    
    for num in photo_list:
        if st.session_state.nav_bar != "קצת עידו":
            break
            
        with placeholder.container():
            img_path = f"Image_{num}.jpg"
            try:
                st.image(img_path, use_container_width=True)
                st.markdown(f"<p style='text-align:right; font-size:18px; color:#f08080;'>#{num}</p>", unsafe_allow_html=True)
            except:
                st.info(f"טוען רגע #{num}...")
        
        for _ in range(40):
            time.sleep(0.1)
            if st.session_state.nav_bar != "קצת עידו":
                st.rerun()
    
    st.rerun()

# ==========================================
# עמוד 2: הפינה של עידודו
# ==========================================
else:
    if not st.session_state.balloons_fired:
        st.balloons()
        st.session_state.balloons_fired = True
        
    st.title("כל מיני דברים חמודים")
    
    # לוגיקה לשינוי מספר ההודעות החצופות
    insult_count = 22 if st.session_state.clicks >= TARGET_CLICKS else 21

    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="cute-card"><h3>{max(0, days_together)}</h3><p>ימים שאנחנו ביחד</p></div>', unsafe_allow_html=True)
    with col2:
        # המספר משתנה ל-22 כשהכספת נפתחת
        st.markdown(f'<div class="cute-card"><h3>{insult_count}</h3><p>כמות הודעות חצופות וארוכות</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="cute-card"><h3>∞</h3><p>כמות המחשבות שלי עליך</p></div>', unsafe_allow_html=True)
    
    st.divider()
    
    st.subheader("למה אתה העידודו שלי? ✨")
    reasons = [
        "בגלל החיוך שגורם לי לשכוח מהכל",
        "בגלל שאתה תמיד יודע מה להגיד כשקשה",
        "בגלל הדרך שבה אתה מצחיק אותי עד דמעות",
        "בגלל 8 שנים של חברות שהיא הבית שלי",
        "בגלל שאתה פשוט... אתה.",
        "בגלל שאתה החבר הכי טוב שיכולתי לבקש"
    ]
    
    if st.button("לחץ כאן למשהו קטן וטוב ✨"):
        st.session_state.current_reason = random.choice(reasons)
        trigger_hearts()
    
    if st.session_state.current_reason:
        st.markdown(f'<div class="cute-card"><h3>💖</h3><p>{st.session_state.current_reason}</p></div>', unsafe_allow_html=True)

    st.divider()

    st.subheader("כספת הלב 🔒")
    
    if st.session_state.clicks < TARGET_CLICKS:
        st.write("כדי לפתוח את המכתב הסודי, צריך למלא את מדד האהבה.")
        st.progress(st.session_state.clicks / TARGET_CLICKS)
        if st.button("שלח אהבה ❤️"):
            st.session_state.clicks += 1
            st.rerun()
    else:
        st.success("הכספת נפתחה! ❤️")
        trigger_hearts()
        st.markdown("""
        <div style="background: white; padding: 25px; border-radius: 15px; border: 2px dashed #f08080; text-align: right; line-height: 1.6;">
            <b>עידודו שלי,</b><br><br>
            אחרי 8 שנים, אני פשוט רוצה להגיד תודה על מי שאתה.<br>
            תודה שאתה תמיד שם, מצחיק, מקשיב ואוהב.<br><br>
            אני אוהבת אותך המון,<br>
            <b>נאנה</b>
        </div>
        """, unsafe_allow_html=True)
        
        if st.button("לנעול מחדש 🔐"):
            st.session_state.clicks = 0
            st.rerun()
