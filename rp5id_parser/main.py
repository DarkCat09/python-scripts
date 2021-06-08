import re
import requests
import urllib.parse
from lxml import html

# Get web page with Russian cities from RP5
russian_cities_page = requests.get('https://rp5.ru/Погода_в_России')
russian_cities_tree = html.fromstring(russian_cities_page.content)

# Extract the table with cities
columns = russian_cities_tree.xpath('//div[@class="countryMap"]//div[@class="countryMap-cell"]')

# File
cities_file = open('cities.csv', 'wt')
cities_file.write('ID,City\n')

# Write all identifiers and cities
city_link_regex = re.compile(r'^https*://rp5.ru/(Погода_в[А-Яа-я\w.,\-()]+)')
added_ids = []
for col in columns:
    ids = col.xpath('.//span[@class="Ajax-PointID"]//@id')
    for city in ids:

        str_to_write = ''
        # Check identifier
        for added in added_ids:
            if city == added:
                break
        else:
            # Write identifier
            added_ids.append(city)
            str_to_write += str(city)

            # Comment this block to execute script faster and prevent DDoS detecting on RP5 server
            city_response = requests.get('https://rp5.ru/town.php?id=' + city)
            redirect = urllib.parse.unquote(city_response.url)
            print(redirect)
            str_to_write += (',' + city_link_regex.search(redirect).group(1))

            # Write to file
            cities_file.write(str_to_write + '\n')
            print(city)

cities_file.close()
print('')
input('Press ENTER to exit ...')
