import streamlit as st

# st.title("Bienvenue sur le QCM")
# st.write("Veuillez entrer votre nom et votre email pour commencer.")

if "user_name" not in st.session_state or "user_email" not in st.session_state:

    st.title("Inscription")
    st.write("Veuillez entrer votre nom et email pour commencer le QCM.")

    name = st.text_input("Nom", "")
    email = st.text_input("Email", "")

    if st.button("Commencer"):
        if name and email:
            
            st.session_state["user_name"] = name
            st.session_state["user_email"] = email
            st.session_state["score"] = 0
            st.experimental_rerun()
            st.write(f"Bienvenue, {name} !")
            

            st.write("Première question : ...")
        else:
            st.warning("Veuillez entrer à la fois un nom et un email valide.")
else:

    st.title("Questions du QCM")
    st.write(f"Bonjour, {st.session_state['user_name']} ! Répondez aux questions ci-dessous :")

 
    question_1 = st.radio("Question 1 : Quelle est la capitale de la France ?", ("Paris", "Lyon", "Marseille"))
    if question_1 == "Paris":
        st.session_state["score"] += 1  

    question_2 = st.radio("Question 2 : Quelle est la couleur du ciel par temps clair ?", ("Bleu", "Vert", "Rouge"))
    if question_2 == "Bleu":
        st.session_state["score"] += 1  


    if st.button("Terminer le QCM et voir le classement"):
      
        st.write("Votre score est :", st.session_state["score"])
        
       