n = int(input())
store = {}
maxCost = 0
maxCostItem = ""
total = 0

for _ in range(n):
    item = input()
    quantity = int(input())
    price = int(input())
    totalPrice = quantity * price

    store[item] = store.get(item, 0) + totalPrice

for item, val in store.items():
    total += val
    if val > maxCost:
        maxCost = val
        maxCostItem = item

average = total / len(store)

print("Item: {}\nTotal price: {:.2f}\nAverage Price: {:.2f}".format(maxCostItem, total, average))
