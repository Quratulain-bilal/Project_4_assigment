import streamlit as st

# Page configuration
st.set_page_config(
    page_title="My Python Website",
    page_icon="🌐",
    layout="wide"
)

# Navigation menu
st.sidebar.title("Navigation 🧭")
page = st.sidebar.radio("Go to:", ["Home", "About", "Health Dashboard", "Contact"])

# Home Page
if page == "Home":
    st.title("Welcome to My Python Website! 🌟")
    st.markdown("""
    ### This is a simple website built using Streamlit.
    - Navigate through the sidebar to explore different sections.
    - Use the **Health Dashboard** to track your fitness and wellness.
    - Visit the **About** page to learn more about this project.
    - Fill out the **Contact** form to get in touch.
    """)
    st.image("https://via.placeholder.com/800x400", caption="Placeholder Image")

# About Page
elif page == "About":
    st.title("About This Website 📖")
    st.markdown("""
    This website is built using **Streamlit**, a powerful Python library for creating interactive web applications.
    - **Purpose**: To demonstrate how easy it is to build a website with Streamlit.
    - **Features**:
      - Simple navigation using a sidebar.
      - Interactive components like forms and calculators.
      - Responsive design for better user experience.
    """)

# Health Dashboard Page
elif page == "Health Dashboard":
    st.title("Health Dashboard 🩺")
    st.markdown("Track your daily health metrics and stay fit!")

    # Calorie Tracker
    st.subheader("Calorie Tracker 🍎")
    calorie_goal = st.number_input("Enter your daily calorie goal:", min_value=500, max_value=5000, value=2000)
    calories_consumed = st.number_input("Enter calories consumed today:", min_value=0, max_value=10000, value=0)
    calories_remaining = calorie_goal - calories_consumed

    if calories_remaining > 0:
        st.success(f"You have {calories_remaining} calories remaining today!")
    else:
        st.error("You have exceeded your calorie goal today! ⚠️")

    # Hydration Reminder
    st.subheader("Hydration Reminder 💧")
    water_goal_liters = st.slider("Set your daily water goal (in liters):", min_value=1, max_value=5, value=2)
    water_consumed_liters = st.number_input("How much water have you consumed today? (in liters):", min_value=0.0, max_value=water_goal_liters, format="%.1f")

    if water_consumed_liters >= water_goal_liters:
        st.success("Great job! You've met your hydration goal! ✅")
    else:
        st.warning(f"Drink {water_goal_liters - water_consumed_liters:.1f} more liters of water today!")

    # Daily Step Goal
    st.subheader("Daily Step Goal 🚶‍♂️")
    step_goal = st.number_input("Enter your daily step goal:", min_value=1000, max_value=20000, value=10000)
    steps_taken = st.number_input("How many steps have you taken today?", min_value=0, max_value=step_goal * 2, value=0)

    if steps_taken >= step_goal:
        st.success("Congratulations! You've reached your step goal! 🎉")
    else:
        st.info(f"You need {step_goal - steps_taken} more steps to reach your goal.")

# Contact Page
elif page == "Contact":
    st.title("Contact Us 📞")
    st.markdown("Fill out the form below to get in touch:")

    with st.form("contact_form"):
        name = st.text_input("Your Name:")
        email = st.text_input("Your Email:")
        message = st.text_area("Your Message:")
        submit = st.form_submit_button("Submit")

        if submit:
            if name and email and message:
                st.success("Thank you for contacting us! We'll get back to you soon.")
            else:
                st.error("Please fill out all fields.")