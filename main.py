import random
from typing import List, Tuple


def generate_secret_code()  -> List[int]:
    return [random.randint(0, 9) for _ in range(4)]


def get_feedback(secret: List[int], guess: List[int]) -> Tuple[int, int]:
    # Calculate Bulls (correct digit and position)
    bulls_count = sum(
        secret_digit == guess_digit for secret_digit, guess_digit in zip(secret, guess)
    )

    secret_digit_counts = {digit: secret.count(digit) for digit in set(secret)}
    guess_digit_counts = {digit: guess.count(digit) for digit in set(guess)}

    total_matches = sum(
        min(secret_digit_counts.get(digit, 0), guess_digit_counts.get(digit, 0))
        for digit in guess_digit_counts
    )

    # Calculate Cows (total matches excluding Bulls)
    cows_count = total_matches - bulls_count

    return bulls_count, cows_count


def mastermind() -> None:
    print("Welcome to mastermid Game!")
    print("Try to guess the 4-digits secret code")

    secret_code = generate_secret_code()
    # print(secret_code)
    guessed_code = 4

    attampts = 0
    while True:
        guess = input("Enter your 4-digits guess (numbers only): ")

        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input! eneter exacly 4 digits.")
            continue

        guess = [int(digit) for digit in guess]
        attampts += 1

        bulls, cows = get_feedback(secret_code, guess)
        print(f"Bulls: {bulls}, Cows: {cows}")

        if bulls == guessed_code:
            print(f"You guessed right the code in {attampts} attampts")
            break


if __name__ == "__main__":
    mastermind()
