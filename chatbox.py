import pyttsx3
import speech_recognition
from datetime import date, datetime

#initalize
robot_brain = ""
robot_ear = speech_recognition.Recognizer()
robot_mouth = pyttsx3.init()

#set-up voice
""" RATE"""
rate = robot_mouth.getProperty('rate')   # getting details of current speaking rate
#print (rate)                        #printing current voice rate
robot_mouth.setProperty('rate', 125)     # setting up new voice rate


"""VOLUME"""
volume = robot_mouth.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
#print (volume)                          #printing current volume level
robot_mouth.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

"""VOICE"""
voices = robot_mouth.getProperty('voices')       #getting details of current voice
#robot_mouth.setProperty('voice', voices[0].id)  #changing index, changes voices. o for male
robot_mouth.setProperty('voice', voices[1].id)   #changing index, changes voices. 1 for female


while True:
    #listening
    with speech_recognition.Microphone() as mic:
        print("Marvis: I'm listening")
        audio = robot_ear.listen(mic)
    print("Marvis: ...")

    #catch error
    try: 
        you = robot_ear.recognize_google(audio)
    except: 
        you = ""

    #create reply
    print("You: "+ you)
    if you == "":
        print("I cannot hear you, try again")
    elif "today" in you:
        today = date.today()
        robot_brain = today.strftime("%B %d, %Y")
    elif "time" in you:
        now = datetime.now()
        robot_brain = now.strftime("%H hours %M minutes %S seconds")
    elif "hello" in you:
        robot_brain = "Hello Minh"
    #get off the loop
    elif "bye" in you:
        robot_brain = "Bye Minh"
        print("Marvis: ",robot_brain)    
        robot_mouth.say(robot_brain)
        robot_mouth.runAndWait()
        break
    else:
        robot_brain = "Thank you"

    #response
    print("Marvis: ",robot_brain)    
    robot_mouth.say(robot_brain)
    robot_mouth.runAndWait()