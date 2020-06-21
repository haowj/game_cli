from django.shortcuts import render
from django.views import View
from client.models import ClientData
from dss.Serializer import serializer
from django.shortcuts import HttpResponse
import asyncio

def response_as_json(data, foreign_penetrate=False):
    json_string = serializer(data=data, output_type="json", foreign=foreign_penetrate)
    response = HttpResponse(
        json_string,
        content_type="application/json",
    )
    response["Access-Control-Allow-Origin"] = "*"
    return response

class IntegralSelect(View):
    def __init__(self):
        super(IntegralSelect, self).__init__()
        self.name = None
        self.start = None
        self.end = None
        self.data = None
        self.loop = None
        self.name_integral = None

    @staticmethod
    def post(request):
        name = request.POST.get('user_name')
        integral = request.POST.get('integral')
        data = {
            "code": 200,
            "msg": "成功",
        }
        try:
            ClientData.objects.update_or_create(defaults={'integral': integral}, user_name=name)
        except Exception as e:
            data["code"] = 500
            data["msg"] = str(e)
        return response_as_json(data)

    def get(self, request,):
        data = {
            "code": 200,
            "msg": "成功",
            "data": '',
        }
        try:
            self.name = request.GET.get('user_name')
            self.start = int(request.GET.get('start'))
            self.end = int(request.GET.get('end'))
            self.data = ClientData.objects.all().order_by('-integral').values('user_name', 'integral')
            self.name_integral = ClientData.objects.get(user_name=self.name).integral
        except Exception as e:
            data["code"] = 500
            data["msg"] = str(e)
            return response_as_json(data)
        self.loop = asyncio.new_event_loop()
        asyncio.set_event_loop(self.loop)
        try:
            results = self.loop.run_until_complete(self.gather_tasks())
        finally:
            self.loop.close()
        data["data"] = results
        return response_as_json(data)


    async def gather_tasks(self):
        """
         也可以用回调函数处理results
        task1 = self.loop.run_in_executor(None, self.io_task1, 2)
        future1 = asyncio.ensure_future(task1)
        future1.add_done_callback(callback)

        def callback(self, future):
            print("callback:",future.result())
        """
        tasks = (
            self.make_future(self.ranking_points),
            self.make_future(self.binary_search)
        )
        results = await asyncio.gather(*tasks)
        return results

    async def make_future(self, func, *args):
        future = self.loop.run_in_executor(None, func, *args)
        response = await future
        return response

    def ranking_points(self):
        tem_s = self.start - 1
        data = self.data[tem_s :self.end]

        for tem in data:
            tem_s += 1
            tem['id'] = tem_s
        return data

    def binary_search(self):
        name_integral = self.name_integral
        data_list = self.data
        low = 0
        high = len(data_list) - 1
        while low <= high:
            mid = (low + high) // 2  # 取中间值
            if data_list[mid]['integral'] == name_integral:
                return {'user_name': self.name,'integral': name_integral, 'id': mid + 1}
            elif data_list[mid]['integral'] < name_integral:
                high = mid - 1
            else:
                low = mid + 1
        return {'user_name': self.name,'integral': name_integral, 'id': -1}

