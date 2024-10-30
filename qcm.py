import streamlit as st
import random
from functions import get_name_by_email, save_new_player, save_score, get_top_scores, reset_quiz, initialize_db
from questions import questions


#initialize_db()

def qcm_bible():
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
                    st.session_state["answers"] = [None] * 20
                    st.session_state["quiz_completed"] = False
                    st.session_state["selected_questions"] = random.sample(questions, 20)
                    st.session_state["feedback"] = [None] * 20
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
                st.session_state["answers"] = [None] * 20
                st.session_state["quiz_completed"] = False
                st.session_state["selected_questions"] = random.sample(questions, 20)
                st.session_state["feedback"] = [None] * 20
                st.session_state["new_user"] = False
                st.experimental_rerun()
            else:
                st.warning("Veuillez entrer un pseudo.")

    elif st.session_state.get("quiz_completed", False):
        st.title("Résultats du QCM Bible")
        save_score(st.session_state["user_email"], st.session_state["score"])

        
        st.markdown(f"**Votre score final est : {st.session_state['score']} / 20**")

        
        if st.button("Recommencer ?"):
            reset_quiz()
            st.experimental_rerun()

    else:
        st.title("QCM sur la Bible")
        current_index = st.session_state["question_index"]
        question_data = st.session_state["selected_questions"][current_index]
        answer_selected = st.session_state["answers"][current_index] is not None

       
        progress = (current_index + 1) / 20
        st.progress(progress)

        st.write(f"**Question {current_index + 1}** : {question_data['question']}")
        answer = st.radio(
            "", 
            question_data["options"], 
            index=None, 
            key=f"question_{current_index}",
            disabled=answer_selected
        )

        if not answer_selected and answer:
            st.session_state["answers"][current_index] = answer
            if answer == question_data["answer"]:
                st.session_state["feedback"][current_index] = "Correct"
                st.session_state["score"] += 1
            else:
                st.session_state["feedback"][current_index] = "Incorrect"

        if st.session_state["feedback"][current_index] == "Correct":
            st.success("Correct !")
        elif st.session_state["feedback"][current_index] == "Incorrect":
            st.error("Incorrect !")

        if current_index + 1 < 20:
            if st.button("Suivant"):
                st.session_state["question_index"] += 1
                st.experimental_rerun()
        else:
            if st.button("Terminer le QCM"):
                st.session_state["quiz_completed"] = True
                st.experimental_rerun()
def qcm_chemin():
    st.title("Cette partie arrive bientôt")
    st.markdown("*Streamlit* is **really** ***cool***.")
    st.markdown('''
        :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
        :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
   