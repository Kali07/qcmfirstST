import streamlit as st
from functions import get_name_by_email, save_new_player, save_score, get_top_scores, reset_quiz, initialize_db
from questions import questions
from qcm import *


initialize_db()

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Menu", ["Accueil", "QCM Bible", "QCM Chemin", "Scores Bible", "Scores Chemin"])

st.sidebar.markdown("---")
st.sidebar.markdown("### Réalisé par :sunglasses: Richard Kali :balloon:")


if page == "Accueil":
    st.title("Bienvenue sur notre application de QCM")
    st.write("Choisissez un QCM dans le menu de gauche ou consultez les scores des meilleurs participants.")

elif page == "QCM Bible":
    st.title("QCM Bible")
    qcm_bible()

elif page == "QCM Chemin":
    st.title("QCM Chemin")
    qcm_chemin()  

elif page == "Scores Bible":
    st.title("Scores Bible des meilleurs participants")
    top_scores = get_top_scores()    
    
    st.subheader("Classement des meilleurs scores")
    for i, (name, score) in enumerate(top_scores, 1):
        st.write(f"{i}. {name} : {score}/20")

    # if st.button("Retour à l'accueil"):
    #     reset_quiz()
    #     st.experimental_rerun()
        
elif page == "Scores Chemin":
    st.title("Scores des meilleurs au Chemin ")
    #get_top_scores()