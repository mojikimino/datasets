num_lines = 100000
with open("data.txt", "w") as f:
    for i in range(num_lines):
        text = "12345" * 10 + "\n"
        f.write(text)
