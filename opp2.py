import streamlit as st
from datetime import date
import random

# הגדרות דף - חייב להיות הפקודה הראשונה של Streamlit
st.set_page_config(page_title="עבור עידודו ❤️", page_icon="❤️", layout="wide")

# --- CSS חם, נקי ומותאם למובייל ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');

:root {
    --soft-cream: #FFF9F5; 
    --warm-text: #432818;  
    --accent-pink: #ffb5a7;
    --card-bg: #ffffff;
}

html, body, [data-testid="stAppViewContainer"] {
    direction: rtl;
    text-align: right;
    font-family: 'Assistant', sans-serif;
    background-color: var(--soft-cream);
    color: var(--warm-text);
}

.cute-card {
    background: var(--card-bg);
    padding: 15px;
    border-radius: 20px;
    border: 1px solid #f8ad9d;
    text-align: center;
    box-shadow: 0 4px 12px rgba(248, 173, 157, 0.15);
    margin-bottom: 20px;
}

.cute-card h3 {
    color: #f08080 !important;
    margin-bottom: 5px;
    font-size: 28px;
}

.cute-card p {
    color: var(--warm-text) !important;
    font-size: 16px;
    margin: 0;
}

.gallery-img {
    width: 100%;
    border-radius: 15px;
    margin-bottom: 10px;
    object-fit: cover;
    aspect-ratio: 1 / 1; /* הופך את התמונות לריבועיות ואחידות */
}

/* התאמה למובייל */
@media (max-width: 768px) {
    .cute-card h3 { font-size: 22px; }
    .cute-card p { font-size: 14px; }
}

div[data-testid="stSelectbox"] label {
    color: var(--warm-text) !important;
    font-weight: bold;
}
</style>
""", unsafe_allow_html=True)

# לוגיקת תאריכים (עדכנתי ל-2018 לפי ה-8 שנים שציינת, תשני חזרה אם טעיתי)
START_DATE = date(2018, 1, 1) 
days_together = (date.today() - START_DATE).days

# --- ניווט עליון ---
st.write("### היי עידודו 👋")
page = st.selectbox(
    "לאן נטייל?",
    ["קודם כל", "רגעים קטנים", "קיר זיכרונות", "הפתעה חסויה 🔒"],
    label_visibility="visible"
)
st.divider()

# --- דף 1: קודם כל ---
if page == "קודם כל":
    st.title("הפינה שלנו ❤️")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f'<div class="cute-card"><h3>{days_together:,}</h3><p>ימים של ביחד</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="cute-card"><h3>8</h3><p>שנים של חברות</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="cute-card"><h3>∞</h3><p>כמות אהבה</p></div>', unsafe_allow_html=True)
    
    st.write("---")
    st.info("כיף שאתה כאן. האתר הזה נבנה במיוחד בשבילך, כדי להזכיר לנו כמה עברנו.")

# --- דף 2: רגעים קטנים ---
elif page == "רגעים קטנים":
    st.title("רגעים קטנים בלב")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="cute-card"><h3>∞</h3><p>צחוקים משותפים</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="cute-card"><h3>2,920</h3><p>בקרים שקמנו חברים</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="cute-card"><h3>1</h3><p>לב אחד</p></div>', unsafe_allow_html=True)

# --- דף 3: קיר זיכרונות ---
elif page == "קיר זיכרונות":
    st.title("הזיכרונות שלנו 📸")
    
    TOTAL_PHOTOS = 23  
    
    if 'photo_order' not in st.session_state:
        st.session_state.photo_order = list(range(1, TOTAL_PHOTOS + 1))
        random.shuffle(st.session_state.photo_order)

    # הצגת התמונות ב-2 טורים (מצוין למובייל)
    cols = st.columns(2)
    
    for i, num in enumerate(st.session_state.photo_order):
        # ודאי שהשמות ב-GitHub הם בדיוק Image_1.jpg (כולל I גדולה)
        image_filename = f"Image_{num}.jpg"
        
        with cols[i % 2]:
            st.markdown(f"""
            <div class="cute-card">
                <img src="{image_filename}" class="gallery-img" 
                     onerror="this.onerror=null; this.src='https://via.placeholder.com/300?text=Missing+Photo';">
                <p>רגע מתוק #{num}</p>
            </div>
            """, unsafe_allow_html=True)
    
    if st.button("ערבב זיכרונות 🎲"):
        random.shuffle(st.session_state.photo_order)
        st.rerun()

# --- דף 4: הפתעה חסויה ---
elif page == "הפתעה חסויה 🔒":
    st.title("אזור סודי 🔒")
    st.write("סדר את התחנות שלנו לפי הזמן כדי לפתוח את המכתב:")

    s1 = st.selectbox("תחנה ראשונה:", ["", "הווידוי במסיבת הגיוס", "היכרות בחטיבה", "חברים טובים במגמה"], key="s1")
    s2 = st.selectbox("תחנה שנייה:", ["", "הווידוי במסיבת הגיוס", "היכרות בחטיבה", "חברים טובים במגמה"], key="s2")
    s3 = st.selectbox("תחנה שלישית:", ["", "הווידוי במסיבת הגיוס", "היכרות בחטיבה", "חברים טובים במגמה"], key="s3")

    if s1 == "היכרות בחטיבה" and s2 == "חברים טובים במגמה" and s3 == "הווידוי במסיבת הגיוס":
        st.success("זה בדיוק הסדר הנכון! ❤️")
        st.balloons()
        
        st.divider()
        st.subheader("המכתב שלי אליך")
        st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 15px; border: 1px dashed #f08080; color: #432818; text-align: center;">
        עידודו שלי,<br><br>
        אחרי 8 שנים, אני פשוט רוצה להגיד תודה על מי שאתה.<br>
        על כל רגע, על התמיכה ועל הצחוק.<br><br>
        אני אוהבת אותך המון,<br>
        נאנה
        </div>
        """, unsafe_allow_html=True)
        st.snow()
    elif s1 != "" and s2 != "" and s3 != "":
        st.error("משהו פה התבלבל בסדר... תנסה שוב! 🤔")
