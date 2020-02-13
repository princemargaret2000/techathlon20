import gif
import wikipedia
import wolframalpha
import requests
import os
import webbrowser
import pyttsx3
import speech_recognition as sr
from pygame import mixer
from googlesearch import search
from tkinter import *
from tkinter import ttk
import time





root = Tk()

root.geometry('520x650')
root.title('Prince Margaret Personal assistant')

root.iconbitmap("Microphone_icon.ico")

style = ttk.Style()
style.theme_use('winnative')

logo=gif.AnimatedGIF(root, 'earth.gif')
logo.pack()


frame=Frame(root)
sc=Scrollbar(frame)
msgs=Listbox(frame,width=80,height=10,bg="lightblue")
sc.pack(side=RIGHT,fill=Y)
msgs.pack(side=LEFT,fill=BOTH,pady=10)
frame.pack()

logo1=gif.AnimatedGIF(root, 'buffer.gif')

label = ttk.Label(root, text='Query:')
entry = ttk.Entry(root, width=50)

label.pack(side=LEFT)
entry.pack(side=LEFT)


btn2 = StringVar()





a=0

photo = PhotoImage(file='microphone.png').subsample(20, 20)

def chrome(question):
    
    
    try:
      
      url=next(search(question))
      margaret_speak("opening  " + question)
      webbrowser.open(url)
      
    except:
        webbrowser.open(question)
       

   

def margaret_speak(output):

    a='Margaret'+ " :   "+ output

    msgs.focus()
    
    msgs.insert(0, a)


    engine = pyttsx3.init()
    voices = engine.getProperty('voices')

    engine.setProperty('voice', voices[0].id)  # MARGREAT
    engine.setProperty('rate', 175)
    engine.setProperty('volume', 120.0)

    engine.say(output)
    engine.runAndWait()
    engine.stop()



def NewsFromBBC():
    try:
        main_url = "https://newsapi.org/v2/top-headlines?country=in&category=science&apiKey=af87328db1b042ed8452ee054068c446"
        open_bbc_page = requests.get(main_url).json()  
        article = open_bbc_page["articles"]
        results = []

        for ar in article:
            results.append(ar["title"])

        for i in range(len(results)):
            
            margaret_speak('{}, '.format(i + 1) + results[i])
    except:
        margaret_speak("api key error so i can not fetch current news")

def open_application(input):
    try:
        if "chrome" in input:
            margaret_speak(" opening Google Chrome")
            os.startfile('Google Chrome.lnk')
        elif "vlc" in input:
            margaret_speak(" opening VLC media player")
            os.startfile("VLC media player.lnk")

        elif "arduino" in input:
            margaret_speak(" opening arduino")
            os.startfile("Arduino.lnk")

        elif "notepad" in input:
            margaret_speak(" opening notepad")
            os.startfile("notepad.exe")
        elif "codeblocks" in input or "codeblock" in input:
            margaret_speak("Opening codeblocks ")
            os.startfile('codeblocks.exe')


        elif "wordpad" in input or "word" in input:
            margaret_speak("Opening  Word Pad")

            os.startfile("WordPad.lnk")
        

        elif "excel" in input:

            margaret_speak("Opening Microsoft Excel")
            os.startfile('Excel 2016.lnk')

        elif "firefox" in input:
            os.startfile("Firefox.lnk")

        else:
            margaret_speak("Application not available")
    except:
        margaret_speak("Application not available")

def close():
    os.system("TASKKILL /F /IM chrome.exe")
    os.system("TASKKILL /F /IM arduino.exe")
    os.system("TASKKILL /F /IM notepad.exe")
    os.system("TASKKILL /F /IM codeblocks.exe")
    os.system("TASKKILL /F /IM chrome.exe")
    os.system("TASKKILL /F /IM WordPad.lnk")


def wol(question):
    try:
        margaret_speak(next(wolframalpha.Client("4QHXVE-U8T54TTH6V").query(question.upper()).results).text)

    except:
        margaret_speak(" I have error in wolframalpha module so I am unable to search on wolframalpha ")
def wiki(question):
    try:
        margaret_speak(wikipedia.summary(question, 2))
    except:
        margaret_speak(" I have error in wikipedia module so I am unable to search on wikipedia")








