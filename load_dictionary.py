# Implementation done by Juan Pablo Prada Mejia
import os


def dictionary2list(
    filepath: str = os.path.abspath(os.path.join(".", "2of4brif"))
) -> list[str]:
    ext: str = ".txt"
    words = []
    try:
        with open(filepath + ext, "r") as file:
            words = file.read().strip().split("\n")
            words = [word.lower() for word in words]
    except FileNotFoundError as fnf:
        print(f"error: {fnf.strerror}")

    return words


if __name__ == "__main__":
    filepath: str = os.path.abspath(os.path.join(".", "2of4brif"))
    dictionary2list(filepath)
