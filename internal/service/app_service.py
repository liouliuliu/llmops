import uuid
from dataclasses import dataclass

from flask_sqlalchemy import SQLAlchemy
from injector import inject

from internal.model import App


@inject
@dataclass
class AppService:
    """应用服务逻辑"""
    db: SQLAlchemy

    def create_app(self):
        app = App(name="测试机器人", account_id=uuid.uuid4(), description="这是一个简单的机器人")

        self.db.session.add(app)
        self.db.session.commit()
        return app
    def select_app(self,id: uuid.UUID) -> App:
        app = self.db.session.query(App).get(id)
        return  app
    def update_app(self,id:uuid.UUID) -> App:
        app =  self.select_app(id)
        app.name = "慕课网聊天机器人"
        self.db.session.commit()
        return app
    def delete_app(self,id:uuid.UUID) -> App:
        app = self.select_app(id)
        self.db.session.delete(app)
        self.db.session.commit()
        return app