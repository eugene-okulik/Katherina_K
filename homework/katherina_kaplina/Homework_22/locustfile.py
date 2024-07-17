from locust import task, HttpUser
import random


class PostUser(HttpUser):

    @task(1)
    def get_all_posts(self):
        self.client.get('/posts')

    @task(3)
    def get_one_post(self):
        self.client.get(f'/posts/{random.randint(1, 100)}', name="/posts/[id]")
