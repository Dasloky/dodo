import streamlit as st
from datetime import date
import time
import random

st.set_page_config(page_title="מערכת עידודו ❤️", page_icon="🔒", layout="wide")

st.markdown("""
<style>

@import url('https://fonts.googleapis.com/css2?family=Assistant:wght@300;400;700&display=swap');

/* צבעים גלובליים */
:root{
--bg: #f1f5f9;
--card: #ffffff;
--text: #0f172a;
--primary: #0284c7;
--accent: #f472b6;
}

/* בסיס */
html, body, .main{
direction: rtl;
text-align: right;
font-family: 'Assistant', sans-serif;
background: var(--bg);
color: var(--text);
}

/* כותרות */
h1,h2,h3{
color: var(--primary) !important;
}

/* כרטיסים */
.stat-card{
background: var(--card);
padding: 25px;
border-radius: 18px;
border-bottom: 5px solid var(--primary);
text-align:center;
box-shadow:0 6px 16px rgba(0,0,0,0.06);
transition:0.2s;
}

.stat-card:hover{
transform:translateY(-3px);
}

/* תמונות */
.styled-img{
border-radius:15px;
object-fit:cover;
}

/* תמונות */
img{
border-radius:14px;
}

/* מובייל */
@media (max-width: 768px){

h1{
font-size:28px;
}

.stat-card{
padding:18px;
font-size:14px;
}

.stat-card h3{
color:#0284c7;
margin-bottom:8px;
}

.stat-card p{
color:#334155 !important;
font-size:16px;
margin:0;
}

[data-testid="stSidebar"]{
width:100% !important;
}

.block-container{
padding-top:1rem;
padding-left:1rem;
padding-right:1rem;
}

}

/* טאבלט */
@media (max-width: 1000px){

.stat-card{
padding:20px;
}

}

</style>
""", unsafe_allow_html=True)

START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

with st.sidebar:
    st.title("מערכת עידודו v3.0")
    page = st.selectbox(
        "לאן תרצה לגשת?",
        ["לוח הבקרה","המספרים שלנו","קיר זיכרונות חי","כספת חסויה 🔒"]
    )
    st.divider()
    st.write("נוצר על ידי נאנה ❤️")

# לוח הבקרה
if page == "לוח הבקרה":

    st.title("מצב המערכת 📊")

    col1,col2 = st.columns(2)

    col1.metric("זמן כזוג",f"{days_together} ימים")
    col2.metric("ותק קשר","8 שנים")

    st.divider()

    st.info("עידודו, המערכת מדווחת על רמות גבוהות של געגוע. מומלץ לשלוח הודעה לנאנה.")

# המספרים שלנו
elif page == "המספרים שלנו":

    st.title("8 שנים במספרים 🔢")
    st.write("כי כדאטה אנליסטית, אני אוהבת למדוד את מה שחשוב:")

    c1,c2,c3 = st.columns(3)

    with c1:
        st.markdown('<div class="stat-card"><h3>∞</h3><p>הודעות "בוקר טוב"</p></div>', unsafe_allow_html=True)

    with c2:
        st.markdown('<div class="stat-card"><h3>2,920</h3><p>ימים של חברות אמת</p></div>', unsafe_allow_html=True)

    with c3:
        st.markdown('<div class="stat-card"><h3>1</h3><p>וידוי אחד ב-12.12</p></div>', unsafe_allow_html=True)

    st.write("")

    st.markdown(
    '<div class="stat-card" style="border-bottom-color: #f472b6;"><h3>99,999+</h3><p>בדיחות פרטיות שרק שנינו מבינים</p></div>',
    unsafe_allow_html=True
    )

# קיר זכרונות
elif page == "קיר זיכרונות חי":

    st.title("הזיכרונות שלנו 📸")
    st.write("התמונות מתעדכנות אוטומטית...")

    col1,col2,col3 = st.columns(3)

    placeholder1 = col1.empty()
    placeholder2 = col2.empty()
    placeholder3 = col3.empty()

    for _ in range(5):

        nums = random.sample(range(1,15),3)

        placeholder1.image("PHOTO.jpg",caption=f"רגע {nums[0]}",use_container_width=True)
        placeholder2.image("PHOTO.jpg",caption=f"רגע {nums[1]}",use_container_width=True)
        placeholder3.image("PHOTO.jpg",caption=f"רגע {nums[2]}",use_container_width=True)

        time.sleep(4)

# כספת
elif page == "כספת חסויה 🔒":

    st.title("הכספת 🔒")

    st.write("כדי להיכנס, אתה חייב להוכיח שזה אתה.")

    st.subheader("החידה:")
    st.write("באיזה תאריך הכל השתנה במסיבת הגיוס ההיא?")

    user_answer = st.text_input("הכנס תאריך",placeholder="DD.MM")

    if user_answer == "12.12":

        st.success("הקוד התקבל. פותחת את הכספת...")

        st.balloons()

        st.warning("⚠️ חריגה בנהלי לבוש טקטי. נאנה דורשת הסברים!")

        st.divider()

        st.subheader("המכתב שלי אליך:")

        st.info("""
עידודו שלי,

אין מספר או קוד שיכולים לתאר מה אתה בשבילי.
אחרי 8 שנים אני עדיין בוחרת בך כל יום מחדש.

אוהבת אותך,
נאנה ❤️
""")

        st.snow()

    elif user_answer != "":
        st.error("קוד שגוי. נסה להיזכר במסיבת הגיוס של בן דוד...")
