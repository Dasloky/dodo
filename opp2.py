import streamlit as st
from datetime import date

# הגדרות דף
st.set_page_config(page_title="עבור עידודו ❤️", page_icon="💙", layout="centered")

# --- עיצוב CSS משופר (RTL, ניגודיות גבוהה ועיצוב כפתורים) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Assistant:wght@400;700&display=swap');
    
    /* הגדרות כלליות */
    html, body, [data-testid="stSidebarNav"], .main {
        direction: rtl;
        text-align: right;
        font-family: 'Assistant', sans-serif;
        background-color: #F8FAFC; /* רקע בהיר מאוד וקריא */
    }
    
    /* טקסט ראשי - שחור/כחול עמוק לניגודיות מקסימלית */
    div[data-testid="stMarkdownContainer"] p, h1, h2, h3, h4, li, span {
        text-align: right;
        color: #1E293B !important; 
    }

    /* כותרות בולטות בכחול עידודו */
    h1, h2 {
        color: #0284C7 !important;
    }

    /* עיצוב כפתורים */
    .stButton>button {
        width: 100%;
        border-radius: 12px;
        background-color: #0284C7;
        color: white !important;
        border: none;
        padding: 10px;
        font-weight: bold;
        transition: 0.3s;
    }
    .stButton>button:hover {
        background-color: #0369A1;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    }

    /* עיצוב ה-Easter Egg */
    .easter-egg {
        background-color: #FFFFFF;
        padding: 25px;
        border-right: 6px solid #0284C7;
        border-radius: 15px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.05);
        color: #1E293B;
        line-height: 1.6;
    }
