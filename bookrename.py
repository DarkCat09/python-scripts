import os
import re

# ---
# Шаблон для форматирования строки.
# То, как будет переименована книга.
#
# (F-строки не стал использовать для простоты редактирования шаблона)
#
# author=автор,title=название,year=год,ext=расширение(лучше не трогать)
#
template = '{author} -- {title} -- {year}.{ext}'
# ---

# Получаем текущий каталог
curdir = os.getcwd()
# Компилируем регулярку
# https://regexr.com/5q42v
bookregex = re.compile(r'[\[\(]*([А-Яа-я\w\s]+?)[\]\)]*[:\.\-\s]*([А-Яа-я\w\d\s]+?)[:\.\-\s]*(\d+)(?:\.(pdf|doc[x]*|epub|fb2|txt))')

# Получаем дерево каталогов и файлов в curdir
for rootdir, subdirs, files in os.walk(curdir):
	# Пробегаемся по всем файлам в дереве
	for filename in files:
		# Ищем совпадения имени файла с RegEx
		result = bookregex.search(filename)
		# И если получилось, ...
		if (result != None):
			# ... то всё прекрасно, переименовываем по шаблону
			os.rename(os.path.join(rootdir, filename), os.path.join(rootdir, \
				template.format(author=result.group(1),title=result.group(2),year=result.group(3),ext=result.group(4))))
