def main():
    book_path = "books/frankenstein.txt"
    #book_path = '\\\\wsl.localhost\\Ubuntu\\home\\ddr7o\\workspace\\github.com\\ddr7of8\\bookbot\\books\\frankenstein.txt'
    text = get_book_text(book_path)
    report(text)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def numOfWords(text):
    words = text.split()
    length = len(words)
    return length
    
def letterCount(text):
    lowerText = text.lower()
    countDict = {}
    for i in lowerText:
        if i.isalpha():
            if i in countDict.keys():
                countDict[i] += 1
            else:
                countDict[i] = 1
    return countDict

def report(text):
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{numOfWords(text)} words found in the document")
    countDict = letterCount(text)
    countList = []
    for i in countDict:
        countList.append(  {"name": i, "num": countDict[i]})
    countList.sort(reverse=True, key=sort_on)
    for i in countList:
        c=5
        print(f"The {i['name']} character was found {i['num']} times")
    print("--- End report ---")

def sort_on(dict):
    return dict["num"]


main()

