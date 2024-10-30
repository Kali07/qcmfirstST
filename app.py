import streamlit as st
from functions import *
import pandas as pd
from qcm import *
from css import *


initialize_db()
css_page()
st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Menu", ["Accueil", "QCM Bible", "QCM Chemin", "Scores Bible", "Scores Chemin"])

st.sidebar.markdown("---")
st.sidebar.markdown("### Réalisé par :sunglasses: Richard Kali :balloon:")


if page == "Accueil":
    st.title("Bienvenue sur notre application de QCM")
    st.write("Choisissez un QCM dans le menu de gauche ou consultez les scores des meilleurs participants.")

elif page == "QCM Bible":
    #st.title("QCM Bible")
    qcm_bible()

elif page == "QCM Chemin":
    st.title("QCM Chemin")
    qcm_chemin()  

elif page == "Scores Bible":
    st.title("Scores Bible")
    st.balloons()
    top_scores = get_top_scores()    
    
    st.subheader("Classement des meilleurs scores")
    
    df_scores = pd.DataFrame(top_scores, columns=["Nom", "Score"])
    df_scores.index += 1
    
    # Afficher le DataFrame sous forme de tableau
    st.table(df_scores)
    # if st.button("Nettoyer la base de données"):
    # # Fonction pour supprimer les données
    #     conn = get_connection()
    #     cursor = conn.cursor()
    #     cursor.execute("DELETE FROM scores")
    #     conn.commit()
    #     conn.close()
    
    # for i, (name, score) in enumerate(top_scores, 1):
    #     st.write(f"{i}. {name} : {score}/20")

    # if st.button("Retour à l'accueil"):
    #     reset_quiz()
    #     st.experimental_rerun()
        
elif page == "Scores Chemin":
    st.title("Scores Chemin ")
    st.snow()
    #get_top_scores()