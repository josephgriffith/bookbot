def main():
    with open("./books/frankenstein.txt") as f:
        text = f.read()
        words = text.split()
        print(wordCount(text))
        chars = getCharCounts(text, True)
        for c in chars:
            print(f"{c}: {chars[c]}")

#takes a string and returns the number of words based on whitespace
def wordCount(text):
    return len(text.split())

#takes a string and returns a dictionary where each character is a key and the number of times it appears in the string is the value
def getCharCounts(text, insensitive=False):
    chars = {}
    if insensitive:
        text = text.lower()
    for i in range(len(text)):
        if text[i] in chars:
            chars[text[i]] = chars[text[i]]+1
        else:
            chars[text[i]] = 1
    return chars
main()







