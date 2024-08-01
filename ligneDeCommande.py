import random
import string
import argparse


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


# Fonction pour supprimer un mot de passe enregistré
def delete_saved_password():
    try:
        with open("passwords.txt", "r") as file:
            lines = file.readlines()
            if not lines:
                print("Aucun mot de passe enregistré.")
                return
            else:
                print("Mots de passe enregistrés :")
                print(''.join(lines))
    except FileNotFoundError:
        print("Aucun mot de passe enregistré.")
        return

    where = input("Quel mot de passe voulez-vous supprimer ?")
    new_lines = []
    found = False

    for line in lines:
        if line.strip().endswith(where):
            found = True
        else:
            new_lines.append(line)

    if not found:
        print("Ce mot de passe n'existe pas.")
    else:
        with open("passwords.txt", "w") as file:
            file.writelines(new_lines)
        print(f"Mot de passe '{where}' supprimé.")


# Fonction principale d'interaction avec l'utilisateur
def main():
    parser = argparse.ArgumentParser(
        description="""Générateur de mots de passe aléatoires
            et stockage de mots de passe.""")
    subparsers = parser.add_subparsers(dest="command")

    # Sous-commande pour générer un mot de passe
    generate_parser = subparsers.add_parser(
        "generate", help="Générer un mot de passe")
    generate_parser.add_argument(
        "length", type=int,
        help="Longueur du mot de passe")
    generate_parser.add_argument(
        "--uppercase", action="store_true",
        help="Inclure des majuscules")
    generate_parser.add_argument(
        "--digits", action="store_true",
        help="Inclure des chiffres")
    generate_parser.add_argument(
        "--special_chars", action="store_true",
        help="Inclure des caractères spéciaux")
    generate_parser.add_argument(
        "--save", action="store_true",
        help="Enregistrer le mot de passe généré")
    generate_parser.add_argument(
        "--username", type=str,
        help="Nom d'utilisateur pour enregistrer le mot de passe")

    # Sous-commande pour afficher les mots de passe enregistrés
    subparsers.add_parser(
        "view", help="Voir les mots de passe enregistrés")

    # Sous-commande pour supprimer un mot de passe enregistré
    subparsers.add_parser(
        "delete", help="Supprimer un mot de passe enregistré")

    args = parser.parse_args()

    if args.command == "generate":
        password = generate_password(
            args.length, args.uppercase, args.digits, args.special_chars)
        print("\nMot de passe généré :")
        print(password)
        if args.save:
            if args.username:
                save_password(args.username, password)
            else:
                print("Vous devez fournir un nom d'user avec l'option --save")

    elif args.command == "view":
        view_saved_passwords()

    elif args.command == "delete":
        delete_saved_password()

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
