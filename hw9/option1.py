def transform_lines(filename):
    with open(filename, "r") as f:
        lines = f.readlines()

    transformed_lines = [line.strip("\n").split("a", 1)[-1].capitalize() if "a" in line else "" for line in lines]

    return transformed_lines


if __name__ == "__main__":
    filename = "input.txt"
    transformed_lines = transform_lines(filename)
    print(transformed_lines)
