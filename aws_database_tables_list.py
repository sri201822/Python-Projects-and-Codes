import boto3
client = boto3.client('glue',region_name='us-east-1')
responseGetDatabases = client.get_databases()
databaseList = responseGetDatabases['DatabaseList']
db_name=[]
for i in range(len(databaseList)):
    db_name.append(databaseList[i]['Name'])
x=[]
for i in db_name:
    y=client.get_tables( DatabaseName = i )
    x.append(y['TableList'])
table_name=[]
database_name=[]
for i in range(len(x)):
    for j in x[i]:
        table_name.append(j['Name'])
        database_name.append(j['DatabaseName'])
tables=pd.DataFrame(table_name)
tables.columns=['table_name']
tables['db_name']=database_name
tables
