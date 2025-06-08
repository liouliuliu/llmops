from flask import Flask

from config.config import Config
from internal.exception import CustomException
from internal.model import App
from internal.router import Router
from pkg.response.http_code import HttpCode
from pkg.response.response import json, Response
from pkg.sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


class Http(Flask):
    def __init__(self,
                 *args,
                 conf: Config,
                 db: SQLAlchemy,
                 migrate:Migrate,
                 router: Router,
                 **kwargs):
        super().__init__(*args, **kwargs)
        # 初始化应用配置
        self.config.from_object(conf)
        # 注册绑定异常错误
        self.register_error_handler(Exception, self._register_error_handler)
        # 初始化 flask 扩展
        db.init_app(self)
        migrate.init_app(self,db,directory="internal/migration")
        # 注册应用路由
        router.register_router(self)

    def _register_error_handler(self, error: Exception):
        if isinstance(error, CustomException):
            return json(Response(
                code=error.code,
                message=error.message,
                data=error.data if error.data is not None else {}
            ))
        if self.debug:
            raise error
        else:
            return json(Response(
                code=HttpCode.FAIL,
                message=str(error),
                data={}
            ))
