from flask import  request;

class AppHandler:


    def completion(self):
        """
        处理用户请求
        """
        # 1、提取从接口中传递的参数
        query = request.json.get("query");

        # 2、构建 openAI 客户端，并发起请求.


        # 3、得到请求结果，返回客户端.




    def ping(self):
        return {"ping":"pong"}