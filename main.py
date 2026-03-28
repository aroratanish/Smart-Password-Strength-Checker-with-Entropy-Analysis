from trie import Trie
from entropy import calculate_entropy
from patterns import has_sequence, has_repetition

def load_common_passwords(file):
    trie = Trie()
    with open(file, "r") as f:
        for line in f:
            trie.insert(line.strip())
    return trie

def estimate_crack_time(entropy):
    guesses_per_sec = 1e9
    combinations = 2 ** entropy
    seconds = combinations / guesses_per_sec

    if seconds < 60:
        return f"{seconds:.2f} seconds"
    elif seconds < 3600:
        return f"{seconds/60:.2f} minutes"
    elif seconds < 86400:
        return f"{seconds/3600:.2f} hours"
    elif seconds < 31536000:
        return f"{seconds/86400:.2f} days"
    else:
        return f"{seconds/31536000:.2f} years"

def analyze(password, trie):
    entropy = calculate_entropy(password)

    if trie.search(password):
        return "Very Weak (Common Password)", entropy

    if has_sequence(password):
        return "Weak (Sequential Pattern)", entropy

    if has_repetition(password):
        return "Weak (Repetition)", entropy

    if entropy < 28:
        return "Weak", entropy
    elif entropy < 50:
        return "Medium", entropy
    else:
        return "Strong", entropy


if __name__ == "__main__":
    trie = load_common_passwords("dataset.txt")

    password = input("Enter password: ")

    strength, entropy = analyze(password, trie)
    crack_time = estimate_crack_time(entropy)

    print("\n--- RESULT ---")
    print(f"Strength: {strength}")
    print(f"Entropy: {entropy:.2f}")
    print(f"Estimated Crack Time: {crack_time}")
