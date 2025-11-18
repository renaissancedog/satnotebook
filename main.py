import re
from collections import Counter
with open("wordlist.txt") as f:
    wordlist = [line.strip() for line in f]
books=["frankenstein","mobydick","pride"]
w, h = len(wordlist), len(books)
data = [[0 for x in range(w)] for y in range(h)] 
for book in books:
    file="books/"+book+".txt"
    with open(file, errors="ignore") as f:
        text = f.read().lower()
        words = re.findall(r"[a-zA-Z0-9']+", text)
        word_counts = Counter(words)
        print({word: word_counts.get(word, 0) for word in wordlist})
        for word in wordlist:
          count=word_counts.get(word,0)
          if (count!=0):
            data[books.index(book)][wordlist.index(word)]=count
            print(count, word, "found in", book, books.index(book), wordlist.index(word))
for i in range(len(wordlist)):
    goodword=False
    count=0
    for j in range(len(books)):
        if data[j][i]>0:
           count+=1
    if count>=3:
       goodword=True
       print(wordlist[i], "is a good word found in", count, "books")
       continue