from gtts import gTTS
def text_to_speech(text, filename):
    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine
    tts = gTTS(text=text, lang=language, slow=False)

    # Save the converted audio to a file
    tts.save(filename)

# Example usage
text = '''


'''
filename = "Texttospeech.mp3"

text_to_speech(text, filename)