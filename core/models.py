#!/usr/bin/python3
""" class urls """
from sqlalchemy import Column, String, Integer, DateTime
from datetime import datetime
from core.db import Base


class URL(Base):
    """Representation of urls"""

    __tablename__ = "urls"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    original_url = Column(String(255), nullable=False)
    short_code = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow, nullable=False)
