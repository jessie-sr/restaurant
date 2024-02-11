# SQLAlchemy base and engine setup.

from sqlalchemy import create_engine

DATABASE_URI = 'postgresql+psycopg2://jessiesun:Sr6208H%llo1019@localhost/restaurant_dev_db'
engine = create_engine(DATABASE_URI, echo=True)
