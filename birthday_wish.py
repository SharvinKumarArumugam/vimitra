

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

# Function to play a birthday wish using text-to-speech
def say_birthday_wish(name):
    engine = pyttsx3.init()
    message = f"Happy Birthday, {name}! Have a wonderful year ahead!"
    engine.say(message)
    engine.runAndWait()

# Function to create a heart shape
def plot_heart():
    t = np.linspace(0, 2 * np.pi, 1000)
    x = 16 * np.sin(t)**3
    y = 13 * np.cos(t) - 5 * np.cos(2 * t) - 2 * np.cos(3 * t) - np.cos(4 * t)

    fig, ax = plt.subplots()
    ax.plot(x, y, color='red')
    ax.fill(x, y, color='red')
    ax.axis('off')

    ax.text(0, 0, "Sharvin 💖 Vimitra", fontsize=12, color='white', 
            ha='center', va='center')

    st.pyplot(fig)

# Streamlit UI
st.title("🎉 Birthday Wish Generator 🎂")
st.write("A special birthday wish with love! ❤️")

# Input for the name
bby_name = st.text_input("Enter your name Chellow:", "")

# Button to generate the wish
if st.button("Generate Wish"):
    if bby_name:
        st.subheader(f"🎉 Happy Birthday, {bby_name} Chellow! 🎉")
        st.text("I love you a lot... I miss you a lot, bby! ❤️")
        
        st.text(birthday_cake())  # Display ASCII cake
        say_birthday_wish(bby_name)  # Play the TTS birthday wish
        plot_heart()  # Show heart plot
    else:
        st.warning("Please enter your name!")

