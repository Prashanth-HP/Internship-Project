import streamlit as st
import bcrypt
from datetime import datetime
from supabase import create_client

def authentication():
    # Supabase credentials (replace with your project details)
    SUPABASE_URL = "https://bhbthgusfmoyhbplpljh.supabase.co"
    SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImJoYnRoZ3VzZm1veWhicGxwbGpoIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NDI4MDQ3OTgsImV4cCI6MjA1ODM4MDc5OH0.kgpSMQ5NhEA2GJbQ-dmim9zBaDa9t4_lOYtPMWxpMc4"
    supabase = create_client(SUPABASE_URL, SUPABASE_KEY)

    # Function to hash passwords before storing
    def hash_password(password):
        return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

    # Function to verify a hashed password
    def verify_password(stored_hash, password):
        return bcrypt.checkpw(password.encode(), stored_hash.encode())

    # Function to register a new user with hashed password
    def register_user(username, password):
        hashed_pw = hash_password(password)  # Hash the password before storing
        data = {"username": username, "password": hashed_pw, "last_login": None}
        response = supabase.table("users").insert(data).execute()
        return response

    # Function to authenticate user (check hashed password)
    def authenticate_user(username, password):
        response = supabase.table("users").select("password").eq("username", username).execute()
        user_data = response.data
        if user_data and verify_password(user_data[0]["password"], password):
            return True
        return False

    # Function to update last login timestamp
    def update_last_login(username):
        last_login_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        supabase.table("users").update({"last_login": last_login_time}).eq("username", username).execute()

    # Streamlit UI
    st.title("🔐 Secure User Login with Supabase (Hashed Passwords)")

    auth_mode = st.radio("Choose an option:", ["Login", "Sign Up"])

    if auth_mode == "Login":
        username = st.text_input("👤 Username")
        password = st.text_input("🔑 Password", type="password")
        login_button = st.button("Login")

        if login_button:
            if authenticate_user(username, password):
                update_last_login(username)
                st.success(f"Welcome back, {username}! 🎉")
            else:
                st.error("Invalid username or password!")

    elif auth_mode == "Sign Up":
        new_username = st.text_input("👤 Choose a Username")
        new_password = st.text_input("🔑 Choose a Password", type="password")
        signup_button = st.button("Sign Up")

        if signup_button:
            response = register_user(new_username, new_password)
            if "error" in response:
                st.error("Username already exists. Choose a different one.")
            else:
                st.success("✅ Account created successfully! You can now log in.")
