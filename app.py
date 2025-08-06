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

# Custom CSS for an aerospace theme
# This CSS uses a modern, clean design with a space-themed color palette.
# Fonts are selected for readability and style.
# The layout is responsive and includes subtle animations for a polished feel.
st.markdown("""
<style>
    @import url('https://fonts.googleapis.com/css2?family=Merriweather:wght@400;700&family=Inter:wght@400;700&display=swap');

    body {
        font-family: 'Merriweather', serif;
        color: #333333;
    }
    
    .main-header {
        background: linear-gradient(45deg, #0a1f44, #12345e);
        color: #e0e7ff;
        padding: 2.5rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 16px rgba(0,0,0,0.3);
    }
    .main-header h1 {
        font-family: 'Inter', sans-serif;
        font-size: 3rem;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.5);
    }
    .module-card {
        background: #e0e7ff;
        color: #0a1f44;
        padding: 1.5rem;
        border-radius: 12px;
        margin: 1rem 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .module-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 10px 20px rgba(0,0,0,0.25);
    }
    .concept-box {
        background: #f1f5ff;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #4a7ab5;
    }
    .activity-box {
        background: #e9f0ff;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #007bff;
    }
    .standards-box {
        background: #e6f7ff;
        padding: 1rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #00a2d9;
    }
    .resources-box {
        background: #e6fff0;
        padding: 1.5rem;
        border-radius: 8px;
        margin: 1rem 0;
        border-left: 4px solid #28a745;
    }
    .stButton>button {
        background-color: #007bff;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1rem;
        border: none;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }
    .stButton>button:hover {
        background-color: #0056b3;
        transform: translateY(-2px);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div class="main-header">
    <h1>✈️ AEROSPACE 🚀</h1>
    <h3>An Interactive Math & Engineering Curriculum</h3>
    <p>Exploring the mathematics behind flight and space exploration</p>
</div>
""", unsafe_allow_html=True)

# Sidebar navigation
st.sidebar.title("📚 Modules")
page = st.sidebar.selectbox(
    "Choose a section:",
    ["🏠 Home & Overview", "✈️ Flight Trajectories", "🛰️ Orbital Mechanics", 
     "🚀 Rocket Science", "👨‍🚀 Aaron's Lunar Mission", "📊 Quiz: The Flight Test"]
)

