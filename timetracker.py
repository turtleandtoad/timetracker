# -*- coding: utf-8 -*-
"""
Created on Thu Jan  8 07:20:33 2015

@author: joylee
"""

#import pandas as pd
#import numpy as np
#import matplotlib.pyplot as plt
import datetime

#def importdf(filename):
#    df = pd.read_csv(filename+".csv", names=["date", "time", "subject", "topic", "course", "notes"],sep=",", infer_datetime_format=True)
#    pd.to_timedelta(df.time, unit="m")
#    return df
#
#if __name__ == "__main__":
#    countdata = importdf("decembercounts")
#    


import tkinter as tk

class Window(tk.Tk):
    def __init__(self):
        
        tk.Tk.__init__(self)
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)
        
        self.frames = {}
        frame = MainPage(container, self)
        self.frames[MainPage] = frame
        frame.grid(row=0, column=0, sticky = "nsew")
        self.show_frame(MainPage)
    
    def show_frame(self, cont): 
        frame = self.frames[cont]
        frame.tkraise()
        
class MainPage(tk.Frame):
    start_time = 0
    end_time = 0
    elapsed_time = 0
    notes = "NA"

    subjectlist = ["CS", "Exercise", "Language", "Music", "Stats", "Writing"]

    alltopics = {"CS": ["CSS/HTML", "JavaScript", "Python", "R", "SQL",
    "C/C++"], 
    "Exercise": ["Mix"], "Language": ["Korean", "Russian", "Spanish"],
    "Music": ["Flute", "Piano"],
    "Stats": ["School"], "Writing": ["Fun"]} 

    allcourses = {"CSS/HTML": ["Mozilla", "freeCodeCamp"],
                "JavaScript": ["Mozilla", "Codecademy"],
                "Python": ["Counts"],
                "R": ["Fun"],
                "SQL": ["Codecademy", "HackerRank", "Pgexercises", "SQLZOO"],
                "C/C++": ["EdX: CS50"],
                "Mix": ["NA"],
                "Korean": ["Anki", "Duolingo", "Immersion"],
                "Russian": ["Anki", "Duolingo", "Immersion"],
                "Spanish": ["Anki", "Duolingo", "Immersion"],
                "School": ["STAT303", "STAT335", "STAT410"],
                "Fun": ["NA"]
                }

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        #label = tk.Label(self, text="Main Page")
        #label.grid(sticky=E)
       
        #start button
        start_button = tk.Button(self, text="Start", 
                           command=lambda: self.start(self.start_time))
        start_button.grid(row=0, column=0)

        #stop button
       	stop_button = tk.Button(self, text = "Stop!", command=lambda: self.stop(self.end_time))
       	stop_button.grid(row=1, column=0)

        #enter button
        enter_button = tk.Button(self, text = "Print Everything", 
               command=lambda: self.enter_time(self.start_time, self.end_time))
        enter_button.grid(row=2, column=0)

        #subject menu
        self.s_entry = tk.StringVar()
        self.s_entry.set("CS")
        self.s_entry.trace("w", self.update_topics)
        self.subject_menu = tk.OptionMenu(self, self.s_entry, *self.subjectlist)
        self.subject_menu.config(width=12)
        self.subject_menu.grid(row=0, column=1)

        #topic menu
        self.t_entry = tk.StringVar()
        self.t_entry.trace("w", self.update_courses)
        self.topic_menu = tk.OptionMenu(self, self.t_entry, "")
        self.topic_menu.config(width=12)
        self.topic_menu.grid(row=1, column=1)

        #course menu
        self.c_entry = tk.StringVar()
        self.course_menu = tk.OptionMenu(self, self.c_entry, "")
        self.course_menu.config(width=12)
        self.course_menu.grid(row=2, column=1)

        #notes box
        self.notes_label = tk.Label(self, text="Notes", anchor="n")
        self.notes_label.grid(row=0, column=3, sticky="N")

        self.notes_box = tk.Text(self, height=15)
        self.notes_box.grid(row=1, column=3, sticky="E")
        
        # self.notes_scroll = tk.Scrollbar(self, orient="vertical", command=self.notes_box.yview)
        # self.notes_box.config(yscrollcommand=self.notes_box.set)
        # self.notes_scroll.grid(row=1, column=3, sticky=N+S)


    def start(self, start_time):
        print("Starting timer!")
        self.start_time = datetime.datetime.now()
        return self.start_time
    
    def stop(self, end_time):
        self.end_time = datetime.datetime.now()
        self.elapsed_time = self.end_time - self.start_time
        print("Stopping timer")
        return self.end_time
        return self.elapsed_time


    def update_topics(self, *args):
        self.subject = self.s_entry.get()
        topiclist = self.alltopics[self.s_entry.get()]
        self.t_entry.set(topiclist[0])

        tmenu = self.topic_menu["menu"]
        tmenu.delete(0, "end")

        for topic in topiclist:
            tmenu.add_command(label=topic, command=lambda t=topic: self.t_entry.set(t))

    def update_courses(self, *args):
        self.topic = self.t_entry.get()
        courselist = self.allcourses[self.t_entry.get()]
        self.c_entry.set(courselist[0])

        cmenu = self.course_menu["menu"]
        cmenu.delete(0, "end")

        for course in courselist:
            cmenu.add_command(label=course, command=lambda c=course: self.c_entry.set(c))


    def note_taking(self):
         self.notes = self.notes_box.get("1.0", "end-1c")
         return self.notes

    def enter_time(self, start_time, end_time):
        self.course = self.c_entry.get()
        self.notes = self.notes_box.get("1.0", "end-1c")
        print(start_time)
        print(end_time)
        print(self.elapsed_time)
        print(self.subject)
        print(self.topic)
        print(self.course)

        count_file = open("counts2.csv", "a")
        count_file.write("\n" + str(self.start_time) + "," + str(self.elapsed_time) +
                         "," + str(self.subject) + "," + str(self.topic) + "," + 
                         str(self.course) + "," + str(self.notes))

        count_file.close()    


app = Window()
 
app.mainloop()

