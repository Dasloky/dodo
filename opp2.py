import streamlit as st
from datetime import date

# הגדרות דף
st.set_page_config(page_title="עבור עידודו ❤️", page_icon="💙", layout="centered")

# --- עיצוב CSS מותאם (RTL, צבעי כחול-תכלת, ותיקוני סליידר) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');
    
    html, body, [data-testid="stSidebarNav"], .main {
        direction: rtl;
        text-align: right;
        font-family: 'Assistant', sans-serif;
        background-color: #f0f8ff; /* רקע תכלת עדין */
    }
    
    div[data-testid="stMarkdownContainer"] p, h1, h2, h3, h4, li {
        text-align: right;
        color: #003366; /* כחול כהה לטקסט */
    }

    /* עיצוב כפתורים בכחול */
    .stButton>button {
        width: 100%;
        border-radius: 15px;
        background-color: #4682B4;
        color: white;
        border: none;
        font-weight: bold;
    }

    /* תיקון הסליידר */
    div[data-testid="stSelectSlider"] { direction: ltr !important; }
    div[data-testid="stSelectSlider"] label { direction: rtl !important; text-align: right !important; display: block; }
    
    /* עיצוב ל-Easter Egg */
    .easter-egg {
        background-color: #ffffff;
        padding: 20px;
        border-right: 5px solid #4682B4;
        border-radius: 10px;
        font-style: italic;
    }
    </style>
    """, unsafe_allow_html=True)

# --- לוגיקה של תאריכים ---
START_DATE = date(2026, 1, 1)
days_together = (date.today() - START_DATE).days

# --- תפריט צד ---
st.sidebar.title(f"שלום {st.sidebar.selectbox('מי גולש עכשיו?', ['עידודו', 'נאנה'])}")
menu = st.sidebar.radio("לאן נלך?", ["דף הבית", "המסע שלנו (8 שנים!)", "גלריית רגעים", "הקדשה מהלב"])

if menu == "דף הבית":
    st.balloons()
    st.title(f"מזל טוב, עידודו שלי! 🎂")
    st.subheader(f"נאנה בנתה לך אתר קטן, כי הגיע הזמן.")
    
    col1, col2 = st.columns(2)
    col1.metric("ימים של אהבה רשמית", f"{days_together}")
    col2.metric("שנים של חברות", "8")
    
    st.divider()
    
    # הבדיחה הפרטית
    st.warning("⚠️ אזהרת בטיחות חמורה!")
    st.write("**נא לשלוח אזהרה מראש לפני שליחת תמונות עם טקטי, ריצ'רץ' פתוח ויד מאחורי הראש. נאנה לא עומדת בזה.**")
    
    # מד האהבה
    st.subheader("מד האהבה היומי:")
    st.select_slider("", options=["אוהבת", "אוהבת מאוד", "חולה עליך", "עידודו, אין לי מילים"], value="עידודו, אין לי מילים")

elif menu == "המסע שלנו (8 שנים!)":
    st.header("מכיתה ח' ועד היום... 🗺️")
    st.write("הדרך שעשינו היא הדבר האהוב עליי:")
    
    with st.expander("🎒 ימי החטיבה והתיכון"):
        st.write("מלהיות חלק מאותה חבורה, לבחור באותה מגמה ופשוט להיות שם אחד בשביל השנייה כל יום בכיתה.")
    
    with st.expander("🎆 12.12 - הלילה ששינה הכל"):
        st.write("מסיבת הגיוס של בן דוד שלך. הרגע שבו אמרת לי מה אתה מרגיש, והרגע שבו הכל פתאום הסתדר בראש.")
    
    with st.expander("🥂 1.1.2026 - התחלה חדשה"):
        st.write("היום שבו הפכנו רשמית ל'אנחנו'. המתנה הכי טובה לשנה החדשה.")

elif menu == "גלריית רגעים":
    st.header("התמונות שלנו 📸")
    st.write("קצת רגעים מהשמונה שנים האלו (ועוד כמה שנוספו לאחרונה):")
    
    tab1, tab2 = st.tabs(["אנחנו יחד", "עידודו (זהירות, חתיך)"])
    
    with tab1:
        # כאן תשימי 11 תמונות. דוגמה למבנה:
        cols = st.columns(2)
        for i in range(1, 12):
            with cols[i % 2]:
                # st.image(f"images/together_{i}.jpg")
                st.write(f"🖼️ תמונה שלנו #{i}")
                
    with tab2:
        # כאן תשימי 3 תמונות שלו
        cols_he = st.columns(3)
        for i in range(1, 4):
            with cols_he[i-1]:
                # st.image(f"images/he_{i}.jpg")
                st.write(f"🌟 עידודו #{i}")
        st.write("*(בתהליך השגת תמונות ילדות...)*")

elif menu == "הקדשה מהלב":
    st.header("משהו ממני אלייך 💌")
    st.write("""
    עידודו שלי, השמונה שנים האלו היו רק ההקדמה לסיפור האמיתי שלנו. 
    אני כל כך שמחה שבחרנו אחד בשנייה שוב ושוב, מהמגמה בתיכון ועד היום.
    """)
    
    # ה-Easter Egg (המכתב הארוך)
    st.write("---")
    if st.checkbox("יש לך הודעה חדשה מנאנה (לחץ לקריאה)"):
        st.markdown(f"""
        <div class="easter-egg">
        <b>הודעה בתגובה למכתב שלך:</b><br><br>
        כאן תדביקי את הטקסט הארוך שכתבת לו. 
        זה המקום לכל המילים העמוקות, התגובות לדברים שהוא כתב לך,
        וכל הרגש שאת רוצה לשמור רק לשניכם.
        <br><br>
        אוהבת אותך הכי בעולם, נאנה.
        </div>
        """, unsafe_allow_html=True)
        st.snow()
