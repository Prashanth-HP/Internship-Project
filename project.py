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
    st.write("The dataset includes 8 air pollutants, which are harmful to human health and the environment:")
    st.header("NH3 (Ammonia)")
    st.write("1. Source: Agriculture (fertilizers, livestock waste), industrial processes.\n2. Effects: Causes respiratory irritation and contributes to the formation of fine particulate matter (PM2.5).")
    st.header("CO (Carbon Monoxide)")
    st.write("1. Source: Vehicle emissions, burning of fossil fuels, wildfires.\n2. Effects: Reduces oxygen delivery in the body, leading to headaches, dizziness, or even death at high concentrations.")
    st.header("PM2.5 (Fine Particulate Matter)")
    st.write("1. Source: Vehicle emissions, industrial activities, burning of biomass and coal.\n2. Effects: Can penetrate deep into the lungs, causing respiratory diseases, heart problems, and cancer.")
    st.header("PM10 (Coarse Particulate Matter)")
    st.write("1. Source: Construction dust, road dust, industrial emissions.\n2. Effects: Causes lung irritation, worsens asthma, and affects cardiovascular health.")
    st.header("NO (Nitric Oxide)")
    st.write("1. Source: Vehicle emissions, power plants, and industrial combustion. \n2. Effects: Contributes to smog formation, reduces lung function, and reacts with other pollutants to form NO₂.")
    st.header("NO2 (Nitrogen Dioxide)")
    st.write("1. Source: Fossil fuel combustion, vehicle emissions, industrial processes.\n2. Effects: Causes lung inflammation, worsens asthma, and contributes to acid rain formation.")
    st.header("NOx (Nitrogen Oxides - NO + NO2 mixture)")
    st.write("1. Source: Combustion of fuel in vehicles, power plants, and industrial facilities. \n2. Effects: Major contributor to smog, acid rain, and respiratory illnesses.")
    st.header("SO2 (Sulfur Dioxide)")
    st.write("1. Source: Coal and oil burning in power plants, industrial facilities.\n2. Effects: Causes respiratory issues, contributes to acid rain, and can damage crops.")
    st.title("Cities Covered in the Dataset")
    st.write("This dataset includes air quality data from 26 Indian cities, including major metro cities (Delhi, Mumbai, Kolkata, Chennai, Bengaluru, Hyderabad, etc.) and smaller cities (Shillong, Talcher, Jorapokhar, Brajrajnagar, etc.).")
    st.header("Why These Cities?")
    st.write("1. These cities likely have high pollution levels due to urbanization, industrialization, and vehicular emissions. \n2. Metro cities (like Delhi and Mumbai) experience high PM2.5 and NO2 levels due to traffic and industries. \n3. Industrial towns (like Talcher and Brajrajnagar) may have high SO2 and NOx levels due to power plants and factories.\n4. Smaller cities (like Shillong and Aizawl) might show lower pollution levels due to fewer industries.")
    st.title("How Can You Use This Data?")
    st.write("1. Monitor Air Quality Trends – Analyze how pollution levels change over time in different cities.\n2. Compare Pollution Levels – Identify the most and least polluted cities for specific pollutants.\n3. Policy & Awareness – Help policymakers implement air quality improvement measures.\n4. Predict Future Trends – Use Machine Learning to forecast pollution spikes and take preventive actions.")

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
