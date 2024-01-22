def zombie_adventure():
    print("Bienvenue dans l'aventure de survie zombie !")
    print("Vous êtes dans une école infestée de zombies. Deux couloirs s'offrent à vous.")
    print("1. Explorer le couloir de gauche")
    print("2. Courir vers le couloir de droite")

    choice = input("Quel couloir choisissez-vous ? (1/2) : ")

    if choice == "1":
        print("Vous trouvez une salle de classe sécurisée avec des provisions.")
        print("Vous entendez du bruit. Voulez-vous enquêter ?")
        print("1. Enquêter sur le bruit")
        print("2. Rester caché et silencieux")
        second_choice = input("Votre choix ? (1/2) : ")
        if second_choice == "1":
            print("C'était un autre survivant ! Vous avez maintenant un allié.")
        elif second_choice == "2":
            print("Vous restez en sécurité mais seul. La survie continue.")
        else:
            print("Choix non valide. Les zombies vous surprennent. Fin de l'aventure.")
    elif choice == "2":
        print("Malheureusement, vous tombez sur un groupe de zombies ! Fin de l'aventure.")
    else:
        print("Choix non valide. Les zombies vous attrapent. Fin de l'aventure.")

    print("Merci d'avoir joué !")

# Lancer le jeu
zombie_adventure()
