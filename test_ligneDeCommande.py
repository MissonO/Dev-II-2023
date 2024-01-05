import unittest
import string
import io
from unittest.mock import patch
import os

# Importer les fonctions à tester
from ligneDeCommande import generate_password, save_password
from ligneDeCommande import view_saved_passwords


class TestPasswordGenerator(unittest.TestCase):

    def test_generate_password(self):
        # Tester si la longueur du mot de passe est correcte
        password = generate_password(10, True, True, True)
        self.assertEqual(len(password), 10)

        # Tester si les caractères spécifiés sont inclus
        password = generate_password(8, True, True, False)
        self.assertTrue(any(c.isupper() for c in password))
        self.assertTrue(any(c.isdigit() for c in password))
        print(password)  # Afficher le mot de passe généré
        self.assertTrue(any(c in string.ascii_uppercase for c in password))

    def test_save_password(self):
        # Créer un fichier de test et vérifier
        # son contenu après l'enregistrement
        with open("passwords.txt", "w"):
            with patch("builtins.input", side_effect=["testuser"]):
                save_password("testuser", "testpassword")

        with open("passwords.txt", "r") as file:
            content = file.read()
            self.assertIn("testuser: testpassword", content)

    def test_view_saved_passwords(self):
        # Tester si la fonction affiche correctement
        # les mots de passe enregistrés
        with patch("builtins.input", side_effect=["testuser"]):
            save_password("testuser", "testpassword")

        with patch("builtins.input", side_effect=["oui"]):
            with patch("sys.stdout", new_callable=io.StringIO) as mock_stdout:
                view_saved_passwords()
                output = mock_stdout.getvalue().strip()
                self.assertIn("Mots de passe enregistrés :", output)
                self.assertIn("testuser: testpassword", output)

        # Nettoyer le fichier de test
        os.remove("passwords.txt")


if __name__ == "__main__":
    unittest.main()
