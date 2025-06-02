import os
import uuid
from dataclasses import dataclass

from flask import request
from injector import inject
from openai import OpenAI
from internal.schema.app_schema import CompletionReq
from pkg.response import success_json, validate_error_json, success_message
from internal.exception import FailException
from internal.service import AppService


@inject
@dataclass
class AppHandler:
    """应用控制器"""
    app_service: AppService

    def create_app(self):
        """调用服务创建新的app记录"""
        app = self.app_service.create_app()
        return success_message(f"应用已创建,id为{app.id}")
    def select_app(self, id: uuid.UUID):
        """查询app"""
        app = self.app_service.select_app(id)
        return success_message(f"应用已经成功获取，名字是{app.name}")
    def update_app(self, id: uuid.UUID):
        """更新app"""
        app = self.app_service.update_app(id)
        return success_message(f"应用已经成功更新，名字是{app.name}")
    def delete_app(self, id: uuid.UUID):
        """删除app"""
        app = self.app_service.delete_app(id)
        return success_message(f"应用已经成功删除，id为{app.id}")

    def completion(self):
        """聊天接口"""
        # 1.提取接口中的输入信息
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)
        query = request.json.get("query")

        # 2.构建OPENAI客户端，并发起请求
        client = OpenAI(
            # 若没有配置环境变量，请用百炼API Key将下行替换为：api_key="sk-xxx",
            api_key=os.getenv("DASHSCOPE_API_KEY"),
            base_url=os.getenv("DASHSCOPE_BASE_URL"),
        )
        # 3.得到请求相应，将OPENAI响应返回给前端
        completion = client.chat.completions.create(
            model="qwen-plus",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": query}
            ],
        )
        content = completion.choices[0].message.content
        return success_json({"content": content})

    def ping(self):
        raise FailException("数据未找到")
