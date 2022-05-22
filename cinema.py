#"film name":[minimum age to enter, number of tickets]
films = {
    "Ponyo":[3,5],
    "Terminator":[18,3],
    "Avengers":[13,1],
    "Alien":[18,5],
    "Inception":[13,0]
}

while True:
    
    print("Welcome to the Theater!")
    choice = input("What film will you be seeing?:").strip().title()
    
    if choice in films:
        
        age = int(input("How old are you?:").strip())
        
        #checks user age and if any tickets left
        if age >= films[choice][0] and films[choice][1]>0:
            print("Enjoy the movie!")
            films[choice][1] =  films[choice][1] - 1
        elif age < films[choice][0]:
            print("Sorry, you're too young to see this movie!")
         #checks in enouoch seats   
        elif films[choice][1] == 0:
            print("Sorry, this movie is sold out.")
    else:
        print("That film isn't currently showing.")
