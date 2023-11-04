file_path = "c:/dev/file.txt"

with open(file_path,'r')as f:
    words_to_read = 240
    contents = f.read(words_to_read)
    print(contents)

with open(file_path, 'a')as w:
    contents_added = a.write('added more line')
    print(contents_added)