# from mongoengine import  Document, ListField, StringField, URLField, LazyReferenceField, ReferenceField, LineStringField 
import mongoengine as orm
import os
import keys

def init_db():
   is_production = True if 'IS_PRODUCTION' in os.environ and os.environ['IS_PRODUCTION'] == '1' else False
   if is_production: #currently the db is in same server as the bot i.e.(use localhost conn string)
      conn_string = r'mongodb://localhost:27017/'
   else: #the DB is in the home server and I usually develop not from home server machine :) ! i.e.(use remote  conn string)
      conn_string = keys.mongo_db_conn_str
      
   conn = orm.connect(host=conn_string)
   
   return conn