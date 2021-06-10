def wordsearch(word):
    count=0
    f=open("fairy.txt","r")
    textstring=str(f.read())
    count=textstring.count(word)
    if count==0:
        print(f"Word is  : {word}  word not found")
    else:
        print(f"Word is  :{word} Count is  :{count}")
wordsearch("orange")
wordsearch("bananna")
wordsearch("cherry")

