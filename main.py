import qcm
from difficulty import quoting

if __name__ == '__main__':
    filename = "./QCM.txt"
    print("Bienvenue sur le QCM de projet 2 !")
    """
    user = (input("Choissisez votre nom d'utilisateur C> "))
    print(f"Bonjour {user}")
    difficulty_choice = ""
    while difficulty_choice == "" or difficulty_choice not in ["sympa", "severe", "mystere"]:
        print("Vous devez choisir un niveau existant !")
        difficulty_choice = input("Sélectionné un niveau de difficulté (sympa/severe/mystere) C> ")
    """
    #temp
    user = "Damien"
    print("\n\n") #passement de ligne
    # Chargement du questionnaire
    questions = qcm.build_questionnaire(filename)
    print("Lecture du questionnaire.")
    for q in range(len(questions)):
        print("\tQuestion " + str(q + 1) + ": \"" + questions[q][0] + "\"")
        print("\tPropositions de réponses")
        for r in range(len(questions[q][1])):
            print("\t\tReponses " + str(r + 1) + ":")
            print("\t\t\tMessage: \"" + questions[q][1][r][0] + "\"")
        while True:
            answer = int(input(f"{user} C> "))
            if 1 <= answer <= len(questions[q][1]):
                quoting(questions[q][1][answer-1][1], 1, 1) #Renvoi true ou false
                if questions[q][1][answer-1][1]:
                    print("Bonne réponse !")
                    if questions[q][1][answer-1][2] != "":
                        print("\t\t\tFeedback: \"" + questions[q][1][answer-1][2] + "\"")
                else:
                    print("Mauvaise réponse")
                    if questions[q][1][answer-1][2] != "":
                        print("Feedback: \"" + questions[q][1][answer-1][2] + "\"")
                break
            else:
                continue

