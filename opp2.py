import streamlit as st
from datetime import date
import time
import random

# הגדרות דף
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

.gallery-img {
    width: 100%;
    border-radius: 15px;
    margin-bottom: 10px;
    object-fit: cover;
    max-height: 450px;
}

@media (max-width: 768px) {
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 100% !important;
    }
}
</style>
""", unsafe_allow_html=True)

# לוגיקת תאריכים
START_DATE = date(2026, 1, 1)
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
        st.markdown(f'<div class="cute-card"><h3>{days_together}</h3><p>ימים שאנחנו ביחד</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="cute-card"><h3>8</h3><p>שנים של חברות אמת</p></div>', unsafe_allow_html=True)
    with col3:
        st.markdown('<div class="cute-card"><h3>∞</h3><p>כמות המחשבות שלי עליך</p></div>', unsafe_allow_html=True)
    
    st.write("---")
    st.write("כיף שאתה כאן. האתר הזה הוא רק בשבילך.")

# --- דף 2: רגעים קטנים ---
elif page == "רגעים קטנים":
    st.title("עמוד נורמלי לגמרי")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="cute-card"><h3>∞</h3><p>צחוקים משותפים</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="cute-card"><h3>2,920</h3><p>בקרים שקמנו חברים</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="cute-card"><h3>1</h3><p>לב אחד (שלי)</p></div>', unsafe_allow_html=True)

# --- דף 3: קיר זיכרונות ---
elif page == "קיר זיכרונות":
    st.title("הזיכרונות שלנו 📸")
    
    TOTAL_PHOTOS = 14  # תוודאי שזה המספר המדויק של התמונות שהעלית
    
    # יצירת מיכל ריק שמתנקה בכל פעם כדי שלא ייווצרו כפילויות בדף
    placeholder = st.empty()
    
    # רשימה רנדומלית של תמונות
    if 'photo_order' not in st.session_state:
        st.session_state.photo_order = list(range(1, TOTAL_PHOTOS + 1))
        random.shuffle(st.session_state.photo_order)

    # לולאת התמונות
    for num in st.session_state.photo_order:
        img_path = f"PHOTO_{num}.jpg"
        
        with placeholder.container():
            # יצירת הכרטיסייה הלבנה שרצית, ורק התמונה בתוכה
            st.markdown(f'<div class="cute-card">', unsafe_allow_html=True)
            
            # ניסיון טעינה של התמונה - אם היא לא קיימת, הוא לא יציג אייקון שבור
            try:
                st.image(img_path, caption=f"רגע מתוק #{num}", use_container_width=True)
            except:
                st.error(f"לא הצלחתי למצוא את התמונה {img_path}")
            
            st.markdown('</div>', unsafe_allow_html=True)
            
            # זמן המתנה בין תמונות
            time.sleep(4)
    
    if st.button("לראות שוב"):
        random.shuffle(st.session_state.photo_order)
        st.rerun()

# --- דף 4: הפתעה חסויה ---
elif page == "הפתעה חסויה 🔒":
    st.title("אזור סודי 🔒")
    st.write("סדר את התחנות שלנו לפי הזמן כדי לפתוח את המכתב:")

    s1 = st.selectbox("תחנה ראשונה:", ["", "הווידוי במסיבת הגיוס", "היכרות בחטיבה", "חברים טובים במגמה"])
    s2 = st.selectbox("תחנה שנייה:", ["", "הווידוי במסיבת הגיוס", "היכרות בחטיבה", "חברים טובים במגמה"])
    s3 = st.selectbox("תחנה שלישית:", ["", "הווידוי במסיבת הגיוס", "היכרות בחטיבה", "חברים טובים במגמה"])

    if s1 == "היכרות בחטיבה" and s2 == "חברים טובים במגמה" and s3 == "הווידוי במסיבת הגיוס":
        st.success("זה בדיוק הסדר הנכון! ❤️")
        st.balloons()
        
        st.divider()
        st.subheader("המכתב שלי אליך")
        st.markdown("""
        <div style="background: white; padding: 20px; border-radius: 15px; border: 1px dashed #f08080; color: #432818;">
        עידודו שלי,<br><br>
        אחרי 8 שנים, אני פשוט רוצה להגיד תודה על מי שאתה.<br>
        אני אוהבת אותך המון,<br>
        נאנה
        </div>
        """, unsafe_allow_html=True)
        st.snow()
    elif s1 != "" and s2 != "" and s3 != "":
        st.error("משהו פה התבלבל בסדר... תנסה שוב!")
