# Task 2 – Analyse de logs
# TODO : lire un fichier log.txt et compter les lignes et erreurs

try:
    with open("log.txt", "r") as f:
        lines = f.readlines()
        errors = [l for l in lines if "ERROR" in l]
    print(f"Nombre de lignes : {len(lines)}")
    print(f"Nombre d'erreurs : {len(errors)}")
except FileNotFoundError:
    print("Fichier log.txt non trouvé")
