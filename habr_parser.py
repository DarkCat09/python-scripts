import requests
from lxml import html
from lxml import etree

useragent_headers={
    "User-agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'
    }

site_tree = html.fromstring(requests.get("https://habr.com/", headers=useragent_headers).text)

habr_news = site_tree.xpath('//div[@class="new-block"]//ul[@class="content-list"]/li[@class="content-list__item content-list__item_news-topic"]' +
                            '//a[@class="news-topic__title"]')

for habr_new in habr_news:

    try:
        article_text = etree.tostring(
            html.fromstring(requests.get(habr_new.xpath('./@href')[0], headers=useragent_headers).text).xpath(
                '//div[@class="post__text post__text-html post__text_v1" and @id="post-content-body"]')[0]).decode("utf-8")
    except Exception:
        continue

    print()
    print("----- beginning of article")
    print(habr_new.text_content())
    print("----- beginning of text")
    print(article_text)
    print("----- end of text")
    print("----- end of article")
