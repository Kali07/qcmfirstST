import streamlit as st
import random
from functions import get_name_by_email, save_new_player, save_score, get_top_scores, reset_quiz, initialize_db
from questions import questions


initialize_db()

# Initialisation de la session et tirage des questions aléatoires
if "user_email" not in st.session_state:
    st.title("Inscription")
    email = st.text_input("Email", "")

    if st.button("Suivant"):
        if email:
            st.session_state["user_email"] = email
            name = get_name_by_email(email)
            if name:
                st.session_state["user_name"] = name
                st.session_state["score"] = 0
                st.session_state["question_index"] = 0
                st.session_state["answers"] = [None] * 20  # Initialise les réponses pour 20 questions
                st.session_state["quiz_completed"] = False
                # Tirer 20 questions aléatoires parmi toutes les questions disponibles
                st.session_state["selected_questions"] = random.sample(questions, 20)
                st.experimental_rerun()
            else:
                st.session_state["new_user"] = True
        else:
            st.warning("Veuillez entrer un email valide.")

elif st.session_state.get("new_user", False):
    st.title("Bienvenue !")
    st.write("Il semble que vous êtes un nouveau joueur. Veuillez entrer votre pseudo.")
    name = st.text_input("Pseudo", "")

    if st.button("Commencer"):
        if name:
            st.session_state["user_name"] = name
            save_new_player(st.session_state["user_email"], name)
            st.session_state["score"] = 0
            st.session_state["question_index"] = 0
            st.session_state["answers"] = [None] * 20  # Initialise les réponses pour 20 questions
            st.session_state["quiz_completed"] = False
            # Tirer 20 questions aléatoires parmi toutes les questions disponibles
            st.session_state["selected_questions"] = random.sample(questions, 20)
            st.session_state["new_user"] = False
            st.experimental_rerun()
        else:
            st.warning("Veuillez entrer un pseudo.")

elif st.session_state.get("quiz_completed", False):
    st.title("Résultats du QCM")
    save_score(st.session_state["user_email"], st.session_state["score"])
    
    top_scores = get_top_scores()
    st.subheader("Classement des meilleurs scores")
    for i, (name, score) in enumerate(top_scores, 1):
        if name == st.session_state["user_name"]:
            st.markdown(f"**{i}. {name} : {score}/20**")
        else:
            st.write(f"{i}. {name} : {score}/20")
    
    if st.button("Retour à l'accueil"):
        reset_quiz()
        st.experimental_rerun()

else:
    st.title("QCM sur la Bible")
    current_index = st.session_state["question_index"]
    questions_to_display = st.session_state["selected_questions"][current_index:current_index+2]

    for i, question_data in enumerate(questions_to_display):
        st.write(f"**Question {current_index + i + 1}** : {question_data['question']}")
        answer = st.radio("", question_data["options"], index=None, key=f"question_{current_index + i}")
        st.session_state["answers"][current_index + i] = answer

    progress = (current_index + len(questions_to_display)) / 20
    st.progress(progress)

    if current_index + 2 < 20:
        if st.button("Suivant"):
            st.session_state["question_index"] += 2
            st.experimental_rerun()
    else:
        if st.button("Terminer le QCM"):
            if "final_score_calculated" not in st.session_state:
                st.session_state["score"] = sum(
                    1 for i, question_data in enumerate(st.session_state["selected_questions"])
                    if st.session_state["answers"][i] == question_data["answer"]
                )
                st.session_state["final_score_calculated"] = True
                st.session_state["quiz_completed"] = True
            st.experimental_rerun()
