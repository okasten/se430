import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from datetime import *
import event  #our Event Class
import user
import data
from functools import partial
#pur User Class


LARGEFONT =("Verdana", 35)

#creating Global List to keep track of users During the running instance of the application since we are not
#going as far as connecting to a database
#if time permits will add auxillary function to store these Data Structures to be called at Application start up
#in order to maintain persistant data

months=["January","February","March","April","May","June","July","August","September","October","November","December"]

currentId=-1
myEvents = list()
eventDis=list()
eHelp=list()


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
        label = ttk.Label(self, text = "", font = ('Arial',15)).grid(row=0,column =2, padx=10, pady=10)
        labelEmail = ttk.Label(self, text ="Please Enter Your Email Address>>").grid(row =3, column =0, padx =10, pady =10)
        labelPass = ttk.Label(self, text ="Please Enter a Password").grid(row =4, column =0, padx =10, pady =10)

        #Entrys for the Login Page
        EntryEmail = ttk.Entry(self)
        EntryEmail.grid(row =3, column =1, padx =10, pady =10)

        EntryPass = ttk.Entry(self)
        EntryPass.grid(row =4, column =1, padx =10, pady =10)




        LoginButton = ttk.Button(self, text ="Login to Account", command = lambda :[LoginPage.Authenticate(controller, EntryEmail.get(), EntryPass.get()), UserPage.showName()]).grid(row = 6, column = 0, padx = 10, pady = 10)
        QuitButton = ttk.Button(self, text ="Quit",command =quit).grid(row = 6, column = 1, padx = 10, pady = 10)
        Register = ttk.Button(self, text ="Register NEW", command = lambda :controller.show_frame(RegistrationPage)).grid(row = 6, column = 2, padx = 10, pady = 10)


    def Authenticate(frameSwitcher, em, ps):
        if (user.User.login(em, ps)):
            print(em)
            global currentUser,currentId
            currentUser = em
            print (currentUser)
            for u in data.users:
                if (u['email']==currentUser):
                    currentId = u['id']
                    print("Current User is ...:"+str(currentId))
                    print(currentUser)
                else:
                    print("NOT A MATCH")

            
            
            frameSwitcher.show_frame(UserPage)
        else:
            print("Authentication Failed")
            frameSwitcher.show_frame(LoginPage)
        


