import streamlit as st
import google.generativeai as genai

# Konfiguration
API_KEY = "AIzaSyDkdXr1jLRDRLTFXK-Agiu9fmOh-g95LE4"
genai.configure(api_key=API_KEY)

# Automatischer Modell-Check
def get_model():
    # Wir testen die drei gängigsten Namen für deine Region
    for name in ['gemini-1.5-flash', 'gemini-pro', 'models/gemini-pro']:
        try:
            m = genai.GenerativeModel(name)
            # Kleiner Test-Aufruf
            m.generate_content("test", generation_config={"max_output_tokens": 1})
            return m
        except:
            continue
    return None

model = get_model()

# App Design
st.set_page_config(page_title="Physio-Doku-Pro", page_icon="🩺")
st.title("🩺 Physio-Doku Assistent")

if model is None:
    st.error("Google erreicht kein Modell. Bitte prüfe deinen API-Key im AI Studio.")
else:
    raw_input = st.text_area("Behandlungs-Notizen:", placeholder="z.B. Knie 8/10...")
    
    if st.button("Protokoll erstellen"):
        if raw_input:
            with st.spinner('KI arbeitet...'):
                try:
                    response = model.generate_content(f"Erstelle ein Physio-SOAP-Protokoll: {raw_input}")
                    st.success(response.text)
                except Exception as e:
                    st.error(f"Fehler bei der Generierung: {e}")


