import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize the translator
translator = Translator()

# Available languages (including African languages)
languages = {
    'isiZulu': 'zu',
    'Xhosa': 'xh',
    'Swahili': 'sw',
    'French': 'fr',
    'Afrikaans': 'af',
    'Shona': 'sn',
    'Sesotho': 'st'
}

def translate_text(text, target_language):
    """Translate text from English to the target language."""
    try:
        # Perform translation
        translation = translator.translate(text, src='en', dest=target_language)
        return translation.text
    except Exception as e:
        # Handle errors that may occur during translation
        st.error(f"An error occurred during translation: {e}")
        return None

# Streamlit application
def main():
    st.title("African Languages Translator")

    # Dropdown for selecting target language
    selected_language = st.selectbox("Select language", options=list(languages.keys()))

    # Input text from user
    english_text = st.text_area("Enter text in English:")

    if st.button("Translate"):
        if english_text.strip() == "":
            st.error("Please enter some text to translate.")
        else:
            # Perform translation
            target_language_code = languages[selected_language]
            translated_text = translate_text(english_text, target_language_code)
            if translated_text:
                # Display the translation
                st.write(f"**English:** {english_text}")
                st.write(f"**{selected_language}:** {translated_text}")

if __name__ == "__main__":
    main()

