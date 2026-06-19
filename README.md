# Simple Weather App

This is a basic weather application made with Python and PyQt5. It takes a city name from the user, connects to the OpenWeatherMap API, and shows the live temperature, weather descriptions, and cool matching animated weather GIFs.

A. Features
- Clean dark theme design with proper margins and layout.
- Typing color inside input box is purely white for easy reading.
- Dynamic layout structure that auto-adjusts based on text updates.
- Full error handling for wrong city names, bad connections, or API key errors.

B. Requirements
You need python installed on your system along with these packages:
- PyQt5
- requests

You can install them using terminal:
pip install PyQt5 requests

C. How to setup and run
1. Clone this repository or copy the code files.
2. Make sure you have a folder named `gifs` in the same directory containing your weather gif files (like `clear.gif`, `rain.gif`, `clouds.gif` etc.).
3. Open your terminal or command prompt inside the project folder.
4. Run the application with this command:
python app.py

 D.How it works
- It takes the string typed inside the line input box.
- Sends a request call to OpenWeatherMap servers.
- Converts the JSON return dataset into dictionaries.
- Displays the absolute Celsius metrics and sets up a QMovie container to play the weather animation path matched by the ID rules.
