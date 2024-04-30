
def mood_response(mood):
    
    while True:
        if mood == "happy":
            return "Glad to hear that!"
        elif mood == "sad":
            return "I am sorry! Let me know if I can help you with anything."
        elif mood == "okay":
            return "Hope tomorrow is going to be a better day for you!"
        else:
            return "Invalid input."
            
            break
            
     
          
