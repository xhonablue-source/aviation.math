import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import openai

# Page configuration
st.set_page_config(
    page_title="AEROSPACE: Interactive Math & Engineering Curriculum",
    page_icon="✈️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Header
st.title("✈️ AEROSPACE 🚀")
st.subheader("An Interactive Math & Engineering Curriculum")
st.write("Exploring the mathematics behind flight and space exploration")

# Sidebar navigation
st.sidebar.title("📚 Modules")
page = st.sidebar.selectbox(
    "Choose a section:",
    ["🏠 Home & Overview", "✈️ Flight Trajectories", "🛰️ Orbital Mechanics",
     "🚀 Rocket Science", "🧑🏾‍🚀 Aaron's Lunar Mission", "📊 Quiz: The Flight Test", "📚 External Resources"]
)

# Home Page
if page == "🏠 Home & Overview":
    st.header("Welcome to the Aerospace Curriculum!")
    st.markdown("""
This program is designed to explore key mathematical concepts through the lens of aerospace engineering. You will discover how algebra, trigonometry, and calculus are essential tools for designing aircraft, launching rockets, and navigating the solar system.
""")

    cols = st.columns(2)
    with cols[0]:
        st.info("""
        **Module 1: Flight Trajectories**  
        The mathematics of flight paths using quadratic equations. Learn how to calculate a plane's altitude and trajectory.  
        Common Core Standards: A-REI.4b, F-IF.7a
        """)
        st.info("""
        **Module 3: Rocket Science**  
        Exploring exponential growth and decay in rocket propulsion. Understand the Tsiolkovsky rocket equation and its impact on space travel.  
        Common Core Standards: A-CED.1, F-LE.1
        """)

    with cols[1]:
        st.info("""
        **Module 2: Orbital Mechanics**  
        Solving systems of linear equations to understand gravitational forces and satellite orbits. This module covers Kepler's Laws.  
        Common Core Standards: A-REI.5, A-REI.6
        """)
        st.info("""
        **Module 4: The Flight Test**  
        A comprehensive quiz to test your knowledge across all key concepts. Put your new aerospace math skills to the test!  
        Assessment of all key concepts.
        """)

# Module 1
elif page == "✈️ Flight Trajectories":
    st.header("✈️ Module 1: Flight Trajectories")
    st.subheader("The Parabolic Path of Flight")
    st.markdown("""
    In this module, we examine the equation of a projectile's vertical motion:

    $$h(t) = -4.9t^2 + v_0 t$$

    **Where:**
    - $h(t)$ is the height (in meters) after $t$ seconds
    - $t$ is time in seconds since launch
    - $v_0$ is the initial vertical velocity (in meters per second)
    - The constant -4.9 represents half of the gravitational acceleration ($g \approx 9.8$ m/s²) on Earth

    This formula models the upward and downward motion of an object launched straight up.
    """)

    v0 = st.slider("Initial Velocity $v_0$ (m/s):", 10, 100, 50)
    t_vals = np.linspace(0, 2*v0/9.8, 300)
    h_vals = -4.9 * t_vals**2 + v0 * t_vals

    fig, ax = plt.subplots()
    ax.plot(t_vals, h_vals, label=f"v₀ = {v0} m/s", color="blue")
    ax.set_xlabel("Time (s)")
    ax.set_ylabel("Height (m)")
    ax.set_title("Projectile Motion")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

    st.success(f"Maximum height: {max(h_vals):.2f} meters")

# Quiz Module: LLM-enhanced Feedback
elif page == "📊 Quiz: The Flight Test":
    st.header("📊 The Flight Test")

    st.subheader("1. Quadratic Trajectory")
    st.write("A rocket's height is given by the equation:")
    st.latex(r"h(t) = -16t^2 + 192t")
    answer_1 = st.radio("What is the maximum height the rocket reaches?",
                        ["A. 192 ft", "B. 576 ft", "C. 16 ft", "D. 384 ft"], index=None)

    feedback_1 = ""
    if answer_1:
        if answer_1 == "B. 576 ft":
            st.success("Correct! Max height is found at vertex: t = 6, h(6) = 576 ft.")
        else:
            feedback_1 = "To find the vertex of a quadratic equation in the form ax^2 + bx + c, use t = -b/2a. Here, a = -16 and b = 192."
            st.error(feedback_1)

    st.subheader("2. Solve the System")
    st.write("Solve: 2x + y = 8 and x - y = 1")
    user_input = st.text_input("Enter value of x:")
    feedback_2 = ""
    if user_input:
        try:
            if float(user_input) == 3:
                st.success("Correct! x = 3")
            else:
                feedback_2 = "Try using elimination: Add both equations after isolating variables."
                st.error("Incorrect. Try elimination or substitution.")
        except:
            feedback_2 = "Make sure you're entering a numeric value."
            st.warning("Please enter a valid number.")

    if user_input:
        if st.button("🤖 Dr. X Help on Question 2"):
            with st.spinner("Dr. X is analyzing your response..."):
                prompt_2 = f"""
                The student attempted to solve a system: 
                2x + y = 8 and x - y = 1
                Their input for x was: {user_input}.
                Feedback so far: {feedback_2}
                Provide a clear explanation of how to solve this using substitution or elimination.
                End with one encouragement and a mindset-building resource.
                """
                response_2 = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are Dr. X, a math coach helping a student understand how to solve systems of equations using elimination or substitution."},
                        {"role": "user", "content": prompt_2}
                    ]
                )
                st.info(response_2["choices"][0]["message"]["content"])

    st.subheader("3. Exponential Decay")
    st.write("A satellite's solar panel efficiency drops 5% annually. What's the equation for E(t)?")
    answer_3 = st.text_input("Enter equation for E(t):")
    feedback_3 = ""
    if answer_3:
        if "100 * (0.95)**t" in answer_3.replace(" ", "") or "100*(0.95)^t" in answer_3.replace(" ", ""):
            st.success("Correct! E(t) = 100 * (0.95)^t")
        else:
            feedback_3 = "A 5% decrease per year means the multiplier is 0.95."
            st.error("Incorrect. Remember 5% loss means 95% remains.")

    if answer_3:
        if st.button("🤖 Dr. X Help on Question 3"):
            with st.spinner("Dr. X is reviewing exponential decay..."):
                prompt_3 = f"""
                The student was asked to write the exponential decay function for a solar panel losing 5% efficiency annually.
                Their response: {answer_3}
                Feedback so far: {feedback_3}
                Provide an explanation of why the decay factor is 0.95 and how to set up E(t).
                End with one kind encouragement and link to a growth mindset activity.
                """
                response_3 = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are Dr. X, helping a student understand exponential decay in a supportive tone."},
                        {"role": "user", "content": prompt_3}
                    ]
                )
                st.info(response_3["choices"][0]["message"]["content"])

    with st.expander("🧠 Formula Reminder: Distance = Speed × Time"):
        st.markdown("""
        - **Formula:** `Distance = Speed × Time`
        - To find **Distance**, multiply speed and time.
        - To find **Time**, divide distance by speed.
        - To convert **hours to days**, divide by 24.
        """)

    if st.button("🤖 Get Dr. X Feedback"):
        feedback_prompt = f"""
        Student Quiz Responses Feedback:
        1. Quadratic Trajectory: {answer_1} - {feedback_1}
        2. Solve System: {user_input} - {feedback_2}
        3. Exponential Decay: {answer_3} - {feedback_3}
        """
        with st.spinner("Dr. X is reviewing your answers..."):
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are Dr. X, an encouraging math coach for middle and high school students. Provide clear, helpful feedback on each answer. End with a growth mindset resource."},
                    {"role": "user", "content": feedback_prompt}
                ]
            )
            st.success("Here's what Dr. X says:")
            st.markdown(response["choices"][0]["message"]["content"])

# Resources
elif page == "📚 External Resources":
    st.header("📚 External Resources")
    st.markdown("- [NASA's Fission Surface Power Project](https://www.nasa.gov/space-technology-mission-directorate/tdm/fission-surface-power/)")
    st.markdown("- [NSBE Aerospace](https://www.nsbe-aerospace.org/)")
    st.markdown("- [YouCubed - Growth Mindset](https://www.youcubed.org/resource/growth-mindset/)")
    st.markdown("- [Big Life Journal - Growth Mindset Activities](https://biglifejournal.com/blogs/blog/growth-mindset-activities-children)")

st.markdown("""
---
<div style='text-align: center; font-style: italic; font-size: 1.1rem;'>
"The launch is just the beginning. The math is what takes you to the stars."<br>
<span style='font-style: normal;'>A product of <strong>Cognitive Cloud Education</strong>.</span>
</div>
""", unsafe_allow_html=True)
