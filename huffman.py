def main():
    print("Huffman Compression Program")
    print("=================================================================")
    h = int(input("Enter 1 if you want to enter in command window, 2 if you are using some file: "))
    if h == 1:
        my_string = input("Enter the string you want to compress: ")
    elif h == 2:
        file = input("Enter the filename: ")
        with open(file, 'r') as f:
            my_string = f.read()
    else:
        print("You entered invalid input")
        return

    len_my_string = len(my_string)
    print("Entered string is:", my_string)
    print("Your data is", len_my_string * 7, "bits long")

    letters = []
    only_letters = []
    for letter in my_string:
        if letter not in letters:
            frequency = my_string.count(letter)
            letters.append(frequency)
            letters.append(letter)
            only_letters.append(letter)

    nodes = []
    while len(letters) > 0:
        nodes.append(letters[0:2])
        letters = letters[2:]
    nodes.sort()

    huffman_tree = []
    huffman_tree.append(nodes)

    def combine_nodes(nodes):
        pos = 0
        newnode = []
        if len(nodes) > 1:
            nodes.sort()
            nodes[pos].append("1")
            nodes[pos + 1].append("0")
            combined_node1 = (nodes[pos][0] + nodes[pos + 1][0])
            combined_node2 = (nodes[pos][1] + nodes[pos + 1][1])
            newnode.append(combined_node1)
            newnode.append(combined_node2)
            newnodes = [newnode] + nodes[2:]
            huffman_tree.append(newnodes)
            combine_nodes(newnodes)
        return huffman_tree

    newnodes = combine_nodes(nodes)
    huffman_tree.sort(reverse=True)
    print("Huffman tree with merged pathways:")

    checklist = []
    for level in huffman_tree:
        for node in level:
            if node not in checklist:
                checklist.append(node)
            else:
                level.remove(node)

    count = 0
    for level in huffman_tree:
        print("Level", count, ":", level)
        count += 1
    print()

    letter_binary = []
    if len(only_letters) == 1:
        lettercode = [only_letters[0], "0"]
        letter_binary.append(lettercode * len(my_string))
    else:
        for letter in only_letters:
            code = ""
            for node in checklist:
                if len(node) > 2 and letter in node[1]:
                    code += node[2]
            lettercode = [letter, code]
            letter_binary.append(lettercode)
    print("Binary code generated:")
    for letter in letter_binary:
        print(letter[0], letter[1])

    bitstring = ""
    for character in my_string:
        for item in letter_binary:
            if character in item:
                bitstring += item[1]
    binary = "0b" + bitstring
    print("Your message as binary is:")
    print(bitstring)

    uncompressed_file_size = len(my_string) * 7
    compressed_file_size = len(binary) - 2
    print("Your original file size was", uncompressed_file_size, "bits. The compressed size is:", compressed_file_size)
    print("This is a saving of", uncompressed_file_size - compressed_file_size, "bits")

    with open("compressed.txt", "w+") as output:
        print("Compressed file generated as compressed.txt")
        print("Decoding.......")
        output.write(bitstring)

    bitstring = binary[2:]
    uncompressed_string = ""
    code = ""
    for digit in bitstring:
        code += digit
        pos = 0
        for letter in letter_binary:
            if code == letter[1]:
                uncompressed_string += letter_binary[pos][0]
                code = ""
            pos += 1

    print("Your UNCOMPRESSED data is:")
    print(uncompressed_string)


if __name__ == "__main__":
    main()