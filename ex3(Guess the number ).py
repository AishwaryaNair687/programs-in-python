n=18
number_of_guesses=1

print("number of guesses is limited to 9")
while(number_of_guesses<=9):

    n1 = int(input("guess the number "))

    if n1>18:
            print("the number is too high please guess else smaller than this numb er")
    elif n1<18:
             print("you have guessed a smaller number please guess number greater than this")


    else:
            print("you won ")

            break
    print(number_of_guesses ,"number of guesses he took to finish the task")




print(9-number_of_guesses,"number of gusses left")
number_of_guesses= number_of_guesses+1

if(number_of_guesses>9):
      print("game over")

