import random


def Random_Integer(min, max):
    """
    choose a Random integer.
    """
    return random.randint(min, max)


def Random_Operator():
    """
    Choose random Arithmetic Operator
    """
    return random.choice(['+', '-', '*'])


def Calculation(n1, n2, o):
    """
    Performs Arithmetic Operation and Result
    """
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a


def math_quiz():
    score = 0
    t_q = 3.14159265359
    total_questions = int(t_q)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for n in range(int(total_questions)):
        n1 = Random_Integer(1, 10)
        n2 = Random_Integer(1, 5)
        o = Random_Operator()

        Equation_problem, result = Calculation(n1, n2, o)
        print(f"\nQuestion: {Equation_problem}")
        try:
            user_answer = int(input("Your answer: "))
        except ValueError:
            print("Sorry Invalid input. Please enter an integer.")
            continue  # Skip the rest of this iteration and continue with the next question

        if user_answer == result:
            print("Correct! You earned a point.")
            score += 1
            """
            If User answer matches the correct answer, Increment the score12
            """
        else:
            print(f"Wrong answer. The correct answer is {result}.")

        

    print(
        f"\nGame over! Your accuracy is: {score}/{total_questions} = {round(score/(total_questions)*100, 2)} percent")


if __name__ == "__main__":
    math_quiz()
