from datetime import datetime

from sqlalchemy import Column
import uuid;

from sqlalchemy import (
    Column,
    UUID,
    String,
    Text,
    DateTime,
    PrimaryKeyConstraint,
    Index
)
from internal.extension.database_extenstion import db


class App(db.Model):
    """
    应用表
    """
    __tablename__ = "app"
    __table_args__ = (
        PrimaryKeyConstraint('id',name="pk_app_id"),
        Index('idx_app_account_id', 'account_id'),
    )

    id = Column(UUID, default=uuid.uuid4,nullable=False)
    account_id = Column(UUID, nullable=False)
    name = Column(String(255), nullable=False)
    icon = Column(String(255), nullable=True)
    description = Column(Text, nullable=True)
    updated_at = Column(DateTime, default=datetime.now, onupdate=datetime.now,nullable=False)
    created_at = Column(DateTime, default=datetime.now,nullable=False)