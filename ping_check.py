# Task 3 – Test réseau
# TODO : tester si un hôte est accessible

import os

host = input("Entrez l'adresse IP ou le nom d'hôte : ")
response = os.system(f"ping -c 1 {host}")

if response == 0:
    print(f"{host} est accessible")
else:
    print(f"{host} n'est pas accessible")
