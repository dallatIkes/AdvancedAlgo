import subprocess
import os
import argparse
import time

from abstract import Problem
from cli import Cli

best_score = float('inf')
best_solution = []

def generate_docs():
    sources_files = ["src/geometry.py", "src/cli.py", "src/abstract.py"]
    output_dir = "docs"

    os.makedirs(output_dir, exist_ok=True)

    print('--- Génération de la documentation ---')
    for file in sources_files:
        subprocess.run(["python3", "-m", "pdoc", file, "-o", output_dir], check=True)
        print(f"✅ Documentation générée pour {file} dans {output_dir}/")
    print('--- Terminé ---')

def ask_for_number_of_points(default=20):
    try:
        value = input(f"Combien de points veux-tu générer ? (par défaut: {default}) : ")
        return int(value) if value.strip() != "" else default
    except ValueError:
        print("Entrée invalide. Utilisation de la valeur par défaut.")
        return default
    
def print_results(pb: Problem) -> None:
    """Simple function that displays a search result.

    Args:
        pb (Problem): the problem we're searching.
    """
    print('┌─── RÉSULTAT ────────────────────────────────────────────────────────────────────')
    print("│ ✅ Meilleure solution trouvée :", pb.optRes)
    print("│ Score optimal :", pb.optScore)
    print('└─────────────────────────────────────────────────────────────────────────────────')

def launch_project_essais_successifs():
    n = ask_for_number_of_points()

    pb = Problem(n)
    print("Liste des points générés :", pb.S)
    print("Vecteur de solution initial :", pb.res)

    start_time = time.time()
    pb.solopt(0)
    duration = time.time() - start_time
    print(f"⏱ Temps d'exécution (essais successifs) : {duration:.4f} secondes")

    print_results(pb)
    Cli(pb.S, pb.optRes)
    
    for i in range(len(pb.res)):
        pb.optRes[i] = False
    
def launch_project_programmation_dynamique():
    n = ask_for_number_of_points()

    pb = Problem(n)
    start_time = time.time()
    print(pb.solSearch_progDyn())
    duration = time.time() - start_time
    print(f"⏱ Temps d'exécution (programmation dynamique) : {duration:.4f} secondes")

    print_results(pb)
    Cli(pb.S, pb.optRes)


def main():
    parser = argparse.ArgumentParser(description="Projet Algo Avancée - CLI Tool")
    parser.add_argument(
        "--docs", action="store_true",
        help="Génère la documentation du projet (pdoc)"
    )
    parser.add_argument(
        "--run_essais_successifs", action="store_true",
        help="Lance l'exécution principale du projet au moyen de la méthode des essais successifs"
    )
    
    parser.add_argument(
        "--run_programmation_dynamique", action="store_true",
        help="Lance l'exécution principale du projet au moyen de la méthode des essais successifs"
    )

    args = parser.parse_args()

    if args.docs:
        generate_docs()
    elif args.run_essais_successifs:
        launch_project_essais_successifs()
    elif args.run_programmation_dynamique:
        launch_project_programmation_dynamique()
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
