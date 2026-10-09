
def hanoi(n, source, auxiliary, target):
    if n == 0:
        return

    hanoi(n - 1, source, target, auxiliary)

    print(f"Move disk {n} from {source} to {target}")

    hanoi(n - 1, auxiliary, source, target)


if __name__ == "__main__":
    n = 3

    print("Tower of Hanoi")
    print("Minimum moves:", 2**n - 1)

    hanoi(n, "A", "B", "C")
