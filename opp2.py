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
    st.session_state.last_page = "קיר זיכרונות 📸"
if 'balloons_fired' not in st.session_state:
    st.session_state.balloons_fired = False

# --- CSS נקי ומיושר לימין ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');

html, body, [data-testid="stAppViewContainer"] {
    direction: rtl;
    text-align: right;
    font-family: 'Assistant', sans-serif;
    background-color: #F8F9FA;
    color: #333333;
}

/* יישור כותרות וטקסט לימין */
h1, h2, h3, h4, h5, h6, p, label {
    text-align: right !important;
    direction: rtl !important;
}

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
    text-align: center !important;
    margin: 0;
}

.cute-card p {
    text-align: center !important;
}

/* כפתורים לימין */
.stButton>button {
    display: block;
    margin-right: 0;
    margin-left: auto;
}
</style>
""", unsafe_allow_html=True)

def trigger_hearts():
    heart_html = "".join([
        f'<div class="heart-particle" style="left:{random.randint(0, 95)}%; position:fixed; color:#D63384; font-size:24px; animation: hearts-fall 3s linear forwards;">❤️</div>'
        for _ in range(20)
    ])
    st.markdown(heart_html, unsafe_allow_html=True)

# לוגיקת תאריכים
START_DATE = date(2025, 12, 1) # תאריך מקורי
days_together = (date.today() - START_DATE).days

# --- תפריט ניווט ---
st.write("### היי עידודו 👋")
current_page = st.selectbox("לאן נטייל?", ["קיר זיכרונות 📸", "הפינה של עידודו ❤️"], key="nav_bar")

# איפוס במעבר דף
if current_page != st.session_state.last_page:
    st.session_state.clicks = 0
    st.session_state.current_reason = None
    st.session_state.balloons_fired = False
    st.session_state.last_page = current_page
    st.rerun()

st.divider()

# ==========================================
# עמוד 1: קיר זיכרונות (דף הבית)
# ==========================================
if current_page == "קיר זיכרונות 📸":
    st.title("הזיכרונות שלנו 📸")
    
    TOTAL_PHOTOS = 27
    photo_list = list(range(1, TOTAL_PHOTOS + 1))
    random.shuffle(photo_list)
    
    # מיכל ריק שמתעדכן
    placeholder = st.empty()
    
    for num in photo_list:
        # בדיקה קריטית: האם המשתמש עדיין בדף הזה?
        if st.session_state.nav_bar != "קיר זיכרונות 📸":
            break
            
        with placeholder.container():
            img_path = f"Image_{num}.jpg"
            try:
                st.image(img_path, use_container_width=True)
                st.markdown(f"<h4 style='text-align:right; color:#D63384;'>רגע מתוק #{num}</h4>", unsafe_allow_html=True)
            except:
                st.info(f"טוען רגע #{num}...")
        
        # המתנה של 4 שניות עם בדיקה אקטיבית של הדף
        for _ in range(40): # 40 * 0.1 = 4 שניות
            time.sleep(0.1)
            if st.session_state.nav_bar != "קיר זיכרונות 📸":
                st.rerun() # קופץ מיד החוצה מהלולאה
    
    st.rerun() # להתחלת סיבוב תמונות חדש

# ==========================================
# עמוד 2: הפינה של עידודו
# ==========================================
else:
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
    reasons = ["בגלל החיוך", "בגלל שאתה הבית", "בגלל שאתה תמיד יודע מה להגיד", "בגלל שזה פשוט אתה"]
    
    if st.button("לחץ כאן למשהו קטן וטוב ✨"):
        st.session_state.current_reason = random.choice(reasons)
        trigger_hearts()
    
    if st.session_state.current_reason:
        st.markdown(f'<div class="cute-card"><p style="font-size:20px; text-align:right;">{st.session_state.current_reason}</p></div>', unsafe_allow_html=True)

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
        <div style="background: white; padding: 25px; border-radius: 15px; border: 2px dashed #f08080; text-align: center; line-height: 1.6;">
            <b>עידודו שלי,</b><br><br>
            אחרי 8 שנים, אני פשוט רוצה להגיד תודה על מי שאתה.<br>
            תודה שאתה תמיד שם, מצחיק, מקשיב ואוהב.<br><br>
            אני אוהבת אותך המון,<br>
            <b>נאנה</b>
        </div>
        """, unsafe_allow_html=True)
        
        st.write("")
        if st.button("לנעול מחדש? 🔐"):
            st.session_state.clicks = 0
            st.rerun()
