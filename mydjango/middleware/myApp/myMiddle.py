from django.utils.deprecation import MiddlewareMixin

class MyMiddle(MiddlewareMixin):

    # 在分发url之前执行的中间件
    def process_request(self,request):
        print("get参数为：",request.GET.get("a"))#例如：http://127.0.0.1:8000/?a=1
