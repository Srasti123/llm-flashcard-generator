import streamlit as st
from flashcard_generator import generate_flashcards
import PyPDF2

st.set_page_config(page_title="Flashcard Generator", layout="centered")
st.title("AI Flashcard Generator")

st.markdown("Upload text or PDF and generate multiple unique flashcards using Hugging Face model.")

# Input methods
uploaded_file = st.file_uploader("Upload a .pdf or .txt file", type=["pdf", "txt"])
text_input = st.text_area("Or paste your educational content here:")
subject = st.text_input("Optional: Subject (e.g., Physics, History):")
cards_per_chunk = st.slider("Flashcards per chunk", min_value=1, max_value=10, value=5)

# Read file content
def read_text_from_file(uploaded_file):
    if uploaded_file.name.endswith(".pdf"):
        reader = PyPDF2.PdfReader(uploaded_file)
        return "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    elif uploaded_file.name.endswith(".txt"):
        return uploaded_file.read().decode("utf-8")
    return ""

# Generate flashcards
if st.button("Generate Flashcards"):
    if uploaded_file:
        input_text = read_text_from_file(uploaded_file)
    elif text_input.strip():
        input_text = text_input
    else:
        st.error("Please upload a file or paste some content.")
        st.stop()

    with st.spinner("Generating multiple flashcards..."):
        try:
            flashcards = generate_flashcards(input_text, subject, cards_per_chunk)
            st.success("✅ Flashcards generated!")
            st.text_area("📋 Flashcards Output", flashcards, height=400)
            st.download_button("📥 Download as TXT", data=flashcards, file_name="flashcards.txt", mime="text/plain")
        except Exception as e:
            st.error(f"⚠️ Error: {e}")
