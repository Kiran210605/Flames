import streamlit as st

# FLAMES calculation function
def flames_game(name1, name2):
    # Remove spaces and convert to lowercase
    name1 = name1.replace(" ", "").lower()
    name2 = name2.replace(" ", "").lower()
    
    # Remove common characters from both names
    for char in name1:
        if char in name2:
            name1 = name1.replace(char, '', 1)
            name2 = name2.replace(char, '', 1)
    
    # Count the total number of remaining characters
    count = len(name1) + len(name2)
    
    # FLAMES mapping to types of relationships
    flames = ['Friends', 'Love', 'Affection', 'Marriage', 'Enemies', 'Siblings']
    
    # Determine the relationship using the remaining count
    while len(flames) > 1:
        index = count % len(flames) - 1
        if index >= 0:
            right = flames[index + 1:]
            left = flames[:index]
            flames = right + left
        else:
            flames = flames[:-1]

    return flames[0]

# Title and description
st.title('FLAMES Game')
st.write('Find out what type of relationship exists between two names according to the classic FLAMES game.')

# Initialize session state variables
if 'name1' not in st.session_state:
    st.session_state.name1 = ""
if 'name2' not in st.session_state:
    st.session_state.name2 = ""
if 'result' not in st.session_state:
    st.session_state.result = ""

# Input fields
st.session_state.name1 = st.text_input("Enter the first name:", st.session_state.name1)
st.session_state.name2 = st.text_input("Enter the second name:", st.session_state.name2)

# Calculate button
if st.button('Calculate Relationship'):
    if st.session_state.name1 and st.session_state.name2:
        st.session_state.result = flames_game(st.session_state.name1, st.session_state.name2)
        st.success(f"The relationship between {st.session_state.name1} and {st.session_state.name2} is: {st.session_state.result}")
        
        # Clear the names after showing the result
        st.session_state.name1 = ""
        st.session_state.name2 = ""
