#volume of water in litre
prompt = float(input("Enter water in litres to calculate: "))

hectare = 10000

if prompt != 0:
    vol_of_litre = hectare * (prompt / 100)
    print(vol_of_litre, 'litres')
else:
    print("Please enter a true litre value")
