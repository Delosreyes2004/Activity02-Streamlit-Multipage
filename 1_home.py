import streamlit as st

st.set_page_config(page_title="My Portfolio", page_icon="🌐", layout="wide")

col1, col2 = st.columns([2, 1], gap="medium")

with col1:
    st.title("🌐 Welcome to My Portfolio")
    st.subheader("Hi, I'm April Ann M. Delos Reyes 👋")
    st.write("""
    This is my personal web application built using *Streamlit*.  
    I specialize in Python development, data visualization, and creating  
    interactive tools to simplify complex problems.  

    Explore my work using the sidebar to see my calculators,  
    data analysis projects, and more!
    """)

    name = st.text_input("Let's get to know you! What's your name?")
    if name:
        st.success(f"Nice to meet you, {name}! Enjoy exploring my site. 😊")

with col2:
        st.image("pages/aprilann.jpg", width=250)


st.write("---")
st.write("### 🚀 What I Do")

skills_col1, skills_col2, skills_col3 = st.columns(3)

with skills_col1:
    st.markdown("*Python Development*")
    st.write("Building logic and back-end systems.")

with skills_col2:
    st.markdown("*Data Visualization*")
    st.write("Creating charts with Matplotlib and NumPy.")

with skills_col3:
    st.markdown("*Web Apps*")
    st.write("Deploying interactive apps via Streamlit.")

# Sidebar hint
st.sidebar.success("Select a page above to view my projects.")

    