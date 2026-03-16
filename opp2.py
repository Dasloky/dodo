import streamlit as st

st.set_page_config(page_title="Birthday Surprise ❤️")

if "stage" not in st.session_state:
    st.session_state.stage = 0

# עמוד פתיחה
if st.session_state.stage == 0:

    st.title("יש לי הפתעה בשבילך 🎁")

    st.image("photo.jpg")

    if st.button("תתחיל"):
        st.session_state.stage = 1

# גלריית זיכרונות
elif st.session_state.stage == 1:

    st.header("כמה רגעים שאני אוהבת ❤️")

    st.image("photo.jpg", caption="הדייט הראשון שלנו")

    if st.button("המשך"):
        st.session_state.stage = 2

# מסך Easter Egg
elif st.session_state.stage == 2:

    st.header("יש פה הפתעה סודית...")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.button("🐱")

    with col2:
        st.button("🎮")

    with col3:
        if st.button("❤️"):
            st.session_state.stage = 3

    with col4:
        st.button("🍕")

# הודעת ברכה
elif st.session_state.stage == 3:

    st.balloons()

    st.title("יום הולדת שמח אהוב שלי 🎂")

    st.write("""
    תודה שאתה בחיים שלי.  
    מאז ה-1.1.26 כל יום איתך מיוחד.  
    אני אוהבת אותך ❤️
    """)

    st.image("photo.jpg")