def main():
    try:
        question = entry.get().lower().rstrip()
        msgs.focus()
        msgs.delete(0, END)
        msgs.insert(0, "You :  " + entry.get())
        entry.focus()
        entry.delete(0, END)
    except:
        margaret_speak("error in taking input")


    try:
        if "who are you" in entry.get() or "define yourself" in entry.get():
            margaret_speak('''Hello, I am Margreat of Prince Agrahari.
                   I am here to make your life easier.
                   You can command me to perform various tasks such as calculating sums or opening applications etcetra''')
        elif "hello" in question or "hi" in question or "hey" in question:
            margaret_speak("Yes sir, what can i help you")
        elif "close" in question:
            close()



        elif "who made you" in question or "created you" in question:
            margaret_speak("I have been created by Prince Sir")
        elif "who is your boss" in question or "who is your commander" in question:
            margaret_speak(" Prince Sir")




        elif "where do you live" in question:
            margaret_speak("i live in your heart")
        elif "what is your name" in question:
            margaret_speak("I am Margaret")
        elif "who are you" in question:
            margaret_speak("I am assistant of Prince Sir")

        elif "how are you" in question:
            margaret_speak("i am fine and you?")
        elif "open" in question:
            open_application(question)
        elif "news" in question:
            NewsFromBBC()
        elif "song" in question or "music" in question or "songs" in question or "gana" in question or "ganna" in question or "play" in question:
            
            
            chrome(question)

        elif "video" in question or "videos" in question:
            chrome(question)
        elif "photo" in question or "pic" in question or "pics" in question or "diagram" in question or "figure" in question or "chitra" in question:
            chrome(question)
        elif "about" in question:
            wiki(question)
        elif "tell" in question:
            wol(question)
        else:
            
            try:
                margaret_speak("Can I search on web sir? say yes or ok")
                
                if"yes" in microphone() or "yesh" in microphone() or "ya" in microphone() or "ok" in microphone():
                     chrome(question)
                else:
                    pass
            except:
                pass


    except:
        if btn2.get() == 'google' and entry.get() != '':
            webbrowser.open('http://google.com/search?q=' + entry.get())

        elif btn2.get() == 'duck' and entry.get() != '':
            webbrowser.open('http://duckduckgo.com/?q=' + entry.get())

        elif btn2.get() == 'amazon' and entry.get() != '':
            webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords=' + entry.get())

        elif btn2.get() == 'youtube' and entry.get() != '':
            webbrowser.open('https://www.youtube.com/results?search_query=' + entry.get())

        else:
            pass








def callback():
    if btn2.get() == 'google' and entry.get() != '':
        webbrowser.open('http://google.com/search?q=' + entry.get())

    elif btn2.get() == 'duck' and entry.get() != '':
        webbrowser.open('http://duckduckgo.com/?q=' + entry.get())

    elif btn2.get() == 'amazon' and entry.get() != '':
        webbrowser.open('https://amazon.com/s/?url=search-alias%3Dstripbooks&field-keywords=' + entry.get())

    elif btn2.get() == 'youtube' and entry.get() != '':
        webbrowser.open('https://www.youtube.com/results?search_query=' + entry.get())

    else:
        pass







def get(event):
    if btn2.get() == 'google' and entry.get() != '':
        main()



def microphone():
    
    mixer.init()
    mixer.music.load('alart_sound.mp3')
    mixer.music.play()

    # enter the name of usb microphone that you found
    # using lsusb
    # the following name is only used as an example
    #mic_name = "USB Device 0x46d:0x825: Audio (hw:1, 0)
    # Sample rate is how often values are recorded
    sample_rate = 48000
    # Chunk is like a buffer. It stores 2048 samples (bytes of data)
    # here.
    
    chunk_size = 2048   # it is advisable to use powers of 2 such as 1024 or 2048
    try:
        r = sr.Recognizer()
        with sr.Microphone() as source:
            r.pause_threshold =1
            r.adjust_for_ambient_noise(source)
            audio = r.listen(source)
            text = r.recognize_google(audio)
            try:
               entry.focus()
               entry.delete(0, END)
               entry.insert(0, text)
               main()
            except:
                pass
    
                      
    except sr.UnknownValueError:
            margaret_speak('I could not find you. Please try again.')

    except sr.RequestError as e:
            margaret_speak('Please check your Internet connection. ')
    except Exception:
        pass
   


entry.bind('<Return>', get)    


Search= ttk.Button(root, text='Search', width=10, command=main)
mic = Button(root, image=photo, command=microphone, bd=1, activebackground='#c1bfbf', overrelief='groove',relief='sunken')
close= ttk.Button(root, text='close', width=10, command=close)
Google= ttk.Radiobutton(root, text='Google', value='google', variable=btn2)
Duck= ttk.Radiobutton(root, text='Duck', value='duck', variable=btn2)
Amazon= ttk.Radiobutton(root, text='Amazon', value='amazon', variable=btn2)
Youtube= ttk.Radiobutton(root, text='Youtube', value='youtube', variable=btn2)

#buttons

Search.pack(fill=X,side=LEFT,padx=5)
mic.pack(side=LEFT,padx=5)
close.pack(fill=Y,side=TOP)
Google.pack()
Duck.pack()
Amazon.pack()
Youtube.pack()



entry.focus()
root.wm_attributes('-topmost', 1)
btn2.set("google")

root.mainloop()
