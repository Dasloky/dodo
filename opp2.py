import streamlit as st

st.set_page_config(page_title="Birthday Surprise ❤️", layout="centered")

# תפריט ניווט
page = st.sidebar.radio(
    "ניווט",
    ["🏠 פתיחה", "📸 זיכרונות", "🕵️ סוד", "🎂 הברכה"]
)

# עמוד פתיחה
if page == "🏠 פתיחה":

    st.title("יש לי הפתעה בשבילך 🎁")

    st.image("PHOTO.jpg")

    st.write("""
    הכנתי משהו קטן בשבילך ❤️  
    תשתמש בתפריט בצד כדי לגלות הכל
    """)

# עמוד זיכרונות
elif page == "📸 זיכרונות":

    st.title("כמה רגעים שאני אוהבת ❤️")

    col1, col2 = st.columns(2)

    with col1:
        st.image("PHOTO.jpg", caption="רגע ראשון שלנו")

    with col2:
        st.image("PHOTO.jpg", caption="טיול שלנו")

    st.image("PHOTO.jpg", caption="רגע מצחיק שאני אוהבת")

# עמוד סוד (Easter Egg)
elif page == "🕵️ סוד":

    st.title("יש כאן משהו סודי...")

    st.write("רק כפתור אחד יגלה את ההפתעה")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        if st.button("🐱"):
            st.toast("לא זה 😅")

    with col2:
        if st.button("🍕"):
            st.toast("כמעט")

    with col3:
        if st.button("🎮"):
            st.toast("נסה שוב")

    with col4:
        if st.button("❤️"):
            st.session_state.secret_found = True
            st.success("מצאת את הסוד 😉")

# עמוד הברכה
elif page == "🎂 הברכה":

    if "secret_found" not in st.session_state:
        st.warning("צריך למצוא את הסוד קודם 😉")
    else:
        st.balloons()

        st.title("יום הולדת שמח אהוב שלי 🎂")

        st.write("""
        מאז ה-1.1.26 כל יום איתך מיוחד יותר.  
        תודה שאתה בחיים שלי ❤️
        """)

        st.image("PHOTO.jpg")
