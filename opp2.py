import streamlit as st
from datetime import date
import time
import random

# הגדרות דף
st.set_page_config(page_title="מערכת עידודו ❤️", page_icon="🔒", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');

/* הגדרות בסיס */
:root {
    --bg: #f8fafc;
    --primary: #0284c7;
    --text: #0f172a;
}

html, body, .main {
    direction: rtl;
    text-align: right;
    font-family: 'Assistant', sans-serif;
    background-color: var(--bg);
}

/* תיקון מרחקים למובייל */
.block-container {
    padding-top: 1rem !important;
    padding-bottom: 5rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}

/* עיצוב כרטיסיות */
.stat-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    border-bottom: 4px solid var(--primary);
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 15px;
}

.stat-card h3 {
    margin: 0;
    font-size: 28px;
    color: var(--primary);
}

/* התאמות מובייל קריטיות */
@media (max-width: 768px) {
    /* הפיכת עמודות לרשימה אנכית */
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 100% !important;
    }
    
    /* הבלטת הניווט בראש הדף */
    div[data-testid="stSelectbox"] {
        margin-bottom: 20px;
        background-color: white;
        border-radius: 10px;
        padding: 5px;
        box-shadow: 0 2px 5px rgba(0,0,0,0.1);
    }
}

/* הסתרת כפתור התפריט המובנה של Streamlit בטלפון כדי שלא יפריע */
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# --- ניווט חכם ---
# בגלל שהסרגל הצידי בעייתי במובייל, נשים את הניווט בראש הדף כתיבת בחירה
st.write("### 🧭 ניווט במערכת")
page = st.selectbox(
    "בחר לאן תרצה לגשת:",
    ["לוח הבקרה", "המספרים שלנו", "קיר זיכרונות חי", "כספת חסויה 🔒"],
    label_visibility="collapsed" # מחביא את הכותרת הסטנדרטית בשביל מראה נקי
)
st.divider()

# --- תוכן הדפים ---

# דף 1: לוח הבקרה
if page == "לוח הבקרה":
    st.title("מצב המערכת 📊")
    
    # שימוש ב-columns (שבמובייל יהיו אחד מתחת לשני)
    col1, col2 = st.columns(2)
    with col1:
        st.metric("זמן כזוג", f"{days_together} ימים")
    with col2:
        st.metric("ותק קשר", "8 שנים")
    
    st.info("עידודו, המערכת מדווחת על רמות גבוהות של געגוע. מומלץ לשלוח הודעה לנאנה.")

# דף 2: המספרים שלנו
elif page == "המספרים שלנו":
    st.title("8 שנים במספרים 🔢")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="stat-card"><h3>∞</h3><p>הודעות "בוקר טוב"</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="stat-card"><h3>2,920</h3><p>ימים של חברות</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="stat-card"><h3>1</h3><p>וידוי ב-12.12</p></div>', unsafe_allow_html=True)

    st.markdown(
        '<div class="stat-card" style="border-bottom-color: #f472b6;"><h3>99,999+</h3><p>בדיחות פרטיות</p></div>',
        unsafe_allow_html=True
    )

# דף 3: קיר זיכרונות
elif page == "קיר זיכרונות חי":
    st.title("הזיכרונות שלנו 📸")
    st.write("מתעדכן אוטומטית...")

    # במובייל, עדיף להציג תמונה אחת גדולה וברורה בכל פעם
    p = st.empty()

    for _ in range(5):
        num = random.randint(1, 14)
        p.image("PHOTO.jpg", caption=f"זיכרון {num} מתוך 14", use_container_width=True)
        time.sleep(4)

# דף 4: כספת
elif page == "כספת חסויה 🔒":
    st.title("הכספת 🔒")
    st.subheader("חידת אימות:")
    st.write("באיזה תאריך הכל השתנה במסיבת הגיוס?")

    user_answer = st.text_input("הכנס תאריך", placeholder="DD.MM")

    if user_answer == "12.12":
        st.success("הקוד התקבל.")
        st.balloons()
        st.warning("⚠️ חריגה בנהלי לבוש טקטי!")
        st.divider()
        st.info("עידודו שלי, אין מספר שיכול לתאר מה אתה בשבילי. אוהבת אותך, נאנה ❤️")
        st.snow()
    elif user_answer != "":
        st.error("קוד שגוי.")
