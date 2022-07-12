import fridge
f = fridge.Fridge()
apple = fridge.Food()
elephant = fridge.Food()

print(f.open())
print(f.put(apple))
print(f.put(elephant))
print(f.foods)