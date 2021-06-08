import os
import mmap

def remove_twice_soi(imgdata):
	first_soi_index = imgdata.find(b'\xff\xd8') + 2
	main_data = imgdata[first_soi_index:]
	return imgdata[:first_soi_index] + main_data.replace(b'\xff\xd8', b'\x00\x00')

if __name__ == '__main__':
	for root, dirs, files in os.walk(os.curdir):
		for file in files:
			if (file.startswith('FJIMG_')):
				print(os.path.join(root, file))
				print('read')
				readbytes = b''
				soi = False
				img = open(os.path.join(root, file), 'rb')
				readbytes = img.read()
				corrected = remove_twice_soi(readbytes)
				img.close()
				print('write')
				newimg = open(os.path.join(root, file.replace('FJIMG_', 'corrected_')), 'wb')
				newimg.write(corrected)
				newimg.close()
				print('OK')
				print('')
