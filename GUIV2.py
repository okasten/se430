import tkinter as tk
from tkinter import ttk
import Event  #our Event Class
import user   #pur User Class


LARGEFONT =("Verdana", 35)

#creating Global List to keep track of users During the running instance of the application since we are not
#going as far as connecting to a database
#if time permits will add auxillary function to store these Data Structures to be called at Application start up
#in order to maintain persistant data 
UsersList = list()
AuthList = [("email@mapaydin.com","MooseyPoo"),("Olivia@gmail.com","OlivesareGreen23"),("jaimi@aol.com","carebears29")]
EventRosters= list()


class tkinterApp(tk.Tk):
    
    # __init__ function for class tkinterApp 
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

            # initializing frame of that object from
            # startpage, page1, page2 respectively with 
            # for loop
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
        labelPhone = ttk.Label(self, text ="Please Enter Your PhoneNumber>>").grid(row =3, column =0, padx =10, pady =10)
        labelEmail = ttk.Label(self, text ="Please Enter Your Email Address>>").grid(row =4, column =0, padx =10, pady =10)
        labelPass = ttk.Label(self, text ="Please Enter a Password").grid(row =5, column =0, padx =10, pady =10)

        #here are the input feilds for the page
        EntryName = ttk.Entry(self)
        EntryName.grid(row=2, column =1, padx =10, pady =10)
        
        EntryPhone = ttk.Entry(self)
        EntryPhone.grid(row =3, column =1, padx =10, pady =10)
        
        EntryEmail = ttk.Entry(self)
        EntryEmail.grid(row =4, column =1, padx =10, pady =10)
        
        EntryPass = ttk.Entry(self)
        EntryPass.grid(row =5, column =1, padx =10, pady =10)

        

        


        loginButton = ttk.Button(self, text ="Already a User? ",
                                         command = lambda :controller.show_frame(LoginPage)).grid(row = 6, column = 1, padx = 10, pady = 10)
    

        ## button to show frame 2 with text layout2
        CreateButton = ttk.Button(self, text ="Create Account",
                                          command = lambda : [makeNewUser, controller.show_frame(LoginPage)]).grid(row = 6, column = 2, padx = 10, pady = 10)

    def makeNewUser():
            userInstance = User( EntryName.get(), EntryPhone.get(), EntryEmail.get(), EntryPass.get(), False)
            UsersList.add(userInstance) #adds the user to our User list seems redundent rn but useful when abstracting the Events later
            print("New user created") #print to see if point reached

            AuthList.add((EntryEmail.get(), EntryPass.get()))
            #above we add the email and pass into a seperate list for authentication purposes.

            
            


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        
        tk.Frame.__init__(self, parent)

        #labels for Page
        label = ttk.Label(self, text ="LoginPage", font = LARGEFONT).grid(row = 0, column = 2, padx = 10, pady = 10)
        labelEmail = ttk.Label(self, text ="Please Enter Your Email Address>>").grid(row =3, column =0, padx =10, pady =10)
        labelPass = ttk.Label(self, text ="Please Enter a Password").grid(row =4, column =0, padx =10, pady =10)

        #Entrys for the Login Page
        EntryEmail = ttk.Entry(self)
        EntryEmail.grid(row =3, column =1, padx =10, pady =10)
        
        EntryPass = ttk.Entry(self)
        EntryPass.grid(row =4, column =1, padx =10, pady =10)




        def Authenticate():
            #if condition is met then do controller.show_frame(UserPage))
            print("Authenticating")

            for emails in AuthList:
                print("Authenticating")
                if(emails[0]==EntryEmail.get()):
                    if(emails[1] == EntryPass.get()):
                        print("Authenticated")
                        controller.show_frame(UserPage)
                    else:
                        #reload the loginPage for now also want to show a dialog to
                        #direct user that the password was incorrect
                        controller.show_frame(LoginPage)
                else:
                    Label.text("WE COULD NOT FIND YOUR EMAIL ARE YOU REGISTERED???")

        

        LoginButton = ttk.Button(self, text ="Login to Account", command =Authenticate).grid(row = 6, column = 0, padx = 10, pady = 10)
        QuitButton = ttk.Button(self, text ="Quit",command =quit).grid(row = 6, column = 1, padx = 10, pady = 10)
        Register = ttk.Button(self, text ="Register NEW", command = lambda :controller.show_frame(RegistrationPage)).grid(row = 6, column = 2, padx = 10, pady = 10)


                    

            
            

#####Left OFF HERE will create later So far it will login you in and we can switch pages 
class UserPage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
    
        # putting the button in its place by 
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
    
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


class AdminPage(tk.Frame): 
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        label.grid(row = 0, column = 4, padx = 10, pady = 10)

        # button to show frame 2 with text
        # layout2
        button1 = ttk.Button(self, text ="Page 1",
                            command = lambda : controller.show_frame(Page1))
    
        # putting the button in its place by 
        # using grid
        button1.grid(row = 1, column = 1, padx = 10, pady = 10)

        # button to show frame 3 with text
        # layout3
        button2 = ttk.Button(self, text ="Startpage",
                            command = lambda : controller.show_frame(StartPage))
    
        # putting the button in its place by
        # using grid
        button2.grid(row = 2, column = 1, padx = 10, pady = 10)


# Driver Code
app = tkinterApp()
app.mainloop()
