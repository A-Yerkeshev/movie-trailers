import os
import media
import fresh_tomatoes
from flask import Flask

app = Flask(__name__)

# Populate the template with data
taxi = media.Movie("Taxi",
                   '''To work off his tarnished driving record, a hip taxi
                   driver must chauffeur a loser police inspector on the
                   trail of German bank robbers.''',
                   'static/img/taxi1.jpg',
                   "static/videos/taxi1.mp4")
taxi_2 = media.Movie("Taxi 2",
                     '''Police inspector Emilien and his taxi-driver pal
                     Daniel are back, this time on the tail of a group of
                     Japanese yakuza.''',
                     'static/img/taxi2.png',
                     "static/videos/taxi2.mp4")
taxi_3 = media.Movie("Taxi 3",
                     '''Out to stop a new gang disguised as Santa Claus, Emilien
                     and Daniel must also handle major changes in their
                     personal relationships.''',
                     'static/img/taxi3.jpg',
                     "static/videos/taxi3.mp4")
taxi_4 = media.Movie("Taxi 4",
                     '''Unlucky, clumsy, charming Marseile PD detective Emilien
                     Coutant-Kerbalec must assist worse-than-Clouseau
                     commissioner Gibert guarding a Belgian criminal reputed as
                     dangerous as - and caged like Hannibal Lector.''',
                     'static/img/taxi4.jpg',
                     "static/videos/taxi4.mp4")

# Open the page in browser
@app.route('/')
def openPage():
  return fresh_tomatoes.open_movies_page([taxi, taxi_2, taxi_3, taxi_4])

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 4321))
    app.run(host='0.0.0.0', port=port)

#Authors attribution
#https://en.wikipedia.org/w/index.php?curid=24751162
#By Source, Fair use, https://en.wikipedia.org/w/index.php?curid=1124037
#https://en.wikipedia.org/w/index.php?curid=4842798
#By Source, Fair use, https://en.wikipedia.org/w/index.php?curid=37030442


