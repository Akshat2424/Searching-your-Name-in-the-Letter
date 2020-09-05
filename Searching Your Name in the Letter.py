def searcher():
    letter1="Riya"
    letter2="Rahul"
    letter3="Vaishanavi"
    letter4="Aditya"
    letter5="Shweta"
    letter6="Hadeeqa"
    letter7="Rehan"
    letter8="Sunderam"
    letter9="Aman"
    letter10="Astra"

    while True:
        text=(yield)
        if text in [letter1,letter2,letter3,letter4,letter5,letter6,letter7,letter8,letter9,letter10]:
            print("Your name is in the letter")
        else:
            print("sorry your name is not in any letter")
search=searcher()
next(search)
a=input("Enter your name")
search.send(a)