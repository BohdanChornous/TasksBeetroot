import aiohttp
import asyncio
import json

# Task 2
async def main(name: str):
    comments = []
    query = {"subreddit": name}
    url = f"https://api.pushshift.io/reddit/comment/search/"
    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=query) as response:
            print("Staatus: ", response.status)
            data = await response.json()
            for comment in data['data']:
                comm = comment.get('body')
                date_time = comment.get("utc_datetime_str")
                comments.append((comm, date_time))
            comment_dict = {comm: data for comm, data in sorted(comments, key=lambda x: x[1])}
            with open("comments_asyncio.json", "w") as file:
                json.dump(comment_dict, file, indent=3)
                print("Complited")


if __name__ == '__main__':
    name = input("Enter username: ")
    asyncio.run(main(name))


