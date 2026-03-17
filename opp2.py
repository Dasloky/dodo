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

# --- CSS מעודכן ונקי ---
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
START_DATE = date(2025, 12, 1) # עדכני לתאריך הנכון שלכם
days_together = (date.today() - START_DATE).days

# --- תפריט ניווט ---
st.write(f"### היי עידודו 👋")
page = st.selectbox("לאן נטייל?", ["הפינה של עידודו ❤️", "קיר זיכרונות 📸"])

# איפוס במעבר דף כדי למנוע "שאריות"
if page != st.session_state.last_page:
    st.session_state.last_page = page
    st.rerun()

# --- עמוד 1: הכל ביחד (1, 2, 4) ---
if page == "הפינה של עידודו ❤️":
    st.title("הפינה שלנו ❤️")
    
    # חלק 1: כרטיסיות
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="cute-card"><h3>{max(0, days_together)}</h3><p>ימים שאנחנו ביחד</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="cute-card"><h3>8</h3><p>שנים של חברות אמת</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="cute-card"><h3>∞</h3><p>כמות המחשבות שלי עליך</p></div>', unsafe_allow_html=True)
    
    st.divider()
    
    # חלק 2: סיבות לחייך
    st.subheader("למה אתה העידודו שלי? ✨")
    reasons = [
        "בגלל החיוך שגורם לי לשכוח מהכל",
        "בגלל שאתה תמיד יודע מה להגיד כשקשה",
        "בגלל הדרך שבה אתה מצחיק אותי עד דמעות",
        "בגלל שאתה הבית שלי",
        "בגלל המבט הזה ששמור רק לי"
    ]
    
    if st.button("לחץ למשהו קטן וטוב ✨"):
        st.session_state.current_reason = random.choice(reasons)
        trigger_hearts()
    
    if st.session_state.current_reason:
        st.markdown(f'<div class="cute-card"><h3>💖</h3><p>{st.session_state.current_reason}</p></div>', unsafe_allow_html=True)

    st.divider()

    # חלק 3: כספת
    st.subheader("כספת הלב 🔒")
    if st.session_state.clicks < 2:
        st.write("מלא את מדד האהבה כדי לפתוח:")
        st.progress(st.session_state.clicks / 2)
        if st.button("שלח אהבה ❤️"):
            st.session_state.clicks += 1
            st.rerun()
    else:
        st.success("הכספת נפתחה!")
        st.markdown("""
        <div style="background: white; padding: 25px; border-radius: 15px; border: 2px dashed #f08080; text-align: center;">
            <p>עידודו שלי, תודה על 8 שנים מדהימות. אוהבת אותך, נאנה ❤️</p>
        </div>
        """, unsafe_allow_html=True)
        if st.button("לנעול מחדש 🔐"):
            st.session_state.clicks = 0
            st.rerun()

# --- עמוד 2: קיר זיכרונות ---
elif page == "קיר זיכרונות 📸":
    st.title("הזיכרונות שלנו 📸")
    st.write("התמונות מתחלפות אוטומטית כל כמה שניות...")
    
    TOTAL_PHOTOS = 27
    if 'photo_order' not in st.session_state:
        st.session_state.photo_order = list(range(1, TOTAL_PHOTOS + 1))
        random.shuffle(st.session_state.photo_order)
        
    placeholder = st.empty()
    
    # לולאת הצגה נקייה
    for num in st.session_state.photo_order:
        with placeholder.container():
            img_path = f"Image_{num}.jpg"
            try:
                st.image(img_path, use_container_width=True)
                st.info(f"רגע מתוק #{num}")
            except:
                st.warning(f"לא מצאתי את תמונה מספר {num} (ודאי שהשם נכון: Image_{num}.jpg)")
            
            time.sleep(4)
            # ב-Streamlit, לולאות עם sleep יכולות להיות כבדות. 
            # אם את רוצה שזה יפסיק כשהוא עובר דף, ה-rerun למעלה דואג לזה.
