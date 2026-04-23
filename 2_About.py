import streamlit as st

# Page Configuration
st.set_page_config(page_title="About Me", page_icon="👩‍💻")

st.title("👩‍💻 About Me")


col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    ### I am *April Ann M.Delos Reyes*.
    I am an comsie student passionate about web development and technology.
    I enjoy creating systems that solve real-world problems and exploring data visualization.
    """)
    

with col2:
        st.image("pages/aprilann.jpg", width=250, caption="Comsie Student & Developer")


st.write("### 🛠️ My Technical Skills")
skills = {
    "Python": 85,
    "Streamlit": 80,
    "HTML/CSS": 75,
    "Networking": 70,
    "Data Analysis": 65
}
for skill, level in skills.items():
    st.write(f"*{skill}*")
    st.progress(level)

st.divider()


st.write("### ✨ Fun Fact")
if st.button("Click for a Surprise! 🎉"):
    st.balloons()
    st.success("I love building creative apps and solving complex coding logic.")
st.write("### 📬 Get in Touch")
st.info("Let's collaborate! You can reach me through my academic or professional channels.")



