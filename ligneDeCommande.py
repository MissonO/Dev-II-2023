import random
import string


# Fonction qui génère un mot de passe aléatoire
# en fonction des paramètres donnés
def generate_password(length, uppercase, digits, special_chars):
    chars = string.ascii_lowercase
    if uppercase:
        chars += string.ascii_uppercase
    if digits:
        chars += string.digits
    if special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password


# Fonction qui enregistre un mot de passe dans un fichier
def save_password(username, password):
    with open("passwords.txt", "a") as file:
        file.write(f"{username}: {password}\n")
    print(f"Mot de passe enregistré pour {username}.")


# Fonction qui affiche les mots de passe enregistrés
def view_saved_passwords():
    try:
        with open("passwords.txt", "r") as file:
            passwords = file.read()
            if passwords:
                print("Mots de passe enregistrés :")
                print(passwords)
            else:
                print("Aucun mot de passe enregistré.")
    except FileNotFoundError:
        print("Aucun mot de passe enregistré.")


def delete_saved_password():
    try:
        with open("passwords.txt", "r") as file:
            passwords = file.read()
            if passwords:
                print("Mots de passe enregistrés :")
                print(passwords)
            else:
                print("Aucun mot de passe enregistré.")
    except FileNotFoundError:
        print("Aucun mot de passe enregistré.")
        return

    where = input("Quel mot de passe voulez-vous supprimer ?")
    if where in passwords:
        passwords = passwords.replace(where, "")
        with open("passwords.txt", "w") as file:
            file.write(passwords)
    else:
        print("Ce mot de passe n'existe pas.")


# Fonction principale d'interaction avec l'utilisateur
def main():
    print("Générateur de mots de passe aléatoires")

    # Demander les paramètres de génération du mot de passe
    # Attention la valeur pour oui doit être exactement 'oui'
    length = int(input("Longueur du mot de passe : "))
    uppercase = input("Inclure des majuscules ? (oui/non) ").lower() == 'oui'
    digits = input("Inclure des chiffres ? (oui/non) ").lower() == 'oui'
    special_chars = input(
        "Inclure des caractères spéciaux ? (oui/non) "
    ).lower() == 'oui'

    password = generate_password(length, uppercase, digits, special_chars)

    print("\nMot de passe généré :")
    print(password)

    save_option = input(
        "Voulez-vous enregistrer ce mot de passe ? (oui/non)"
    ).lower()
    if save_option == 'oui':
        username = input("Nom d'utilisateur : ")
        save_password(username, password)

    view_saved_option = input(
        "Voulez-vous voir les mots de passe enregistrés ? (oui/non) "
    ).lower()
    if view_saved_option == 'oui':
        view_saved_passwords()
    view_saved_option = input(
        "Voulez-vous supprimer un mot de passe ? (oui/non) "
    ).lower()
    if view_saved_option == 'oui':
        delete_saved_password()


if __name__ == "__main__":
    main()
