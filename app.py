#streamlit
import streamlit as st

st.set_page_config(page_title="Groth Mindset Project",project_icon="✮")
st.title("Groth Mindset Challenge:Web App with Streamlit ")
st.header("🚀Welcome to your Growth Journey!")
st.write("Embracing challenges is the key to growth and success. Every obstacle presents an opportunity to learn, and every mistake is a lesson rather than a failure. Instead of fearing setbacks, view them as stepping stones to improvement. Adapt, refine your approach, and keep pushing forward. True strength comes from learning through struggles, and real growth begins when you step out of your comfort zone.")
#qute section
st.header("💡 Todays's Growth MindsetQuote")
st.write('"Success is not final, failuer is not fatal: it is the courage to continue that counts.--Winston Churchill"')

st.header("🔧 What's your Challenge Today?")
user_input=st.text_input("Describe a Challenge you'r facing: ")

#condition
if user_input:
    st.success(f"you are facing: {user_input}. Keep Pushing forward toword your target gole!...🚀")
else:st.warning("Tellus about your Challange get started!")

#refexing
st.header("Reflect on You Learning.")
reflection = st.text_area("Write your reflections here: ")

if reflection:
    st.success(f"✨Great Insight! Your reflection: {reflection}")
else:
    st.info("Reflection on past exprience help you Grow! Share Your Difficulties")

#acheivements
st.header("🏆Celebrate Your Wins!🥇")
acheivement= st.text_input("Share something you've recently Accomplished: ")

if acheivement:
    st.success(f"💐Amazing! Your achived: {acheivement}✨")

else:
    st.info("Big or Small, Every Acheivment Counts! Share One Now face😍")

    #footer
    st.write("- - -")
    st.write("👍Keep belive in yourself. Growth is a journey, not a destination! ₊•.°.⋆✮⋆.°.•₊")
    st.write("© Created by ꧁Rabia 𝓺𝓾𝓮𝓮𝓷꧂")