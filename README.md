# projet_bts_ciel

![Python](https://img.shields.io/badge/python-3.11-blue)

![Docs](https://img.shields.io/badge/docs-complete-brightgreen)

![CI](https://github.com/boudjelaba/projet_bts_ciel/actions/workflows/ci.yml/badge.svg)

## Objectifs

- Gérer un projet avec GitHub Projects
- faire le lien entre informatique et réseaux
- Rédiger un rapport et planifier les tâches
- utiliser Git et GitHub correctement
- Tester automatiquement le code avec GitHub Actions

## Contenu du projet
- Task 1 – Python : prise en main
- Task 2 – Analyse de logs
- Task 3 – Test réseau
- Task 4 – BONUS : Mini serveur HTTP
- Diagramme de Gantt : `gantt.md`
- Rapport à compléter : `RAPPORT.md`

* Chaque tâche est indépendante.
* Lisez bien les consignes dans chaque fichier `.py`.

---

## Prérequis
- Python 3 installé
- Un terminal
- Un éditeur de code (VS Code recommandé)

Pour vérifier Python :
```bash
python --version
````

---

## Règles importantes

* Faites **au moins un commit par tâche**
* N’effacez pas les commentaires `# TODO`

---

## Comment lancer un script

```bash
python nom_du_fichier.py
```

---

## Structure du projet

```
📦projet_bts_ciel
 ┣ 📂.github
 ┃ ┗ 📂workflows
 ┃   ┗ 📜ci.yml
 ┣ 📂tests
 ┃ ┣ 📜conftest.py
 ┃ ┣ 📜test_log_analyzer.py
 ┃ ┣ 📜test_main.py
 ┃ ┗ 📜test_ping_check.py
 ┣ 📜.gitignore
 ┣ 📜.pre-commit-config.yaml
 ┣ 📜.releaserc.json
 ┣ 📜CONTRIBUTING.md
 ┣ 📜LICENSE
 ┣ 📜README.md
 ┣ 📜VERSION
 ┣ 📜log.txt
 ┣ 📜log_analyzer.py
 ┣ 📜main.py
 ┣ 📜mini_server.py
 ┣ 📜package.json
 ┣ 📜ping_check.py
 ┣ 📜requirements.txt
 ┗ 📜version.py
```
