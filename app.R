#
# This is a Shiny web application. You can run the application by clicking
# the 'Run App' button above.
#
# Find out more about building applications with Shiny here:
#
#    http://shiny.rstudio.com/
#

library(shiny)

# Define UI for application that draws a histogram
ui <- fluidPage(
  
   # Application title
   titlePanel("Timer"),
   
   # Sidebar with a slider input for number of bins 
   sidebarLayout(
      sidebarPanel(
    
        selectInput(inputId = "Subject",
                    label = "Subject",
                    choices = c("CS", "Exercise", "Language", "Music",
                                "Stats", "Writing")),
        selectInput(inputId = "Topic",
                    label = "Topic",
                    choices = c("NA")),
        
        selectInput(inputId = "Course",
                    label = "Course",
                    choices = c("NA"))
      ),
      
      mainPanel(
        
        textOutput("currentTime")
        
      )
      
   )
)

# Define server logic required to draw a histogram
server <- function(input, output) {
   alltopics = list(CS=c("CSS.HTML", "JavaScript", "Python", "R", "SQL", "C/C++"), 
                    Exercise=c("Cardio", "Mix", "Strength", "Yoga"),
                    Language=c("Korean", "Russian", "Spanish"),
                    Music=c("Flute", "Piano"),
                    Stats=c("School"),
                    Writing=c("Fun"))
   allcourses = list(CSS.HTML=c("Mozilla", "freeCodeCamp"),
                     JavaScript=c("Mozilla", "Codecademy"),
                     Python=c("Counts"),
                     R=c("Counts"))
   
   topiclist <- reactive({
     topiclist <- alltopics(parse(text=input$Subject))
     topiclist <- as.list(topiclist)
     return(topiclist)
   })
   
   
   output$currentTime <- renderText({
     paste("Time", Sys.time())
   })
   
   
}

# Run the application 
shinyApp(ui = ui, server = server)

