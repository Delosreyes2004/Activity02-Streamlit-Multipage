import streamlit as st 
st.set_page_config(page_title="Contact Me", page_icon="✉️")
st.title("📩 Let's Get in Touch!")
st.write("Have any questions or just want to say hi? Fill out the form below!")

col1, col2 = st.columns([2, 1])

with col1:
    with st.form("contact_form"):
        name = st.text_input("👤 Your Name", placeholder="April Ann M. Delos Reyes")
        email = st.text_input("📧 Your Email", placeholder="aprilanndelosreyes@gmail.com")
        message = st.text_area("💬 Message", placeholder="How can I help you?")

        submit_button = st.form_submit_button("Send Message")

        if submit_button:
            if name and email and message:
                # You can put the logic to actually send email here (e.g., formsubmit.co)
                st.success(f"Thank you, {name}! I have received your message.")
                st.balloons()
            else:
                st.error("Oops! Please fill out all fields so I won't be sad. 😢")

with col2:
    st.subheader("Connect with me")
    st.write("💻 [GitHub](https://github.com/Delosreyes2004)")
    st.write("📧 aprilanndelosreyes0@gmail.com")








