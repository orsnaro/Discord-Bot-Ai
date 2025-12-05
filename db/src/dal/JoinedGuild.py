import mongoengine as orm

class GuildParams(orm.EmbeddedDocument):
   auto_memequote_state = orm.IntField(default= 1)
   wizy_ai_type         = orm.StringField(default= "deep")
   quotesz              = orm.IntField(default= 200)

class GuildRole(orm.EmbeddedDocument):
   role_id               = orm.IntField(required= True, unique= True, primary_key= True)
   role_name             = orm.StringField(required=True)
   
class CmdAllowedRoles(orm.EmbeddedDocument):
   cmd_name              = orm.StringField(required= True)
   allowed_roles         = orm.ListField(orm.EmbeddedDocumentField)
   
class JoinedGuild(orm.Document):
   #NOTE: for now bot can be assigned  3 channels of each type (admin, voice, chat, feed) per Guild
   guild_id             = orm.IntField(required= True, unique= True, primary_key= True)
   admin_channels       = orm.ListField(orm.IntField(), max_length= 3)
   wizy_voice_channels  = orm.ListField(orm.IntField(), max_length= 3)
   wizy_chat_channels   = orm.ListField(orm.IntField(), max_length= 3)
   wizy_feed_channels   = orm.ListField(orm.IntField(), max_length= 3)
   params               = orm.EmbeddedDocumentField(GuildParams)
   cmds_allowed_roles   = orm.ListField(orm.EmbeddedDocumentField)