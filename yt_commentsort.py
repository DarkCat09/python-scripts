import requests

class YtComment:
	def __init__(self, content, authorname, authorurl):
		self._content = content
		self._authorname = authorname
		self._authorurl = authorurl
	@property
	def content(self):
		return self._content
	@property
	def authorname(self):
		return self._authorname
	@property
	def authorurl(self):
		return self._authorurl


def get_comments(videoid, apikey):
	comments = requests.get(
		'https://www.googleapis.com/youtube/v3/commentThreads' + \
		f'?part=id,snippet&videoId={videoid}&textFormat=plainText&key={apikey}').json()
	return comments['items']

def search_in_comments(comments, query):
	filtered = []
	for comment in comments:
		info = comment['snippet']['topLevelComment']['snippet']
		text = info['textDisplay']
		author_name = info['authorDisplayName']
		author_link = info['authorChannelUrl']
		if (text.find(query.lower()) > -1):
			filtered.append(YtComment(text, author_name, author_link))
	return filtered


if __name__ == '__main__':
	apikey = '***YOUR_API_KEY***'
	video_id = input('Enter video identifier:\t')
	search_query = input('Enter search query:\t')
	comments = get_comments(video_id, apikey)
	filtered = search_in_comments(comments, search_query)
	for ytcomment in filtered:
		print('----------')
		print(ytcomment.authorname)
		print(ytcomment.authorurl)
		print(ytcomment.content)
	print('----------')
	input()
