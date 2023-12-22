#mini Application
#Movie class
#Creation Multiple movie Objects
#Add these Objects to the list
#try to get these objects one by one fronm the list
#Invoke Movie class Functionality object on that obect

class Movie:
    def __init__(self, title, hero, heroine):
        self.title = title
        self.hero=hero
        self.heroine=heroine
    def info(self):
        print("movie Name:",self.title)
        print("Hero Name:", self.hero)
        print("heroine Name:", self.heroine)


list_of_movies=[]

while True:
    title=input("Enter movie name:")
    hero=input("enter hero name")
    heroine=input("enter the heroine name")
    m=Movie(title,hero,heroine)
    list_of_movies.append(m)
    print("Movie added to the list")
    option=input("Do you want to add one more movie [Yes | No]:")
    if option.lower()=='no':
        break
for movie in list_of_movies:
    movie.info()








