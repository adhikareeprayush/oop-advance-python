file_path = "sample_notes.txt"

with open(file_path, "w") as f:
    f.write("I love python programming\n")
    f.write("Python makes data manipulation easy\n")

with open(file_path, "r") as f:
    for line in f:
        tokens = line.split()
        print(f"Line: {line.strip()} | Word Count: {len(tokens)}")

with open(file_path, "a") as f:
    f.write("Appended line: Learning Python is fun!\n")
