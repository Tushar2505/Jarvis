import speech_recognition as sr
import webbrowser
import pyttsx3
import datetime
import wikipedia
import random
import pyautogui
import os
import pyjokes
import subprocess


# Initialize the speech recognizer and text-to-speech engine
recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text) -> None:
    """Convert text to speech."""
    engine.say(text)
    engine.runAndWait()

def time() -> None:
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("The Current Time is")
    speak(Time)
    print("The Current Time is ", Time)

def date() -> None:
    day = datetime.datetime.now().day
    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    speak("The Current Date is")
    speak(day)
    speak(month)
    speak(year)
    print(f"The Current Date is {day}/{month}/{year}")

def greetOwner() -> None:
    print("Welcome back sir!!")
    speak("Welcome back sir!!")

    hour: int = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning Sir!!")
        print("Good Morning Sir!!")
    elif 12 <= hour < 16:
        speak("Good Afternoon Sir!!")
        print("Good Afternoon Sir!!")
    elif 16 <= hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speak("Please tell me how may I help you.")
    print("Please tell me how may I help you.")

def screenshot() -> None:
    img = pyautogui.screenshot()
    img_path = os.path.expanduser(r"C:\Users\tusha\OneDrive\Pictures\\ss.png")
    img.save(img_path)

def tell_joke():
    """Tell a random joke."""
    joke = pyjokes.get_joke()
    speak(joke)
    print(joke)

def open_application(app_name):
    """Open a specified application."""
    if app_name == "notepad":
        os.startfile("notepad.exe")
        speak("Opening Notepad")
    # Add more applications as needed

def shutdown_computer():
    """Shutdown the computer."""
    speak("Shutting down the computer")
    os.system("shutdown /s /t 1")

def change_volume(direction):
    """Change the system volume."""
    if direction == "up":
        pyautogui.press("volumeup")
        speak("Volume increased")
    elif direction == "down":
        pyautogui.press("volumedown")
        speak("Volume decreased")

def control_media(action):
    """Control media playback."""
    if action == "play":
        pyautogui.press("playpause")
        speak("Playing media")
    elif action == "pause":
        pyautogui.press("playpause")
        speak("Media paused")

def open_camera():

    # Open the default camera application on Windows
    subprocess.run("start microsoft.windows.camera:", shell=True)
    
    # Wait for the camera app to open
    time.sleep(2)

    print("Press 'Enter' to Capture Photo and 'Space' to Close Camera")
    speak("Press 'Enter' to Capture Photo and 'Space' to Close Camera")

    while True:
        try:
                # Take a photo when 'capture' is said
                if pyautogui.press('space'):
                    # Simulate pressing the spacebar
                    speak("Photo Captured")
                    print("Photo captured!")

                # Close the camera application when 'exit' is said
                elif pyautogui.hotkey('alt', 'f4'):
                    # Close the active window
                    break

        except sr.RequestError as e:
            print("Error; {0}".format(e))

def process_command(command):
    """Search and open any website based on the voice command."""
    if 'open' in command:
        # Extract the website name from the command
        website = command.replace('open ', '').strip()

        # Open the website
        search_url = f"https://{website}.com"
        speak(f"Searching for {website}")
        webbrowser.open_new_tab(search_url)

    else:
        speak("Please say a valid command like 'open YouTube'.")

def listen_for_command():
    """Listen for a voice command and return it as text."""
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print("Recognizing...")
        command = recognizer.recognize_google(audio, language="en-in")
        print(command)

    except Exception as e:
        print(e)
        return "Try Again"

    return command

if __name__ == "__main__":
        speak("Initializing Jarvis....")
        greetOwner()
        
        while True:
            try:
                # Listen for command
                command = listen_for_command().lower()

                # Check for exit command
                if 'exit' in command:
                    speak("Good Bye! See You Again Sir")
                    quit()

                elif "time" in command:
                    time()

                elif "date" in command:
                    date()

                elif "open notepad" in command:
                    open_application("notepad")

                elif "open camera" in command:
                    open_camera()

                elif "shutdown" in command:
                    shutdown_computer()

                elif "volume up" in command:
                    change_volume("up")

                elif "volume down" in command:
                    change_volume("down")

                elif "play" in command:
                    control_media("play")
                    
                elif "pause" in command:
                    control_media("pause")

                elif 'open' in command:
                    process_command(command)

                elif 'joke' in command:
                    tell_joke()

                elif "tell me" in command:
                    try:
                        speak("Ok wait sir, I'm searching...")
                        query = command.replace("wikipedia", "")
                        result = wikipedia.summary(query, sentences=2)
                        print(result)
                        speak(result)
                    except:
                        speak("Can't find this page sir, please ask something else")

                elif "search" in command:
                    try:
                        speak("What should I search?")
                        print("What should I search?")
                        search_query = listen_for_command()
                        search_url = f"https://www.google.com/search?q={search_query}"
                        webbrowser.open_new_tab(search_url)
                        speak(f"Searching Google for {search_query}.")
                    except Exception as e:
                        speak("Can't open now, please try again later.")
                        print("Can't open now, please try again later.")

                    except Exception as e:
                        speak("Can't open now, please try again later.")
                        print("Can't open now, please try again later.")
                
                elif "screenshot" in command:
                    screenshot()
                    speak("I've taken screenshot, please check it")
                
                else:
                    speak("Please say a valid command.") 

            except sr.UnknownValueError:
                print("Could not understand the audio.")
                speak("I didn't catch that. Please repeat.")

            except sr.RequestError as e:
                print(f"Could not request results from Google Speech Recognition service; {e}")
                speak("There seems to be an issue with the speech recognition service.")

            except Exception as e:
                print(f"Error: {e}")
                speak("An error occurred.")

