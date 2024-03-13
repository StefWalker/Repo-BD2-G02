import json
import random

from faker import Faker

# Create an instance of the Faker class
fake = Faker()

# Define the fields for posts, comments, and user information
post_fields = ["title", "content"]
comment_fields = ["text", "timestamp"]
user_fields = ["name", "email", "age"]

# Generate a list of 30 users with random information
users = []
for i in range(30):
    user = {}
    user["name"] = fake.name()
    user["email"] = fake.email()
    user["age"] = random.randint(18, 60)
    users.append(user)

# Generate random posts and comments for each user
data = []
for user in users:
    num_posts = random.randint(1, 100)
    for _ in range(num_posts):
        post = {}
        post["user"] = user["name"]
        post["user_email"] = user["email"]
        post["user_age"] = user["age"]
        post["post"] = {}
        post["post"]["title"] = f'Random title for {user["name"]}'
        post["post"]["content"] = f'Random content for {user["name"]} {fake.text()}'
        post["post"]["timestamp"] = fake.date_time().isoformat()
        num_comments = random.randint(0, 5)
        post["comments"] = []
        for _ in range(num_comments):
            comment = {}
            comment["user"] = random.choice(users)["name"]
            comment["user_email"] = random.choice(users)["email"]
            comment["user_age"] = random.choice(users)["age"]
            comment["comment"] = {}
            comment["comment"]["text"] = f"Random text {fake.text()}"
            comment["comment"]["timestamp"] = fake.date_time().isoformat()
            post["comments"].append(comment)
        data.append(post)

# Save the data in a JSONL file
with open("data.jsonl", "w") as file:
    for item in data:
        file.write(json.dumps(item) + "\n")
