import streamlit as st

# FLAMES calculation function
def flames_game(name1, name2):
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)
    count = len(name1) + len(name2)
    flames = ['❤️ Friends', '💘 Love', '💫 Affection', '💍 Marriage', '😠 Enemies', '👨‍👩‍👧 Siblings']
    while len(flames) > 1:
        index = count % len(flames) - 1
        if index >= 0:
            flames = flames[index+1:] + flames[:index]
        else:
            flames = flames[:-1]
    return flames[0]

# Custom Background and Style
st.markdown(
    """
    <style>
    .stApp {
        background-image: url("https://wallpaperaccess.com/full/2593235.jpg");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }
    .stButton button {
        background-color: #ff69b4 !important;
        color: white !important;
        border-radius: 10px;
        height: 50px;
        width: 200px;
        font-size: 16px;
    }
    .stTextInput>div>div>input {
        border: 2px solid #ff69b4;
        border-radius: 10px;
        height: 40px;
        font-size: 16px;
    }
    .stSuccess {
        font-size: 24px !important;
        color: white !important;
        font-weight: bold;
        background-color: #ff69b4;
        border-radius: 10px;
        padding: 10px;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title and Instructions
st.title("💖 FLAMES Game 💖")
st.write("**Find out your special connection using the classic FLAMES game.**")

# Session state management
if 'name1' not in st.session_state:
    st.session_state.name1 = ""
if 'name2' not in st.session_state:
    st.session_state.name2 = ""
if 'result' not in st.session_state:
    st.session_state.result = ""

# Input fields
st.session_state.name1 = st.text_input("💑 Enter the first name:", st.session_state.name1)
st.session_state.name2 = st.text_input("💏 Enter the second name:", st.session_state.name2)

# Button to calculate relationship
if st.button('💞 Calculate Relationship 💞'):
    if st.session_state.name1 and st.session_state.name2:
        st.session_state.result = flames_game(st.session_state.name1, st.session_state.name2)
        st.success(f"💖 The relationship between {st.session_state.name1} and {st.session_state.name2} is: {st.session_state.result}! 💖")
        
        # Reset names for next entry
        st.session_state.name1 = ""
        st.session_state.name2 = ""
