# 📊 Projet Algo Avancée – Approximation de Points

Ce projet Python permet de résoudre un problème d’approximation de points à l’aide de différentes stratégies algorithmiques, telles que la **méthode des essais successifs** et la **programmation dynamique**.

## 🧠 Objectif

Générer un ensemble de points, puis calculer une solution optimale selon des contraintes spécifiques en utilisant l’une des deux méthodes disponibles. Une interface en ligne de commande (CLI) permet de visualiser les résultats.

## ⚙️ Installation

1. Clone le dépôt :
   ```bash
   git clone git@github.com:dallatIkes/AdvancedAlgo.git
   cd AdvancedAlgo
   ```

2. Installe les dépendances (facultatif selon ton usage de `pdoc`) :
   ```bash
   pip install pdoc
   ```

## 🚀 Utilisation

Lancement depuis le terminal avec différents arguments :

### Générer la documentation :
   ```bash
   python main.py --docs
   ```

> 📁 La documentation sera générée dans le dossier `docs/`.

### Exécution avec la méthode des essais successifs :
   ```bash
   python main.py --run_essais_successifs
   ```

### Exécution avec la programmation dynamique :
   ```bash
   python main.py --run_programmation_dynamique
   ```

> 🧩 Une question te demandera combien de points tu veux générer (valeur par défaut : 20).

## 🗂 Structure du projet

```
.
├── src/
│   ├── main.py            # Script principal
│   ├── abstract.py        # Classe Problem avec les méthodes de résolution
│   ├── cli.py             # Interface CLI pour visualiser les solutions
│   └── geometry.py        # Outils géométriques (utilisé en interne)
└── docs/                  # Documentation générée automatiquement
```
