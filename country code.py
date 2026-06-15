country_code = {'India' : '0091',
                'Australia' : '0025',
                'Nepal' : '00977',
                'Japan' : '0051'}

print("country code for India -")
print(country_code.get('India', 'Not Found'))

print("country code for Japan -")
print(country_code.get('Japan', 'Not Found'))
