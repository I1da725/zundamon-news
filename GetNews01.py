import feedparser

feed =  feedparser.parse("https://www.nhk.or.jp/rss/news/cat0.xml")
print("=======================================================")
for entry in feed.entries:
    print('タイトル:', entry.title)
    print('まとめ:', entry.summary)
    print('URL:', entry.link)
    print("=======================================================")
