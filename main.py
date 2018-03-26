#terminal: source activate timetrackenv

import kivy
kivy.require("1.10.0")

import datetime


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

#from kivy.garden.graph import Graph, MeshLinePlot

from kivy.lang import Builder
Builder.load_file("main.kv")

class TabPanelsWidget(TabbedPanel):

###############     subject/topic/course updating functions     #########
    alltopics = {"Subjects": ["Topics"], "CS": ["CSS/HTML", "JavaScript", "Python", "R",
    "SQL", "C/C++"], "Exercise": ["Cardio", "Mix", "Strength", "Yoga"], "Language": ["Korean", "Russian",
    "Spanish"],"Music": ["Flute", "Piano"], "Stats": ["School"], "Writing":
    ["Fun"]}

    allcourses = {"Topics": ["Courses"], "CSS/HTML": ["Mozilla", "freeCodeCamp"],
    "JavaScript": ["Mozilla", "Codecademy"], "Python": ["Counts"], "R":
    ["Fun", "Counts"], "SQL": ["Codecademy", "HackerRank", "Pgexercises", "SQLZOO"],
    "C/C++": ["EdX: CS50"], "Cardio": ["NA"], "Mix": ["NA"], "Strength": ["NA"], "Yoga": ["NA"],
    "Korean": ["Anki", "Duolingo",
    "Immersion"], "Russian": ["Anki", "Duolingo", "Immersion"], "Spanish":
    ["Anki", "Duolingo", "Immersion"], "School": ["STAT303", "STAT335",
    "STAT410", "Research"], "Fun": ["NA"] }


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


################    timer functions     ######################

    start_time = 0
    elapsed_time = 0

    startbtn = ObjectProperty(None)
    stopbtn = ObjectProperty(None)

    def start(self):
        #print("Starting timer!")

        self.startbtn.background_normal = ""
        self.startbtn.background_color = (0.219, 0.490, 0.509, 1)

        self.start_time = datetime.datetime.now()
        return self.start_time

             ###### adds data to counts2.csv ######
    def stop(self):
        #print("Ending timer!")
        self.startbtn.background_color = (0.345, 0.345, 0.345, 1)

        self.stopbtn.background_normal = ""
        self.stopbtn.background_color = (0.219, 0.490, 0.509, 1)

        self.elapsed_time = datetime.datetime.now() - self.start_time

        count_file = open("counts2.csv", "a")
        count_file.write("\n" + str(self.start_time) + "," + 
            str(self.elapsed_time) + "," + str(self.smenu.text) + 
            "," + str(self.tmenu.text) + "," + str(self.cmenu.text) + 
            "," + str(self.notesbox.text))

        count_file.close()   

    def reset(self):
        self.startbtn.background_color = (0.345, 0.345, 0.345, 1)
        self.stopbtn.background_color = (0.345, 0.345, 0.345, 1)

        self.start_time = 0
        self.elapsed_time = 0

        self.smenu.text = "Subjects"

        self.tmenu.values = ["Topics"]
        self.tmenu.text = "Topics"

        self.cmenu.values = ["Courses"]
        self.cmenu.text = "Courses"

        self.notesbox.text = ""

    

#######################     journal functions     #################

    journalbox = ObjectProperty(None)
    hlevel = ObjectProperty(None)

    def journal_enter(self):
        journal_file = open("journal.csv", "a")
        journal_file.write("\n" + str(datetime.datetime.now()) +
            "," + str(self.hlevel.value) +
            "," + str(self.journalbox.text))





########################         App      ########################

class MyApp(App):
    subjectlist = ["CS", "Exercise", "Language", "Music", "Stats", "Writing"]
    topiclist = []
    courselist = []

    def build(self):
        return TabPanelsWidget()



if __name__ == "__main__":
    MyApp().run()





    