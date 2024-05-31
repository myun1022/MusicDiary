from sqlalchemy import Column, BigInteger, String, Date, Text, JSON

class Diary(Base):
    __tablename__ = "diaries"

    id = Column(BigInteger, primary_key=True)
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    music = Column(JSON)
    createdAt = Column(Date, nullable=False)