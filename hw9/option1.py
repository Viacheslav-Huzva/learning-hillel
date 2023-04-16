def transform_lines(input):
    with open(input, "r") as f:
        lines = f.readlines()

    transformed_lines = []
    for line in lines:
        words = line.strip("\n").split("a")
        second_word = words[1].capitalize() if len(words) > 1 else ""
        transformed_lines.append(words[0] + second_word)

    return transformed_lines


if __name__ == "__main__":
    filename = "input.txt"
    transformed_lines = transform_lines(filename)
    print(transformed_lines)

