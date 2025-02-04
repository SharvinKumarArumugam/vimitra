

import streamlit as st

import numpy as np


# Function to display ASCII birthday cake
def birthday_cake():
    cake = """
        🎂🎂🎂🎂🎂🎂  
        🎂🎂🎂🎂🎂🎂  
     🎂🎂🎂🎂🎂🎂🎂🎂🎂  
    🎂🎂🎂🎂🎂🎂🎂🎂🎂🎂🎂  
    🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉🎉
    """
    return cake



# Streamlit UI
st.title("🎉 Birthday Wish Generator 🎂")
st.write("A special birthday wish with love! ❤️")
st.write("❤️")
# Input for the name
bby_name = st.text_input("Enter your name Chellow:", "")

# Button to generate the wish
if st.button("Generate Wish"):
    if bby_name:
        st.text("❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤")
        st.subheader(f"🎉 Happy Birthday, {bby_name} Chellow! 🎉          ❤️❤❤️")
        st.text("I love you a lot... I miss you a lot, bby! ❤️             ❤️❤❤️")
        st.text("Sharvin ❤️ Vimitra                                        ❤️❤❤️")
        st.text("❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤❤️❤")
        
        st.text(birthday_cake())  # Display ASCII cake
        say_birthday_wish(bby_name)  # Play the TTS birthday wish
        plot_heart()  # Show heart plot
    else:
        st.warning("Please enter your name!")

