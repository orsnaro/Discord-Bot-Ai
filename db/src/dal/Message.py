import mongoengine as orm
from JoinedGuild import JoinedGuild



class Channel(orm.EmbeddedDocument):
   ch_id = orm.IntField(required= True, unique= True, primary_key= True)
   name  = orm.StringField()

class Sender(orm.EmeddedDocument):
   user_id = orm.IntField(required= True, unique= True, primary_key= True)
   name    = orm.StringField()
   
class Time(orm.EmbeddedDocument):
   created_at = orm.DateTimeField()
   deleted_at = orm.DateTimeField()


class Message(orm.Document):
   msgId      = orm.IntField(required= True, unique= True, primary_key= True)
   url        = orm.URLField(required= True, unique= True)
   guild      = orm.LazyReferenceField(JoinedGuild, reverse_delete_rule= 1)#nullify
   channel    = orm.EmbeddedDocumentField(Channel)
   sender     = orm.EmbeddedDocumentField(Sender)
   time       = orm.EmbeddedDocumentField(Time)
   is_deleted = orm.BooleanField(default= False)
   