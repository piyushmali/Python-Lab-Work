base_price = float(input("Enter car\'s base price "))
tax = 8/100
lic = 7/100
dealer = 80
destination = 150

tax *= base_price

lic *= base_price

total = base_price + tax + lic + dealer + destination

print("\nCar base price", base_price)
print("\n Taxes (8%)\t\t", round(tax, 2))
print("\n Licensing fees (7%) \t ", round(lic, 2))
print("\n Dealership fee \t", dealer)
print("\n Destination fee \t", destination)

print("\nTotal \t\t\t", round(total, 2))
