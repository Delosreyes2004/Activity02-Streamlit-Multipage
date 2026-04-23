import streamlit as st

st.set_page_config(page_title="Technical Skills", page_icon="🛠️")

st.title("Technical Toolbox")
st.write("A breakdown of my technical proficiency and the tools I use to build solutions.")

programming_skills = {
    "Python": 0.9,
    "SQL": 0.75,
    "JavaScript": 0.6,
    "HTML/CSS": 0.7
}

libraries = ["Pandas", "NumPy", "Scikit-Learn", "Matplotlib", "Streamlit", "Flask"]
tools = ["Git/GitHub", "Docker", "VS Code", "PostgreSQL", "AWS"]

st.subheader("Programming Languages")
for skill, level in programming_skills.items():
    col1, col2 = st.columns([1, 3])
    with col1:
        st.write(skill)
    with col2:
        st.progress(level)

st.divider()

col_a, col_b = st.columns(2)

with col_a:
    st.markdown("### 📚 Frameworks & Libs")
    for lib in libraries:
        st.markdown(f"- {lib}")

with col_b:
    st.markdown("### ⚙️ Tools & Platforms")
    for tool in tools:
        st.markdown(f"- {tool}")

st.divider()

st.subheader("Need a specific stack?")
contact_ask = st.radio(
    "Are you looking for someone with experience in a specific technology not listed here?",
    ("Yes", "No")
)

if contact_ask == "Yes":
    tech_req = st.text_input("Which technology are you interested in?")
    if tech_req:
        st.info(f"I am always learning! I haven't listed {tech_req} here, but I'd love to discuss how my current skills translate to your needs.")

