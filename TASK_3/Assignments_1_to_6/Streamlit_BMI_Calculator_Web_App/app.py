import streamlit as st
import string

# Page configuration with updated icon and title
st.set_page_config(
    page_title="BMI Calculator by Annashahadd",  # Updated name
    page_icon="💪",  # Updated icon (muscle emoji)
    layout="centered"
)

# Title of the app
st.title("BMI Calculator by Annashahadd")  # Updated name
st.markdown("## Enter your weight and height to calculate your BMI")

# Create two columns for weight and height input
col1, col2 = st.columns(2)
with col1:
    weight = st.number_input("Enter your weight in kilograms:", min_value=1.0, format="%.2f")
with col2:
    height = st.number_input("Enter your height in centimeters:", min_value=10.0, format="%.2f")

if weight > 0 and height > 0:
    # Convert height from centimeters to meters
    height_in_m = height / 100
    bmi = weight / (height_in_m ** 2)

    st.subheader("Your BMI is:")
    st.markdown(f"**{bmi:.2f}**", unsafe_allow_html=True)  # Bold formatting for BMI value

    # Provide feedback based on the BMI value
    if bmi < 18.5:
        st.error("You are underweight! ⚠️")
    elif 18.5 <= bmi < 24.9:
        st.success("You are normal weight! ✅")
    elif 25 <= bmi < 29.9:
        st.warning("You are overweight! ⚠️")
    else:
        st.error("You are obese! ⚠️")
else:
    st.info("Please enter valid values for weight and height.")