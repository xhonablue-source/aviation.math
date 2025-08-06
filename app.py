import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# --- Page Setup ---
st.set_page_config(page_title="Fluid Dynamics: The Bernoulli Principle", page_icon="💧", layout="wide")

# --- Developer Credit ---
st.markdown("### www.cognitivecloud.ai")
st.markdown("**Developed by Xavier Honablue M.Ed**")

st.markdown("---")

# --- Title and Intro ---
st.title("💧 The Bernoulli Principle Explorer")
st.markdown("""
Welcome! This lesson helps you **see, understand, and apply** the Bernoulli principle and its mathematical underpinnings in both academic and aviation engineering contexts.

---

### 📘 The Principle:
The **Bernoulli principle** is a fundamental concept in fluid dynamics which states that as the speed of a fluid increases, the pressure within the fluid decreases.

Think of a river: in a narrow section, the water flows faster and the pressure is lower. In a wide section, the water flows slower and the pressure is higher. This simple relationship explains everything from why airplanes fly to how a carburetor works.

---

### 🎯 Objective:
By the end of this lesson, you'll be able to:
- Define and explain the Bernoulli principle
- Identify real-life examples of the principle in action
- Understand the inverse relationship between fluid speed and pressure
- Apply these concepts to aviation engineering scenarios
- Relate these concepts to both Common Core and Aviation Engineering math standards
""")

# Enhanced Standards Alignment Section
st.header("📚 Standards Alignment")

# Create two columns for different standard types
col1, col2 = st.columns(2)

with col1:
    st.subheader("🎓 Common Core Math Standards")
    common_core_standard = st.selectbox("Select a Common Core Math Standard:", [
        "HSA-CED.A.1 - Create equations and inequalities in one variable",
        "HSF-IF.B.4 - Interpret key features of graphs and tables in terms of quantities",
        "HSF-IF.C.7 - Graph functions expressed symbolically and show key features",
        "HSF-BF.A.1 - Write a function that describes a relationship between two quantities",
        "HSA-REI.B.3 - Solve linear equations and inequalities in one variable",
        "HSF-LE.A.2 - Construct linear and exponential functions"
    ])
    
    # Display Common Core alignment info
    if "HSA-CED.A.1" in common_core_standard:
        st.info("🎯 **Focus:** Creating equations from real-world fluid dynamics scenarios")
    elif "HSF-IF.B.4" in common_core_standard:
        st.info("🎯 **Focus:** Interpreting pressure vs. speed relationships in graphs")
    elif "HSF-IF.C.7" in common_core_standard:
        st.info("🎯 **Focus:** Graphing Bernoulli relationships and analyzing key features")
    elif "HSF-BF.A.1" in common_core_standard:
        st.info("🎯 **Focus:** Building functions that model fluid behavior")
    elif "HSA-REI.B.3" in common_core_standard:
        st.info("🎯 **Focus:** Solving Bernoulli equations for unknown variables")
    else:
        st.info("🎯 **Focus:** Constructing mathematical models for fluid systems")

with col2:
    st.subheader("✈️ Aviation Engineering Standards")
    aviation_standard = st.selectbox("Select an Aviation Engineering Math Standard:", [
        "AE-FLUID.1 - Apply continuity equation in aircraft design contexts",
        "AE-AERO.2 - Calculate lift forces using Bernoulli's principle",
        "AE-PROP.3 - Analyze propeller efficiency using fluid dynamics",
        "AE-VENT.4 - Design ventilation systems using pressure differentials",
        "AE-INST.5 - Calibrate airspeed indicators using dynamic pressure",
        "AE-PERF.6 - Optimize aircraft performance using aerodynamic principles",
        "AE-STAB.7 - Analyze stability and control using airflow patterns",
        "AE-TURB.8 - Calculate turbine efficiency in jet engines"
    ])
    
    # Display Aviation Engineering alignment info
    if "AE-FLUID.1" in aviation_standard:
        st.info("✈️ **Application:** Mass flow rate conservation in wing design")
    elif "AE-AERO.2" in aviation_standard:
        st.info("✈️ **Application:** Wing lift generation and airfoil optimization")
    elif "AE-PROP.3" in aviation_standard:
        st.info("✈️ **Application:** Propeller blade design and thrust calculations")
    elif "AE-VENT.4" in aviation_standard:
        st.info("✈️ **Application:** Aircraft cabin pressurization systems")
    elif "AE-INST.5" in aviation_standard:
        st.info("✈️ **Application:** Flight instrument calibration and accuracy")
    elif "AE-PERF.6" in aviation_standard:
        st.info("✈️ **Application:** Fuel efficiency and flight planning optimization")
    elif "AE-STAB.7" in aviation_standard:
        st.info("✈️ **Application:** Flight control system design and analysis")
    else:
        st.info("✈️ **Application:** Jet engine design and performance optimization")

