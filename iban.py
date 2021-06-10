iban="IE44AIBK66666611111111"
countrycode=iban[:2]
checksum=iban[2:4]
swiftcode=iban[4:8]
branchcode=iban[8:14]
accountno=iban[14:22]
print("Countrycode is ",countrycode)
print("Checksum number is ",checksum)
print("Swiftcode is ",swiftcode)
print("Account number is ",accountno)

string1="silpa_pravin"
print("Pascal case is ",string1)
string2=string1.replace('_',' ').title()
string2=string2.replace(' ','')
print("Camel case is ", string2)

string3="SilpaPravin"
print("camel case is ",string3)
firstchar=[string3[0].lower()]
for c in string3[1:]:
   if c in('ABCDEFGHIJKLMNOPQRSTUVWXYZ'):
      firstchar.append('_')
  
   else:
       firstchar.append(c.lower())
firstchar=''.join(firstchar)
print("camel case to pascal case is",firstchar)
