import streamlit as st
import google.generativeai as genai

# Konfiguration
API_KEY = "AIzaSyDkdXr1jLRDRLTFXK-Agiu9fmOh-g95LE4"
genai.configure(api_key=API_KEY)

# Hier nehmen wir jetzt das stabile Pro-Modell
model = genai.GenerativeModel('gemini-pro')

# App Design
st.set_page_config(page_title="Physio-Doku-Pro", page_icon="🩺")
st.title("🩺 Physio-Doku Assistent")
st.markdown("---")

# Eingabe-Bereich
st.subheader("Behandlungs-Notizen")
raw_input = st.text_area("Was wurde heute gemacht?", placeholder="z.B. Knieschmerzen 8/10, Faszien gelockert...")

if st.button("Protokoll professionell erstellen"):
    if raw_input:
        with st.spinner('KI erstellt das Protokoll...'):
            try:
                prompt = f"Erstelle ein professionelles Physio-SOAP-Protokoll aus diesen Notizen: {raw_input}"
                response = model.generate_content(prompt)
                st.markdown("---")
                st.subheader("Fertiger Bericht:")
                st.success(response.text)
            except Exception as e:
                st.error(f"Fehler: {e}")
    else:
        st.error("Bitte gib zuerst Notizen ein.")