# --- User Info ---
st.header("👤 Personalization")
name = st.text_input("Enter your name:")
avatar = st.selectbox("Choose your avatar:", [
    "💧 Droplet", "💨 Vortex", "🌊 Wave", "🌪️ Cyclone", "✈️ Pilot", "🚁 Aviator"
])

if name:
    st.success(f"Welcome, {name} the {avatar}! Let's begin exploring fluid dynamics and aviation applications.")

# --- Enhanced Interactive Explorer Section ---
st.header("🔍 Interactive Bernoulli Visualization")

# Create tabs for different visualization modes
viz_tab1, viz_tab2, viz_tab3 = st.tabs(["Basic Relationship", "Aviation Applications", "Engineering Calculations"])

with viz_tab1:
    st.markdown("Use the slider to change the fluid's speed and see the corresponding change in pressure.")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        # Slider for fluid speed
        speed = st.slider("Fluid Speed (v in m/s)", 0, 50, 25, key="basic_speed")
        
        # Generate x and y values for the plot
        x_vals = np.linspace(0, 50, 100)
        y_vals = 1000 - 0.5 * 1.225 * x_vals**2  # Using air density at sea level
        
        # Find the corresponding pressure for the selected speed
        pressure = 1000 - 0.5 * 1.225 * speed**2
        
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.plot(x_vals, y_vals, linewidth=3, color='#1f77b4', label='Pressure vs Speed')
        ax.plot(speed, pressure, 'ro', markersize=10, label=f'Current Point (v={speed}, P={pressure:.1f})')
        ax.set_title("Bernoulli's Principle: Speed vs Pressure Relationship", fontsize=14, fontweight='bold')
        ax.set_xlabel("Fluid Speed (v) [m/s]", fontsize=12)
        ax.set_ylabel("Static Pressure (P) [Pa]", fontsize=12)
        ax.grid(True, alpha=0.3)
        ax.legend()
        st.pyplot(fig)
    
    with col2:
        st.info(f"**Current Analysis:**")
        st.write(f"**Speed (v):** {speed} m/s")
        st.write(f"**Static Pressure:** {pressure:.1f} Pa")
        st.write(f"**Dynamic Pressure:** {0.5 * 1.225 * speed**2:.1f} Pa")
        st.write(f"**Total Pressure:** {1000:.1f} Pa")
        st.markdown("**Bernoulli Equation:**")
        st.latex(r"P + \frac{1}{2}\rho v^2 = \text{constant}")

