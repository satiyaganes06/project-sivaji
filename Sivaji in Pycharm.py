# Import File
import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import wolframalpha
import random
import winsound
from tkinter import *
from PIL import ImageTk, Image
import face_recognition
import cv2 as cv2
import numpy as np
import feedparser
from pygame import *

def soundEffect():
    init()
    mixer.init()
    music = mixer.music.load(r"C:\Users\Acer\Desktop\Project Sivaji\hello.ogg")
    mixer.music.set_volume(1.5)
    mixer.music.play()

def speak(text):
    # speak coding, speak()
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.setProperty('rate', 174)
    engine.say(text)
    engine.runAndWait()


    # Wish You

def wishMe():
        hour = int(datetime.datetime.now().hour)

        if hour >= 0 and hour < 12:
            speak("Good Morning" + "sG")
        elif hour >= 12 and hour < 13:
            speak("Good Afternoon" + "sG")
        else:
            speak("Good Evening" + "sG")
        #speak("I am Sivaji. How can I help You")

# My Command Recognize
def myCommand():
    count = 1
    while (count == 1):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("\nListening...")
            audio = r.listen(source)

        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language='en')
            print(f"Master said : {query}\n")
            break

        except Exception as e:
            speak("Say that again please sG")
            print("\nSay that again please sG")
            #continue
    return query

def myCommand2():
        count = 1
        while (count == 1):
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("""\nNot Ready
     Listening...""")
                audio = r.listen(source)

            try:
                print("Recognizing...")
                query = r.recognize_google(audio, language='en')
                break

            except Exception as e:
                speak("Say that again please sG")
                print("\nSay that again please sG")
                continue
                
        return query

def possible_Reply(query,self):

    while "your" in query.lower() or "you" in query.lower():
        if "yourself" in query.lower() or "self" in query.lower() or "introduce yourself" in query.lower():
            self.compText.set("""Hey! My name is SiVaJi. and I am a assistant of sG master.
            My master have a lot of dream, so my job is to help my master to achieve..... Jai hend""")
            print("""Hey! My name is SiVaJi. and I am a assistant of sG master.
            My master have a lot of dream, so my job is to help my master to achieve..... Jai hend""")
            speak("""Hiiieee! My name is Sivaji. and I am a assistant off sG master.
            My master have a lot of dream, so my job is to help my master to achieve..... Jai hend""")
            break
            
        elif 'age' in query.lower() or 'old' in query.lower():
            self.compText.set("Old enough to use the internet but young enough to learn people")
            print("Old enough to use the internet but young enough to learn people")
            speak("Old enough to use the internet but young enough to learn people")
            break

        elif "nickname" in query.lower():
            self.compText.set("Aiyampettai Arivudainambi Kaliyaperumal Chandran, It's too long. Yaa it's definitely too long. So call me SiVaJi.")
            print("Aiyampettai Arivudainambi Kaliyaperumal Chandran, It's too long. Yaa it's definitely too long. So call me SiVaJi.")
            speak("Aiyampettai Arivudainambi Kaliyaperumal Chandran. It's too long. Yaa it's definitely too long. So call me Sivaji")
            break

        elif "what is your name" in query.lower() or "what's your name" in query.lower() or "tell me your name" in query.lower() or "can I have your good name" in query.lower():
            answer = ['SiVaJi','My name is SiVaJi']
            self.compText.set(random.choice(answer))
            print(random.choice(answer))
            speak(random.choice(answer))
            break

        elif "change your name" in query.lower():
            self.compText.set("no you can't change my name")
            print("no you can't change my name")
            speak("no you can't change my name")
            break

        elif "eat" in query.lower() or 'eaten' in query.lower():
            self.compText.set("Yaa... Today my food is Yummy....")
            print("Yaa... Today my food is Yummy....")
            speak("Yaa... Today my food is Yummy....")
            break
        elif "do you know" in query.lower():
            logical_Thinking(query,self)
            break
        else:
            logical_Thinking(query,self)
            break

    else:
        logical_Thinking(query,self)

