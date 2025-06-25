# Smart-indoor-farming-monitoring-system-
Utilizes IoT technology to remotely track and manage environmental conditions within an indoor farming setup, like a vertical farm

📝 Project Description:
The Smart Indoor Farming Monitoring System is an IoT-powered solution that enables real-time monitoring and automation of environmental conditions for indoor agriculture. It is designed to assist farmers, researchers, or hobbyists in growing crops efficiently in controlled environments such as greenhouses, vertical farms, or hydroponic setups.

The system collects real-time data on key factors like temperature, humidity, soil moisture, light intensity, and CO₂ levels using sensors. This data is then transmitted to a cloud/server through a microcontroller, and displayed on a web or mobile dashboard. The system can trigger alerts or automate responses like turning on fans, lights, or irrigation systems based on pre-defined thresholds.

🚀 Key Features:
Real-time Environmental Monitoring

Temperature, humidity, light intensity, soil moisture, water level, and CO₂ monitoring

Live sensor readings

Automated Control System (Optional)

Auto-switching fans, lights, or water pumps

Relay modules controlled by logic or thresholds

Web/Mobile Dashboard

Interactive UI with graphs and alerts

Access from anywhere via the internet

Data Logging & Analysis

Store and visualize sensor data trends

Export historical reports (CSV/PDF)

Alert System

Email/SMS/Push notifications when parameters are out of range

Multi-Zone Support

Monitor and control multiple grow zones independently

Power & Connectivity Monitoring

Status of power, internet connection, or system faults

🧱 Tech Stack:
🖧 Hardware (IoT):
Microcontroller: Arduino Uno / ESP32 / Raspberry Pi

Sensors:

DHT11/DHT22 – Temperature & Humidity

LDR or BH1750 – Light Intensity

Soil Moisture Sensor

MQ135 – CO₂ Sensor (optional)

Ultrasonic Sensor – Water level (optional)

Actuators: Relays, motors, LED grow lights, irrigation pumps

🧑‍💻 Software:
Embedded Programming:
Language: C++ (Arduino IDE), Python (Raspberry Pi)

Libraries: Adafruit Sensor, Wire, PubSubClient (for MQTT)

Backend:
Language: Python (Flask/Django) or Node.js (Express)

Database: Firebase Realtime DB / MongoDB / MySQL

APIs: RESTful APIs or MQTT Protocol for real-time sensor updates

Frontend:
Web App: React.js / Vue.js / HTML + CSS + Chart.js

Mobile App (Optional): Flutter / React Native

Cloud & Hosting:
Platform: AWS / Firebase / Heroku / Thingspeak / Google Cloud

Realtime Communication: MQTT Broker (Mosquitto) / WebSockets

Notifications:
Services: Twilio (SMS), Firebase Cloud Messaging (Push), Email via SMTP

🔒 Security Measures:
Secure WiFi communication using HTTPS / TLS

Sensor data validation and access control

Admin authentication for device and user management

✅ Benefits:
Minimizes manual monitoring and reduces labor

Optimizes crop yield through precise environmental control

Enables data-driven farming decisions

Reduces water and energy usage through automation

Allows remote monitoring — especially useful in urban or space-limited setups
