from django.test import TestCase
import requests

# Create your tests here.
class UserTest(TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/users'


    def test_get_user(self):
        r=requests.get(self.base_url+'/1/')
        result=r.json()

        self.assertEqual(result['username'],'root')

    def test_add_user(self):
        form_data={'username':'zxw2229','email':'zxw668@qq.com','groups':'http://127.0.0.1:8000/groups/2/'}
        r=requests.post(self.base_url+'/',data=form_data)
        result=r.json()

        self.assertEqual(result['username'],'zxw2229')

class GroupTest(TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/groups'

    def test_group_developer(self):
        r=requests.get(self.base_url+'/2/')
        result=r.json()

        self.assertEqual(result['name'],'group2')