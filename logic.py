import string
from random import randint, choice, shuffle


def generate_password(passwordmin=8, passwordmax=16):
    length = randint(passwordmin, passwordmax)

    letters_lower = string.ascii_lowercase
    letters_upper = string.ascii_uppercase
    digits = string.digits
    symbols = "!@#$%&?"

    password_chars = [
        choice(letters_upper),
        choice(letters_lower),
        choice(digits),
        choice(symbols)
    ]

    all_chars = letters_lower + letters_upper + digits + symbols

    for _ in range(length-4):
        password_chars.append(choice(all_chars))

    shuffle(password_chars)
    return "".join(password_chars)


def check_strength(password):
    score = 0

    if len(password) >= 8:
        score += 1
    if any(c.islower() for c in password):
        score += 1
    if any(c.isupper() for c in password):
        score += 1
    if any(c.isdigit() for c in password):
        score += 1
    if any(c in "!@#$%&?" for c in password):
        score += 1

    if score <= 2:
        return "Faible 🔴", "red"
    elif score <= 4:
        return "Moyen 🟠", "orange"
    else:
        return "Fort 🟢", "green"
