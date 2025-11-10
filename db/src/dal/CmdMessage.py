import mongoengine as orm
from Message import Message

class Response(orm.EmbeddedDocument):
   text  = orm.StringField()
   media = orm.ListField(orm.URLField)


class CmdMessage(Message):
   name     = orm.StringField(required= True)
   args     = orm.ListField(orm.StringField)  #let even int and numeric vals to be received as srting at first!
   response = orm.EmbeddedDocumentField(Response)
   