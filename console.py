import pdb
from models.artist import Artist
from models.album import Album

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository


artist_repository.delete_all()

artist_1 = Artist("Spice Girls")
artist_repository.save(artist_1)

artist_2 = Artist("Backstreet Boys")
artist_repository.save(artist_2)


res = artist_repository.select_all()
for artist in res:
    print(artist.__dict__)


pdb.set_trace()
