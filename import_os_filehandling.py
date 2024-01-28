import os
def create_file(hello):
    try:
        with open('hello','w') as f:
            f.write('Hello world\n')
        print("File"+hello+"created successfully")
    except IOError:
        print("Error could not create file",hello)
def read_file(hello):
    try:
        with open('hello','r') as f:
            content = f.read()
            print(content)
    except IOError:
        print("Error could not read file",hello)
def append_file(hello,FileAppended):
    try:
        with open('hello','a') as f:
            f.write(FileAppended)
            print("Text file appended to the file"+hello+"Successfully")
    except IOError:
        print("Could not append the file",hello)
def rename_file(hello,hy):
    try:
        os.rename(hello,hy)
        print("File"+hello+"renamed to "+hy+"successfully")
    except IOError:
        print("could not rename the file",hello)
def delete_file(hello):
    try:
        os.remove(hello)
        print("file"+hello+"deleted successfully")
    except IOError:
        print("Could not read the file"+hello)
if __name__ == '__main__':
    hello = "Example.txt"
    hy = "new example.txt"
    create_file(hello)
    read_file(hello)
    append_file(hello,"This is some additional text\n")
    read_file(hello)
    rename_file(hello,hy)
    read_file(hy)
    delete_file(hy)

