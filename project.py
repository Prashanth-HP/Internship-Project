import streamlit as st
import pandas as pd


# Home Page
def Home():
    st.title("🌍 Welcome to Your Air Quality Companion!")
    
    # Add a welcoming image (Ensure you have 'home_banner.jpg' in your project)

    st.markdown(
        """
        ### Hey there! 👋  
        Ever wondered how clean the air around you really is? You're in the right place!  
        Our **Air Quality Monitoring App** helps you track pollution levels, compare cities, and make informed choices for a healthier life. 🌱💨
        """
    )

    st.divider()

    st.subheader("🚀 What You Can Do Here")
    st.write("Here's what makes this app awesome:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("📍 **City-wise Pollution Analysis** – Compare different locations")
        st.markdown("📊 **Interactive Dashboards** – Visualize trends easily")
        st.markdown("🌍 **Make Healthier Choices** – Breathe better, live better")

    with col2:
        st.markdown("💡 **Understand Gases & Pollutants** – Learn what affects your health")
        st.markdown("🤖 **Data-Driven Chatbot.** – Ask questions, get insights")


    st.divider()

    st.subheader("🛠️ How to Get Started?")
    st.markdown(
        """
        - 📊 **Go to the Dashboard** → Explore real-time pollution data  
        - 📍 **Check Info Section** → Understand pollutants & gases  
        - 💬 **Chat with our bot** → Get quick air quality insights  
        """
    )

    st.warning("Your health matters. Stay informed. Breathe fresh! 😊")





def get_best_match(user_input):
    match = process.extractOne(user_input, qa_df["Question"].dropna())
    if match and len(match) >= 2 and match[1] > 70:
        return qa_df.loc[qa_df["Question"] == match[0], "Answer"].values[0]
    return "I couldn't find an exact match. Please try rephrasing your question."

def chatbot_page():
    st.title("Chatbot")
    user_input = st.text_input("You: ", "")
    if st.button("Send"):
        st.write(f"Chatbot: {get_best_match(user_input)}")

# City and Gases Page
def city_and_gases():
    st.title("Explanation of Gases in the Dataset")
    st.header("NH3 (Ammonia)")
    st.write("Sources: Agriculture, industrial processes.")
    st.header("CO (Carbon Monoxide)")
    st.write("Sources: Vehicle emissions, fossil fuels.")

# Main Function
def main():
    st.sidebar.title("Menu")
    sidebar = st.sidebar.radio("", ["Home", "About Gases", "Dashboard", "Chatbot"])
    if sidebar == "Dashboard":
        dashboard_page()
    elif sidebar == "Home":
        Home()
    elif sidebar == "About Gases":
        city_and_gases()
    elif sidebar == "Chatbot":
        chatbot_page()

if __name__ == "__main__":
    main()
