import speech_recognition as sr

def understand_vocal():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening... Please speak.")
        try:
            # Adjust for ambient noise and capture audio
            recognizer.adjust_for_ambient_noise(source)
            audio = recognizer.listen(source, timeout=5)  # 5 seconds to start speaking
            print("Processing...")
            
            # Recognize speech using Google Web Speech API
            text = recognizer.recognize_google(audio)
            print(f"You said: {text}")
        except sr.UnknownValueError:
            print("Sorry, I couldn't understand what you said.")
        except sr.RequestError as e:
            print(f"Could not request results; {e}")
        except Exception as ex:
            print(f"An error occurred: {ex}")

if __name__ == "__main__":
    understand_vocal()
