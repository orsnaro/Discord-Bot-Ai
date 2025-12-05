import mongoengine as orm


# Each discord user have their global i.e(can be used across multiple servers) playlist of local track 
# And soon tracks from online platforms
#TODO: this needs wizy track Queue feature to be implimented first

class Playlist(orm.Document): #TODO
	...

