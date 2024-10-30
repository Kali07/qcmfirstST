import streamlit as st
import sqlite3

# Initialisation de la base de données
conn = sqlite3.connect("qcm_scores.db")
cursor = conn.cursor()
cursor.execute("""
CREATE TABLE IF NOT EXISTS scores (
    id INTEGER PRIMARY KEY,
    email TEXT UNIQUE,
    name TEXT,
    score INTEGER
)
""")
conn.commit()

# Fonction pour enregistrer le score
def save_score(name, email, score):
    cursor.execute("INSERT OR REPLACE INTO scores (email, name, score) VALUES (?, ?, ?)", (email, name, score))
    conn.commit()

# Fonction pour récupérer les 10 meilleurs scores
def get_top_scores():
    cursor.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 10")
    return cursor.fetchall()

# Fonction pour réinitialiser les variables de session
def reset_quiz():
    for key in ["user_name", "user_email", "score", "question_index", "answers", "quiz_completed", "final_score_calculated"]:
        if key in st.session_state:
            del st.session_state[key]

# Initialisation de la session
if "user_name" not in st.session_state or "user_email" not in st.session_state:
    # Écran d'inscription
    st.title("Inscription")
    st.write("Veuillez entrer votre nom et email pour commencer le QCM.")

    name = st.text_input("Nom", "")
    email = st.text_input("Email", "")

    if st.button("Commencer"):
        if name and email:
            st.session_state["user_name"] = name
            st.session_state["user_email"] = email
            st.session_state["score"] = 0
            st.session_state["question_index"] = 0
            st.session_state["answers"] = [None] * 10  # Initialise les réponses des utilisateurs
            st.session_state["quiz_completed"] = False  # Variable pour indiquer la fin du QCM
            st.experimental_rerun()
        else:
            st.warning("Veuillez entrer un nom et un email valide.")
elif st.session_state.get("quiz_completed", False):
    # Page des résultats
    st.title("Résultats du QCM")
    
    # Enregistrer le score de l'utilisateur
    save_score(st.session_state["user_name"], st.session_state["user_email"], st.session_state["score"])
    
    # Récupérer les 10 meilleurs scores
    top_scores = get_top_scores()

    # Afficher les 10 meilleurs scores
    st.subheader("Classement des meilleurs scores")
    for i, (name, score) in enumerate(top_scores, 1):
        if name == st.session_state["user_name"]:
            st.markdown(f"**{i}. {name} : {score}/10**")  # Met en gras le score de l'utilisateur
        else:
            st.write(f"{i}. {name} : {score}/10")
    
    # Bouton pour retourner à l'accueil
    if st.button("Retour à l'accueil"):
        reset_quiz()
        st.experimental_rerun()

else:
    # Questions du QCM
    st.title("QCM sur la Bible")
    questions = [
        {"question": "Combien y a-t-il de livres dans la Bible ?", "options": ["66", "73", "80"], "answer": "66"},
        {"question": "Qui a construit l'arche ?", "options": ["Noé", "Moïse", "Abraham"], "answer": "Noé"},
        {"question": "Qui a reçu les Dix Commandements ?", "options": ["David", "Moïse", "Salomon"], "answer": "Moïse"},
        {"question": "Dans quelle ville Jésus est-il né ?", "options": ["Nazareth", "Bethléem", "Jérusalem"], "answer": "Bethléem"},
        {"question": "Qui a été avalé par un grand poisson ?", "options": ["Jonas", "Jérémie", "Elie"], "answer": "Jonas"},
        {"question": "Quelle est la première phrase de la Bible ?", "options": ["Au commencement...", "Dieu créa la terre", "Il y avait la lumière"], "answer": "Au commencement..."},
        {"question": "Combien de jours a duré la création ?", "options": ["6", "7", "10"], "answer": "6"},
        {"question": "Qui a trahi Jésus ?", "options": ["Pierre", "Judas", "Thomas"], "answer": "Judas"},
        {"question": "Quel est le dernier livre de la Bible ?", "options": ["Actes", "Révélation", "Psaumes"], "answer": "Révélation"},
        {"question": "Qui est le père de tous les croyants ?", "options": ["Moïse", "Abraham", "Isaac"], "answer": "Abraham"},
    ]

    # Affiche deux questions à la fois
    current_index = st.session_state["question_index"]
    questions_to_display = questions[current_index:current_index+2]

    for i, question_data in enumerate(questions_to_display):
        st.write(f"**Question {current_index + i + 1}** : {question_data['question']}")
        # Utilise None comme valeur par défaut pour éviter la présélection
        answer = st.radio(
            "",
            question_data["options"],
            index=None,
            key=f"question_{current_index + i}"
        )
        st.session_state["answers"][current_index + i] = answer  # Stocke la réponse choisie par l'utilisateur

    # Barre de progression
    progress = (current_index + len(questions_to_display)) / len(questions)
    st.progress(progress)

    # Navigation des questions
    if current_index + 2 < len(questions):
        if st.button("Suivant"):
            st.session_state["question_index"] += 2
            st.experimental_rerun()
    else:
        if st.button("Terminer le QCM"):
            # Calculer le score une seule fois
            if "final_score_calculated" not in st.session_state:
                st.session_state["score"] = sum(
                    1 for i, question_data in enumerate(questions)
                    if st.session_state["answers"][i] == question_data["answer"]
                )
                st.session_state["final_score_calculated"] = True  # Marque le score comme calculé
                st.session_state["quiz_completed"] = True  # Indique que le QCM est terminé
            st.experimental_rerun()  # Recharge pour afficher la page de résultats
