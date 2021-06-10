def camel2pascal(cameltext):
  pascaltext = cameltext[0].upper() + cameltext[1:]
  return pascaltext

def test_camel2pascal(test_number,inputtext,expectedoutput):
  print(f"{test_number }. Input={ inputtext}")
  print(f"{test_number }. Expectedoutput={ expectedoutput}")
  actualoutput=camel2pascal(inputtext)
  print(f"{test_number}. Actual Output={actualoutput}")
  if actualoutput==expectedoutput:
      print("Output correct")   
  else:
      print("OUTPUT INCORRECT")
      return False

print("CAMEL TO PASCAL")

test_camel2pascal(1,"oneTwoThree","OneTwoThree")
test_camel2pascal(2,"1TwoThree","1TwoThree")
test_camel2pascal(3,"_TwoThree","_TwoThree")
test_camel2pascal(4,"'TwoThree","'TwoThree")
test_camel2pascal(5,"\nTwoThree","TwoThree")


##########################################################################################


def pascal2camel(pascaltext):
  cameltext = pascaltext[0].lower() + pascaltext[1:]
  return cameltext

def test_pascal2camel(test_number,inputtext,expectedoutput):
  print(f"{test_number }. Input={ inputtext}")
  print(f"{test_number }. Expectedoutput={ expectedoutput}")
  actualoutput=pascal2camel(inputtext)
  print(f"{test_number}. Actual Output={actualoutput}")
  if actualoutput==expectedoutput:
      print("Output correct")   
  else:
      print("OUTPUT INCORRECT")
      return False

print("PASCAL TO CAMEL")

test_pascal2camel(1,"OneTwoThree","oneTwoThree")
test_pascal2camel(2,"1TwoThree","1TwoThree")
test_pascal2camel(3,"_TwoThree","_TwoThree")
test_pascal2camel(4,"'TwoThree","'TwoThree")
test_pascal2camel(5,"\nTwoThree","TTTwoThree")


 

#name_camel="oneTwoThree"
#name_pascal=camel2pascal(name_camel)
#print("1. Pascal case is ",camel2pascal(name_camel))

#name_camel="1TwoThree"
#name_pascal=camel2pascal(name_camel)
#print("2. Pascal case is ",camel2pascal(name_camel))

#name_camel="'TwoThree"
#name_pascal=camel2pascal(name_camel)
#print("3. Pascal case is ",camel2pascal(name_camel))

#name_camel="_TwoThree"
#name_pascal=camel2pascal(name_camel)
#print("4. Pascal case is ",camel2pascal(name_camel))

#name_camel="\nTwoThree"
#name_pascal=camel2pascal(name_camel)
#print("5.Pascal case is ",camel2pascal(name_camel))
