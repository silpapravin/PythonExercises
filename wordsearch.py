def wordsearch(word):
  
  textstring="Python is an interpreted high-level general-purpose programming language. Python's design philosophy emphasizes code readability with its notable use of significant indentation."
  if word in textstring:
      index=textstring.find(word)
      print("Word matched")
      print("Index is ",index+1)
  else:
      print("word not found")

wordsearch("Python")
wordsearch("language")
wordsearch("silpa")
searchword=input("Enter a search word")
wordsearch(searchword)