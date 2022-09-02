#Import Libatu
import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput

#Create My Grid (columns = 2) 
class myGrid(GridLayout):
    def __init__(self, **kwargs):
        super(myGrid, self).__init__(**kwargs)
        #my column
        self.cols = 2
        #create Label and Input text Name
        self.add_widget(Label(text="Name: "))
        self.Name = TextInput(multiline=False)
        self.add_widget(self.Name)
        #create Label and Input text LastName
        self.add_widget(Label(text="Last Name: "))
        self.Last_Name = TextInput(multiline=False)
        self.add_widget(self.Last_Name)
        #create Label and Input text Email
        self.add_widget(Label(text="Email: "))
        self.Email = TextInput(multiline=False)
        self.add_widget(self.Email)
#here Name your application and run 
class FirstApp(App):

    def build(self):
        return myGrid()


#run 
if __name__ == "__main__":
    FirstApp().run()
