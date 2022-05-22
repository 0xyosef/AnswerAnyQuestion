import wikipedia
import pyttsx3

subjectNumber = 0
while True:
    x = input("what is Question?")
    print(wikipedia.summary(x, sentences=2))
    s = pyttsx3.init()
    s.say(wikipedia.summary(x, sentences=2))
    s.runAndWait()
    if x == 'q':
        exit(0)

    r = wikipedia.search(x)
    chose = 0
    for i in r:
        print(chose, ".....", i)
        chose += 1
    s.say("Enter subject number")
    s.runAndWait()
    subjectNumber = int(input("Enter subject number:"))
    page = wikipedia.page(r[subjectNumber])

    print(page.title)
    print('-----------------')
    print(page.summary)
    # s.say(page.summary)
    # s.runAndWait()
    more = int(input("see more press 1:"))
    print('-----------------')
    print(page.content)
