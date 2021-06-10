def wordsearch(word):
  textstring="Python is an interpreted high-level is general-purpose programming is language. Python's design philosophy emphasizes code readability with its notable use of significant indentation."
  count=textstring.count(word)
  if (count==0):
   print(f"word {word} not found")
  else:
   print(f"word is {word} and count is {count}")

def stringsplitsearch(word):
    textstring1="orange,green,blue,black,white,yellow,red,dragon fruit"
    textstring2=textstring1.split(",")
    if word in textstring2:
      print(f"word {word} found")
    else:
      print(f"word {word} not found")

wordsearch("is")
wordsearch("silpa")
stringsplitsearch("orange")
stringsplitsearch("grapes")
