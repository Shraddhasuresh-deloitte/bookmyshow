

import movies as movies




class nw (movies):
    def add_new_movie_info(self, movie_dict):
        print("******Welcome Admin*******")
        self.title="lorem"
        self.genre="horror"
        self.length="1hr 20 mins"
        self.cast="John Doe"
        self.admin_rating="5/10  "
        self.director="Moon Fard's"
        self.language = "English  "
        self.show_timings = "8-10,12-2,6-8 "
        self.capacity = "50  "
        movie_dict[3]="Lorem"
        return movies()






class am():
    def edit_movie(self):
        print("******Welcome Admin*******")
        self.title = "annabell"
        self.genre = "horror"
        self.length = "1hr 20 mins"
        self.cast = "John Doe"
        self.admin = "5/10"
        self.director = "Moon Fard's"
        self.language="English "
        self.show_timings="8-10,12-2,6-8 "
        self.capacity="50"
        exit()


class dm():
    def delete_movie(self):
        print("******Welcome Admin*******")
        self.title_del=str(input("Title of the movie to be deleted"))
class movies():
    movies_dict:{ 1:"Movie1", 2:"Movie2"}




class admin():
    print("******** Welcome Admin ********")
    print("1. Add New Movie Info")
    print("2.Edit Movie Info ")
    print("3.Delete Movies ")
task = int(input("Choose task to perform"))
if task == 1:
      nw()
if task == 2:
     am()
if task == 3:
     dm()

class customer():
 def user(self):
print("******** Welcome to Book My Show ********")
usemail = 'User1 @qwe.com'
uspwrd = 'efgh'
usentemail = str(input("Enter email-id"))
usentpass = str(input("Enter Password"))
if (usentemail ==usemail) & (usentpass == uspwrd):
    print("******Welcome User1*******")
    print("1. Movie1")
    print("2. Movie2 ")
    print("3. Lorem ")
    print("4.Logout ")


class guest():
 def new_acc(self,name,email,phone_no,age,passwrd):
     print("****Create new Account****")
     self.name=name
     self.email=email
     self.phone_no=phone_no
     self.age=age
     self.passwrd=passwrd
     customer()




class person():
    ademail = 'admin@gmail.com'
    pswrd = 'abcd'
    email = str(input("Enter email-id"))
    pwrd = str(input("Enter Password"))
    if (email == ademail) & (pwrd == pswrd):
        admin()
    elif customer():

class login():
    def __init__(self,email,pwrd):
        self.__email= email
        self.__pwrd=pwrd
        person()

class options():
    def __init__(self):
        print("******** Welcome to Book My Show ******** ")
        print("1. Login")
        print("2. Register new account")
        print("3. Exit")

    opt = int(input("choose your option"))
    if opt == 1:
        login()
    elif opt == 2:
        guest()
    elif opt == 3:
        exit()
    else:
        print("Wrong choice")
