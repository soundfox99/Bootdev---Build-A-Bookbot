
def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    
        words = file_contents.split()
        print(len(words))

        keys = "abcdefghijklmnopqrstuvwxyz"
        book_dict = dict.fromkeys(keys, 0)
        
        for char in file_contents.lower():
            if ('a' <= char <= 'z'):
                book_dict[char] += 1
        
        for key, value in book_dict.items():
            print(key, value)

    return

if __name__ == "__main__":
    main()