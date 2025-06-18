import streamlit as st
from streamlit_lottie import  st_lottie
import requests


st.set_page_config(page_title = "Banking App" , layout = "centered")
def load_lottieur(url:str):
    r= requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_url = "http://assets9.lottiefiles.com/packages/lf20_u4yrau.json"
lottie_json = load_lottieur(lottie_url)

st_lottie(lottie_json, speed=1, height=200, key="Banking")


st.title("🏦NOVA BANK ")
st.header('Welcome to NOVA BANK, your trusted partners in secure and seamless dorllar transactions.')
st.subheader('We’re here to help you manage your finances with ease. From tracking your balances to accessing personalized insights, everything you need is just a click away. Explore your Current and Savings dashboards, monitor your transactions, and stay in control — anytime, anywhere. Your money. Your control.')
st.write('Use the icon to your left to navigate through ; ')
st.write('# Withdrawal')
st.write('# &')
st.write('# Deposit')
st.write('Within your current and savings account')

col1, col2 = st.columns(2)
with col1:
    st.page_link("pages/savings_Account.py", label="💰 Savings Account", help="Manage your savings")
with col2:
    st.page_link("pages/current_account.py", label="🏦 Current Account", help="Manage your current account")
