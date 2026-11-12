# Chatbot de Djikol's

Application de bureau de chatbot construite avec Python et CustomTkinter.
Les réponses sont volontairement simples et se trouvent dans le dictionnaire
`RESPONSES` de `chatbot.py`, afin de pouvoir les compléter selon l'évolution
du projet.

## Installation

Depuis le dossier du projet, créez un environnement virtuel et installez la
dépendance :

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Lancement

```powershell
python chatbot.py
```

Les messages sont comparés sans tenir compte des majuscules ni des espaces
autour. Ajoutez de nouvelles paires question/réponse dans `RESPONSES`.

## Tests

```powershell
python -m unittest -v
```
