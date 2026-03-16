import streamlit as st
from datetime import date

# הגדרות דף - חייב להיות הדבר הראשון בקוד
st.set_page_config(
    page_title="מזל טוב!",
    page_icon="🎁",
    layout="centered"
)

# --- הזרקת CSS לטיפול בעברית (RTL) ועיצוב כללי ---
st.markdown("""
    <style>
    /* הגדרת פונט ויישור לימין לכל האפליקציה */
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');
    
    html, body, [data-testid="stSidebarNav"], .main {
        direction: rtl;
        text-align: right;
        font-family: 'Assistant', sans-serif;
    }
    
    /* יישור כותרות וטקסט מרכזי */
    div[data-testid="stMarkdownContainer"] p, h1, h2, h3, h4, li {
        text-align: right;
    }

    /* תיקון כיוון הניווט בצד */
    section[data-testid="stSidebar"] > div {
        direction: rtl;
    }

    /* עיצוב כפתורים */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
        background-color: #ff4b4b;
        color: white;
        border: none;
        padding: 10px;
    }
    
    /* תיקון יישור למדדים (Metrics) */
    [data-testid="stMetricValue"] {
        text-align: right;
        direction: ltr; /* מספרים נראים טוב יותר משמאל לימין */
    }
    </style>
    """, unsafe_allow_html=True)

# --- פונקציות עזר ---
def calculate_days(start_date):
    today = date.today()
    delta = today - start_date
    return delta.days

# הגדרת תאריך תחילת הקשר (שני לתאריך שלכם)
ANNIVERSARY = date(2022, 5, 15) 

# --- תפריט צד (Sidebar) ---
st.sidebar.title("הניווט שלנו 🧭")
page = st.sidebar.radio("עברי בין הדפים:", 
    ["הבית שלנו", "ציר זמן של אהבה", "גלריית רגעים", "בוחן פתע", "הקדשה אישית"])

# --- דף 1: דף הבית ---
if page == "הבית שלנו":
    st.balloons()
    st.title("מזל טוב, אהוב שלי! 🎂")
    st.write("ברוך הבא למקום הקטן שבניתי בשבילך, כדי לחגוג את מי שאתה ואת מה שאנחנו.")
    
    # הצגת נתונים מספריים
    days_together = calculate_days(ANNIVERSARY)
    col1, col2 = st.columns(2)
    with col1:
        st.metric(label="ימים שאנחנו יחד", value=f"{days_together}")
    with col2:
        st.metric(label="חוויות שצברנו", value="∞")

    st.divider()
    st.subheader("מדד האהבה היום:")
    love_score = st.select_slider("כמה אני אוהבת אותך?", options=["המון", "ממש המון", "הכי בעולם", "יותר ממה שאפשר לתאר"])
    st.write(f"התשובה היא: **{love_score}** (ולא הייתה אופציה אחרת...)")

# --- דף 2: ציר זמן ---
elif page == "ציר זמן של אהבה":
    st.header("הדרך שעברנו יחד 🗺️")
    st.write("כל נקודה היא זיכרון שלא הייתי מחליפה בעד שום הון שבעולם:")
    
    st.info("**2023:** הדייט הראשון שלנו. המבוכה, החיוכים וההבנה שיש כאן משהו מיוחד.")
    st.info("**2024:** הטיול ההוא שבו צחקנו עד שכאבה הבטן.")
    st.info("**2025:** רגעים קטנים של יומיום שהפכו לזיכרונות גדולים.")
    st.success("ואנחנו רק בהתחלה...")

# --- דף 3: גלריית תמונות ---
elif page == "גלריית רגעים":
    st.header("תמונות וזיכרונות 📸")
    st.write("כאן תמצאי כמה מהרגעים האהובים עליי:")
    
    # שימוש בטאבים לחלוקת התמונות
    tab1, tab2 = st.tabs(["רגעים מצחיקים", "רגעים מרגשים"])
    
    with tab1:
        # st.image("images/funny1.jpg", caption="זוכר מה קרה כאן?")
        st.write("[כאן תעלי תמונה מהתיקייה images שב-GitHub]")
    with tab2:
        # st.image("images/sweet1.jpg", caption="אחד הרגעים האהובים עליי")
        st.write("[כאן תעלי תמונה מהתיקייה images שב-GitHub]")

# --- דף 4: בוחן פתע ---
elif page == "בוחן פתע":
    st.header("כמה אתה מכיר אותנו? 🤔")
    
    score = 0
    q1 = st.radio("מה הדבר שאני הכי אוהבת לעשות איתך?", ["לראות סרט", "סתם לדבר", "לשחק Minecraft", "לטייל"])
    if q1 == "סתם לדבר": # עדכני לתשובה הנכונה
        score += 1
        
    q2 = st.selectbox("איזה צבע אני הכי אוהבת עליך?", ["כחול", "שחור", "המדים שלך", "לבן"])
    if q2 == "המדים שלך": # עדכני לתשובה הנכונה
        score += 1
        
    if st.button("סיום הבוחן"):
        if score == 2:
            st.snow()
            st.success("אלוף! אתה מכיר אותי בול.")
        else:
            st.warning(f"קיבלת {score}/2. לא נורא, יש לנו את כל החיים להכיר!")

# --- דף 5: הקדשה ---
elif page == "הקדשה אישית":
    st.header("משהו קטן מהלב 💌")
    st.write("""
    כאן את כותבת את כל מה שאת מרגישה...
    
    על כמה הוא משמעותי עבורך, על הביטחון שהוא נותן לך, 
    ועל זה שאת גאה בו (במיוחד עם כל העבודה הקשה בבסיס).
    
    מאחלת לנו עוד שנים של צחוק, למידה משותפת וים של אהבה.
    """)
    
    if st.button("לחץ להפתעה אחרונה"):
        st.snow()
        st.write("❤️ אוהבת אותך הכי בעולם! ❤️")
