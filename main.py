file_path = "c:/dev/file.txt"

with open(file_path,'r')as f:
    words_to_read = 20
    contents = f.read(words_to_read)
    print(contents)