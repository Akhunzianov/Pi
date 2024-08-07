from sqlalchemy import Column, BigInteger, sql, ForeignKey

from utils.db_api.db_gino import TimedBaseModel


class Seen(TimedBaseModel):
    __tablename__ = 'seen'
    viewer_id = Column(BigInteger, ForeignKey('users.user_id', ondelete='CASCADE'), primary_key=True)
    viewed_id = Column(BigInteger, ForeignKey('users.user_id', ondelete='CASCADE'), primary_key=True)

    query: sql.select