#####Left OFF HERE will create later So far it will login you in and we can switch pages
class UserPage(tk.Frame):
    
    
        
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        c=0        
        #label = ttk.Label(self, text ="Page 2", font = LARGEFONT)
        
        startingDay = date.today()
        m = tk.StringVar()
        month = months[startingDay.month -1]
        m.set(month)
        monthString = m.get()
        
        monthLabel = tk.Label(self, textvariable=m, font=('Arial',25)).grid(row= 1,column=7)
        
        global dayTracker
        dayTracker=0
        global buttonsList
        buttonsList= list()
        counter =0
        for i in range(0,7):
            for j in range(1,3):
                
                calcDay = datetime.now() + timedelta(days = counter)
                numericalDay = str(calcDay.day)+"th"
                numDay= int(str(calcDay.day))

                
                print(calcDay)
                button = tk.Button(self, text = numericalDay, height =3, width=5, command = partial(UserPage.checkDay, numDay, monthString)).grid(row = j, column = i, padx = 5, pady = 5)
                counter=counter+1
                buttonsList.append(button)
                
        for b in buttonsList:
            print(b)

        # button to show frame 2 with text
        # layout2
        logOutButton = tk.Button(self, text =" Log Out ", command = lambda : controller.show_frame(LoginPage)).grid(row = 5, column = 0, padx = 10, pady = 10)
        
        placeHolder = tk.Button(self, text ="All-Events", height = 2, width = 7, command= UserPage.showAllEvents).grid(row = 5, column = 1, padx = 10, pady = 10)

        newEventButton = tk.Button(self, text ="Create-New", command = UserPage.makeNewEvent).grid(row = 5, column = 2, padx = 10, pady = 10)

        myEventsButton = tk.Button(self, text ="Rsvp'd-Events", command = lambda: UserPage.initialize()).grid(row = 5, column = 3, padx = 10, pady = 10)

        hostedEventsButton = tk.Button(self, text ="Hosted-Events", command = lambda: UserPage.initializeH()).grid(row = 5, column = 4, padx = 10, pady = 10)


        nxtWeekButton = tk.Button(self, text ="Next-2wk", command=lambda: UserPage.forward2(self, dayTracker, m)).grid(row = 5, column = 6, padx = 10, pady = 10)

        prvWeekButton = tk.Button(self, text ="Prev-2wk", command=lambda:UserPage.back2(self, dayTracker, m)).grid(row = 5, column = 5, padx = 10, pady = 10)

        
        #nameWindow

    def showName():
        nameGui= tk.Tk()
        textVarName=''
        for names in data.users:
            if currentId == names['id']:
                textVarName=names['name']
        labelName=tk.Label(nameGui, text=textVarName, font=LARGEFONT).grid(row=0, column=0)
        nameGui.mainloop()
        

        ###after column 6 start at row 0 to how ever many events, we create a table of events that User has rsvp'd to using data file
        #find the userId of current User
    
    def forward2(self, dayT, monthV):
        
        dayForward=dayT+14
        global dayTracker
        dayTracker=dayForward
        
        startingDay2 = datetime.now()+timedelta(days=dayTracker)
        month = months[startingDay2.month -1]
        monthV.set(month)
        monStr = monthV.get()
        
        counter2 =dayTracker
        for i2 in range(0,7):
            for j2 in range(1,3):
                
                calcDay = datetime.now() + timedelta(days = counter2)
                numericalDay = str(calcDay.day)+"th"
                numDay= int(str(calcDay.day))
                
                print(calcDay)
                button = tk.Button(self, text = numericalDay, height =3, width=5, command = partial(UserPage.checkDay, numDay, monStr)).grid(row = j2, column = i2, padx = 5, pady = 5)
                counter2=counter2+1
                
    def back2(self, dayT, monthV2):
        dayBack=dayT-14
        global dayTracker
        if dayBack<0:
            dayTracker=0
        else:
            dayTracker=dayBack
        
        startingDay2 = datetime.now()+timedelta(days=dayTracker)
        month = months[startingDay2.month -1]
        monthV2.set(month)
        monStr2 = monthV2.get()

        
        counter2 =dayTracker
        for i2 in range(0,7):
            for j2 in range(1,3):
                
                calcDay = datetime.now() + timedelta(days = counter2)
                numericalDay = str(calcDay.day)+"th"
                numDay= int(str(calcDay.day))
                print(calcDay)
                button = tk.Button(self, text = numericalDay, height =3, width=5, command = partial(UserPage.checkDay, numDay, monStr2)).grid(row = j2, column = i2, padx = 5, pady = 5)
                counter2=counter2+1
        
    def makeNewEvent():
        # create two dates with year, month, day, hour, minute, and second
        #date1 = datetime(2017, 6, 21, 18, 25, 30) constructor example
        global creationGui
        creationGui = tk.Tk()
        
        creationGui.title("Create A New Event")

        LabelTitle = tk.Label(creationGui, text ="Please Enter your events Name:->").grid(row=1, column =1)
        
        
        TextTitle = scrolledtext.ScrolledText(creationGui, wrap = tk.WORD, width = 10, height = 1, font = ("Times New Roman",15))
        TextTitle.grid(row=1, column=2)
        
        TextDes = scrolledtext.ScrolledText(creationGui, wrap = tk.WORD, width = 20, height = 10, font = ("Times New Roman",15))
        TextDes.grid(row=7, column =2)
        

        dayK =tk.IntVar()
        Labelday = tk.Label(creationGui, text ="Day Of :").grid(row=2, column =1)
        entryDay = tk.OptionMenu(creationGui, dayK, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31)
        entryDay.config(width=5, font=('Arial', 8))
        entryDay.grid(row=2, column =2)
        


        monthsList=["January","February","March","April","May","June","July","August","September","October","November","December"]
        LabelMonth = tk.Label(creationGui, text ="Month Of: ").grid(row=3, column =1)
        monthOfCB = tk.StringVar()
        monthOptions = tk.OptionMenu(creationGui, monthOfCB, *monthsList)
        monthOptions.config(width=25, font=('Arial', 12))
        monthOptions.grid(row=3, column=2)

        
        i = tk.IntVar(creationGui)
        tk.Radiobutton(creationGui, text="2021", padx = 20, value=2021, variable =i, command = i.set(2021)).grid(row=4, column=1)
        tk.Radiobutton(creationGui, text="2022", padx = 20, value=2022, variable =i, command = i.set(2022)).grid(row=4, column=2)

        

            
        LabelHour = tk.Label(creationGui, text ="Hour Of: ").grid(row=5, column =1)
        HourVar = tk.IntVar()
        hourOfEntry = tk.OptionMenu(creationGui, HourVar, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12)
        hourOfEntry.config(width=5, font =('Arial',12))
        hourOfEntry.grid(row=5, column =2)
        
        doN=tk.StringVar()
        dayNight = tk.OptionMenu(creationGui, doN, "AM","PM")
        dayNight.config(width = 3, font=('Arial',12))
        dayNight.grid(row=5, column =3)
            
            
            

        Label_Location = tk.Label(creationGui, text ="Location: ").grid(row=6, column =1)
        locationVar = tk.StringVar()
        locationOfCB = tk.OptionMenu(creationGui,locationVar, '614 Main St---Room A - Chrysler Building',  '24 Center Ct. --- Gymnasium') 
        locationOfCB.config(width=30, font=('Arial',12))
        locationOfCB.grid(row=6, column =2)
        

        
        Labeld = tk.Label(creationGui, text ="Please Enter A \nThoughful Description").grid(row=7, column =1)

        def findTime(hourV, dayoN):
            print("----------inside findTime-------------------")
            print("hour")
            print(hourV.get())
            print("am pm..?")
            print(dayoN.get())
            if dayoN.get()=='PM':
                return hourV.get()+12
            elif dayoN.get()=='AM':
                return hourV.get()
            else:
                print("AM PM NOT SELECTED")
                print(dayoN.get)
                return hourV.get()
            

        
        def findLocationNumber(location_Var):
            print("---find location helper function-----")
            print(location_Var.get())
            if (location_Var.get() == '24 Center Ct. --- Gymnasium'):
                locationNumber=1
                print("Location GyM")
                return 1
            else:
                locationNumber=0
                print("Location Room A")
                return 0
            
        
       
        print('the year')
        print(i.get())
        print("title passing ..")
        print(TextTitle.get("1.0",tk.END))
        
        
        CreateButton = tk.Button(creationGui, text="CreateEvent",
                                 command=lambda:[UserPage.createEvent(i.get(),UserPage.findMonth(monthOfCB.get()),
                                                                      dayK.get(), findTime(HourVar, doN), 0, 0, TextTitle.get("1.0",tk.END),
                                                                      TextDes.get("1.0",  tk.END), findLocationNumber(locationVar))]).grid(row = 9, column = 2, padx=5, pady=5)
        exitButton = tk.Button(creationGui, text="Exit", command=creationGui.destroy).grid(row = 10, column = 2, padx=5, pady=5)
        creationGui.mainloop()
        
    def findMonth(StringM):
        print("The selected Month")
        print(StringM)
        if StringM == "January":
            monthNumber=1
        elif StringM == "February":
            monthNumber=2

        elif StringM == "March":
            monthNumber=3

        elif StringM == "April":
            monthNumber=4

        elif StringM == "May":
            monthNumber=5

        elif StringM =="June":
            monthNumber=6

        elif StringM == "July":
            monthNumber=7

        elif StringM ==  "August":
            monthNumber=8    

        elif StringM == "September":
            monthNumber=9

        elif StringM == "October":
            monthNumber=10

        elif StringM == "November":
            monthNumber=11
        
        else :
            monthNumber=12
        print(monthNumber)
        return monthNumber
        #yearInt, monthNumber, day, hour, 0, 0
    def createEvent(y, mN, d, h, mins, secs, TitleIN, TxtD, location):
        print("----------------create Event-----------------------")
        print("Year")
        print(y)
        print("MonthNumber")
        print(mN)
        print("The day is ")
        print(d)
        print("Title in is ..")
        print(TitleIN)
        print("Description")
        print(TxtD)
        print("location")
        print(location)
        print("Hour of event")
        print(h)
        
        #start_datetime, description, name
        eventDateTime = datetime(y,mN,d,h,mins,secs)
        myEvent = event.Event(eventDateTime, TxtD, TitleIN)
        intEventId = myEvent.getId(myEvent)
        myEvent.add_location(location)
        makeEventUserNow = event.EventUser(intEventId, currentId, True)
        print("EventUserCreated")
        UserPage.initialize()
        
    def cancel(stringDesEvent):
        print("-----------cancel Function---------")
        print("to delete This event ID ..")
        print(stringDesEvent)
        target=-1
        print("Current USer ID")
        print(currentId)

        for et in eventDis:
            
            if et[1]==stringDesEvent:
                print("EVENT MATCH FOUND STARTING DELETE")
                print("et[0] is equal to..")
                print(et[0])
                print("et[1] is ..")
                print(et[1])
                target=et[1]
        indexTarget=0
        for evUser in event.event_users:
            if evUser['event_id']==target:
                if evUser['user_id']==currentId:
                    break;
            indexTarget+=1
        print(indexTarget)
        print(event.event_users[indexTarget])
        event.event_users.pop(indexTarget)
        print("You have been removed from Event Roster")
        
    def findT(dayNight, hourSelection):
        return dayNight+hourSelection



    def checkDay(dayN, monthN):
        print("-------entered checkday function-----------")
        print(dayN)
        print(monthN)
        dayGui = tk.Tk()
        titleString = "Make New Event: "+str(monthN)+"-"+str(dayN)+"-2021"
        dayGui.title(titleString)
        
        monthNumber = UserPage.findMonth(monthN)
        dayNumber= dayN
        
        l = tk.IntVar(dayGui)
        tk.Radiobutton(dayGui, text="Room A- Chrysler Building", padx=20, value=1, variable =l, command = l.set(1)).grid(row=3, column =1)
        tk.Radiobutton(dayGui, text="Gymnasium", padx=20, value=0, variable =l, command = l.set(0)).grid(row=3, column =2)
        

        labelTday = tk.Label(dayGui, text="Title   : >>").grid(row=4, column=1)
        titleText = scrolledtext.ScrolledText(dayGui, wrap = tk.WORD, width = 20, height = 1, font = ("Times New Roman",15))
        titleText.grid(row=4, column=2)
        
         
        
        DescL = tk.Label(dayGui, text="Description: >>").grid(row=5, column=1)
        desText = scrolledtext.ScrolledText(dayGui, wrap = tk.WORD, width = 20, height = 10, font = ("Times New Roman",15))
        desText.grid(row=5, column =2)



        timeLabel = tk.Label(dayGui, text="select time").grid(row=6, column=1)
        time = tk.IntVar()
        timeOM = tk.OptionMenu(dayGui, time, 1,2,3,4,5,6,7,8,9,10,11,12)
        timeOM.config(width=2, font=('Arial',12))
        timeOM.grid(row=6, column=2)

        
        amPMvar = tk.IntVar()
        pmRB = tk.Radiobutton(dayGui, text="PM", value =12, command = amPMvar.set(12), ).grid(row=7, column=1)
        amRB = tk.Radiobutton(dayGui, text="AM", value =0, command= amPMvar.set(0)).grid(row=7, column=2)

        hourint = UserPage.findT(time.get(), amPMvar.get())



        submitButton = tk.Button(dayGui, text="submit", command =lambda: UserPage.checkDayEventCreator(2021, monthNumber, dayNumber, 0, 0, 0, l.get(), titleText.get("1.0",tk.END), desText.get("1.0", tk.END)))
        submitButton.grid(row =8, column =2, padx=10, pady=10)
        exitButton = tk.Button(dayGui, text="exit", command= dayGui.destroy).grid(row=8, column=0, padx=10, pady=10)
        

        
        

        



        dayGui.mainloop()
        
    
        
    def checkDayEventCreator(yr, mnN, dayNm, hrz, Mins_in, Secs_in, loc_Numb, ttStr, d_Str):
        print("--------inside checkdayevent creatorrr_---------")
        print("year")
        print(yr)
        print("month")
        print(mnN)
        print("day")
        print(dayNm)
        print(Mins_in)
        print(Secs_in)
        print("loc number")
        print(loc_Numb)
        print("title")
        print(ttStr)
        print("Descript:")
        print(d_Str)

        datetime_DayGui = datetime(yr,mnN,dayNm,hrz, Mins_in, Secs_in)
        print("newevents__datetimeObject--created___")

        newEvent = event.Event(datetime_DayGui, d_Str, ttStr,)
        print("New Event Created")
        dayGui_eventId = newEvent.getId(newEvent)
        print("Event ID Extracted")
        newEvent.add_location(loc_Numb)
        print("location added")

        newUserEvent = event.EventUser(dayGui_eventId, currentId, True)
        print("eventUserObject created")
        return
        
        
    def showAllEvents():
        #iterate through events - if were not 
        print("-------creating all events Window gui-------------")
    
        notRsvp = list()
        myEs= list()
        resvButtons = list()
        for e in event.event_users:
            if e['user_id']==currentId:
                myEs.append(e['event_id'])
        for e2 in event.events:
            if e2['id'] not in myEs:
                notRsvp.append(e2)

        showAll = tk.Tk()
        showAll.title("All Events Available")
        
        for i in range(0,len(notRsvp)):
            labeli= tk.Label(showAll, text = notRsvp[i]['name']).grid(row=i, column=1)
            eventInt = notRsvp[i]['id']
            button= tk.Button(showAll, text="RSVP?", command=partial(UserPage.addSelfEventRoster, eventInt, i)).grid(row=i, column=2)
            resvButtons.append(button)
        showAll.mainloop()



        
    def addSelfEventRoster(event_num, buttonNum):
        print("-------adding self roster--------")
        print("Button Number")
        print(buttonNum)
        print("eventNumber")
        print(event_num)
        print("userId")
        print(currentId)
        data.event_users.append({'event_id':event_num,'user_id':currentId,'is_host':False})
        UserPage.initialize()


        
    def initialize():
        print("----------------initialize function-----------------------")
        print(currentId)
        global myEvents
        myEvents=list()
        for eu in data.event_users:
            if currentId == eu['user_id']:
                myEvents.append(eu['event_id'])

        global eventDis
        eventDis=list()
        for e in data.events:
            if e['id'] in myEvents:
                eventDis.append((e['name'], e['id']))

        print('is myEvents Empty?')
        print(len(myEvents)==0)
        print('is myDes Empty?')
        print(len(eventDis)==0)
        eventGui = tk.Tk()
        eventGui.title("My-Events")
        print("initializing in method initialize now----")
        print(currentUser)
        print('currentID:'+str(currentId))

        if (len(myEvents)!=0):
            print('length of event Dis list')
            print(len(eventDis))
            for num in range(0,len(myEvents)):
                label = tk.Label(eventGui, text=eventDis[num][0] ).grid(row = num, column = 0, padx =5, pady=5)
                eventDPass = int(eventDis[num][1])
                button = tk.Button(eventGui,text='Cancel RSVP', command=partial(UserPage.cancel, eventDPass)).grid(row=num, column = 1, padx=5, pady =5)
                
        else:
            print("No EVENTS")
            label = tk.Label(eventGui, text='NO EVENTS PLEASE RSVP', font=LARGEFONT ).grid(row = 0, column = 0, padx =5, pady=5)

        exitButton = tk.Button(eventGui, text="Exit", command= eventGui.destroy).grid(row = len(myEvents)+1, column = 0, padx=5, pady=5)
        eventGui.mainloop()

        

        
    def updateTime(eventIdinteger):
        print("--------Time Update-------")
        updateTimeGui=tk.Tk()
        labelp=tk.Label(updateTimeGui, text="Please Select A Time", font=('Arial',20)).grid(row=1, column= 0)
        tV = tk.IntVar()
        tk.Radiobutton(updateTimeGui, text="1:00", value =1, variable = tV, command = tV.set(1)).grid(row=0,column=1)
        tk.Radiobutton(updateTimeGui, text="2:00", value =2, variable = tV, command = tV.set(1)).grid(row=1,column=1)
        tk.Radiobutton(updateTimeGui, text="3:00", value =3, variable = tV, command = tV.set(1)).grid(row=2,column=1)
        tk.Radiobutton(updateTimeGui, text="4:00", value =4, variable = tV, command = tV.set(1)).grid(row=3,column=1)
        tk.Radiobutton(updateTimeGui, text="5:00", value =5, variable = tV, command = tV.set(1)).grid(row=4,column=1)
        tk.Radiobutton(updateTimeGui, text="6:00", value =6, variable = tV, command = tV.set(1)).grid(row=5,column=1)
        tk.Radiobutton(updateTimeGui, text="7:00", value =7, variable = tV, command = tV.set(1)).grid(row=6,column=1)
        tk.Radiobutton(updateTimeGui, text="8:00", value =8, variable = tV, command = tV.set(1)).grid(row=7,column=1)
        tk.Radiobutton(updateTimeGui, text="9:00", value =9, variable = tV, command = tV.set(1)).grid(row=8,column=1)
        tk.Radiobutton(updateTimeGui, text="10:00", value =10, variable = tV, command = tV.set(1)).grid(row=9,column=1)
        tk.Radiobutton(updateTimeGui, text="11:00", value =11, variable = tV, command = tV.set(1)).grid(row=10,column=1)
        tk.Radiobutton(updateTimeGui, text="12:00", value =12, variable = tV, command = tV.set(1)).grid(row=11,column=1)
        amPM= tk.IntVar()
        tk.Radiobutton(updateTimeGui, text="AM", value =0, variable = amPM, command = amPM.set(1)).grid(row=13,column=0)
        tk.Radiobutton(updateTimeGui, text="PM", value =12, variable = amPM, command = amPM.set(1)).grid(row=13,column=1)
        updateTimeGui.mainloop()

        


    def updateDay():
        print("--------Time Day-------")
    def updateTit(intIdEvent):
        update_Tit= tk.Tk()
        updateTitle = scrolledtext.ScrolledText(update_Tit, wrap = tk.WORD, width = 10, height = 1, font = ("Times New Roman",12))
        print("--------Time title-------")
        for e in data.events:
            if e['id']==intIdEvent:
                e['name']=updateTitle.get("1.0",tk.END)
        UserPage.Initialize()
                
                

        
    def updateD():
        print("--------Time description-------")
        
     
    def initializeH():
        print("Hosted Events Initilize Button pressed")
        hostedGui = tk.Tk()
        hostedGui.title("My Hosted Events")
        global eventDs
        eventDs = list()
        global userHostIds
        userHostIds = list()
        for evU in event.event_users:
            if evU['user_id']==currentId:
                if evU['is_host']==True:
                    userHostIds.append(evU['event_id'])
        for eDs in event.events:
            if eDs['id'] in userHostIds:
                eventDs.append((eDs['name'],eDs['id']))
        if(len(eventDs)==0):
            tk.Label(hostedGui, text="Hosting No Events", font=LARGEFONT).grid(row=0,column=0)

        for u in range(0, len(eventDs)):
            tk.Label(hostedGui, text=eventDs[u][0]).grid(row=u, column =0, padx=10, pady=10)
            eventIdInt = eventDs[u][1]
            butTime=tk.Button(hostedGui, text= "Update Time", command= partial(UserPage.updateTime, eventIdInt)).grid(row=u, column =1)
            butDay=tk.Button(hostedGui, text= "Update Day", command= partial( UserPage.updateDay)).grid(row=u, column =2)
            buttitle=tk.Button(hostedGui, text= "Update Title", command= partial(UserPage.updateTit, eventIdInt)).grid(row=u, column =3)
            butDes=tk.Button(hostedGui, text= "Update Desc:", command= lambda: UserPage.updateD).grid(row=u, column =4)
        hostedGui.mainloop()

        
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
