num_lines = 200000
with open("data.txt", "w") as f:
    for i in range(num_lines):
        text = "***" * 10 + "\n"
        f.write(text)
