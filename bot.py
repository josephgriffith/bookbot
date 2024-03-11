def main():
    path = "./books/frankenstein.txt"
    report(path)

#takes a string and returns the number of words based on whitespace
def wordCount(text):
    return len(text.split())

#takes a string and returns a dictionary where each character is a key and the number of times it appears in the string is the value
def getCharCounts(text, insensitive=True, alpha=True):
    chars = {}
    if insensitive:
        text = text.lower()
    for c in text:
        if alpha and not c.isalpha():
            continue
        if c in chars:
            chars[c] = chars[c]+1
        else:
            chars[c] = 1
    return chars

#reports some facts about the given text
def report(path):
    print(f"--================ Report on file: {path} ================--")
    with open(path) as f:
        text = f.read()
        words = text.split()
        print(f"File contains {wordCount(text)} words separate by whitespace.")
        print("Found the following number of occurrences of letter characters (case insensitive):")
        chars = getCharCounts(text)
        for c in dict(sorted(chars.items(), key=lambda item: item[1],reverse=True)):
            print(f"\"{c}\": {chars[c]}")

main()