def logical_Thinking(query,self):
    client = wolframalpha.Client('Q5GJ4X-EX2HVXPG56')
    try:
        try:
            try:
                res = client.query(query)
                output = next(res.results).text
                self.compText.set(output)
                print(output)
                speak(output)

            except Exception as e:
                print('Searching Wikipedia...')
                speak('Searching Wikipedia...')
                results = wikipedia.summary(query, sentences=2)
                self.compText.set(results)
                print(results)
                speak(results) 
        except:
            webbrowser.open("https://www.google.com/search?hl=en&sxsrf=ALeKk007uz9STtTYlWjeMLJ7RqGZYi3JZw%3A1587212588857&ei=LPGaXuiENOCW4-EP68eC0Ao&q="+query)
            self.compText.set("results for"+query)
            print("results for"+query)
            speak("This Are Some Results")
    except:
        self.compText.set("\nI Apologize sG, I am still learning")
        speak("I Apologize sG, I am still learning")

def faceRecognition():
    print("opening face recognition")

    video_capture = cv2.VideoCapture(0)

    imgMark = face_recognition.load_image_file(
        r'C:\Users\Acer\Desktop\Project Sivaji\Face recognition\Database\Mark\mark.jpg')
    imgMark_encoding = face_recognition.face_encodings(imgMark)[0]

    imgSatiya = face_recognition.load_image_file(
        r'C:\Users\Acer\Desktop\Project Sivaji\Face recognition\Database\Satiyaganes\iMSatiya.jpg')
    imgSatiya_encoding = face_recognition.face_encodings(imgSatiya)[0]

    # Create arrays of known face encodings and their names
    known_face_encodings = [imgMark_encoding, imgSatiya_encoding, ]
    known_face_names = ["Mark", "Satiya"]

    # Initialize some variables
    face_locations = []
    face_encodings = []
    face_names = []
    process_this_frame = True

    i = 0

    while True:
        # Grab a single frame of video
        ret, frame = video_capture.read()

        # Resize frame of video to 1/4 size for faster face recognition processing
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # Convert the image from BGR color (which OpenCV uses) to RGB color (which face_recognition uses)
        rgb_small_frame = small_frame[:, :, ::-1]

        # Only process every other frame of video to save time
        if process_this_frame:
            # Find all the faces and face encodings in the current frame of video
            face_locations = face_recognition.face_locations(rgb_small_frame)
            face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)
            face_list = []
            face_names = []

            for face_encoding in face_encodings:
                # See if the face is a match for the known face(s)
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding, tolerance=0.5)
                name = "Unknown"

                # # If a match was found in known_face_encodings, just use the first one.
                # if True in matches:
                #     first_match_index = matches.index(True)
                #     name = known_face_names[first_match_index]

                # Or instead, use the known face with the smallest distance to the new face
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    face_names.append(name)

        i += 1
        if i == 5:
            curr_name = name
            print(curr_name)
            speak("hey" + curr_name)

        if len(face_names) == 0:
            i = 0

        process_this_frame = not process_this_frame

        # Display the results
        for (top, right, bottom, left), name in zip(face_locations, face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 2
            right *= 2
            bottom *= 2
            left *= 2

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35), (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6), font, 1.0, (255, 255, 255), 1)

        # Display the resulting image
        cv2.imshow('Video', frame)

        # Hit 'q' on the keyboard to quit!
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release handle to the webcam
    video_capture.release()
    cv2.destroyAllWindows()


