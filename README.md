🌦️ Weather Forecast Application

A Python-based command-line weather application that retrieves real-time weather data for any city using the OpenWeatherMap API.
This project demonstrates how to integrate REST APIs, handle JSON responses, and build simple data-driven applications in Python.

📌 Features

✅ Fetch real-time weather data

✅ User input for any city worldwide

✅ Displays key weather information including:

Weather description

Temperature

Humidity

✅ Error handling for invalid cities or API issues

✅ Lightweight command-line application


🧠 Technologies Used


| Technology             | Purpose                     |
| ---------------------- | --------------------------- |
| **Python**             | Core programming language   |
| **Requests Library**   | API communication           |
| **OpenWeatherMap API** | Real-time weather data      |
| **JSON Parsing**       | Extract weather information |


📂 Project Structure

weather-forecast-app

│

├── weather-forecast.py

└── README.md

⚙️ Installation

1️⃣ Clone the repository

git clone https://github.com/your-username/weather-forecast-app.git

2️⃣ Navigate to the project directory

cd weather-forecast-app

3️⃣ Install required dependencies

pip install requests

🔑 API Setup

This project uses the OpenWeatherMap API.

1. Create a free account at
https://openweathermap.org/api
2. Generate your API key.
3. Replace the placeholder API key inside the script:
   API_KEY = "your_api_key_here"
⚠️ Never upload your real API key to public GitHub repositories.


▶️ Running the Application

Run the Python script:
python weather-forecast.py
The program will prompt you to enter a city name.

📊 Example Output

Enter a city name: New York

Weather forecast for New York
--------------------------------
Description : clear sky
Temperature : 295.15 K
Humidity    : 56 %

🛠️ Error Handling

The application handles:

1. Invalid city names
2. API request failures
3. Missing API responses
4. Network errors

🚀 Future Improvements

Planned enhancements include:
1. 🌡 Convert temperature to Celsius and Fahrenheit
2. 🌬 Add wind speed and pressure
3. 📅 Show 5-day weather forecast
4. 🖥 Build a GUI version
5. 🔒 Store API keys securely using environment variables
6. 📊 Add weather visualization charts

📚 Learning Outcomes

This project helped develop practical experience in:
1. REST API integration
2. JSON data parsing
3. Exception handling
4. Python CLI applications
5. Working with third-party APIs


📜 License

This project is licensed under the MIT License.


🤝 Contributing

Contributions are welcome!
If you would like to improve this project:
Fork the repository
Create a new branch
Submit a pull request

⭐ Support

If you find this project useful, please consider giving it a ⭐ star on GitHub!
