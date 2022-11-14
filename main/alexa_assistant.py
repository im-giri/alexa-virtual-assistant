import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(command):
    engine.say(command)
    engine.runAndWait()


def take_command():
    command = ''
    try:
        with sr.Microphone() as source:
            print("Go on, listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            # print('sss')
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa', '')
    except:
        # print("error")
        pass
    return command


def run_alexa():
    command = take_command()
    if 'play' in command:
        song = command.replace('play', '')
        talk("playing " + song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time = datetime.datetime.now().strftime('%I:%M %p')
        talk("The time is " + time)
    elif 'who is' in command:
        try:
            search_word = command.replace('who is', '')
            wiki_info = wikipedia.summary(search_word, 1)
            talk(wiki_info)
        except:
            talk("sorry!, I don't think this person is a famous personality! please try again")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    elif 'are you single' in command:
        talk("No, i'm in a relationship with Wifi")
    elif 'bye' or 'turn off' in command:
        print("Turning off! Bye")
        talk("Turning off, Bye")
        return "end"

    else:
        talk("Sorry, can you please repeat that again?")


while True:
    a = run_alexa()
    if a == "end":
        break

# run_alexa()