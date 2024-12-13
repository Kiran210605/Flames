import streamlit as st

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

st.title('FLAMES Game')
st.write('Find out what type of relationship exists between two names according to the classic FLAMES game.')

name1 = st.text_input("Enter the first name:")
name2 = st.text_input("Enter the second name:")

if st.button('Calculate Relationship'):
    result = flames_game(name1, name2)
    st.success(f"The relationship between {name1} and {name2} is: {result}")
