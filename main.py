#! /usr/bin/env python

import speech_recognition as sr
import argparse


r = sr.Recognizer()

# def Arguments():
#     parser = argparse.ArgumentParser(description="Converts WAV in to txt.\n"
#                                                  "Example use:\n"
#                                                  "main.py example.wav")
#     #Argument for the languague of the audiofile
#     parser.add_argument("-de", action="store_true" ,help="Sets the languague to German", required=False )
#     #Filename argument
#     parser.add_argument('filename', help="Filename of the Converting File" )
#
#     args = parser.parse_args()
#
#     return args.filename


#Converts Audio in to Text

def startConvertion(path, lang):
    with sr.AudioFile(path) as source:
        print('Fetching File')
        audio_text = r.listen(source)
        # recoginize_() method will throw a request error if the API is unreachable, hence using exception handling
        try:

            # using google speech recognition
            print('Converting audio transcripts into text ...')
            text = r.recognize_google(audio_text, language= lang)
            return text

        except:
            print('Sorry.. run again...')


if __name__ == '__main__':

    parser = argparse.ArgumentParser(description="Converts WAV in to txt.\n"
                                                     "Example use:\n"
                                                     "main.py example.wav")
    #Argument for the languague of the audiofile
    parser.add_argument("-de", action="store_true" ,help="Sets the languague to German", required=False )
    #Filename argument
    parser.add_argument('filename', help="Filename of the Converting File" )

    args = parser.parse_args()


    if args.de:
       language = "de-DE"



    else:
        language = "en-UK"

    file = args.filename
    print(file[:-3])

    with open(file[:-3] + "txt", 'w') as f:
        f.write(startConvertion(file, language))



