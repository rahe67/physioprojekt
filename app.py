import streamlit as st
import google.generativeai as genai

# Konfiguration mit deinem neuen Key
API_KEY = "AIzaSyB5bWqpNuBG--N81rXvBclf4y7vrmC6hC8"
genai.configure(api_key=API_KEY)

# Wir nutzen das zuverlässige Modell
model = genai.GenerativeModel('gemini-1.5-flash-8b')

# App Design
st.set_page_config(page_title="Physio-Doku-Pro", page_icon="🩺")
st.title("🩺 Physio-Doku Assistent")
st.markdown("---")

# Eingabe-Bereich
st.subheader("Behandlungs-Notizen")
st.info("Tipp: Nutze das Mikrofon-Symbol deiner Tastatur zum Diktieren!")
raw_input = st.text_area("Was wurde heute gemacht?", placeholder="z.B. Knieschmerzen 8/10, Quadriceps gekräftigt...")

if st.button("Protokoll professionell erstellen"):
    if raw_input:
        with st.spinner('KI erstellt das Protokoll...'):
            try:
                prompt = f"""
                Du bist ein Experte für Physiotherapie-Dokumentation. 
                Erstelle aus diesen Notizen ein sauberes SOAP-Protokoll:
                {raw_input}
                """
                response = model.generate_content(prompt)
                st.markdown("---")
                st.subheader("Fertiger Bericht:")
                st.success(response.text)
            except Exception as e:
                st.error(f"Verbindung steht, aber die KI meldet: {e}")
    else:
        st.error("Bitte gib zuerst ein paar Notizen ein.")



