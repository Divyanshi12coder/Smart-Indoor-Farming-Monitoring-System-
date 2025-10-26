🌱 Smart Indoor Farming Monitoring System
An IoT-powered solution for real-time monitoring and automation of environmental conditions in indoor agriculture setups — including vertical farms, greenhouses, and hydroponic systems.
📝 Project Overview
The Smart Indoor Farming Monitoring System enables farmers, researchers, and hobbyists to remotely track and manage key environmental parameters. It uses sensors and microcontrollers to collect data, transmit it to the cloud, and visualize it on an interactive dashboard. The system can also automate responses like activating fans, lights, or irrigation pumps based on predefined thresholds.
🚀 Key Features
🌡️ Real-Time Environmental Monitoring
- Temperature, humidity, light intensity, soil moisture, water level, and CO₂ levels
- Live sensor readings via dashboard
⚙️ Automated Control System (Optional)
- Auto-switching fans, lights, and water pumps
- Relay modules triggered by sensor thresholds
📊 Web/Mobile Dashboard
- Interactive UI with graphs and alerts
- Remote access via internet
📁 Data Logging & Analysis
- Historical data storage and visualization
- Export reports in CSV/PDF formats
🔔 Alert System
- Push notifications when parameters exceed safe thresholds
🧩 Multi-Zone Support
- Monitor and control multiple grow zones independently
🔌 Power & Connectivity Monitoring
- Status of power, internet connection, and system faults
🧱 Tech Stack
🖧 Hardware (IoT)
- Microcontroller: ESP32
- Sensors:
- DHT11 – Temperature & Humidity
- LDR or BH1750 – Light Intensity
- Soil Moisture Sensor
- MQ135 – CO₂ Sensor
- Ultrasonic Sensor – Water Level
- Actuators: Relays, motors, LED grow lights, irrigation pumps
🧑‍💻 Software
- Embedded Programming:
- Language: C++ (Arduino IDE)
- Libraries: Adafruit Sensor, Wire, PubSubClient (MQTT)
- Backend:
- Language: Python (Flask)
- Database: MySQL
- Protocol: MQTT for real-time updates
- Frontend:
- Web App: React.js
- Cloud & Hosting:
- Platform: Firebase
- MQTT Broker: Mosquitto
- Notifications: Firebase Cloud Messaging
🔒 Security Measures
- Secure WiFi communication via HTTPS
- Sensor data validation and access control
- Admin authentication for device and user management
✅ Benefits
- Reduces manual monitoring and labor
- Optimizes crop yield through precise control
- Enables data-driven farming decisions
- Conserves water and energy via automation
- Supports remote monitoring — ideal for urban or space-limited setups.







