import streamlit as st
import pandas as pd
import joblib

# --- Load the Trained Model ---
# The model is loaded once when the app starts and stored in memory.
@st.cache_resource
def load_model():
    model = joblib.load('pokemon_model.joblib')
    return model

model = load_model()

# --- App Interface ---
st.title('🔮 Pokémon Type Predictor')
st.write("A simple app to predict the primary type of a Pokémon based on its stats.")

st.sidebar.header('Input Pokémon Stats')

# Create sliders in the sidebar for user input
hp = st.sidebar.slider('HP (Hit Points)', 1, 255, 50)
attack = st.sidebar.slider('Attack', 5, 190, 50)
defense = st.sidebar.slider('Defense', 5, 230, 50)
sp_atk = st.sidebar.slider('Special Attack', 10, 194, 65)
sp_def = st.sidebar.slider('Special Defense', 20, 230, 65)
speed = st.sidebar.slider('Speed', 5, 180, 50)

# --- Prediction Logic ---
if st.sidebar.button('Predict Type'):
    # Create a DataFrame from the user's inputs
    new_pokemon_stats = pd.DataFrame({
        'HP': [hp],
        'Attack': [attack],
        'Defense': [defense],
        'Sp. Atk': [sp_atk],
        'Sp. Def': [sp_def],
        'Speed': [speed]
    })
    
    st.write("New Pokémon Stats:")
    st.dataframe(new_pokemon_stats)

    # Use the loaded model to make a prediction
    prediction = model.predict(new_pokemon_stats)
    
    # Display the prediction
    st.success(f"🎉 The model predicts the primary type is: **{prediction[0]}**")
