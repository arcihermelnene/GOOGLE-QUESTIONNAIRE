'''
Complete the code to iterate through the keys and values 
of the car_prices dictionary,
 printing out some information about each one.
'''

def car_listing(car_prices):
  result = ""
  for car_model, price in car_prices.items():
    result += "{} costs {} dollars".format(car_model,price) + "\n"
  return result

print(car_listing({"Kia Soul":19000, "Lamborghini Diablo":55000, "Ford Fiesta":13000, "Toyota Prius":24000}))