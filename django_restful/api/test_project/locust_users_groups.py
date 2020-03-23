from locust import  HttpLocust,TaskSet,task,between

class UserBehavior(TaskSet):

    def on_start(self):
        #设置user和group参数下标初始值
        self.users_index=0
        self.groups_index=0

    @task
    def test_users(self):
        #读取参数
        users_id=self.locust.id[self.users_index]
        url="/users/"+str(users_id)+'/'
        self.client.get(url)
        #取余运算循环遍历参数
        self.users_index=(self.users_index+1)%len(self.locust.id)

    @task
    def test_groups(self):
        #参数化
        groups_id=self.locust.id[self.groups_index]
        url="/groups/"+str(groups_id)+"/"
        self.client.get(url)
        self.groups_index=(self.groups_index+1)%len(self.locust.id)

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    #参数配置
    id=[1,2]
    wait_time = between(3, 6)
    #host配置
    host = 'http://127.0.0.1:8000'

