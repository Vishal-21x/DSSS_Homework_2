import random


def Random_Integer_Generator(min, max):
    """
    Random integer.
    """
    return random.randint(min, max)


def Operator():
    """
    Arithmetic Operator
    """
    return random.choice(['+', '-', '*'])


def Arithmetic_Operation(n1, n2, o):
    """
    Arithmetic Operation and Result
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
    total_questions = 3.14159265359
    total_questions = int(total_questions)

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(int(total_questions)):
        n1 = Random_Integer_Generator(1, 10)
        n2 = Random_Integer_Generator(1, 5)
        o = Operator()

        PROBLEM, ANSWER = Arithmetic_Operation(n1, n2, o)
        print(f"\nQuestion: {PROBLEM}")
        try:
            useranswer = int(input("Your answer: "))
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            continue  # Skip the rest of this iteration and continue with the next question

        if useranswer == ANSWER:
            print("Correct! You earned a point.")
            score += 1
            """
            If User answer matches the correct answer, point is added to the score
            """
        else:
            print(f"Wrong answer. The correct answer is {ANSWER}.")

        value = round(score/(total_questions)*100, 2)

    print(
        f"\nGame over! Your accuracy is: {score}/{total_questions} = {value} percent")


if __name__ == "__main__":
    math_quiz()
