import speech_recognition  # Import the speech recognition library

def record_voice():
    # Create a Recognizer object for recognizing speech
    microphone = speech_recognition.Recognizer()	

    # Adjust microphone for ambient noise
    with speech_recognition.Microphone() as live_phone:
        microphone.adjust_for_ambient_noise(live_phone)

        # Prompt the user to speak
        print("I'm trying to hear you: ")
        
        # Listen for audio input from the microphone
        audio = microphone.listen(live_phone)
        
        try:
            # Recognize speech using Google Speech Recognition
            phrase = microphone.recognize_google(audio, language='en')
            return phrase  # Return the recognized phrase
        except speech_recognition.UnknownValueError:
            return "I didn't understand what you said"  # Return a message if speech could not be recognized

if __name__ == '__main__':
    # Call the record_voice function to capture speech input
    phrase = record_voice()

    # Write the recognized phrase to a text file
    with open('you_said_this.txt', 'w') as file:
        file.write(phrase) 

    print('the last sentence you spoke was saved in you_said_this.txt') 
