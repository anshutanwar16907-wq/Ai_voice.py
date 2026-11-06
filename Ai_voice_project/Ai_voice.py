import os
from google import genai
from gtts import gTTS

client=genai.Client()

question= input("-----ASK WHAT YOU WANT TO LISTEN-----")
lang= input("-----Audio language (en/hi)-----")

if question == "":
    print("-----WRITE SOMETHING HERE-----")
elif lang != "en" and lang != "hi":
    print("-----ASK ONLY IN HINDI OR ENGLISH-----")
else:
    if lang== "hi":
        instruction= "---GIVE ANSWER IN HINDI LANGUAGE, SIMPLE TEXT, WITHOUT SYMBOLES "
    else:
        instruction= "---GIVE ANSWER IN ENGLISH ;ANGUAGE, SIMPLE TEXT, WITHOUT SYMBOLS"
    response=client.models.generate_content(
        model="gemini-3.6-flash",
        contents=question + ("-----ASK SOMETHING , SIMPLE TEXT , WITHOUT SYMBOLS")
    )

    answer= response.text
    print("AI",answer)

    tts=gTTS(text=answer , lang=lang)
    tts.save("replt.mp3")
    os.startfile("reply.mp3")

    try:
        os.startfile("reply.mp3")
    except Exception as e:
        print("-----AUDIO NOT PLAY ITSELF , OPEN REPLY.MP3 PLEASE----- ")

