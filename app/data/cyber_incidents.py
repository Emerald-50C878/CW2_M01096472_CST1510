import pandas as pd

def migrate_cyber_incidents(conn):
    path = "C:\Users\sstev\CW2--M01096472--CST1510\CW2_M01096472_CST1510\DATA\cyber_incidents.csv"
    df = pd.read.csv(path)
    print(df.head())
    df.to_sql('cyber_incidents', conn, if_exists = 'append', index = False)
    print("Data loaded successfully! ")

def get_all_cyber_incidents(conn):
    sql = "SELECT * FROM cyber incidents"
    data = pd.read_sql(sql, conn)
    return data