with viz_tab2:
    st.markdown("Explore how Bernoulli's principle applies to aviation scenarios.")
    
    scenario = st.selectbox("Choose Aviation Scenario:", [
        "Wing Airfoil Analysis",
        "Pitot Tube Measurement",
        "Venturi Effect in Carburetor",
        "Propeller Blade Design"
    ])
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        if scenario == "Wing Airfoil Analysis":
            upper_speed = st.slider("Upper Surface Speed (m/s)", 50, 150, 100, key="upper_speed")
            lower_speed = st.slider("Lower Surface Speed (m/s)", 30, 120, 80, key="lower_speed")
            
            # Calculate pressures
            upper_pressure = 101325 - 0.5 * 1.225 * upper_speed**2
            lower_pressure = 101325 - 0.5 * 1.225 * lower_speed**2
            lift_pressure_diff = lower_pressure - upper_pressure
            
            fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))
            
            # Speed comparison
            surfaces = ['Upper Surface', 'Lower Surface']
            speeds = [upper_speed, lower_speed]
            colors = ['lightblue', 'lightcoral']
            
            ax1.bar(surfaces, speeds, color=colors)
            ax1.set_title("Airfoil Surface Speeds", fontweight='bold')
            ax1.set_ylabel("Speed (m/s)")
            
            # Pressure comparison
            pressures = [upper_pressure, lower_pressure]
            ax2.bar(surfaces, pressures, color=colors)
            ax2.set_title("Airfoil Surface Pressures", fontweight='bold')
            ax2.set_ylabel("Pressure (Pa)")
            
            plt.tight_layout()
            st.pyplot(fig)
            
        elif scenario == "Pitot Tube Measurement":
            airspeed = st.slider("Aircraft Airspeed (m/s)", 50, 200, 100, key="pitot_speed")
            altitude = st.slider("Altitude (m)", 0, 10000, 3000, key="altitude")
            
            # Calculate air density at altitude (simplified)
            rho = 1.225 * np.exp(-altitude / 8400)
            
            static_pressure = 101325 * (1 - 0.0065 * altitude / 288.15)**5.256
            dynamic_pressure = 0.5 * rho * airspeed**2
            total_pressure = static_pressure + dynamic_pressure
            
            fig, ax = plt.subplots(figsize=(10, 6))
            
            pressures = [static_pressure/1000, dynamic_pressure/1000, total_pressure/1000]
            labels = ['Static Pressure', 'Dynamic Pressure', 'Total Pressure']
            colors = ['lightblue', 'orange', 'lightgreen']
            
            bars = ax.bar(labels, pressures, color=colors)
            ax.set_title(f"Pitot Tube Measurements at {altitude}m altitude", fontweight='bold')
            ax.set_ylabel("Pressure (kPa)")
            
            # Add value labels on bars
            for bar, pressure in zip(bars, pressures):
                height = bar.get_height()
                ax.text(bar.get_x() + bar.get_width()/2., height + 0.5,
                       f'{pressure:.1f}', ha='center', va='bottom')
            
            st.pyplot(fig)
    
    with col2:
        if scenario == "Wing Airfoil Analysis":
            st.info("**Airfoil Analysis Results:**")
            st.write(f"**Upper Surface Speed:** {upper_speed} m/s")
            st.write(f"**Lower Surface Speed:** {lower_speed} m/s")
            st.write(f"**Upper Surface Pressure:** {upper_pressure:.0f} Pa")
            st.write(f"**Lower Surface Pressure:** {lower_pressure:.0f} Pa")
            st.write(f"**Pressure Difference:** {lift_pressure_diff:.0f} Pa")
            st.success(f"**Lift Generated:** {'Positive' if lift_pressure_diff > 0 else 'Negative'}")
            
        elif scenario == "Pitot Tube Measurement":
            st.info("**Flight Instrument Readings:**")
            st.write(f"**Airspeed:** {airspeed} m/s ({airspeed * 1.944:.0f} knots)")
            st.write(f"**Altitude:** {altitude} m ({altitude * 3.281:.0f} ft)")
            st.write(f"**Air Density:** {rho:.3f} kg/m³")
            st.write(f"**Static Pressure:** {static_pressure/1000:.1f} kPa")
            st.write(f"**Dynamic Pressure:** {dynamic_pressure/1000:.1f} kPa")
            st.write(f"**Total Pressure:** {total_pressure/1000:.1f} kPa")

with viz_tab3:
    st.markdown("Perform engineering calculations using Bernoulli's principle.")
    
    calc_type = st.selectbox("Choose Calculation Type:", [
        "Required Airspeed for Lift",
        "Pressure Drop in Duct",
        "Venturi Flow Rate",
        "Propeller Thrust Calculation"
    ])
    
    if calc_type == "Required Airspeed for Lift":
        st.subheader("Calculate Required Airspeed for Aircraft Lift")
        
        col1, col2 = st.columns(2)
        
        with col1:
            aircraft_weight = st.number_input("Aircraft Weight (N)", value=50000, step=1000)
            wing_area = st.number_input("Wing Area (m²)", value=25.0, step=0.5)
            air_density = st.number_input("Air Density (kg/m³)", value=1.225, step=0.001)
            cl_max = st.number_input("Maximum Lift Coefficient", value=1.5, step=0.1)
        
        with col2:
            # Calculate stall speed
            v_stall = np.sqrt(2 * aircraft_weight / (air_density * wing_area * cl_max))
            v_cruise = v_stall * 1.3  # Typical cruise speed safety factor
            
            st.info("**Calculation Results:**")
            st.write(f"**Stall Speed:** {v_stall:.1f} m/s ({v_stall * 1.944:.0f} knots)")
            st.write(f"**Recommended Cruise Speed:** {v_cruise:.1f} m/s ({v_cruise * 1.944:.0f} knots)")
            
            st.latex(r"V_{stall} = \sqrt{\frac{2W}{\rho S C_{L,max}}}")
            
            # Show calculation breakdown
            st.markdown("**Calculation Breakdown:**")
            st.write(f"Weight/Wing Area: {aircraft_weight/wing_area:.1f} N/m²")
            st.write(f"Wing Loading: {aircraft_weight/(wing_area * 9.81):.1f} kg/m²")

