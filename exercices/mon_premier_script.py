import unittest

MIN_LENGTH: int = 7

message: str = "C'est mon premier script !!!"
print(message)

variable_dynamique = 1
print(type(variable_dynamique))

variable_dynamique = "coucou"
print(type(variable_dynamique))


def names(prenoms: list[str]) -> int:
    """Compter les prénoms qui ont plus de MIN_LENGTH lettres (et afficher le message associé)."""
    compteur_prenoms_longs: int = 0

    for prenom in prenoms:
        if len(prenom) > MIN_LENGTH:
            compteur_prenoms_longs += 1
            print(f"{prenom} est un prénom avec un nombre de lettres supérieur à {MIN_LENGTH}")
        else:
            print(f"{prenom} est un prénom avec un nombre de lettres inférieur ou égal à {MIN_LENGTH}")

    return compteur_prenoms_longs


liste_prenoms = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
nombre_prenoms_longs = names(liste_prenoms)

print(f"Nombre de prénoms dont le nombre de lettres est supérieur à {MIN_LENGTH} : {nombre_prenoms_longs}")
print("----------------------------------------------------------------------")


def saluer(nom: str) -> str:
    return f"Bonjour {nom}"
# print(saluer("Alice"))  # Affiche : Bonjour Alice


class TestNamesMethod(unittest.TestCase):
    def test_names(self) -> None:
        prenoms_test = ["Guillaume", "Gilles", "Juliette", "Antoine", "François", "Cassandre"]
        self.assertEqual(names(prenoms_test), 4)


if __name__ == "__main__":
    unittest.main()