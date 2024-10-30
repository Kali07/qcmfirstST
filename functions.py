import sqlite3
import streamlit as st

# Fonction pour ouvrir une connexion SQLite
def get_connection():
    conn = sqlite3.connect("qcm_scores.db", check_same_thread=False)
    return conn

# Fonction pour initialiser la base de données
def initialize_db():
    conn = get_connection()
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
    conn.close()

# Fonction pour récupérer le nom d'un joueur existant
def get_name_by_email(email):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name FROM scores WHERE email = ?", (email,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else None

# Fonction pour enregistrer un nouveau joueur
def save_new_player(email, name):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("INSERT OR IGNORE INTO scores (email, name, score) VALUES (?, ?, 0)", (email, name))
    conn.commit()
    conn.close()

# Fonction pour enregistrer le score
def save_score(email, score):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("UPDATE scores SET score = ? WHERE email = ?", (score, email))
    conn.commit()
    conn.close()

# Fonction pour récupérer les 10 meilleurs scores
def get_top_scores():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT name, score FROM scores ORDER BY score DESC LIMIT 10")
    top_scores = cursor.fetchall()
    conn.close()
    return top_scores

# Fonction pour réinitialiser les variables de session
def reset_quiz():
    for key in ["user_name", "user_email", "score", "question_index", "answers", "quiz_completed", "final_score_calculated", "new_user"]:
        if key in st.session_state:
            del st.session_state[key]
