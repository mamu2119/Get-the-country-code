country_code = {'India' : '0091',
                'Russia' : '0025',
                'Bhutan' : '00977'}
print("Country code for India -")
print(country_code.get('India', 'Not Found'))
print("Country code for America -")
print(country_code.get('America', 'Not Found'))