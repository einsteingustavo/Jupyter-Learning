import random


while (True):
    print ("\n")
    print ("Rock, Paper, Scissors - Shoot!")
    user = input("Choose your weapon [R]ock], [P]aper, or [S]cissors: ").upper()[0]

    if user not in "SRP":
        print("Please choose a letter:")
        print("[R]ock, [S]cissors or [P]aper.")
        continue

    print ("You chose: " + user)

    opponent = random.choice("RPS")

    print ("I chose: " + opponent)

    #
    # Modifique o código abaixo de modo a também informar o resultado
    # detalhado quando você vence.  Depois, compare com a outra versão
    # que o professor irá disponibilizar.
    #
    if opponent == user:
        print ("Tie! ")
    elif opponent == 'R' and user == 'S':
        print ("Rock beats Scissors, I win! ")
    elif opponent == 'S' and user == 'P':
        print ("Scissors beats paper! I win! ")
    elif opponent == 'P' and user == 'R':
        print ("Paper beat rock, I win!")
    else:
        print ("You win!")
