import os
import uuid
from dataclasses import dataclass

from flask import request
from injector import inject
from openai import OpenAI
from internal.schema.app_schema import CompletionReq
from pkg.response.response import success_json, validate_error_json, success_message
from internal.exception import FailException
from internal.service import AppService
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.chat_models import ChatTongyi
from langchain_core.output_parsers import StrOutputParser


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

    def debug(self, app_id: uuid.UUID):
        """聊天接口"""
        # 1.提取接口中的输入信息
        req = CompletionReq()
        if not req.validate():
            return validate_error_json(req.errors)
        # 2.组件
        prompt = ChatPromptTemplate.from_template("{query}")
        llm = ChatTongyi()
        parser = StrOutputParser()
        # 3.构建链
        chain = prompt | llm | parser
        # 4.调用链
        content = chain.invoke({"query": req.query.data})
        return success_json({"content": content})

    def ping(self):
        raise FailException("数据未找到")
