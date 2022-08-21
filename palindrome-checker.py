print("Welcome!")

#keep program running until user wants to exit
while(str != "exit"):
    #convert string to lowercase
    str = input("Enter the string you want to check or enter \"exit\" to exit the program: ").lower()

    #declare new variable to store clean string
    newstr = ""
    
    #strips away punctuation and stores clean string
    for x in str:
        if (x.isalnum()):
            newstr += x

    #checks if it is palindrome or if user wants to exit program
    if (newstr == "exit"):
        print("Exiting Program")
    elif (newstr == newstr[::-1]):
        print("The string is a palindrome")
    else:
        print("It is not a palindrome")
