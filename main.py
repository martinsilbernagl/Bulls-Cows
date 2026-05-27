import random

DIGITS_COUNT = 4
SEPARATOR = "-" * 47


def generate_secret(length: int = DIGITS_COUNT) -> str:
    """Generate secret number with unique digits and no leading zero."""
    first_digit = random.choice("123456789")
    remaining = random.sample([d for d in "0123456789" if d != first_digit], length - 1)
    return first_digit + "".join(remaining)


def validate_guess(guess: str, length: int = DIGITS_COUNT) -> str | None:
    """Validate user guess, return error message or None when valid."""
    if len(guess) != length:
        return f"The number must have exactly {length} digits."
    if not guess.isdigit():
        return "The input must contain only digits."
    if guess[0] == "0":
        return "The number must not start with 0."
    if len(set(guess)) != length:
        return "Digits must be unique (no duplicates)."
    return None


def count_bulls_cows(secret: str, guess: str) -> tuple[int, int]:
    """Count bulls (correct position) and cows (correct digit, wrong position)."""
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = sum(d in secret for d in guess) - bulls
    return bulls, cows


def word(value: int, singular: str, plural: str) -> str:
    """Return singular/plural word by count."""
    return singular if value == 1 else plural


def print_intro() -> None:
    """Print game intro text."""
    print("Hi there!")
    print(SEPARATOR)
    print(f"I've generated a random {DIGITS_COUNT} digit number for you.")
    print("Let's play a bulls and cows game.")
    print(SEPARATOR)


def main() -> None:
    """Run the Bulls & Cows game loop."""
    secret = generate_secret()
    guesses = 0

    print_intro()
    print("Enter a number:")
    print(SEPARATOR)

    while True:
        guess = input(">>> ").strip()
        error = validate_guess(guess)

        if error:
            print(error)
            print(SEPARATOR)
            continue

        guesses += 1
        bulls, cows = count_bulls_cows(secret, guess)

        if guess == secret:
            print("Correct, you've guessed the right number")
            print(f"in {guesses} {word(guesses, 'guess', 'guesses')}!")
            print(SEPARATOR)
            print("That's amazing!")
            return

        print(
            f"{bulls} {word(bulls, 'bull', 'bulls')}, "
            f"{cows} {word(cows, 'cow', 'cows')}"
        )
        print(SEPARATOR)


if __name__ == "__main__":
    main()
