import qcm
from difficulty import quoting, set_difficulty

if __name__ == '__main__':
    filename = "./QCM.txt"
    print("Bienvenue sur le QCM de projet 2 !")
    user = (input("Choissisez votre nom d'utilisateur C> "))
    print(f"Bonjour {user}")
    difficulty_choice = ""
    while difficulty_choice == "" or difficulty_choice not in ["sympa", "severe", "mystere"]:
        print("Vous devez choisir un niveau existant !")
        difficulty_choice = input("Sélectionné un niveau de difficulté (sympa/severe/mystere) C> ")
    diff = set_difficulty(difficulty_choice)

    print("\n\n") #passement de ligne
    # Chargement du questionnaire
    questions = qcm.build_questionnaire(filename)
    print("Lecture du questionnaire.")
    quotes = []
    #modifié aléatoirement l'ordre des questions
    for q in range(len(questions)):
        print("\tQ| " + str(q + 1) + ": \"" + questions[q][0] + "\"")
        for r in range(len(questions[q][1])):
            print("\t\tA|" + str(r + 1) + ":" + f"\t{questions[q][1][r][0]}""")
        while True:
            answer = int(input(f"{user} C> "))
            if 1 <= answer <= len(questions[q][1]):
                if questions[q][1][answer-1][1]:
                    print("Bonne réponse !")
                else:
                    print("Mauvaise réponse")
                if questions[q][1][answer - 1][2] != "":
                    print("Feedback: \"" + questions[q][1][answer - 1][2] + "\"")
                quotes.append(quoting(questions[q][1][answer-1][1], q+1, diff)) #Renvoi true ou false
                break
            else:
                if answer == -1:
                    if diff == 1:
                        quotes.append(0)
                    elif diff == 2:
                        quotes.append(-1)
                    break
                print("Cette réponse n'est pas disponible, si vous ne voulez pas répondre tapez -1")
                continue
    print(f"Notes total : {quotes}")
