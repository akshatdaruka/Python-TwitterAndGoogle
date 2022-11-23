g=input("Type a language (hindi/espanol/french/english):")
def greet(lang):
    if lang=='hindi':
        return "namaste"
    elif lang=='espanol':
        return "hola"
    elif lang=='french':
        return "bonjour"
    elif lang=='english' :
        return "hello"
    else:
        print("enter a language from the given option please")
        quit()
print(greet(g),"you have chosen the language",g)