# Home Page
if page == "🏠 Home & Overview":
    st.markdown("""
    ## Welcome to the Aerospace Curriculum!

    This program is designed to explore key mathematical concepts through the lens of aerospace engineering. You will discover how algebra, trigonometry, and calculus are essential tools for designing aircraft, launching rockets, and navigating the solar system.

    The curriculum is structured into four main modules, each focusing on a different aspect of aerospace math. This is a journey that connects classroom learning to real-world applications that power human ingenuity.
    """)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="module-card">
            <h3>Module 1: Flight Trajectories</h3>
            <p>The mathematics of flight paths using quadratic equations. Learn how to calculate a plane's altitude and trajectory.</p>
            <small>Common Core Standards: A-REI.4b, F-IF.7a</small>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("""
        <div class="module-card">
            <h3>Module 3: Rocket Science</h3>
            <p>Exploring exponential growth and decay in rocket propulsion. Understand the Tsiolkovsky rocket equation and its impact on space travel.</p>
            <small>Common Core Standards: A-CED.1, F-LE.1</small>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown("""
        <div class="module-card">
            <h3>Module 2: Orbital Mechanics</h3>
            <p>Solving systems of linear equations to understand gravitational forces and satellite orbits. This module covers Kepler's Laws.</p>
            <small>Common Core Standards: A-REI.5, A-REI.6</small>
        </div>
        """, unsafe_allow_html_true=True)
        
        st.markdown("""
        <div class="module-card">
            <h3>Module 4: The Flight Test</h3>
            <p>A comprehensive quiz to test your knowledge across all key concepts. Put your new aerospace math skills to the test!</p>
            <small>Assessment of all key concepts.</small>
        </div>
        """, unsafe_allow_html=True)

# Module 1 content
elif page == "✈️ Flight Trajectories":
    st.title("✈️ Module 1: Flight Trajectories")
    st.header("The Parabolic Path of Flight")
    
    st.markdown("""
    <div class="standards-box">
        <strong>📚 Relevant Common Core Standards:</strong>
        <ul>
            <li>A-REI.4b: Solve quadratic equations.</li>
            <li>F-IF.7a: Graph quadratic functions, showing intercepts, maxima, and minima.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="activity-box">
        <h4>🎯 Activity: "Projectile Motion Simulator"</h4>
        <p>The height $h$ (in meters) of a projectile launched from the ground after $t$ seconds can be modeled by the equation $h(t) = -4.9t^2 + v_0 t$, where $v_0$ is the initial vertical velocity. This equation is a quadratic function, and its graph is a parabola. The motion of an aircraft or rocket is a real-world example of this parabolic motion. </p>
        <p>Use the slider below to change the initial velocity and see how it affects the projectile's flight path. Notice how a higher initial velocity results in a higher and longer flight.</p>
        
        <br>
        
        <h5>Interactive Simulator</h5>
    </div>
    """, unsafe_allow_html=True)
    
    initial_velocity = st.slider('Select Initial Velocity ($v_0$ in m/s)', 10, 100, 50, 5)
    
    # Calculate the time to reach the ground (t_final)
    # The equation is h(t) = -4.9t^2 + v0*t = 0
    # t * (-4.9t + v0) = 0
    # So t = 0 or t = v0/4.9
    time_to_ground = initial_velocity / 4.9
    
    t = np.linspace(0, time_to_ground, 100)
    h = -4.9 * t**2 + initial_velocity * t
    
    df = pd.DataFrame({'Time (s)': t, 'Height (m)': h})
    
    fig, ax = plt.subplots()
    ax.plot(df['Time (s)'], df['Height (m)'])
    ax.set_title('Projectile Trajectory')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Height (m)')
    ax.grid(True)
    
    st.pyplot(fig)
    
    # Calculate key metrics
    max_height = (initial_velocity**2) / (4 * 4.9)
    time_to_max = initial_velocity / (2 * 4.9)
    total_time = initial_velocity / 4.9
    
    st.markdown(f"""
    <div class="concept-box">
        <h4>Analysis of this trajectory:</h4>
        <ul>
            <li><strong>Maximum Height:</strong> {max_height:.2f} meters</li>
            <li><strong>Time to Maximum Height:</strong> {time_to_max:.2f} seconds</li>
            <li><strong>Total Time in the Air:</strong> {total_time:.2f} seconds</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# Module 2 content
elif page == "🛰️ Orbital Mechanics":
    st.title("🛰️ Module 2: Orbital Mechanics")
    st.header("The Math of Gravitational Forces")

    st.markdown("""
    <div class="standards-box">
        <strong>📚 Relevant Common Core Standards:</strong>
        <ul>
            <li>A-REI.5: Prove that a new system with a multiple of another equation has the same solutions.</li>
            <li>A-REI.6: Solve systems of linear equations.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="activity-box">
        <h4>🎯 Activity: "Solving for Force and Mass"</h4>
        <p>In orbital mechanics, forces and masses must be in perfect balance for a stable orbit. This balance can be represented by a system of linear equations. Consider the following system of equations representing forces acting on a satellite:</p>
        <p>$3x + 2y = 12$</p>
        <p>$5x - y = 7$</p>
        <p>where $x$ and $y$ represent unknown variables. Your task is to solve this system for $x$ and $y$ to find the balanced state, which is the precise configuration for a stable orbit.</p>
        
        <br>
        
        <h5>Solve the System:</h5>
        
        <p>Solution method using Elimination:</p>
        <ol>
            <li>Multiply the second equation by 2: $2(5x - y) = 2(7) \implies 10x - 2y = 14$</li>
            <li>Add the modified second equation to the first: $(3x + 2y) + (10x - 2y) = 12 + 14$</li>
            <li>This simplifies to $13x = 26$, so $x = 2$.</li>
            <li>Substitute $x=2$ back into the first original equation: $3(2) + 2y = 12 \implies 6 + 2y = 12 \implies 2y = 6$, so $y = 3$.</li>
        </ol>
        
        <p>The solution is $x=2$ and $y=3$.</p>
    </div>
    """, unsafe_allow_html=True)

# Module 3 content
elif page == "🚀 Rocket Science":
    st.title("🚀 Module 3: Rocket Science")
    st.header("Exponential Functions in Propulsion")
    
    st.markdown("""
    <div class="standards-box">
        <strong>📚 Relevant Common Core Standards:</strong>
        <ul>
            <li>A-CED.1: Create equations and inequalities to solve problems.</li>
            <li>F-LE.1: Distinguish between linear and exponential functions.</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("""
    <div class="activity-box">
        <h4>🎯 Activity: "Simulating Rocket Fuel Consumption"</h4>
        <p>A rocket's fuel consumption can be modeled by an exponential decay function. This is because a rocket expels a fraction of its remaining fuel over a given time interval. The mass of a rocket's fuel (in metric tons) over time is given by the function $M(t) = 1000 \cdot (0.9)^t$, where $t$ is the time in minutes since launch.</p>
        
        <br>
        
        <h5>Interactive Simulation</h5>
        
        <p>Use the slider to see how the fuel mass changes over time. Observe how the rate of change is not constant, which is a key characteristic of exponential functions.</p>
    </div>
    """, unsafe_allow_html=True)
    
    time_sim = st.slider('Time (t in minutes)', 0, 30, 0, 1)
    fuel_mass = 1000 * (0.9)**time_sim
    st.metric(label="Fuel Mass Remaining", value=f"{fuel_mass:.2f} tons")

    t_vals = np.linspace(0, 30, 300)
    m_vals = 1000 * (0.9)**t_vals
    
    fig, ax = plt.subplots()
    ax.plot(t_vals, m_vals)
    ax.axvline(x=time_sim, color='red', linestyle='--', label=f't = {time_sim} min')
    ax.set_title('Rocket Fuel Mass vs. Time')
    ax.set_xlabel('Time (minutes)')
    ax.set_ylabel('Fuel Mass (tons)')
    ax.legend()
    ax.grid(True)
    
    st.pyplot(fig)

# Aaron's Lunar Mission Module
elif page == "👨‍🚀 Aaron's Lunar Mission":
    st.title("👨‍🚀 Aaron's Lunar Mission")
    st.header("The Math of Interplanetary Travel")
    
    st.markdown("""
    <div class="activity-box">
        <h4>🎯 Word Problem: "Aaron's Journey to the Moon"</h4>
        <p>Aaron, an aerospace pilot, is on a mission to the Moon to help with the construction of a new power system. The average distance from the Earth to the Moon is approximately 238,900 miles. If his spacecraft travels at an average speed of 3,500 miles per hour, how many days will it take for him to reach the Moon?</p>
        
        <br>
        
        <p><strong>Hint:</strong> Remember the formula $distance = speed \times time$. You need to solve for time, and then convert the result from hours to days.</p>
        
        <br>
        
        <p><strong>Step-by-Step Solution:</strong></p>
        <ol>
            <li>Find the time in hours: $time = \frac{distance}{speed} = \frac{238,900}{3,500} \approx 68.26$ hours</li>
            <li>Convert hours to days: $days = \frac{hours}{24} = \frac{68.26}{24} \approx 2.84$ days</li>
        </ol>
        
        <p>Answer: It will take approximately **2.84 days** for Aaron to reach the Moon.</p>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="resources-box">
        <h4>External Resources:</h4>
        <p>For more information on the real-world engineering problem Aaron is solving, check out this link about the proposed lunar power station:</p>
        <a href="https://www.nasa.gov/space-technology-mission-directorate/tdm/fission-surface-power/" target="_blank">NASA's Fission Surface Power Project</a>
        <br>
        <p>You can also learn about opportunities and resources from the **National Society of Black Engineers (NSBE)** Aerospace Special Interest Group:</p>
        <a href="https://www.nsbe-aerospace.org/" target="_blank">NSBE Aerospace</a>
    </div>
    """, unsafe_allow_html=True)

# Quiz Page
elif page == "📊 Quiz: The Flight Test":
    st.title("📊 The Flight Test")
    st.header("Test Your Knowledge")
    
    st.markdown("Answer the following questions to test your understanding of aerospace math concepts.")
    
    st.markdown("---")
    
    # Question 1
    st.subheader("Question 1: Quadratic Trajectory")
    st.write("A rocket's height is given by the function $h(t) = -16t^2 + 192t$. What is the maximum height the rocket reaches?")
    q1_options = ["A) 192 feet", "B) 576 feet", "C) 16 feet", "D) 12 seconds"]
    q1_answer = st.radio("Choose your answer:", options=q1_options, index=None)
    
    if q1_answer is not None:
        if q1_answer == "B) 576 feet":
            st.success("Correct! The maximum height is found at the vertex of the parabola.")
        else:
            st.error("Incorrect. The maximum height is at the vertex, which occurs at $t = -b/(2a)$. In this case, $t = -192/(2 * -16) = 6$ seconds. Plugging this back in, $h(6) = -16(6^2) + 192(6) = 576$ feet.")
    
    st.markdown("---")
    
    # Question 2
    st.subheader("Question 2: Systems of Equations")
    st.write("A force analysis results in the following system: $2x + y = 8$ and $x - y = 1$. What is the value of x?")
    q2_answer = st.text_input("Enter your answer for x:", key="q2_input")
    
    if q2_answer:
        try:
            if float(q2_answer) == 3:
                st.success("Correct! Adding the two equations eliminates y, giving you $3x = 9$, which simplifies to $x=3$.")
            else:
                st.error("Incorrect. Try solving the system of equations using elimination or substitution. Adding the two equations gives $3x = 9$.")
        except ValueError:
            st.error("Please enter a valid number.")
            
    st.markdown("---")

    # Question 3
    st.subheader("Question 3: Exponential Decay")
    st.write("A satellite's solar panel efficiency decreases by 5% each year. If its initial efficiency is 100%, what is the equation for its efficiency $E(t)$ after $t$ years?")
    q3_answer = st.text_input("Enter your equation (e.g., E(t) = 100 * (0.5)^t):", key="q3_input")
    
    if q3_answer:
        if "100 * (0.95)**t" in q3_answer or "100 * (0.95)^t" in q3_answer or "100 * (0.95)t" in q3_answer:
            st.success("Correct! An exponential decay function is used, and a 5% decrease means you are left with 95% of the original amount, or 0.95.")
        else:
            st.error("Incorrect. Remember that a 5% decrease is modeled by multiplying by 0.95 each year. The correct equation is $E(t) = 100 \cdot (0.95)^t$.")
    
st.markdown("---")
st.markdown("""
<div style="text-align: center; padding: 20px; color: #666; font-style: italic;">
    <p><em>"The launch is just the beginning. The math is what takes you to the stars."</em></p>
    <p>A product of Cognitive Cloud Education.</p>
</div>
""", unsafe_allow_html=True)
