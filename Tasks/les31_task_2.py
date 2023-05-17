import multiprocessing
import requests
import json

# Task 3


def get_comments(name: str):
    comments = []
    query = {"subreddit": name}
    url = f"https://api.pushshift.io/reddit/comment/search/"
    response = requests.get(url, params=query)
    data = response.json()["data"]
    for comment in data:
        comm = comment.get('body')
        date_time = comment.get("utc_datetime_str")
        comments.append((comm, date_time))
    comment_dict = {comm: data for comm, data in sorted(comments, key=lambda x: x[1])}
    with open("comments_process.json", "w") as file:
        json.dump(comment_dict, file, indent=3)


if __name__ == '__main__':
    username = input("Enter username: ")
    process_comment = multiprocessing.Process(target=get_comments, args=(username,))
    process_comment.start()
    process_comment.join()
