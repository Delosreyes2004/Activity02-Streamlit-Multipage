import streamlit as st


st.set_page_config(page_title="CodeCraft Portfolio", page_icon="💻")
                   
st.title("💻 CodeCraft: My Digital Creations")

st.write("Welcome! Explore my projects below 👇")


project = st.selectbox("Choose a project:", [
    "IoT Smart Irrigation System",
    "Student Attendance System",
    "Portfolio Website"
])


st.subheader("📌 Project Details")

if project == "IoT Smart Irrigation System":
    st.write("A smart system that automates watering plants using sensors and IoT technology.")
    st.success("Features: Soil moisture detection, automatic watering, real-time monitoring")

elif project == "Student Attendance System":
    st.write("A web-based system for tracking student attendance efficiently.")
    st.info("Features: Digital check-in, database storage, easy monitoring")

else:
    st.write("A personal website that showcases my skills, projects, and achievements.")
    st.warning("Features: About me, project gallery, contact page")


st.subheader("⭐ Rate this Project")

rating = st.slider("Your rating:", 1, 5)

st.write(f"You rated this project: {rating}/5 ⭐")


st.markdown("---")
st.caption("Created using Streamlit 💙")
