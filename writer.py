num_lines = 100001
with open("data.txt", "w") as f:
    for i in range(num_lines):
        text = "***" * 10 + "\n"
        f.write(text)
