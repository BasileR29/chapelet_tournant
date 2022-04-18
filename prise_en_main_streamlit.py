# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import streamlit as st

import numpy as np

mes_mysteres = np.array([
    "1er Mystère Joyeux:  L'Annonciation de l'Ange Gabriel à la Vierge Marie.",
    "2e Mystère Joyeux:  Visite de la Vierge Marie à sa cousine Élisabeth.",
    "3e Mystère Joyeux:  La naissance de Jésus dans la grotte de Bethléem.",
    "4e Mystère Joyeux:  Jésus est présenté au temple par Marie et Joseph.",
    "5e Mystère Joyeux:  Jésus retrouvé dans le temple."])

st.title('En dév')

st.text_input("Prénom", key="name")
st.text_input("Nom", key="Last_Name")
st.text_input("email", key="email")

# You can access the value at any point with:
prenom = st.session_state.name
nom = st.session_state.Last_Name
email = st.session_state.email

mon_boutton = st.button('Recevoir mon rosaire')

if mon_boutton and email:
    #Je viens lire mes données
    df = pd.read_csv('priants.csv', index_col='index')
    
    # Je repère mon nouveau user
    i = df.shape[0] + 1
    groupe = i//5
    m = (i-1)%5
    
    # Je l'ajoute
    df.loc[i, 'prenom'] = prenom
    df.loc[i, 'nom'] = nom
    df.loc[i, 'email'] = email
    df.loc[i, 'groupe'] = email
    df.loc[i, 'mystere'] = mes_mysteres[m].split(':')[0]
    
    # Je vide mes champs
    st.session_state['name'] = ""
    st.session_state['Last_Name'] = ""
    st.session_state['email'] = ""
    
    #Je donne le mystère
    st.write('Voici votre mystère du jour :')
    st.write(mes_mysteres[m])
    
    # Je sauvegarde mes résultats
    df.to_csv('priants.csv')