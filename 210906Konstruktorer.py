class Elev:
  def __init__(self, name, age, godkänd): # Elevens konstruktor 
    self.name = name
    self.age = age
    self.godkänd = godkänd

  def main():
      elev1 = Elev("Erik", 15, "glad")
      elev1.drive()

e1 = Elev("Erik", 15, "glad")

print(e1.name)
print(e1.age)

if __name__ == "__main__":
    print("Erik är glad")
    main()
