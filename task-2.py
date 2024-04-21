from googletrans import Translator, LANGUAGES
from langdetect import detect_langs, DetectorFactory

def TransLate(txt, lang):
    translator = Translator()
    try:
        translated_text = translator.translate(txt, dest=lang).text
        return translated_text
    except Exception as e:
        return f"Translation Error: {str(e)}"

def LangDetect(txt):
    DetectorFactory.seed = 0
    try:
        result = detect_langs(txt)
        lang = result[0].lang
        confidence = result[0].prob
        return f"Detected(lang={lang}, confidence={confidence})"
    except Exception as e:
        return f"Language Detection Error: {str(e)}"

def CodeLang(lang):
    lang = lang.lower()
    return LANGUAGES.get(lang, f"Language '{lang}' not found")

def main():
    print("Welcome to the Translation Chat!")
    while True:
        print("\nEnter 'exit' to quit the chat.")
        txt = input("Enter the text you want to translate: ")
        if txt.lower() == 'exit':
            print("Goodbye!")
            break
        lang = input("Enter the language code or name to translate to: ")
        print(f"\nOriginal text: {txt}")
        print(LangDetect(txt))
        translated_text = TransLate(txt, lang)
        print(f"Translated text: {translated_text}")
        print(f"Language: {CodeLang(lang)}")

if __name__ == "__main__":
    main()
