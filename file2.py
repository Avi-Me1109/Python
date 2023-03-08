def main():
    infile = open("phil.txt", 'r')

    file_contents = infile.readline()
    file_contents2 = infile.readline()

    infile.close()

    print(file_contents.strip(), " ", file_contents2)

main()