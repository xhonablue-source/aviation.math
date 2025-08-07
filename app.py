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

# Module 2
elif page == "🛰️ Orbital Mechanics":
    st.header("🛰️ Module 2: Orbital Mechanics")
    st.latex(r"3x + 2y = 12")
    st.latex(r"5x - y = 7")

    st.subheader("🧮 Step-by-Step Elimination")

    st.markdown("**Step 1: Multiply the second equation by 2**")
    st.latex(r"2(5x - y) = 14 \\Rightarrow 10x - 2y = 14")

    st.markdown("**Step 2: Add the equations**")
    st.latex(r"(3x + 2y) + (10x - 2y) = 12 + 14")
    st.latex(r"13x = 26 \\Rightarrow x = 2")

    st.markdown("**Step 3: Substitute x into first equation**")
    st.latex(r"3(2) + 2y = 12 \\Rightarrow 6 + 2y = 12 \\Rightarrow y = 3")

    st.success("Final Answer: x = 2, y = 3")

    fig, ax = plt.subplots()
    x = np.linspace(0, 5, 100)
    y1 = (12 - 3*x)/2
    y2 = 5*x - 7
    ax.plot(x, y1, label=r"3x + 2y = 12")
    ax.plot(x, y2, label=r"5x - y = 7")
    ax.plot(2, 3, 'ro', label='Solution (2, 3)')
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# (Other modules remain unchanged)

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

    # LLM Feedback Button
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
