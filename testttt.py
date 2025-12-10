from app.data.users import get_user
from app.data.db import connect_database
conn = connect_database("DATA/intelligence_platform.db")

print(type(get_user(conn, 'stev')))


# 
#

