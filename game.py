def evaluate_guess(guess, target):
    if guess < target:
        return "Too low"
    elif guess > target:
        return "Too high"
    else:
        return "Correct"