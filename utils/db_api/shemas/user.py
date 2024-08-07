from sqlalchemy import Column, BigInteger, String, sql, Integer, Text, ARRAY

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    user_id = Column(BigInteger, primary_key=True)
    name = Column(String(200), nullable=False)
    gender = Column(String(200), nullable=False)
    tg_username = Column(String(200), nullable=True)
    age = Column(Integer, nullable=True)
    university = Column(String(200), nullable=True)
    degree = Column(String(200), nullable=True)
    study_year = Column(Integer, nullable=True)
    major = Column(String(200), nullable=True)
    description = Column(Text, nullable=True)
    media = Column(ARRAY(String), nullable=True)
    media_tag = Column(ARRAY(String), nullable=True)

    query: sql.select
