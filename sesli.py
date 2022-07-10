import speech_recognition as sr
import random
import playsound
import os
from gtts import gTTS
import webbrowser
import time
from datetime import datetime
import wikipedia
import feedparser
import pyautogui as auto
# from random import choice

wikipedia.set_lang("tr")

r = sr.Recognizer()

nasilsinkelimeleri = ["nasılsın", "naber", "ne haber", "ne yapıyorsun", "napıyorsun"]
iyidonus = ["iyiyim", "çok iyiyim", "harikayım", "sağ ol iyiyim"]
iyicevap = ["", "duyduğuma sevindim", "çok sevindim"]
kotudonus = ["kötüyüm", "mutlu değilim", "kendimi kötü hissediyorum"]
kotucevap = ["" ,"duyduğuma üzüldüm", "umarım daha mutlu olursun"]


def record_audio(ask=""):
    with sr.Microphone() as source:
        
        r.adjust_for_ambient_noise(source)
        audio =r.listen(source)
        if(ask):
            speak(ask)
        voice_data=""
  
    try:
        voice_data=r.recognize_google(audio, language="tr-tr")
        voice_data= voice_data.lower()
        print("Sedat: "+voice_data)
    except sr.UnknownValueError:
        print("Sesli Asistan: Üzgünüm Ne Dediğini Anlamadım")
        
    except sr.RequestError:
        print("Sesli Asistan: Sistem Çalışmayı Durdurdu")
        
    return voice_data


def speak(audio_string):
    tts= gTTS(text= audio_string, lang="tr")
    r= random.randint(1,10000)
    audio_file = "audio" + str(r) + ".mp3"
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print("Sesli Asistan: "+audio_string)
    os.remove(audio_file)
    
    
    
def respond(voice_data):
    
    if "merhaba" in voice_data:
        
        speak("merhaba Sedat")
        
    if voice_data in nasilsinkelimeleri:
        
        speak("iyiyim, siz nasılsınız")
        
    if voice_data in iyidonus:
        
        speak(iyicevap[random.randint(1, 2)])
       
    if voice_data in kotudonus:
        
        speak(kotucevap[random.randint(1, 2)])
        
    
        
    if "haberler" in voice_data:
        
        speak("Günlük Haberler listelendi")
        url="https://www.cnnturk.com/feed/rss/news"
        haberler=feedparser.parse(url)
        
        i=0
        for x in haberler.entries:
            i+=1
            print(i,". Haber")
            print(str(x.title))
            print(str(x.link))
            print(str(x.description))
            
            
    if "hava durumu" in voice_data:
        
        parse = feedparser.parse("http://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|06420|ANKARA|")
        parse = parse["entries"][0]["summary"]
        parse = parse.split()
        speak("Ankara'da hava şuan "+ parse[4] +" derece")
        print (parse[2], parse[4], parse[5])
           
    
        
    if "mail" in voice_data.split():
        
        url="https://mail.google.com/mail/u/0/?pli=1#inbox?compose=new"
        webbrowser.get().open(url)
        time.sleep(2.5)
     
             
    if "saat kaç" in voice_data:
        selection =["saat şuan: " , "hemen bakıyorum: "]
        clock=datetime.now().strftime("%H:%M:%S")
        selection= random.choice(selection)
        speak(selection + clock)
         
    if "hangi gündeyiz" in voice_data:
        today= time.strftime("%A")
        today.capitalize()
        
        if today == "Monday":
            today="Pazartesi"
        elif today== "Tuesday":
            today="Salı"
        elif today== "Wednesday":
            today="Çarşamba"
        elif today== "Thursday":
            today="Perşembe"
        elif today== "Friday":
            today="Cuma"
        elif today== "Saturday":
            today="Cumartesi"
        elif today== "Sunday":
            today="Pazar"
        
        speak(today)
        
        
        
    if "hangi aydayız" in voice_data:
        today= time.strftime("%B")
        today.capitalize()
        
        if today == "January":
            today="Ocak"
        elif today== "February":
            today="Şubat"
        elif today== "March":
            today="Mart"
        elif today== "April":
            today="Nisan"
        elif today== "May":
            today="Mayıs"
        elif today== "June":
            today="Haziran"
        elif today== "July":
            today="Temmuz"
        elif today== "August":
            today="Ağustos"
        elif today== "September":
            today="Eylül"
        elif today== "October":
            today="Ekim"
        elif today== "November":
            today="Kasım"
        elif today== "December":
            today="Aralık"
        
        speak(today)
        
        
    if "hangi yıldayız" in voice_data:
        today= time.strftime("%Y")
        
        speak(today)
        
        
    if "kapat" in voice_data:
        speak("Program Kapanıyor")
        exit()
               
def who(voice_data):
    if "kimdir" in voice_data.split():
        
        voice_data=voice_data.split()
        kisiismi=""
        
        for i in voice_data[:-1]:
            kisiismi = kisiismi + " " +i
            wiki = wikipedia.summary(kisiismi, sentences=1)
        
        url="https://www.google.com/search?q="+kisiismi
        webbrowser.get().open(url)
        speak(wiki)
        
    
def search(voice_data):
    if "nedir" in voice_data.split():
        
        voice_data=voice_data.split()
        kelime=""
        
        for i in voice_data[:-1]:
            kelime = kelime + " " +i
        
        url="https://www.google.com/search?q="+kelime
        webbrowser.get().open(url)
        
        
def play(voice_data):
    if "çal" in voice_data.split():
        
        voice_data=voice_data.split()
        music=""
        
        for i in voice_data[:-1]:
            music = music + " " +i
        
        url="https://www.youtube.com/results?search_query="+music
        webbrowser.get().open(url)
        time.sleep(2.5)
        auto.click(950, 320)
        
def where(voice_data):
    if "nerede" in voice_data.split():
        
        voice_data=voice_data.split()
        lokasyon=""
        
        for i in voice_data[:-1]:
            lokasyon = lokasyon + " " +i
        
        url="https://www.google.com/maps/place/"+lokasyon
        webbrowser.get().open(url)

    
def greeting():
        hour = datetime.now().hour
        if(hour>=6 and hour<12):
            speak("Günaydın ")
        if(hour>=12 and hour<18):
            speak("Tünaydın ")
        if(hour>=18 and hour<22):
           speak("İyi Akşamlar")
        if(hour>=22 and hour<6):
           speak("İyi Geceler ")
            
        
greeting()
speak("Nasıl Yardımcı Olabilirim")

while 1:
    voice_data = record_audio()
    respond(voice_data)
    search(voice_data)
    who(voice_data)
    play(voice_data)
    where(voice_data)
   
        