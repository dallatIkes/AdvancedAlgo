import subprocess
import os

from abstract import Problem

def generate_docs():
    sources_files = ["src/cli.py", "src/abstract.py"]
    output_dir = "docs"

    os.makedirs(output_dir, exist_ok=True)

    # Generate docs for everything in the src/ directory
    print('---')
    for file in sources_files:
        subprocess.run(["python3", "-m", "pdoc", file, "-o", output_dir], check=True) 
        print(f"✅ {file} docs generated in {output_dir}/")
    print('---')

def main():
    generate_docs()
    subprocess.run(["firefox", "docs/index.html"]) 

    problem = Problem(10)
    print(problem.S)
    print(problem.distance(1, 2))
    print(problem.res)
    print(problem.SD)


if __name__ == '__main__':
    main()