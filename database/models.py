from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Enum, Float
from sqlalchemy.orm import relationship

from .database import Base

class Users(Base):
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    created_at = Column(DateTime)
    updated_at = Column(DateTime)

class Stocks(Base):
    id = Column(Integer, primary_key=True)
    symbol = Column(String, unique=True)
    company_name = Column(String)
    exchange = Column(String)

class UserStockPreferences(Base):
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("Users.id"))
    stock_id = Column(Integer, ForeignKey("Stocks.id"))
    investment_goal = Column(Enum("Long-Term","Short-Term"))
    risk_tolerance = Column(Enum("High","Medium", "Low"))

class HistoricalStockData(Base):
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey("Stocks.id"))
    date = Column(DateTime)
    open_price = Column(Float)
    close_price = Column(Float)
    low_price = Column(Float)
    high_price = Column(Float)
    volume = Column(Integer)

class StockPredictions(Base):
    id = Column(Integer, primary_key=True)
    stock_id = Column(Integer, ForeignKey("Stocks.id"))
    user_id = Column(Integer, ForeignKey("Users.id"))
    prediction_date = Column(DateTime)
    predicted_price = Column(Float)
    

    
    
