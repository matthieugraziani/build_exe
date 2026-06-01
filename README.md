# Build_EXE Enterprise

Framework professionnel pour la création, le déploiement et la mise à jour d'applications Windows développées en Python.

Build_EXE Enterprise fournit une architecture moderne basée sur PySide6, GitHub Actions, GitHub Releases et Inno Setup afin de produire des applications Windows robustes, maintenables et distribuables à grande échelle.

---

## Fonctionnalités

### Application Desktop

* Interface graphique moderne avec PySide6 (Qt6)
* Support du mode sombre
* Architecture modulaire
* Gestion centralisée de la configuration
* Journalisation avancée
* Gestion des erreurs

### Distribution

* Compilation automatique en EXE
* Packaging PyInstaller
* Génération d'installateurs Windows
* Déploiement GitHub Releases
* Gestion des versions

### Mise à jour

* Vérification automatique des nouvelles versions
* Téléchargement sécurisé
* Mise à jour silencieuse
* Redémarrage automatique de l'application
* Validation SHA256

### Qualité Logicielle

* Tests unitaires
* Linting automatique
* Formatage du code
* Intégration continue
* Déploiement continu

---

# Architecture

```text
build_exe_enterprise/
│
├── src/
│   ├── app.py
│   │
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── version.py
│   │   └── security.py
│   │
│   ├── services/
│   │   ├── github_release_service.py
│   │   ├── update_service.py
│   │   └── download_service.py
│   │
│   ├── ui/
│   │   ├── main_window.py
│   │   ├── splash_screen.py
│   │   └── settings_dialog.py
│   │
│   └── assets/
│       ├── icon.ico
│       ├── splash.png
│       └── themes/
│
├── tests/
│
├── installer/
│
├── scripts/
│
├── docs/
│
└── .github/
    └── workflows/
```

---

# Installation

## Prérequis

* Python 3.11+
* Git
* Inno Setup
* Windows 10/11

## Installation des dépendances

```bash
pip install -r requirements.txt
```

---

# Exécution

```bash
python src/app.py
```

---

# Compilation

## Génération de l'EXE

```bash
pyinstaller ^
  --onefile ^
  --windowed ^
  --icon=src/assets/icon.ico ^
  --name BuildEXE ^
  src/app.py
```

Le fichier généré sera disponible dans :

```text
dist/
```

---

# Création de l'installateur

Compiler :

```text
installer/installer.iss
```

Résultat :

```text
dist_installer/
```

---

# Déploiement GitHub

## Nouvelle version

```bash
git tag v2.0.0
git push origin v2.0.0
```

Le pipeline GitHub Actions :

1. Compile l'application
2. Lance les tests
3. Génère l'EXE
4. Crée une Release GitHub
5. Publie les artefacts

---

# Mise à jour automatique

Le système de mise à jour utilise l'API GitHub Releases.

Workflow :

```text
Application
    │
    ▼
Vérification Release
    │
    ▼
Téléchargement
    │
    ▼
Validation SHA256
    │
    ▼
Installation
    │
    ▼
Redémarrage
```

---

# Tests

Exécuter :

```bash
pytest
```

---

# Analyse du code

Lint :

```bash
ruff check .
```

Formatage :

```bash
black .
```

---

# Sécurité

Le framework intègre :

* Validation SHA256
* Gestion des erreurs
* Vérification des versions
* Téléchargement sécurisé
* Isolation des fichiers temporaires

---

# Technologies

* Python
* PySide6
* PyInstaller
* GitHub Actions
* GitHub Releases
* Inno Setup
* Ruff
* Black
* Pytest

---

# Roadmap

## Version 2.x

* Thèmes personnalisés
* Support multilingue
* Mise à jour différentielle
* Télémétrie optionnelle

## Version 3.x

* Support Linux
* Support macOS
* Déploiement cloud
* Gestion des licences

---

# Licence

MIT License

---

# Auteur

Build_EXE Enterprise Framework

Conçu pour le déploiement professionnel d'applications Python sous Windows.
