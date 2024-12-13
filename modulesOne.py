# import calc
# from math import sqrt,factorial


# calc.add(56,24)
# calc.add(46,24)
# calc.substract(50,20)

# print(sqrt(16))

import requests
response = requests.get("https://api.github.com")
print(response.status_code) # output: 200
print(response.json()) # Output: API response in JSON format