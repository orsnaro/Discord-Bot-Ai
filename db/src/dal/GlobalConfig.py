import mongoengine as orm

class GlobalConfig(orm.Document):
   bot_master_id = orm.IntField(default= 726888595754844202)
   wizard_bot_id = orm.IntField(default= 1117540489365827594)