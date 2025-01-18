import requests
import json


def get_posts(url, posts_count=5):
    response = requests.get(url)
    data = response.json()
    result = []
    for index, item in enumerate(data):
        if index >= posts_count:
            break
        result.append({"title": item["title"], "body": item["body"]})
    return result


url = "https://jsonplaceholder.typicode.com/posts"
posts = get_posts(url)

for index, post in enumerate(posts):
    print(f"Заголовок {index + 1}:", post["title"])
    print(f"Тело поста {index + 1}:", post["body"])
    print()
