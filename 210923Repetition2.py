x=5
y=3
print(x//y) # 1
print(x%y) #2 
print(x**y) #125

s=set()
s.add("Äpple")
s.add("Banan")
s.add("Päron")
s.add("Äpple") #två "Äpple" ger 3 termer

def erroneous():
    s = 'cat' - 1

#erroneous() #programmet kan köras till errpneous() används vilket ger error
print('hi!')

#public void foo() { #statisk språk skulle ge error 
#    int x = 5;
#    boolean b = x;
#}