# Build_EXE

Application Python avec interface graphique Tkinter, compilation automatique en EXE Windows via PyInstaller, création d'installateur avec Inno Setup et système de mise à jour via GitHub Releases.

## Fonctionnalités

* Interface graphique Tkinter
* Compilation automatique en EXE Windows
* Déploiement GitHub Actions
* Publication automatique sur GitHub Releases
* Vérification des mises à jour en ligne
* Installateur Windows via Inno Setup
* Compatible Python 3.11+

---

## Structure du projet

```text
build_exe/
│
├── main.py
├── updater.py
├── version.py
├── requirements.txt
├── installer.iss
│
└── .github/
    └── workflows/
        └── release.yml
```

---

## Installation

### Cloner le dépôt

```bash
git clone https://github.com/VOTRE_COMPTE/build_exe.git
cd build_exe
```

### Installer les dépendances

```bash
pip install -r requirements.txt
```

---

## Exécution locale

```bash
python main.py
```

---

## Compilation EXE

### Installation de PyInstaller

```bash
pip install pyinstaller
```

### Génération du fichier EXE

```bash
pyinstaller --onefile --windowed --name MonApp main.py
```

Le fichier compilé sera disponible dans :

```text
dist/MonApp.exe
```

---

## Création de l'installateur

Installer Inno Setup :

https://jrsoftware.org/isinfo.php

Compiler ensuite :

```text
installer.iss
```

Résultat :

```text
dist_installer/MonApplicationSetup.exe
```

---

## Mise à jour automatique

Modifier le fichier :

```python
# version.py

APP_VERSION = "1.0.0"
GITHUB_REPO = "VotreCompte/build_exe"
```

Au démarrage, l'application vérifie automatiquement si une version plus récente est disponible sur GitHub Releases.

---

## Déploiement automatique GitHub

Créer une nouvelle version :

```bash
git tag v1.0.1
git push origin v1.0.1
```

GitHub Actions va automatiquement :

1. Compiler l'application
2. Générer l'EXE
3. Créer une Release
4. Ajouter l'EXE à la Release

---

## Workflow GitHub Actions

Fichier :

```text
.github/workflows/release.yml
```

Déclenchement :

```yaml
on:
  push:
    tags:
      - 'v*'
```

---

## Personnalisation

Modifier :

```python
APP_VERSION
GITHUB_REPO
```

Ajouter une icône :

```bash
pyinstaller --onefile --windowed --icon=icon.ico main.py
```

---

## Technologies utilisées

* Python 3.11+
* Tkinter
* Requests
* PyInstaller
* GitHub Actions
* GitHub Releases
* Inno Setup

---

## Licence

Projet libre d'utilisation et de modification.
