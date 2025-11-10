import mongoengine as orm
from Message import Message

class Content(orm.EmbeddedDocument):
   text  = orm.StringField()
   media = orm.ListField(orm.URLField)

class ChatMessage(Message):
   content = orm.EmbeddedDocument(Content)
   tags    = orm.ListField(orm.StringField(max_length=25))