# --- Enhanced Quiz Section ---
st.header("🎲 Knowledge Assessment")

# Create tabs for different quiz types
quiz_tab1, quiz_tab2 = st.tabs(["Basic Concepts", "Aviation Applications"])

with quiz_tab1:
    st.subheader("Fundamental Understanding")
    
    basic_questions = [
        {
            "question": "According to Bernoulli's principle, what happens to pressure as fluid speed increases?",
            "options": ["It increases", "It decreases", "It stays the same", "It depends on the fluid"],
            "correct": 1,
            "explanation": "The Bernoulli principle states an inverse relationship: as speed goes up, pressure goes down."
        },
        {
            "question": "The mathematical relationship P + ½ρv² = constant represents:",
            "options": ["Newton's law", "Bernoulli's equation", "Conservation of mass", "Ideal gas law"],
            "correct": 1,
            "explanation": "This is the simplified form of Bernoulli's equation for incompressible flow."
        }
    ]
    
    for i, q in enumerate(basic_questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        answer = st.radio(f"Select your answer for Q{i+1}:", q['options'], key=f"basic_q{i}")
        
        if st.button(f"Check Answer {i+1}", key=f"basic_check{i}"):
            if q['options'].index(answer) == q['correct']:
                st.success(f"✅ Correct! {q['explanation']}")
            else:
                st.error(f"❌ Try again! {q['explanation']}")

with quiz_tab2:
    st.subheader("Aviation Engineering Applications")
    
    aviation_questions = [
        {
            "question": "How does an airfoil generate lift according to Bernoulli's principle?",
            "options": [
                "Air moves faster over the top surface, creating lower pressure",
                "Air moves slower over the top surface, creating higher pressure", 
                "Both surfaces have equal pressure",
                "Lift is not related to Bernoulli's principle"
            ],
            "correct": 0,
            "explanation": "The curved upper surface of an airfoil causes air to travel faster, reducing pressure and creating lift."
        },
        {
            "question": "A pitot tube measures airspeed by comparing:",
            "options": [
                "Temperature differences", 
                "Static and dynamic pressure",
                "Air density variations",
                "Wind direction changes"
            ],
            "correct": 1,
            "explanation": "A pitot tube measures the difference between total pressure and static pressure to determine dynamic pressure and thus airspeed."
        },
        {
            "question": "In jet engine design, Bernoulli's principle helps explain:",
            "options": [
                "Fuel combustion efficiency",
                "Thrust generation through pressure differentials",
                "Engine cooling systems",
                "Landing gear operation"
            ],
            "correct": 1,
            "explanation": "Jet engines accelerate air, creating pressure differentials that generate thrust according to Bernoulli's principle."
        }
    ]
    
    for i, q in enumerate(aviation_questions):
        st.write(f"**Question {i+1}:** {q['question']}")
        answer = st.radio(f"Select your answer for AV-Q{i+1}:", q['options'], key=f"av_q{i}")
        
        if st.button(f"Check Answer AV-{i+1}", key=f"av_check{i}"):
            if q['options'].index(answer) == q['correct']:
                st.success(f"✅ Correct! {q['explanation']}")
            else:
                st.error(f"❌ Try again! {q['explanation']}")

# --- Enhanced Reflection Section ---
st.header("🧾 Reflection & Application")

reflection_type = st.radio("Choose your reflection focus:", [
    "Real-world observations",
    "Aviation career connections",
    "Mathematical modeling insights"
])

if reflection_type == "Real-world observations":
    reflection = st.text_area("Describe a real-world situation where you've observed the Bernoulli principle. How would you explain it mathematically?")
elif reflection_type == "Aviation career connections":
    reflection = st.text_area("If you were an aerospace engineer, how would you use Bernoulli's principle in aircraft design? What calculations would be most important?")
else:
    reflection = st.text_area("How has creating mathematical models helped you understand the Bernoulli principle better? What insights did the equations provide?")

if st.button("Submit Reflection"):
    if reflection.strip():
        st.success("✅ Excellent reflection! You're thinking like both a scientist and an engineer.")
        st.balloons()
    else:
        st.warning("Please share your thoughts to complete the reflection.")

# --- Enhanced Learning Resources ---
st.header("📚 Comprehensive Learning Resources")

# Create tabs for organized resources
resource_tab1, resource_tab2, resource_tab3, resource_tab4 = st.tabs([
    "📊 Interactive Tools", 
    "✈️ Aviation Resources", 
    "📖 Academic Materials",
    "🎯 Practice Problems"
])

with resource_tab1:
    st.markdown("### Digital Tools for Exploration")
    tools = [
        {
            "name": "Desmos Graphing Calculator",
            "url": "https://www.desmos.com/calculator",
            "description": "Graph Bernoulli equations and explore parameter relationships",
            "icon": "📊"
        },
        {
            "name": "PhET Fluid Pressure Simulation", 
            "url": "https://phet.colorado.edu/en/simulation/fluid-pressure-and-flow",
            "description": "Interactive fluid dynamics simulations",
            "icon": "🔬"
        },
        {
            "name": "NASA Glenn Beginner's Guide to Aerodynamics",
            "url": "https://www.grc.nasa.gov/www/k-12/airplane/bga.html",
            "description": "Interactive aerodynamics tutorials and simulations",
            "icon": "🚀"
        }
    ]
    
    for tool in tools:
        st.markdown(f"{tool['icon']} **[{tool['name']}]({tool['url']})**")
        st.write(tool['description'])
        st.write("---")

with resource_tab2:
    st.markdown("### Aviation Engineering Resources")
    aviation_resources = [
        {
            "name": "FAA Pilot's Handbook of Aeronautical Knowledge",
            "url": "https://www.faa.gov/regulations_policies/handbooks_manuals/aviation/phak/",
            "description": "Official FAA resource covering aerodynamic principles",
            "icon": "✈️"
        },
        {
            "name": "MIT OpenCourseWare - Aerodynamics",
            "url": "https://ocw.mit.edu/courses/aeronautics-and-astronautics/",
            "description": "University-level aerodynamics courses and materials",
            "icon": "🎓"
        },
        {
            "name": "Aircraft Design Calculator",
            "url": "https://www.aircraftdesign.com/",
            "description": "Online tools for aircraft performance calculations",
            "icon": "📐"
        }
    ]
    
    for resource in aviation_resources:
        st.markdown(f"{resource['icon']} **[{resource['name']}]({resource['url']})**")
        st.write(resource['description'])
        st.write("---")

with resource_tab3:
    st.markdown("### Academic Study Materials")
    
    # Organize by selected standards
    st.subheader(f"📋 Resources for: {common_core_standard[:10]}...")
    
    if "HSA-CED" in common_core_standard:
        st.write("• Khan Academy: Creating equations from word problems")
        st.write("• IXL: Algebra 1 > B.4 - Write linear functions from word problems")
    elif "HSF-IF" in common_core_standard:
        st.write("• Khan Academy: Interpreting functions and their graphs")
        st.write("• IXL: Algebra 1 > A.3 - Domain and range of functions")
    
    st.subheader(f"✈️ Resources for: {aviation_standard[:10]}...")
    
    if "AE-FLUID" in aviation_standard:
        st.write("• Study continuity equation applications in wing design")
        st.write("• Practice mass flow rate calculations")
    elif "AE-AERO" in aviation_standard:
        st.write("• Airfoil analysis and lift coefficient calculations")
        st.write("• Wing design optimization problems")

with resource_tab4:
    st.markdown("### Practice Problem Sets")
    
    problem_difficulty = st.selectbox("Choose difficulty level:", [
        "Beginner - Basic calculations",
        "Intermediate - Real-world applications", 
        "Advanced - Engineering problems"
    ])
    
    if problem_difficulty.startswith("Beginner"):
        st.markdown("""
        **Practice Problems:**
        1. Calculate pressure when air speed is 30 m/s
        2. Find the speed needed to reduce pressure by 500 Pa
        3. Compare pressures at two different speeds
        """)
    elif problem_difficulty.startswith("Intermediate"):
        st.markdown("""
        **Application Problems:**
        1. Calculate lift on an aircraft wing given airfoil data
        2. Determine pitot tube readings at different altitudes  
        3. Analyze carburetor venturi flow rates
        """)
    else:
        st.markdown("""
        **Engineering Challenges:**
        1. Design an airfoil for maximum lift-to-drag ratio
        2. Optimize propeller blade angles for efficiency
        3. Calculate jet engine thrust parameters
        """)

# --- Enhanced Study Plan Generator ---
st.header("📅 Personalized Learning Path")

col1, col2 = st.columns(2)

with col1:
    current_level = st.selectbox("Mathematical Comfort Level:", [
        "Beginner - Learning basic algebra",
        "Intermediate - Comfortable with functions and graphs", 
        "Advanced - Ready for complex modeling"
    ])

with col2:
    career_interest = st.selectbox("Career Interest Level:", [
        "Academic - Focus on math standards",
        "Aviation Curious - Want to learn more",
        "Future Pilot - Serious about aviation",
        "Engineering Track - Aerospace engineering focus"
    ])

if st.button("Generate My Personalized Learning Path"):
    st.success("🎯 Your Customized Learning Plan:")
    
    # Plan based on both math level and career interest
    if "Beginner" in current_level:
        if "Academic" in career_interest:
            st.markdown("""
            **Foundation Phase (Weeks 1-3):**
            • Master basic equation solving with IXL practice
            • Use the Basic Relationship visualization above daily
            • Focus on understanding inverse relationships
            """)
        else:
            st.markdown("""
            **Aviation Foundation (Weeks 1-3):**
            • Start with basic flight principles
            • Use aviation visualizations to see real applications
            • Practice simple airspeed and pressure calculations
            """)
    elif "Intermediate" in current_level:
        if "Future Pilot" in career_interest or "Engineering Track" in career_interest:
            st.markdown("""
            **Application Phase (Weeks 1-4):**
            • Work through aviation calculation examples
            • Practice pitot tube and airfoil problems
            • Study FAA materials on aerodynamics
            • Complete engineering calculation challenges
            """)
        else:
            st.markdown("""
            **Mathematical Modeling (Weeks 1-4):**
            • Create your own Bernoulli equation models
            • Graph complex relationships using Desmos
            • Analyze real-world data applications
            """)
    else:  # Advanced
        st.markdown("""
        **Mastery Project (Ongoing):**
        • Design a complete aircraft performance analysis
        • Research cutting-edge aerospace applications
        • Create your own educational materials
        • Mentor others learning these concepts
        """)

# --- Final Summary ---
st.header("🎓 Learning Outcomes Achieved")
st.markdown(f"""
**Congratulations, {name if name else 'Explorer'}!** 🎉

### You've Successfully Explored:
- ✅ **Bernoulli's Principle** - Core concept and mathematical relationships
- ✅ **Real-World Applications** - From basic examples to aviation engineering
- ✅ **Interactive Modeling** - Hands-on experience with calculations
- ✅ **Standards Alignment** - Connected learning to {common_core_standard.split(' - ')[0]} and {aviation_standard.split(' - ')[0]}
- ✅ **Career Connections** - Aviation and engineering applications
- ✅ **Mathematical Thinking** - Problem-solving with equations and graphs

### Your Next Steps:
Continue exploring the resources provided and remember that fluid dynamics principles are everywhere around us - from the flight of aircraft to the flow of air in HVAC systems!

**Keep questioning, keep calculating, and keep soaring!** ✈️
""")

st.markdown("---")
st.markdown("*Developed with ❤️ for STEM education and aviation inspiration*")
