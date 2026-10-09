
def fibonacci(n):
    """Return the first n Fibonacci numbers."""
    if n <= 0:
        return []

    sequence = [0, 1]

    while len(sequence) < n:
        next_number = sequence[-1] + sequence[-2]
        sequence.append(next_number)

    return sequence[:n]


if __name__ == "__main__":
    n = 10
    print("Fibonacci sequence:", fibonacci(n))
