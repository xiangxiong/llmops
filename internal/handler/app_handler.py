import os
import uuid
from dataclasses import dataclass
from flask import  request;
from openai import OpenAI;
from internal.schema.app_schema import CompletionReq;
from internal.exception import FailException
from pkg.response import success_json, success_message
from internal.service import  AppService
from injector import inject


@inject
@dataclass
class AppHandler:
    app_service: AppService

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

    def create_app(self):
        app = self.app_service.create_app()
        return success_json(f"应用已经创建成功,id为{app.id}")

    def get_app(self,id:uuid.UUID):
        app = self.app_service.get_app(id)
        return success_message(f"应用已经成功修改，修改的名字是:{app.name}")

    def update_app(self,id:uuid.UUID):
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功修改，修改的名字是:{app.name}")

