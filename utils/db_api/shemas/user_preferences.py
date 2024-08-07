from sqlalchemy import Column, BigInteger, String, sql, Integer, ForeignKey

from utils.db_api.db_gino import TimedBaseModel


class UserPreferences(TimedBaseModel):
    __tablename__ = 'users_preferences'
    user_id = Column(BigInteger, ForeignKey('users.user_id', ondelete='CASCADE'), primary_key=True)
    min_age = Column(Integer, nullable=False)
    max_age = Column(Integer, nullable=False)
    gender = Column(String(200), nullable=False)

    query: sql.select
