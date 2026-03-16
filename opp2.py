import streamlit as st
from datetime import date
import time
import random

# הגדרות דף
st.set_page_config(page_title="עבור עידודו ❤️", page_icon="❤️", layout="wide")

# --- CSS חמוד ונעים מותאם לטלפון ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');

:root {
    --primary-pink: #ffafcc;
    --soft-blue: #a2d2ff;
    --bg-color: #fff5f8;
}

html, body, .main {
    direction: rtl;
    text-align: right;
    font-family: 'Assistant', sans-serif;
    background-color: var(--bg-color);
}

/* כרטיסיות חמודות */
.cute-card {
    background: white;
    padding: 20px;
    border-radius: 25px;
    border: 2px solid var(--primary-pink);
    text-align: center;
    box-shadow: 0 4px 10px rgba(255, 175, 204, 0.2);
    margin-bottom: 15px;
}

.cute-card h3 {
    color: #ff8fab;
    margin-bottom: 5px;
}

/* התאמה למובייל */
@media (max-width: 768px) {
    [data-testid="column"] {
        width: 100% !important;
        flex: 1 1 100% !important;
    }
    .block-container {
        padding: 1rem !important;
    }
}

/* עיצוב כפתורים */
.stButton>button {
    border-radius: 20px;
    background-color: var(--primary-pink);
    color: white;
    border: none;
}
</style>
""", unsafe_allow_html=True)

START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# --- ניווט עליון חמוד ---
st.write("## היי עידודו 👋")
page = st.selectbox(
    "לאן נלך היום?",
    ["הבית שלנו", "רגעים קטנים", "קיר זיכרונות", "הפתעה חסויה 🔒"],
    label_visibility="collapsed"
)
st.divider()

# --- דף 1: הבית שלנו ---
if page == "הבית שלנו":
    st.title("הבית של נאנה ועידודו ❤️")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f'<div class="cute-card"><h3>{days_together}</h3><p>ימים של ביחד</p></div>', unsafe_allow_html=True)
    with col2:
        st.markdown('<div class="cute-card"><h3>8</h3><p>שנים של חברות</p></div>', unsafe_allow_html=True)
    
    st.info("סתם רציתי להגיד שאני מתגעגעת אליך ברגע זה ממש.")

# --- דף 2: רגעים קטנים (המספרים בגרסה חמודה) ---
elif page == "רגעים קטנים":
    st.title("כל מיני דברים עלינו ✨")
    
    c1, c2, c3 = st.columns(3)
    with c1:
        st.markdown('<div class="cute-card"><h3>∞</h3><p>נשיקות וחיבוקים</p></div>', unsafe_allow_html=True)
    with c2:
        st.markdown('<div class="cute-card"><h3>2,920</h3><p>לילות שבהם נרדמנו במחשבה אחד על השני</p></div>', unsafe_allow_html=True)
    with c3:
        st.markdown('<div class="cute-card"><h3>1</h3><p>לב אחד ענקי</p></div>', unsafe_allow_html=True)
    
    st.divider()
    st.write("זוכר שפעם חשבנו שנהיה רק חברים? מזל שזה עבר לנו...")

# --- דף 3: קיר זיכרונות (הגלריה שביקשת לא לגעת בה) ---
elif page == "קיר זיכרונות":
    st.title("הזיכרונות שלנו 📸")
    st.write("התמונות מתחלפות כאן לבד...")
    
    col1, col2, col3 = st.columns(3)
    p1 = col1.empty()
    p2 = col2.empty()
    p3 = col3.empty()

    for _ in range(5):
        nums = random.sample(range(1, 15), 3)
        p1.image("PHOTO.jpg", caption=f"רגע מתוק {nums[0]}", use_container_width=True)
        p2.image("PHOTO.jpg", caption=f"רגע מתוק {nums[1]}", use_container_width=True)
        p3.image("PHOTO.jpg", caption=f"רגע מתוק {nums[2]}", use_container_width=True)
        time.sleep(4)

# --- דף 4: הפתעה חסויה (הפאזל החדש) ---
elif page == "הפתעה חסויה 🔒":
    st.title("אזור סודי 🔒")
    st.write("כדי לקרוא את המכתב, סדר את שלבי הסיפור שלנו מההתחלה לסוף:")

    # הפאזל: בחירת סדר אירועים
    step1 = st.selectbox("מה היה השלב הראשון?", ["", "מסיבת גיוס ווידוי", "חברים טובים במגמה", "היכרות בחטיבה"])
    step2 = st.selectbox("מה היה השלב השני?", ["", "מסיבת גיוס ווידוי", "חברים טובים במגמה", "היכרות בחטיבה"])
    step3 = st.selectbox("ומה קרה בסוף?", ["", "מסיבת גיוס ווידוי", "חברים טובים במגמה", "היכרות בחטיבה"])

    if step1 == "היכרות בחטיבה" and step2 == "חברים טובים במגמה" and step3 == "מסיבת גיוס ווידוי":
        st.success("כל הכבוד! הסיפור שלנו מושלם בדיוק ככה.")
        st.balloons()
        
        st.divider()
        st.subheader("המכתב שלי אליך ❤️")
        st.write("""
        עידודו שלי,
        
        אחרי 8 שנים של חברות, אני כל כך שמחה שהיום אני יכולה לקרוא לך שלי.
        תודה על כל רגע, על המיינקראפט, על השיחות בטלפון ועל מי שאתה.
        
        אני אוהבת אותך המון,
        נאנה
        """)
        st.snow()
    elif step1 != "" and step2 != "" and step3 != "":
        st.error("אופס, זה לא הסדר הנכון... תנסה שוב!")
