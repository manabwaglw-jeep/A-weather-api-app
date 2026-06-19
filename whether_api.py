import sys
import requests
from PyQt5.QtWidgets import (QApplication,QWidget,QLabel,
                             QLineEdit,QPushButton,QVBoxLayout)
from PyQt5.QtCore import Qt,QSize
from PyQt5.QtGui import QMovie

class WeatherApp(QWidget):
    def __init__(self):
        super().__init__()
        self.city_label=QLabel("Enter the city name:",self)
        self.city_input=QLineEdit(self)
        self.get_weather_button=QPushButton("Get Weather",self)
        self.temperature_label=QLabel(self)
        self.emoji_label=QLabel(self)
        self.description_label=QLabel(self)
        self.initUI()
    
        
    def initUI(self):
        self.setWindowTitle("Weather app")
        self.setFixedSize(500, 580)
        
    
        vbox=QVBoxLayout() # it arranges the box from top to bottom
        
        vbox.setContentsMargins(25, 25, 25, 25)
        vbox.setSpacing(15)
        
        vbox.addWidget(self.city_label)
        vbox.addWidget(self.city_input)
        vbox.addWidget(self.get_weather_button)
        vbox.addWidget(self.temperature_label)
        
        vbox.addWidget(self.description_label)
        vbox.addWidget(self.emoji_label, alignment=Qt.AlignCenter)
        vbox.addWidget(self.description_label)
        
        self.setLayout(vbox) # giving position to all widgites by setlayout method
        
        self.city_label.setAlignment(Qt.AlignCenter) # align the widget to the center
        self.city_input.setAlignment(Qt.AlignCenter)
        
        self.temperature_label.setAlignment(Qt.AlignCenter)
        self.description_label.setAlignment(Qt.AlignCenter)
       
        self.emoji_label.setFixedSize(160, 160)
       
        self.emoji_label.setAlignment(Qt.AlignCenter)
        # now making it colourfull using css
        
        self.city_label.setObjectName("city_label") # setting a object name to the code
        self.city_input.setObjectName("city_input")
        self.get_weather_button.setObjectName("get_weather_button")
        self.temperature_label.setObjectName("temperature_label")
        self.emoji_label.setObjectName("emoji_label")
        self.description_label.setObjectName("description_label")
        
        
        
        
        self.setStyleSheet("""
                           
                           QWidget{
                               background-color:#1e252b ;
                           }
                           QLabel{ 
                               font-family: 'Segoe UI', calibri;
                                color: #ffffff;
                               
                            }
                           
                           QLineEdit#city_input{
                               font-size: 18px;
                               background-color: #2c3238;
                                color: #ffffff;                
                                border: 1px solid #4f5b66;
                                border-radius: 6px;
                                min-height: 40px;
                           }
                           QLabel#city_label{
                               font-size: 30px;
                               font-style:italic;
                           
                           }
                           QPushButton#get_weather_button {
                                font-size: 24px;
                                font-weight: bold;
                                min-height: 60px;
                                min-width: 220px;
                                border: none;
                                border-radius: 8px;
                                background-color:white ;
                            }
                            QPushButton#get_weather_button:pressed {
                                background-color: #0097e6;
                            }
                           QLabel#temperature_label{
                               font-size : 64px;
                               font-weight:300;
                               
                           }
                           QLabel#emoji_label{
                               font-size:90px;
                               font-family: Segoe UI emoji;
                           }
                           QLabel#description_label{
                               font-size:45px;
                               color:#a4b0be;
                               
                           }
                           
                           """) # here the syntax is class#objectname
        
        self.get_weather_button.clicked.connect(self.get_weather) # IT connects the slots with the input clicked
        
    def get_weather(self):
        
        api_key="6fb51591c0f5c0a47645e592874ef198"
        city=self.city_input.text() # It stores whatever the user types
        url=f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
        
        try:
            
          response=requests.get(url)
          response.raise_for_status() # even if api fails the program will run and crash later and if we used this code I will directly know the error is raised
          
          data=response.json() # just suppose the api reutrns a value that gets stored in the 
                              #response and by json it will arrange it in dictionaries
          if data["cod"]==200:
            self.display_weather(data)

        except requests.exceptions.HTTPError as http_error:       # api le sabai retrun gareko error  haru yesle catch garxa
           match response.status_code:
               case 400:
                   self.display_error("Bad request\n Please check your input") # Print gareko bhaye terminal ma matra show hunthyo tara self.displayerror use garesi o/p ma dekhhauxa
               case 401:
                   self.display_error("Unauthorized\n Invalid API Key")    
               case 402:
                   self.display_error("Forbidden\n Ascess is denied")     
               case 403:
                   self.display_error("Bad request\n Please check your input") 
               case 404:
                   self.display_error("Not found\n City not found")  
               case 500:
                   self.display_error("Internal sever error\n Please check your input") 
               case 501:
                   self.display_error("Bad request\n Please check your input") 
               case 502:
                   self.display_error(" Bad gateway\n Invalid response from the server")
               case 503:
                   self.display_error("Service Unavailable\n Please check your input")
               case 504:
                   self.display_error("Gateway time out\n NO response from the server")
               case _:
                   self.display_error(f"HTTP eroor occured\n{http_error}")
        except requests.exceptions.ConnectionError:
            self.display_error("Connection error\n check your internet connection")
        except requests.exceptions.Timeout:
            self.display_error("Timeout error:\n The requests time out")
        except requests.exceptions.TooManyRedirects:
            self.display_error("Too many redirects \n Check the URL ")
        except requests.exceptions.RequestException as req_error:
            self.display_error(f"Request Error:\n{req_error}")
            
        
    
    def display_error(self,message):
        self.temperature_label.setStyleSheet("font-size:20px; font-style:italic;")
        self.temperature_label.setText(message)
    
    def display_weather(self,data):
       temperature_k=data["main"]["temp"] # extracting the temperature value from given api and ascessing them in the given format main is the dictionaries and temprature is the key
       temperature_c=temperature_k-273.15
       temperature_f=(temperature_k * 9/5) - 459.67
       
       weather_id=data["weather"][0]["id"]   # so here the weather is the dictionaries and id is the key and according that id we cann choose the gifs or emojis
       weather_description=data["weather"][0]["description"]
       
      
       
       self.temperature_label.setText(f"{temperature_c:.0f}°C")
       
       self.description_label.setText(f"{weather_description.title()}")
       
       gif_path = self.get_weather_gif(weather_id)
       

       movie = QMovie(gif_path)
       movie.setScaledSize(self.emoji_label.size())
       self.emoji_label.setMovie(movie)
       movie.start()
       self.emoji_label.movie = movie
       
       
    @staticmethod # It by this method we no need to create the instances(objects)
    def get_weather_gif(weather_id):
        if 200<=weather_id<=232:
            return "gifs/thunderstorm.gif"
        elif 300<= weather_id<=321:
            return "gifs/drizzle.gif"
        elif 500<=weather_id<=531:
            return "gifs/rain.gif"
        elif 600<=weather_id<=622:
            return "gifs/snow.gif"
        elif 701 <= weather_id <= 741:
             return "gifs/fog.gif"
        elif weather_id==762:
            return "gifs/volcano.gif"
        elif weather_id == 771:
            return "gifs/windy.gif"
        elif weather_id == 781:
            return "gifs/tornado.gif"
        elif weather_id==800:
            return "gifs/clear.gif" 
        elif 801 <= weather_id <= 804:
            return "gifs/clouds.gif"
        else:
            return"gifs/default.gif"
            

if __name__=="__main__":
    app=QApplication(sys.argv) # TO INPUT MULTILE ARGUMENTS
    weather_app=WeatherApp()
    weather_app.show()
    sys.exit(app.exec_()) # close the  window till next movement
    
    
    
    
    
            
        