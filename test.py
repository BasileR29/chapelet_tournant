#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr  9 13:31:37 2022

@author: basile
"""

import pandas as pd

df = pd.DataFrame(columns=['index', 'prenom', 'nom', 'email', 'groupe', 'mystere'])
df.to_csv('priants.csv', index=False)


import streamlit as st

input = st.text_input("text", key="text")
   
    
but = st.button("clear text input")
if but:
    st.session_state["text"] = ""
st.write(input)