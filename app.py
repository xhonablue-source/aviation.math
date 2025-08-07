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

# Quiz Module: Auto LLM Feedback
elif page == "📊 Quiz: The Flight Test":
    st.header("📊 The Flight Test")

    st.subheader("1. Quadratic Trajectory")
    st.write("A rocket's height is given by the equation:")
    st.latex(r"h(t) = -16t^2 + 192t")
    answer_1 = st.radio("What is the maximum height the rocket reaches?",
                        ["A. 192 ft", "B. 576 ft", "C. 16 ft", "D. 384 ft"], index=None)
    if answer_1:
        if answer_1 == "B. 576 ft":
            st.success("Correct! Max height is found at vertex: t = 6, h(6) = 576 ft.")
        else:
            st.error("Incorrect.")
            with st.spinner("Dr. X is explaining why..."):
                feedback = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are Dr. X, a math coach."},
                        {"role": "user", "content": f"The student chose: {answer_1}. The correct answer is B. 576 ft. Explain how to solve this using the vertex formula and encourage them."}
                    ]
                )
                st.info(feedback["choices"][0]["message"]["content"])

    st.subheader("2. Solve the System")
    st.write("Solve: 2x + y = 8 and x - y = 1")
    user_input = st.text_input("Enter value of x:")
    if user_input:
        try:
            if float(user_input) == 3:
                st.success("Correct! x = 3")
            else:
                st.error("Incorrect.")
                with st.spinner("Dr. X is analyzing your response..."):
                    prompt = f"The student guessed x = {user_input}. Solve the system: 2x + y = 8 and x - y = 1. Help them understand using substitution or elimination."
                    response = openai.ChatCompletion.create(
                        model="gpt-4",
                        messages=[
                            {"role": "system", "content": "You are Dr. X, a supportive algebra coach."},
                            {"role": "user", "content": prompt}
                        ]
                    )
                    st.info(response["choices"][0]["message"]["content"])
        except:
            st.warning("Please enter a valid number.")

    st.subheader("3. Exponential Decay")
    st.write("A satellite's solar panel efficiency drops 5% annually. What's the equation for E(t)?")
    answer_3 = st.text_input("Enter equation for E(t):")
    if answer_3:
        if "100 * (0.95)**t" in answer_3.replace(" ", "") or "100*(0.95)^t" in answer_3.replace(" ", ""):
            st.success("Correct! E(t) = 100 * (0.95)^t")
        else:
            st.error("Incorrect.")
            with st.spinner("Dr. X is helping explain the decay rule..."):
                response = openai.ChatCompletion.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "You are Dr. X, explaining exponential decay kindly."},
                        {"role": "user", "content": f"The student entered: {answer_3}. Explain how 0.95 is derived and encourage them."}
                    ]
                )
                st.info(response["choices"][0]["message"]["content"])

    with st.expander("🧠 Formula Reminder: Distance = Speed × Time"):
        st.markdown("""
        - **Formula:** `Distance = Speed × Time`
        - To find **Distance**, multiply speed and time.
        - To find **Time**, divide distance by speed.
        - To convert **hours to days**, divide by 24.
        """)

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
