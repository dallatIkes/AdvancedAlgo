from abstract import Problem

def main():
    problem = Problem(10)
    print(problem.S)
    print(problem.distance(1, 2))
    print(problem.res)
    print(problem.SD)

if __name__ == '__main__':
    main()