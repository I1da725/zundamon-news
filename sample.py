from voicevox import Client
import asyncio


async def main():
    async with Client() as client:
        audio_query = await client.create_audio_query(
            "おはよーございます。ずんだもんなのだ。", speaker=1
        )
        with open("voice3.wav", "wb") as f:
            f.write(await audio_query.synthesis(speaker=1))


if __name__ == "__main__":
    asyncio.run(main())
