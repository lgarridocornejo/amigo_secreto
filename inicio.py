import streamlit as st
import pandas as pd
import datetime
import os
import random
from streamlit_extras.let_it_rain import rain

def run_snow_animation():
    rain(emoji=iconos[random_number], font_size=20, falling_speed=5, animation_length="infinite")

st.set_page_config(page_title="Feliz Navidad", page_icon="🎄")

# Diccionario solo de códigos válidos
codigos_validos = {
'alerce': 'Natalia',
'coihue': 'Luis',
'canelo': 'Maria',
'peumo': 'Jose',
'quillay': 'Marisol',
'algarrobo': 'Jorge',
'araucaria': 'Roxana',
'arrayan': 'Mauricio',
'espino': 'Tamara',
'boldo': 'Bruno',
'maiten': 'Javiera',
'palma': 'Tomas',
'patagua': 'Rayen',
'litre': 'Rodrigo'
}

Asignaciones = {'Natalia': 'Tomas', 'Luis': 'Marisol', 'Maria': 'Jorge', 'Jose': 'Roxana', 'Marisol': 'Rodrigo', 'Jorge': 'Mauricio', 'Roxana': 'Javiera', 'Mauricio': 'Rayen', 'Tamara': 'Bruno', 'Bruno': 'Natalia', 'Javiera': 'Tamara', 'Tomas': 'Jose', 'Rayen': 'Luis', 'Rodrigo': 'Maria'}

amigo_secreto = codigos_validos | Asignaciones

random_number = random.randint(1, 6)

iconos = {
    1: "❄️",
    2: "🎅🏼",
    3: "🎄",
    4: "🍀",
    5: "🥂",
    6: "🥵"
}
run_snow_animation()

# Interfaz de Streamlit
st.title("🎄 Portal Navideño 🎄")
st.subheader(f"Bienvenid@")

codigo_ingresado = st.text_input("🔑 Ingresa tu código navideño:").lower()

if codigo_ingresado:
    if codigo_ingresado in codigos_validos:
        st.markdown(f" {codigos_validos[codigo_ingresado]}, Tu amig@ secret@ 👤 es:")
        st.success(f"{amigo_secreto[amigo_secreto[codigo_ingresado]]}")

    else:
        st.error("❌ Código inválido. Intente nuevamente.")
