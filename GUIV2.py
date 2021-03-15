import tkinter as tk
from tkinter import ttk
from datetime import *
import event  #our Event Class
import user
import data
#pur User Class


LARGEFONT =("Verdana", 35)

#creating Global List to keep track of users During the running instance of the application since we are not
#going as far as connecting to a database
#if time permits will add auxillary function to store these Data Structures to be called at Application start up
#in order to maintain persistant data

months=["January","February","March","April","May","June","July","August","September","October","November","December"]

currentUser= None



class calendarApp(tk.Tk):

    # __init__ function for class calendarApp
    def __init__(self, *args, **kwargs):

        # __init__ function for class Tk
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a structure to contain everything
        box = tk.Frame(self)
        box.pack(side = "top", fill = "both", expand = True)

        box.grid_rowconfigure(0, weight = 1)
        box.grid_columnconfigure(0, weight = 1)

        # initializing frames to an empty array
        self.frames = {}

        # iterating through a tuple consisting
        # of the different page layouts
        for F in (RegistrationPage, LoginPage, UserPage, AdminPage):

            frame = F(box, self)
            #initialize frames
            self.frames[F] = frame

            frame.grid(row = 0, column = 0, sticky ="nsew")

        #should be first page we see at startUp
        self.show_frame(RegistrationPage)

    def show_frame(self, cont):
        frame = self.frames[cont]
        frame.tkraise()


class RegistrationPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        # Labels for the input fields of the register Page
        label = ttk.Label(self, text ="Register?", font = LARGEFONT).grid(row = 1, column = 0, padx = 10, pady = 10)
        labelName = ttk.Label(self, text ="Please Enter Your name>>>").grid(row =2, column =0, padx =10, pady =10)
        labelEmail = ttk.Label(self, text ="Please Enter Your Email Address>>").grid(row =3, column =0, padx =10, pady =10)
        labelPass = ttk.Label(self, text ="Please Enter a Password").grid(row =4, column =0, padx =10, pady =10)

        #here are the input feilds for the page
        EntryName = ttk.Entry(self)
        EntryName.grid(row=2, column =1, padx =10, pady =10)

        EntryEmail = ttk.Entry(self)
        EntryEmail.grid(row =3, column =1, padx =10, pady =10)

        EntryPass = ttk.Entry(self)
        EntryPass.grid(row =4, column =1, padx =10, pady =10)






        loginButton = ttk.Button(self, text ="Already a User? ",
                                         command = lambda :controller.show_frame(LoginPage)).grid(row = 5, column = 1, padx = 10, pady = 10)


        ## button to show frame 2 with text layout2
        CreateButton = ttk.Button(self, text ="Create Account",
                                          command = lambda :[RegistrationPage.makeNewUser(controller, EntryName.get(), EntryEmail.get(), EntryPass.get())]).grid(row = 5, column = 2, padx = 10, pady = 10)


    def makeNewUser(frameSwitch, newName, newEmail, newPass):
        newPerson = user.User(newName, newEmail, newPass, False)
        #data.users.append(newPerson)
        userL = {'id':newPerson.id , 'name':newPerson.name,'email':newPerson.email, 'password':newPerson.password,'is_admin':newPerson.is_admin}
        
        data.users.append(userL)
        #  print(userL)
        print("New user created") #print to see if point reached
        frameSwitch.show_frame(LoginPage)




class LoginPage(tk.Frame):
    def __init__(self, parent, controller):

        tk.Frame.__init__(self, parent)

        #labels for Page
        label = ttk.Label(self, text ="Login-Page", font = LARGEFONT).grid(row = 0, column = 2, padx = 10, pady = 10)
        labelEmail = ttk.Label(self, text ="Please Enter Your Email Address>>").grid(row =3, column =0, padx =10, pady =10)
        labelPass = ttk.Label(self, text ="Please Enter a Password").grid(row =4, column =0, padx =10, pady =10)

        #Entrys for the Login Page
        EntryEmail = ttk.Entry(self)
        EntryEmail.grid(row =3, column =1, padx =10, pady =10)

        EntryPass = ttk.Entry(self)
        EntryPass.grid(row =4, column =1, padx =10, pady =10)




        LoginButton = ttk.Button(self, text ="Login to Account", command = lambda :LoginPage.Authenticate(controller, EntryEmail.get(), EntryPass.get())).grid(row = 6, column = 0, padx = 10, pady = 10)
        QuitButton = ttk.Button(self, text ="Quit",command =quit).grid(row = 6, column = 1, padx = 10, pady = 10)
        Register = ttk.Button(self, text ="Register NEW", command = lambda :controller.show_frame(RegistrationPage)).grid(row = 6, column = 2, padx = 10, pady = 10)


    def Authenticate(frameSwitcher, em, ps):
        if (user.User.login(em, ps)):
            currentUser = str (em)
            frameSwitcher.show_frame(UserPage)
        else:frameSwitcher.show_frame(LoginPage)
        


#####Left OFF HERE will create later So far it will login you in and we can switch pages
class UserPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)

        currentId =-1
    
        myEvents = []
        eventDis=[]
        for u in data.users:
            if (u['email']==currentUser):
                currentId = u['id']
                print(currentId)
        for eu in data.event_users:
            if currentId == eu['user_id']:
                myEvents.append(eu['event_id'])

        for e in data.events:
            if e['id'] in myEvents:
                eventDis.append()

        
        
        
        #label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        
        startingDay = date.today()
        month = months[startingDay.month -1]
        labelTop = ttk.Label(self, text =month, font = LARGEFONT)
        labelTop.grid(row = 0, column = 0, padx = 10, pady = 10)
        
        
        counter =0
        
        for i in range(0,7):
            for j in range(1,3):
                
                calcDay = datetime.now() + timedelta(days = counter)
                numericalDay = str(calcDay.day)+"th"
                
                print(calcDay)
                self.button = tk.Button(self, text = numericalDay, height =3, width=5, command = lambda: checkDay(numericalDay)).grid(row = j, column = i, padx = 5, pady = 5)
                counter=counter+1
                

        # button to show frame 2 with text
        # layout2
        button1 = tk.Button(self, text ="Quit", height = 2, width = 7, command = lambda : quit).grid(row = 5, column = 1, padx = 10, pady = 10)

        button2 = tk.Button(self, text ="New Event", command = lambda : controller.show_frame(RegistrationPage)).grid(row = 5, column = 2, padx = 10, pady = 10)


        ###after row 5 we create a table of events that User has rsvp'd to using data file
        print(currentId)
        if (len(myEvents)!=0):
            c=0
            for num in range(7,8+len(myEvents)):
                des= eventDis[c]
                label = ttk.Label(self, text =des, font =('Arial',15)).grid(row = num, column = 1, padx =5, pady=5)
                button = tk.Button(self, text = "Cancel RSVP", command= cancel(c)).grid(row = num, column =2, padx=5, pady =5)
            
    def checkDay(datetime):
        print(datetime.now())
        
    def createCalendar(direction):
        print("Calendar")



class AdminPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="_ADMIN_PAGE_", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

   
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1)).grid(row = 1, column = 1, padx = 10, pady = 10)


        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage)).grid(row = 2, column = 1, padx = 10, pady = 10)


# Driver Code
app = calendarApp()
app.mainloop()
