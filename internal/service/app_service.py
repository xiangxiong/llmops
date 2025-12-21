import uuid

from dataclasses import  dataclass
from injector import inject
from internal.model import App
from pkg.sqlalchemy import SQLAlchemy

@inject
@dataclass
class AppService:

    db: SQLAlchemy

    def create_app(self) -> App:
        with self.db.session.begin():
            app = App(name="测试机器人", account_id=uuid.uuid4(), icon="", description="这是一个简单的聊天机器人")
            self.db.session.add(app)
            self.db.session.commit()
        return app

    def get_app(self, id: uuid.UUID) -> App:
        app = self.db.session.query(App).get(id);
        return app

    def update_app(self,id:uuid.UUID) -> App:
        with self.db.auto_commit():
            app = self.get_app(id);
            app.name = "慕课聊天机器人1"
        return app

    def delete_app(self,id:uuid.UUID):
        with self.db.auto_commit():
            app = self.get_app(id);
            self.db.session.delete(app)
        return app



