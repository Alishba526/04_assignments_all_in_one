import streamlit as st

# Page config
st.set_page_config(page_title="My Python Portfolio", layout="wide")

# Main title
st.title("👩‍💻 Welcome to My Python Portfolio Website")

# About Me section
st.header("🧠 About Me")
st.write("""
Hello! I'm a passionate Python learner currently enrolled in **AI-101**.  
I love exploring how we can build amazing tools using **Python** and **Streamlit**.  
This is one of my five websites made entirely using Python — and I’m just getting started! 🚀
""")

# What I Can Do section
st.header("💡 What I Can Do")
st.markdown("""
- ✅ Develop **interactive Python projects**
- ✅ Build **fun & educational games**
- ✅ Create **Streamlit-based web apps**
- ✅ Work with **APIs, data, and automation**
- ✅ Use **Google Colab** 
""")

# Projects Section
st.header("📂 Projects")

# Example project list (you can update it with your real projects)
project_list = {
    "🔢Professional Unit Converter": "https://assignenn2.streamlit.app/",
    "🕹️password generator": "https://python-password-generator1.streamlit.app/",
    "🌍 All-in-One Translator": "https://python1-traslatore-ebvnzzrzfxk8avrqxsculn.streamlit.app/",
    " Data Sweeper":"https://mindgrowth.streamlit.app/",
}

# Loop through projects
for name, desc in project_list.items():
    st.subheader(name)
    st.write(desc)

# Contact section
st.header("📫 Contact Me")
st.write("📧 Email: alishbarehman526@gmail.com")
st.write("🌐 GitHub: [github.com/Alishba526](https://github.com/Alishba526)")
st.write("💼 LinkedIn: https://www.linkedin.com/in/alishba-rehman-29074821a/)")