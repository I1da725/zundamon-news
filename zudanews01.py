from voicevox import Client
import asyncio
import feedparser

feed =  feedparser.parse("https://www.nhk.or.jp/rss/news/cat0.xml")

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
        voiceovercontents = voiceovercontents + newstitle[n]
        voiceovercontents = voiceovercontents + newscontents[n]
    return voiceovercontents


async def main():
    async with Client() as client:
        newsvoice = createcontents()
        print(newsvoice)
        audio_query = await client.create_audio_query(
            newsvoice , speaker=1
        )
        with open("newsvoice.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker=1))


if __name__ == "__main__":
    asyncio.run(main())


