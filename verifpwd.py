
def initialisation(password) : #Fonction qui va passer en revue le mot de passe donné.

    numbers = 0
    
    for i in range(len(password)) : #On compte le nombre de chiffres dans le mot de passe.
        
        if password[i].isnumeric():
            
            numbers = numbers + 1

    if numbers < 3 : #Si il y a moins de 3 chiffres dans le mot de passe, alors il est invalide.                                                                                             

        print("\nVotre mot de passe doit contenir au moins 3 chiffres. Veuillez reessayer.\n")
        inputpw()

    elif len(password) <= 4 : #Si le mot de passe fait moins de 4 charactères, alors il est invalide.
        
        print("\nVotre mot de passe est trop court. Veuillez reessayer.\n")
        inputpw()
        
    elif len(password) > 10 : #Si le mot de passe fait plus de 10 charactères, alors il est invalide.
        
        print("\nVotre mot de passe est trop long. Veuillez reessayer.\n")
        inputpw()
    
    elif numbers < 3 : #Si il y a moins de 3 chiffres dans le mot de passe, alors il est invalide.
        
        print("\nVotre mot de passe doit contenir au moins 3 chiffres. Veuillez reessayer.\n")
        inputpw()
    
def verification(password) : #Fonction qui va comparer le mot de passe initialement donné avec sa confirmation.
    
    passwordcpy = str(input("Veuillez confirmer votre mot de passe : "))
    error_counter = 0
    len_error = 0
    tries = 3
    is_pwd_good = 0
    
    while tries != 0 : #On crée une boucle tant qu'il reste des essais.

        if len(password) != len(passwordcpy) : #On compare d'abord la taille des deux chaines de caractères.

            len_error = len_error + 1
            error_counter = error_counter + 1

        if len_error == 0 :
            
            for i in range(len(password)) : #On vérifie caractère par caractère si les deux passwords sont identiques.
            
                if passwordcpy[i] != password[i] :
                
                    error_counter = error_counter + 1
    
        if error_counter == 0 : #Si les passwords sont identiques, alors on sort de la fonction.

            print("\nLes deux passwords sont identiques.\n")
            print("\nLe mot de passe a pu être vérifié.")
            is_pwd_good = 42
            return

        if error_counter != 0 : #Si les passwords ne sont pas identiques, alors on repète l'opération.                                                                                        
            print("\nLes deux passwords ne sont pas identiques : veuillez réessayer. Il vous reste", tries,"essais\n")
            passwordcpy = str(input("Veuillez confirmer votre mot de passe : "))
            len_error =	0
            error_counter = 0
            tries = tries - 1

    #Si la fonction sort de la boucle, alors le mot de passe n'est pas vérifié.
    print("\nVous avez mal rentré votre mot de passe trop de fois. Essai aborté.\n")
    print("\nLe mot de passe n'a pas pu être vérifié.\n")
    return

        
def inputpw() : #Fonction qui va permettre de renter un mot de passe.
    
    password = str(input("Veuillez inserer votre mot de passe : "))
    
    initialisation(password)
    verification(password)
    
def main() :
    
    print("\nBienvenue dans l'interface de verification de mot de passe !\n")
    inputpw()

main()
