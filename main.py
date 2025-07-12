import streamlit as st
import pickle

st.subheader('📱Mobile Phone Pricing')
bp=st.number_input('Enter Battery Power')
blu=st.selectbox('  Has Bluetooth Or Not',[1,0])
csp=st.number_input(' Enter Processor Speed')
fc=st.number_input('Enter Front Camera Megapixels')
fg=st.selectbox('Has 4G Or Not',[0,1])
tg=st.selectbox("Has 3G Or Not",[0,1])
inm=st.number_input('Enter Internal Memory in GB')
mw=st.number_input("Enter Weight in Gm")
pc=st.number_input("Enter Primary Camera Megapixels")
ph=st.number_input("Enter Pixel Resolution height ")
pw=st.number_input("Enter Pixel Resolution width ")
ram=st.number_input("Enter Ram in MB")
ttm=st.number_input(" Enter Time a single battery charge will last. In Hours ")
ncore=st.number_input("Enter Processor Core Count")
wifi=st.selectbox("Has WiFi or Not",[0,1])
tchsc=st.selectbox("Has Touch Screen or Not",[0,1])
button=st.button('Predict')
if button:
    model=pickle.load(open('mobile_price_predictor.pkl','rb'))
    res=model.predict([[bp,blu,csp,fc,fg,tg,inm,mw,pc,ph,pw,ram,ttm,wifi,ncore,tchsc]])[0].round(2)
    price_map = {
    0: "Low",
    1: " Medium",
    2: " High",
    3: " Very High"
    }
    st.markdown(f"### The Price is: {price_map.get(res,'unknown')}")



  