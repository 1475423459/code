from locust import HttpLocust,TaskSet,task,between

class UserBehavior(TaskSet):

    @task(2)
    def test_user(self):
        self.client.get("/users/")

    @task(1)
    def test_groups(self):
        self.client.get("/groups/")

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    wait_time = between(3, 6)

