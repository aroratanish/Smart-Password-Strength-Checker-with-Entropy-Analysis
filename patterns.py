def has_sequence(password):
    sequences = ["123", "abc", "qwerty"]
    for seq in sequences:
        if seq in password.lower():
            return True
    return False

def has_repetition(password):
    for i in range(len(password) - 2):
        if password[i] == password[i+1] == password[i+2]:
            return True
    return False
