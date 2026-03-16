import streamlit as st
from datetime import date
import time
import random

# הגדרת layout ל-wide תמיד עוזרת לשליטה ב-CSS
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

/* התאמת ריווח כללי לנייד */
.block-container {
    padding-top: 2rem !important;
    padding-bottom: 2rem !important;
    padding-left: 1rem !important;
    padding-right: 1rem !important;
}

/* עיצוב כרטיסיות (Stats) */
.stat-card {
    background: white;
    padding: 20px;
    border-radius: 18px;
    border-bottom: 4px solid var(--primary);
    text-align: center;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
    margin-bottom: 15px; /* מרווח בין כרטיסים במובייל */
}

.stat-card h3 {
    margin: 0;
    font-size: 28px;
    color: var(--primary);
}

.stat-card p {
    margin: 5px 0 0 0;
    font-size: 16px;
    color: #475569;
}

/* התאמות ספציפיות למסכים קטנים (Media Queries) */
@media (max-width: 768px) {
    h1 {
        font-size: 1.8rem !important;
    }
    
    /* הפיכת עמודות לרשימה אנכית במובייל */
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 100% !important;
    }
    
    .stat-card h3 {
        font-size: 24px;
    }
}

/* עיצוב ה-Metric של Streamlit שייראה טוב יותר */
[data-testid="stMetric"] {
    background: white;
    padding: 15px;
    border-radius: 15px;
    box-shadow: 0 2px 8px rgba(0,0,0,0.04);
}

</style>
""", unsafe_allow_html=True)

START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# תפריט צד (Sidebar)
with st.sidebar:
    st.title("מערכת עידודו v3.0")
    page = st.selectbox(
        "לאן תרצה לגשת?",
        ["לוח הבקרה","המספרים שלנו","קיר זיכרונות חי","כספת חסויה 🔒"]
    )
    st.divider()
    st.write("נוצר על ידי נאנה ❤️")

# דף 1: לוח הבקרה
if page == "לוח הבקרה":
    st.title("מצב המערכת 📊")
    
    col1, col2 = st.columns(2)
    col1.metric("זמן כזוג", f"{days_together} ימים")
    col2.metric("ותק קשר", "8 שנים")
    
    st.divider()
    st.info("עידודו, המערכת מדווחת על רמות גבוהות של געגוע. מומלץ לשלוח הודעה לנאנה.")

# דף 2: המספרים שלנו
elif page == "המספרים שלנו":
    st.title("8 שנים במספרים 🔢")
    st.write("ניתוח דאטה של מה שחשוב:")

    # בטלפון העמודות הללו יופיעו אחת מתחת לשנייה בזכות ה-CSS
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
    st.write("התמונות מתחלפות אוטומטית...")

    # במובייל, כדי שלא יהיה עמוס מדי, נציג אותן אחת אחרי השנייה
    col1, col2, col3 = st.columns(3)
    p1 = col1.empty()
    p2 = col2.empty()
    p3 = col3.empty()

    for _ in range(5):
        nums = random.sample(range(1, 15), 3)
        p1.image("PHOTO.jpg", caption=f"רגע {nums[0]}", use_container_width=True)
        p2.image("PHOTO.jpg", caption=f"רגע {nums[1]}", use_container_width=True)
        p3.image("PHOTO.jpg", caption=f"רגע {nums[2]}", use_container_width=True)
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
        st.subheader("המכתב שלי:")
        st.info("עידודו שלי,\n\nאין מספר שיכול לתאר מה אתה בשבילי. אוהבת אותך, נאנה ❤️")
        st.snow()
    elif user_answer != "":
        st.error("קוד שגוי. נסה שוב...")
