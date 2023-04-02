filename = "input.txt"

with open(filename, "r") as f:
    lines = f.readlines()

transformed_lines = [line.strip("\n").split("a", 1)[-1].capitalize() if "a" in line else "" for line in lines]

print(transformed_lines)
