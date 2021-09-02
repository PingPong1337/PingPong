dic = {"Sverige": "Stockholm", "Norge": "Oslo", "Finland": "Helsingfors"}
x = dic.pop("Finland")               # Tar bort "Finland" från ordboken
print(x)
dic.update({"Danmark": "Köpenhamn"}) # Lägger till "Danmark": "Köpenhamn" i ordboken"
print(dic["Sverige"])                # "Stockholm"
print(dic["Norge"])                  # "Oslo"
print(dic["Finland"])                # "Helsingfors"
print(dic["Danmark"])                # "Köpenhamn"

A = {"Banan", "Päron", "Äpple"}
B = {"Kiwi", "Ananas", "Päron"}
C = A.union(B)
print (C)