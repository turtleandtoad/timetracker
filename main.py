#terminal: source activate timetrackenv

import kivy
kivy.require("1.10.0")

from datetime import datetime
import csv

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout 
from kivy.uix.textinput import TextInput
from kivy.uix.dropdown import DropDown
from kivy.uix.label import Label
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.slider import Slider
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.properties import StringProperty
from kivy.clock import Clock

# from kivy.garden.graph import Graph, MeshLinePlot
# import kivy.garden.matplotlib

# import matplotlib
# matplotlib.use('module://kivy.garden.matplotlib.backend_kivy')


from kivy.lang import Builder
Builder.load_file("main.kv")

class TabPanelsWidget(TabbedPanel):

###############     subject/topic/course updating functions     #########
    alltopics = {"Subjects": ["Topics"], "CS": ["CSS/HTML", "JavaScript", "Python", "R",
    "SQL"}

    allcourses = {"Topics": ["Courses"], "CSS/HTML": ["Mozilla", "freeCodeCamp"],
    "JavaScript": ["Mozilla", "Codecademy"], "Python": ["Counts", "Text Adventure", "Text Analytics", "NLP", "Other"], "R":
    ["Fun", "Counts"], "SQL": ["Codecademy", "HackerRank", "Pgexercises", "SQLZOO"]}


    smenu = ObjectProperty(None)
    tmenu = ObjectProperty(None)
    cmenu = ObjectProperty(None)
    notesbox = ObjectProperty(None)

    def update_topics(self):
        self.topiclist = self.alltopics[self.smenu.text]
        self.tmenu.values = self.topiclist
        return self.topiclist
    
    def update_courses(self):
        self.courselist = self.allcourses[self.tmenu.text]
        self.cmenu.values = self.courselist
        return self.courselist


################    Timer functions     ######################

    start_time = 0
    elapsed_time = StringProperty("0:00:00")

    startbtn = ObjectProperty(None)
    stopbtn = ObjectProperty(None)

    def sw_start(self):
        Clock.schedule_interval(self.update_sw, 1)

    def update_sw(self, nap):
        if self.start_time != 0:
            self.elapsed_time = str(datetime.now().replace(microsecond=0) - self.start_time)
        else:
            self.elapsed_time = "0:00:00"

    def start(self):
        #print("Starting timer!")

        self.startbtn.background_normal = ""
        self.stopbtn.background_normal = ""
        
        self.startbtn.background_color = (0.219, 0.490, 0.509, 1)
        self.stopbtn.background_color = (0.345, 0.345, 0.345, 1)

        self.start_time = datetime.now().replace(microsecond=0)
        self.sw_start()
        return self.start_time

             ###### adds data to counts.csv ######
    def stop(self):
        #print("Ending timer!")
        self.startbtn.background_color = (0.345, 0.345, 0.345, 1)

        self.stopbtn.background_normal = ""
        self.stopbtn.background_color = (0.219, 0.490, 0.509, 1)

        while self.start_time != 0:

            self.notesbox.text = self.notesbox.text.replace("\n", "///")
            self.notesbox.text = self.notesbox.text.replace(",", ">>")

            count_file = open("counts.csv", "a")
            count_file.write("\n" + str(self.start_time) + "," + 
                self.elapsed_time + "," + str(self.smenu.text) + 
                "," + str(self.tmenu.text) + "," + str(self.cmenu.text) + 
                "," + str(self.notesbox.text))

            count_file.close()  

            self.start_time = 0
            self.elapsed_time = "0:00:00"

    def reset(self):
        self.startbtn.background_color = (0.345, 0.345, 0.345, 1)
        self.stopbtn.background_color = (0.345, 0.345, 0.345, 1)

        self.start_time = 0
        self.elapsed_time = "0:00:00"

        self.smenu.text = "Subjects"

        self.tmenu.values = ["Topics"]
        self.tmenu.text = "Topics"

        self.cmenu.values = ["Courses"]
        self.cmenu.text = "Courses"

        self.notesbox.text = ""

    

#######################     Journal functions     #################

    journalbox = ObjectProperty(None)
    hlevel = ObjectProperty(None)

    def journal_enter(self):
        journal_file = open("journal.csv", "a")
        journal_file.write("\n" + str(datetime.now()) +
            "," + str(self.hlevel.value) +
            "," + str(self.journalbox.text))

        self.hlevel.value = 5
        self.journalbox.text = ""


#######################     Graph functions     #################




#######################     Settings functions     #################


########################         App      ########################

class MyApp(App):
    subjectlist = ["CS"]
    topiclist = []
    courselist = []

    def build(self):
        return TabPanelsWidget()



if __name__ == "__main__":
    MyApp().run()





    
