# Parsing linkin-park.ucoz.net and downloading music
# This site is not mine

import requests
from lxml import html
from lxml import etree

site_tree = html.fromstring(requests.get("https://linkin-park.ucoz.net/load/lp_underground/underground_8_0_2008/19").text)
links_for_dl = site_tree.xpath('//a[@style="color:#333; text-decoration:none;" and @class="entryLink"]')
for dllink in links_for_dl:
    correct_dllink = "https://linkin-park.ucoz.net" + (dllink.xpath(".//@href")[0])
    dlpage_tree = html.fromstring(requests.get(correct_dllink).text)
    music_file = open("C:\\Users\\Acer\\Music\\Linkin Park\\Downloaded\\" + correct_dllink.split("/")[6] + ".mp3", 'wb')
    music_file.write(requests.get("https://linkin-park.ucoz.net" + (dlpage_tree.xpath('//td[@class="commSbmFl"]/a/@href')[0])).content)
    music_file.close()
