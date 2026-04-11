import streamlit as st
import google.generativeai as genai

# Konfiguration (Hier kommt DEIN Key rein)
API_KEY = "AIzaSyDkdXr1jLRDRLTFXK-Agiu9fmOh-g95LE4"
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# App Design
st.set_page_config(page_title="Physio-Doku-Pro", page_icon="🩺")
st.title("🩺 Physio-Doku Assistent")
st.markdown("---")

# Eingabe-Bereich
st.subheader("Behandlungs-Notizen")
st.info("Tipp: Nutze am Handy das Mikrofon-Symbol auf deiner Tastatur zum Diktieren!")
raw_input = st.text_area("Was wurde heute gemacht?", placeholder="z.B. Pat. mit Knie-Arthrose, 8/10 Schmerz, Faszien gelockert...")

if st.button("Protokoll professionell erstellen"):
    if raw_input:
        with st.spinner('KI erstellt das Protokoll...'):
            # Der System-Prompt wird hier direkt eingebaut
            prompt = f"""
            Du bist ein Experte für Physiotherapie-Dokumentation in Deutschland. 
            Wandle folgende Notizen in ein professionelles SOAP-Protokoll um.
            
            Notizen: {raw_input}
            
            Struktur:
            S (Subjektiv): Schmerzskala und Patientenaussagen.
            O (Objektiv): Klinische Beobachtungen.
            A (Assessment): Durchgeführte Maßnahmen.
            P (Plan): Weiteres Vorgehen.
            
            Füge am Ende eine Sektion 'ABRECHNUNGSEMPFEHLUNG' hinzu (z.B. MT, KG, KMT).
            """
            
            response = model.generate_content(prompt)
            st.markdown("---")
            st.subheader("Fertiger Bericht:")
            st.success(response.text)
            st.button("In die Zwischenablage kopieren (Funktion folgt)")
    else:
        st.error("Bitte gib zuerst ein paar Stichpunkte ein.")
