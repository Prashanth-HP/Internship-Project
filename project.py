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




def dashboard_page():
    st.title("Power BI Dashboard")

    # Create two columns to display images side by side
    col1, col2 = st.columns(2)

    with col1:
        st.image("data\page1.png", caption="Air Quality Index Dashboard", use_container_width=True)

    with col2:
        st.image("data\page2.png", caption="Pollutant Levels by City", use_container_width=True)

    st.write("Due to a technical issue on our side, we are unable to display the report online, [Install PowerBI Desktop](https://apps.microsoft.com/detail/9ntxr16hnw1t?launch=true&mode=full&hl=en-us&gl=in&ocid=bingwebsearch) , download below given pbix file and view the report ")
    #st.write("[Install PowerBI Desktop](https://apps.microsoft.com/detail/9ntxr16hnw1t?launch=true&mode=full&hl=en-us&gl=in&ocid=bingwebsearch)")
    # Provide download option for the Power BI file
    pbix_file_path = "data\Final Dashboard.pbix"  # Ensure the file is in the correct location
    
    with open(pbix_file_path, "rb") as file:
        st.download_button(
            label="Download Power BI Dashboard (.pbix)",
            data=file,
            file_name="Final Dashboard.pbix",
            mime="application/octet-stream"
        )


# Chatbot Page
qa_df = pd.read_csv("cb_questions.csv").dropna(subset=["Question", "Answer"])
qa_df["Question"] = qa_df["Question"].str.strip()

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
