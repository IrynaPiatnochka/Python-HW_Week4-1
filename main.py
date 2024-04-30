
import moody

def moody_x():
    while True:
        mood = input("How are you feeling today? ")
        print(moody.mood_response(mood))
        break

moody_x()
    