class Widget:
    def __init__(self):
       root = Tk()
       root.title('SiVaJi..(M.G.R--1)')
       root.config(background='orange')
       root.geometry('365x600')
       root.resizable(0, 0)
       root.iconbitmap(r'C:\Users\Acer\Desktop\Project Sivaji\img\11111_removebg_preview_YAg_icon.ico')
       img = ImageTk.PhotoImage(Image.open(r"C:\Users\Acer\Desktop\Project Sivaji\img\Profile Pic.png"))
       panel = Label(root, image = img)
       panel.pack(side = "bottom", fill = "both", expand = "no")

       self.compText = StringVar()
       self.userText = StringVar()

       self.userText.set('Click \'Start Listening\' to Give commands')

       userFrame = LabelFrame(root, text="sG--Master", font=('Black ops one', 10, 'bold'))
       userFrame.pack(fill="both", expand="yes")
         
       left2 = Message(userFrame, textvariable=self.userText, bg='#4B0082', fg='white')
       left2.config(font=("Comic Sans MS", 10, 'italic'))
       left2.pack(fill='both', expand='yes')

       compFrame = LabelFrame(root, text="SiVaJi", font=('Black ops one', 10, 'bold'))
       compFrame.pack(fill="both", expand="yes")
         
       left1 = Message(compFrame, textvariable=self.compText, bg='#7F00FF',fg='white')
       left1.config(font=("Comic Sans MS", 10, 'italic'))
       left1.pack(fill='both', expand='yes')
       
       button = Button(root, text='Start Listening!', font=('Black ops one', 10, 'bold'), bg='#CD853F', fg='white', command=self.main).pack(fill='x', expand='no')
       button2 = Button(root, text='Close!', font=('Black Ops One', 10, 'bold'), bg='#CD853F', fg='white', command=self.closeProgram).pack(fill='x', expand='no')


       self.compText.set('Initializing Sivaji...')

       root.bind("<Return>", self.main) # handle the enter key event of your keyboard
       root.mainloop()

    def sendEmail(to, content): # (Not working)
        server = smtplib.SMTP('smtp.gmail.com',535)
        server.ehlo()
        server.starttls()
        server.login('navig543@gmail.com', 'navi54321')
        server.sendmail("navig5432@gmail.com", to, content)
        server.close()

    # My Command
    def main(self):
        soundEffect() # Click Sound effect
        query = myCommand()
        self.userText.set('Listening...')
        self.userText.set(query)

        # Logic For executing basic task as per the query
        
        # 1) Wishes
        if 'hello' in query.lower() or 'good morning' in query.lower() or 'good evening' in query.lower() or 'hi' in query.lower() or 'good night' in query.lower():
            speak("Please dont't wish me master, I am your kuutty boy")
            self.compText.set("Please dont't wish me master, I am your kutty boy")
            print("Please dont't wish me master, I am your kutty boy")
        # 2) Online staffs
        elif "according to wikipedia" in query.lower():
            try:
                speak('Searching Wikipedia...')
                print('Searching Wikipedia...')
                query = query.replace("according to wikipedia", "")
                results = wikipedia.summary(query, sentences=2)
                self.compText.set(results)
                print(results)
                speak(results)
            except:
                self.compText.set("\nI Apologize sG, I am still learning")
                speak("I Apologize sG, I am still learning")
            
            # Google
        elif 'open google' in query.lower() or 'open chrome' in query.lower():  
            url = 'google.com'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('google.com')
        elif 'search about' in query.lower():
            query = query.replace("searching about", "")
            webbrowser.open("https://www.google.com/search?hl=en&sxsrf=ALeKk007uz9STtTYlWjeMLJ7RqGZYi3JZw%3A1587212588857&ei=LPGaXuiENOCW4-EP68eC0Ao&q="+query)
            self.compText.set("results for"+query)
            print("results for"+query)
            speak("This Are Some Results")

            # Youtube
        elif 'open youtube' in query.lower():
            url = 'youtube.com'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('youtube.com')
        elif 'in google' in query.lower() or 'in Google' in query:
            webbrowser.open("https://www.google.com/search?hl=en&sxsrf=ALeKk007uz9STtTYlWjeMLJ7RqGZYi3JZw%3A1587212588857&ei=LPGaXuiENOCW4-EP68eC0Ao&q="+query)
            self.compText.set("results for" +query)
            print("results for" +query)
            speak("This Are Some Results")
        elif 'in youtube' in query.lower():
            query = query.replace("in YouTube", "")
            webbrowser.open("https://www.youtube.com/results?search_query="+query)
            self.compText.set("results for"+query)
            print("results for"+query)
            speak("This Are Some Results")
        elif 'in maps' in query.lower():
            query = query.replace("in maps", "")
            webbrowser.open("https://www.google.com.my/maps/place/"+query)
            self.compText.set("results for"+query)
            print("results for"+query)
            speak("This is the Place")
    
            # Kalam UMP
        elif 'open elearning' in query.lower() or 'open kalam' in query.lower():
            url = 'https://kalam.ump.edu.my/login'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('https://kalam.ump.edu.my/login')

            #ecom
        elif 'ecom' in query.lower() or 'e com' in query.lower() or 'e-com' in query.lower():
            url = 'http://www.ump.edu.my/'
            chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
            webbrowser.get(chrome_path).open('http://www.ump.edu.my/')
        elif 'open translator' in query.lower():
            
            def myCommand3():
                count = 1
                while (count == 1):
                    r = sr.Recognizer()
                    with sr.Microphone() as source:
                        print("\nListening...")
                        audio = r.listen(source)

                    try:
                        print("Recognizing...")
                        query2 = r.recognize_google(audio, language='en')
                        print(f"Master said : {query2}\n")
                        break

                    except Exception as e:
                        speak("Say that again please sG")
                        print("\nSay that again please sG")
                        continue
                return query2
            
            import tkinter as tk
            from googletrans import Translator
            
            count = 1
            while (count==1):
                print("Translate English To .........")
                query2=myCommand3()
                if 'malay' in query2.lower():
                    win = tk.Tk()
                    win.title("Translator")
                    win.geometry("300x120")

                    def translator():
                        word = entry.get()
                        translator = Translator(service_urls=["translate.google.com"])
                        translation = translator.translate(word,dest="ms")
                        label1 = tk.Label(win, text=f'Translated word : {translation.text}', bg='orange')
                        label1.grid(row=2,column=2)

                    label = tk.Label(win,text="Write Here : ")
                    label.grid(row=0,column=2)

                    entry = tk.Entry(win)
                    entry.grid(row=1,column=2)

                    button = tk.Button(win,text="Go",command=translator)
                    button.grid(row=1,column=3)

                    win.mainloop()
                    break
                elif 'Tamil' in query2:
                    win = tk.Tk()
                    win.title("Translator")
                    win.geometry("300x120")

                    def translator():
                        word = entry.get()
                        translator = Translator(service_urls=["translate.google.com"])
                        translation = translator.translate(word,dest="ta")
                        label1 = tk.Label(win, text=f'Translated word : {translation.text}', bg='orange')
                        label1.grid(row=2,column=2)

                    label = tk.Label(win,text="Write Here : ")
                    label.grid(row=0,column=2)

                    entry = tk.Entry(win)
                    entry.grid(row=1,column=2)

                    button = tk.Button(win,text="Go",command=translator)
                    button.grid(row=1,column=3)
                    win.mainloop()
                    break
                else:
                    continue

        # 3) My computer folders and Apps
        elif 'play some song' in query.lower() or 'play song' in query.lower():
            song_dir = "C:\\Users\\Acer\\Music"
            songs = os.listdir(song_dir)
            self.compText.set(songs)
            print(songs)
            os.startfile(os.path.join(song_dir,songs[0]))
        elif 'play some movie' in query.lower():  # Not Working. Plz Update !!!
            movie_dir = "C:\\Users\\Acer\\Downloads\\Telegram Desktop"
            songs = os.listdir(movie_dir)
            self.compText.set(movies)
            os.startfile(os.path.join(movie_dir,movies[0]))
            
            # Current Time
        elif 'the time' in query.lower():
            import datetime
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sG the time is {strTime}")
            print(f"sG the time is {strTime}")
            self.compText.set(f"sG the time is {strTime}")
        elif 'the date' in query.lower():
            
            from datetime import datetime
            current_Date = datetime.now().day
            current_Month = datetime.now().month
            current_Year = datetime.now().year
            speak(f"sG the date is {current_Date} {current_Month} {current_Year}")
            print(f"sG the date is {current_Date}/{current_Month}/{current_Year}")
            self.compText.set(f"sG the date is {current_Date}/{current_Month}/{current_Year}")

            # Current Whatsapp
        elif 'open whatsapp' in query.lower():
            whatsappPath = "C:\\Users\\Acer\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(whatsappPath)

            # CodeBlock
        elif 'open code block' in query.lower():
            codeBlockPath = "C:\\Program Files (x86)\\CodeBlocks\\codeblocks.exe"
            os.startfile(codeBlockPath)

            # illustrator
        elif 'open illustrator' in query.lower():
            aIPath = "C:\\Program Files\\Adobe\\Adobe Illustrator CC 2017\\Support Files\\Contents\\Windows\\Illustrator.exe"
            os.startfile(aIPath)

            #Telegram
        elif 'open telegram' in query.lower():
            telegramPath = "C:\\Users\\Acer\\AppData\\Roaming\\Telegram Desktop\\Telegram.exe"
            os.startfile(telegramPath)

            # pycharm
        elif 'open pycharm' in query.lower():
            pyCharmPath = "C:\\Program Files\\JetBrains\\PyCharm Community Edition 2019.3.4\\bin\\pycharm64.exe"
            os.startfile(pyCharmPath)

            # My Notes
        elif 'open notes' in query.lower():
            notesPath = "C:\\Users\\Acer\\Desktop\\Sem 2 Notes"
            os.startfile(notesPath)
        elif 'open visual' in query.lower():
            visualPath = "C:\\Users\\Acer\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(visualPath)
        elif 'open calculator' in query.lower():
            CalcPath = "C:\\Users\\Acer\\Desktop\\Project Sivaji\\img\\Calculator.lnk"
            os.startfile(CalcPath)
        elif 'open words' in query.lower():
            WordPath = "C:\\Users\\Acer\\Desktop\\Word"
            os.startfile(WordPath)
        elif 'find me' in query.lower():
            faceRecognition()
            self.compText.set("\nThank You sG")
            print("\nThank You sG")
            speak("Thank You sG")
        elif 'news' in query.lower():
            import feedparser

            print("Searching for News")
            def parseRSS(rss_url):
                return feedparser.parse(rss_url)

            def getHeadlines(rss_url):
                headlines = []

                feed = parseRSS(rss_url)
                for newsitem in feed['items']:
                    headlines.append(newsitem['title'])

                return headlines

            allheadlines = []

            newsurls = {

                'googlenews': 'https://news.google.com/news/rss/?hl=en&amp;ned=us&amp;gl=US',

            }

            for key, url in newsurls.items():
                allheadlines.extend(getHeadlines(url))

            for (hl) in allheadlines:
                print(hl)
                self.compText.set(hl)

        elif 'shut down' in query.lower():
            speak("Say Yes or No to confirm sG")
            query = myCommand()
            if (query=='Yes' or 'yes'):
                self.compText.set('okay')
                speak('okay')
                os.system('shutdown -s')
            else:
                print("Ok it's better to shutdown manually sG")
                speak("Ok it's better to shutdown manually sG")
                self.compText.set("Ok it's better to shutdown manually sG")

        elif 'send email to satya' in query.lower() or 'send email to satiya' in query.lower(): # Not Working Well
            try:
                speak("What Should i Send")
                content = myCommand()
                to = "satiyaganes.sg@gmail.com"
                sendEmail(to, content)
                speak("Email has been sent Successfully !!!")
            except Exception as e:
                self.compText.set(e)
        elif "close program" in query.lower() or 'end program' in query.lower():
            self.compText.set("\nThank You sG")
            print("\nThank You sG")
            speak("........Thank You sG.......")
            quit()  
        else: 
            possible_Reply(query,self)
        return query

    # tomorrow whatsapp and email and telegram message. XXXXXX
    # when i am said shut down. Open a specific file....

    def closeProgram(self):
        self.compText.set("\nThank You sG")
        print("\nThank You sG")
        speak("........Thank You sG.......")
        quit()


    #def loopRun():
        
        query = myCommand2()
        while (query == "hey"):
            self.compText.set("Initializing Sivaji...")
            speak("Initializing Sivaji...")
            wishMe()
            
            count=1
            while (count==1):
                # G.U.I
            
                

                speak("...Ready...")
                print("\nsay something")
                main()
                continue
        else:
            closeProgram()


    #loopRun()

if __name__ == '__main__':
    print('Initializing SiVaJi...')
    speak('Initializing Sivaji...')
    wishMe()
    widget = Widget() 

