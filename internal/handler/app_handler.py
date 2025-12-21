import os
from flask import  request;
from openai import OpenAI;
from internal.schema.app_schema import CompletionReq;
from internal.exception import FailException

class AppHandler:

    def completion(self):
        """
        处理用户请求
        """
        req = CompletionReq();

        if not req.validate():
            return req.errors;

        # 1、提取从接口中传递的参数
        query = request.json.get("query");

        # 2、构建 openAI 客户端，并发起请求.
        client = OpenAI(api_key=os.getenv("OPEN_API_KEY"),
                        base_url=os.getenv("OPEN_API_URL"));

        # 3、得到请求结果，返回客户端.
        completion = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query},
            ]
        );

        content = completion.choices[0].message.content;
        return {"content": content};

    def ping(self):
        raise FailException("测试2222异常")
        # return {"ping":"pong"}