import pyttsx3
import PyPDF2

try:
    book = input('Enter Your Book Or Pdf name with extension(.pdf):')
    which=int(input('Enter The page no.:'))
    book = open(book,'rb')
    pdfreader = PyPDF2.PdfFileReader(book)
    pages = pdfreader.numPages

    if which > pages:
        exit('\nPage limit exceed')
    speaker = pyttsx3.init()
    speaker.setProperty("rate", 178)
    for num in range(which-1,pages):
        page = pdfreader.getPage(num)
        text = page.extractText()
        speaker.say(text)
        speaker.runAndWait()
except FileNotFoundError:
    print('NO DIRECTERY FOUND')
except ValueError as enum:
    print(enum,'This is not the int value')
    
