import linearbag

myBag = linearbag.Bag()
myBag.add(10)
myBag.add(20)
myBag.add(30)
myBag.add(40)

value = int( input("Guess a value contained in the bag: ") )
if value in myBag:
    print( "The bag contains the value", value )
else :
    print( "The bag does not contain the value", value )