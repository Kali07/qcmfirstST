import streamlit as st

def css_page():
    st.markdown("""
        <style>
            /* Couleurs principales */
            body {
                background-color: #f0f2f6;
                color: #333333;
            }
            
            /* Barre latérale */
            .css-1aumxhk, .css-12ttj6m, .css-1y4p8pa {
                background-color: #2d3e50;
                color: white;
            }

            /* Sélecteur du menu */
            .stSelectbox label {
                font-weight: bold;
                color: #ffffff;
            }
            .stSelectbox div[data-baseweb="select"] {
                background-color: #ffffff;
                color: #333333;
            }

            /* Style du bouton principal */
            div.stButton > button {
                background-color: #007acc;
                color: white;
                font-weight: bold;
                border-radius: 10px;
                padding: 8px 16px;
                margin-top: 10px;
                border: none;
            }
            div.stButton > button:hover {
                background-color: #005a99;
            }

            /* Lignes de séparation */
            hr {
                border: 1px solid #cccccc;
            }

            /* Titre et sous-titres */
            h1, h2, h3 {
                color: #2d3e50;
                font-family: 'Arial', sans-serif;
            }
            .styled-table {
                width: 100%;
                border-collapse: collapse;
                margin: 25px 0;
                font-size: 1.1em;
                font-family: 'Arial', sans-serif;
                min-width: 400px;
            }
            .styled-table thead tr {
                background-color: #007acc;
                color: #ffffff;
                text-align: left;
            }
            .styled-table th,
            .styled-table td {
                padding: 12px 15px;
                border: 1px solid #dddddd;
            }
            .styled-table tbody tr {
                border-bottom: 1px solid #dddddd;
            }
            .styled-table tbody tr:nth-of-type(even) {
                background-color: #f3f3f3;
            }
            .styled-table tbody tr:last-of-type {
                border-bottom: 2px solid #007acc;
            }
        </style>
    """, unsafe_allow_html=True)
