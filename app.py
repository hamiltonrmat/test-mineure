import streamlit as st

st.header("mon application")

nombres = [1, 2, 4, 7]
carre = [1**2, 2**2, 4**2, 7**2]

d = {"nombres": nombres, "carre": carre}
data = pd.DataFrame(d)

st.dataframe(data)
