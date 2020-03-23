import requests
import unittest
from mysql_action import DB
import yaml
import logging
class UserTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/users'

    def test_001_get_user(self):
        logging.info('-----test_001_get_user')
        r=requests.get(self.base_url+'/1/')
        result=r.json()

        self.assertEqual(result['username'],'sutune')

    # @unittest.skip('skip add user')
    def test_002_add_user(self):
        logging.info('-----test_002_add_user')
        form_data={'id':3,'username':'zxw666','email':'zxw666@qq.com','groups':'http://127.0.0.1:8000/groups/2/'}
        r=requests.post(self.base_url+'/',data=form_data)
        result=r.json()

        self.assertEqual(result['username'],'zxw666')

    # @unittest.skip('skip test_delete_user')
    def test_003_delete_user(self):
        logging.info('-----test_003_delete_user')
        r=requests.delete(self.base_url+'/2/')

        self.assertEqual(r.status_code,204)

    def test_004_update_user(self):
        logging.info('-----test_004_update_user')
        form_data={'email':'zxw2018@163.com'}
        r=requests.patch(self.base_url+'/1/',data=form_data)
        result=r.json()

        self.assertEqual(result['email'],'zxw2018@163.com')

class GroupTest(unittest.TestCase):
    def setUp(self):
        self.base_url='http://127.0.0.1:8000/groups'
        self.auth=('51zxw','zxw20182018')

    def test_001_group_developer(self):
        logging.info('-----test_001_group_developer')
        r=requests.get(self.base_url+'/1/')
        result=r.json()

        self.assertEqual(result['name'],'Developer')


    def test_002_add_group(self):
        logging.info('-----test_002_add_group')
        form_data={'name':'Pm'}
        r=requests.post(self.base_url+'/',data=form_data)
        result=r.json()

        self.assertEqual(result['name'],'Pm')

    def test_003_update_group(self):
        logging.info('-----test_003_update_group')
        form_data={'name':'Boss'}
        r=requests.patch(self.base_url+'/2/',data=form_data)
        result=r.json()

        self.assertEqual(result['name'],'Boss')

    def test_004_detele_group(self):
        logging.info('-----test_004_detele_group')
        r=requests.delete(self.base_url+'/1/',)

        self.assertEqual(r.status_code,204)


if __name__ == '__main__':
    db=DB()
    f = open('datas.yaml', 'r')
    datas = yaml.load(f)
    db.init_data(datas)
    unittest.main()