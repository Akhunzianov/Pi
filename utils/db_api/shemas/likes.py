from sqlalchemy import Column, BigInteger, sql, ForeignKey, TIMESTAMP

from utils.db_api.db_gino import TimedBaseModel


class Likes(TimedBaseModel):
    __tablename__ = 'likes'
    liker_id = Column(BigInteger, ForeignKey('users.user_id', ondelete='CASCADE'), primary_key=True)
    likee_id = Column(BigInteger, ForeignKey('users.user_id', ondelete='CASCADE'), primary_key=True)

    query: sql.select
