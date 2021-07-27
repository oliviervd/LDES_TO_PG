import pandas
from sqlalchemy import create_engine

engine = create_engine('postgresql://username:password@localhost:5432/mydatabase')
df.to_sql('table_name', engine)