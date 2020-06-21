from django.test import TestCase
import unittest
import requests
import time
# Create your tests here.


class TestClient(TestCase):
    def setUp(self):
        print('setUp')
        self.url = "http://localhost:8000/client/"

    def tearDown(self):
        print('tearDown')

    @unittest.skip
    def test_add_integral(self):
        print('test_demo')
        data = requests.post(url=self.url, data={'user_name': '赵五', 'integral': 9000})
        print(data.json())
    # @unittest.skip
    def test_show_integral(self):
        print('test_demo2')
        start = time.time()
        data = requests.get(url=self.url, params={'user_name': '张三', 'start': 1, 'end': 5})
        print(data.json())
        print('tool %.1f sec' % (time.time() - start))


if __name__ == '__main__':
    TestClient()