import requests

imgsfile = open('list.txt', 'rt')
imgslist = imgsfile.readlines()
imgsfile.close()

try:
	for img in imgslist:

		url = img.strip()

		result = requests.get(url).content
		filepath = url.split('/')

		file = open(filepath[len(filepath) - 1], 'wb')
		file.write(result)
		file.close()

	print('Done!')

except KeyboardInterrupt:
	print('Stopped by keyboard')

except Exception as ex:
	print(ex)

input('')
