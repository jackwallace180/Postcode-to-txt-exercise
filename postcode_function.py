import requests
import json




def write_to_file(file, postcode):
    try:
        with open(file, 'a') as opened_file:
            post_codes = requests.get("http://api.postcodes.io/postcodes/" + postcode)
            post_code_dict = post_codes.json()
            info = post_code_dict['result']['country']
            opened_file.write(postcode + ' ,' + info + '\n')
    except FileNotFoundError:
        print('oh no file not found')

