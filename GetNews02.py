import feedparser

feed =  feedparser.parse("https://www.nhk.or.jp/rss/news/cat0.xml")
i = 0
newstitle = []
newscontents = []

def createcontents():
    i = 0
    voiceovercontents = ""
    for entry in feed.entries:
        newstitle.append(entry.title)
        newscontents.append(entry.summary)
        i += 1
    for n in range(i):
        print(n)
        #print(newstitle)
        #print(newscontents)
        voiceovercontents = voiceovercontents + newstitle[n] + "　"
        voiceovercontents = voiceovercontents + newscontents[n] + "　　"
    return voiceovercontents

newsvoice = createcontents()
print(newsvoice)
