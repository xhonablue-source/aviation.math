import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

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

# Module 3
elif page == "🚀 Rocket Science":
    st.header("🚀 Module 3: Rocket Science")
    st.subheader("Exponential Decay in Fuel Mass")

    st.markdown("""
    A rocket's fuel mass (in tons) after $t$ minutes is modeled by:
    """)
    st.latex(r"M(t) = 1000 \\cdot (0.9)^t")

    t = st.slider("Time elapsed (minutes):", 0, 60, 10)
    mass = 1000 * (0.9)**t
    st.metric("Fuel Remaining (tons)", f"{mass:.2f}")

    t_vals = np.linspace(0, 60, 300)
    m_vals = 1000 * (0.9)**t_vals

    fig, ax = plt.subplots()
    ax.plot(t_vals, m_vals, label="M(t) = 1000 * (0.9)^t")
    ax.axvline(t, color='red', linestyle='--', label=f't = {t} min')
    ax.set_xlabel("Time (min)")
    ax.set_ylabel("Fuel Mass (tons)")
    ax.set_title("Rocket Fuel Consumption Over Time")
    ax.grid(True)
    ax.legend()
    st.pyplot(fig)

# Module 4: Aaron’s Lunar Mission
elif page == "🧑🏾‍🚀 Aaron's Lunar Mission":
    st.header("🧑🏾‍🚀 Aaron's Lunar Mission")
    st.subheader("The Math of Interplanetary Travel")

    st.markdown("""
    We use the **distance-rate-time** formula to calculate how long Aaron's spacecraft will take to reach the Moon:

    \[
    \text{Time} = \frac{\text{Distance}}{\text{Speed}} \quad \text{and} \quad \text{Speed} = \frac{\text{Distance}}{\text{Time}} \quad \text{and} \quad \text{Distance} = \text{Speed} \times \text{Time}
    \]

    To convert from hours to days:

    \[
    \text{Days} = \frac{\text{Hours}}{24}
    \]

    **Where:**
    - **Distance** is the total trip length (in miles)
    - **Speed** is how fast the spacecraft travels (in miles per hour)
    - **Time** is how long it takes to reach the Moon (in hours or days)

    Use the slider below to see how different speeds change the trip duration!
    """)

    st.write("Aaron, a young aerospace pilot, is on a mission to the Moon to help with building a new power system.")

    distance = 238900  # miles
    speed = st.slider("Select spacecraft speed (mph):", 1000, 7000, 3500, 250)
    time_hours = distance / speed
    time_days = time_hours / 24

    st.metric("Travel Time (days)", f"{time_days:.2f} days")

    st.markdown(f"""
    ### 🧠 Calculation:
    - Distance to Moon: **{distance} miles**
    - Speed selected: **{speed} mph**
    - Time to Moon: **{time_hours:.2f} hours** → **{time_days:.2f} days**
    """)

# Quiz Module
elif page == "📊 Quiz: The Flight Test":
    ...

# Resources
elif page == "📚 External Resources":
    ...

st.markdown("""
---
<div style='text-align: center; font-style: italic; font-size: 1.1rem;'>
"The launch is just the beginning. The math is what takes you to the stars."<br>
<span style='font-style: normal;'>A product of <strong>Cognitive Cloud Education</strong>.</span>
</div>
""", unsafe_allow_html=True)
