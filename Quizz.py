quiz = {


    "Quel symbole utilise-t-on pour une condition “égal à” en Python ?": "==",


    "Combien font 12 x 12 ?": "144",


    "Quelle particule possède une charge négative ?": "l’électron",


    "Quelle est la formule de l’eau ?": "H2O",


    "Quelle est la dérivée de cos(x) ?": "-sin(x)",

  
    "Quel est le déterminant d’une matrice 2×2 ?": "ad−bc",


}

 

score = 0

 

print("Bienvenue dans le Quiz ! ")

 

for question, bonne_reponse in quiz.items():


    reponse_utilisateur = input(f"{question} ").strip().lower()


   


    if reponse_utilisateur == bonne_reponse:


        print("Bonne réponse !\n")


        score += 1


    else:


        print(f"Mauvaise réponse. La bonne réponse était : {bonne_reponse}\n")

 

print(f"Quiz terminé ! Votre score est de {score} / {len(quiz)}")
