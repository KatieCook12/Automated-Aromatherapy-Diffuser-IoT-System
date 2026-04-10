# CT5061 – IoT Development  
## Automated Aromatherapy Diffuser System  

This project was developed as part of the **CT5061 – IoT Development module** at the University of Gloucestershire. The system demonstrates how IoT technologies can be used to automate environmental control and improve user wellbeing through smart aromatherapy and humidity monitoring.

---

## 🎯 Project Aim  

The primary aim of this project was to design and implement an **automated aromatherapy diffuser** that:

- Monitors humidity and temperature levels  
- Supports circadian rhythm using automated oil dispensing  
- Provides a user interface for real-time control  
- Demonstrates integration between IoT hardware and software  

---

## 🖥 Application Overview  

The system combines physical hardware with a software dashboard to create a fully interactive IoT solution.

Key capabilities include:

- Real-time monitoring of environmental conditions  
- Automated diffuser activation based on time of day  
- User-controlled humidity settings  
- Visual feedback through a dashboard interface  

The device uses **essential oils** to support user wellbeing — stimulating oils during the day and calming oils at night.

---

## 🛠 Tech Stack  

- **Raspberry Pi** – Main IoT controller and Node-RED host  
- **Arduino Uno** – Sensor data processing  
- **Node-RED** – Dashboard and automation flows  
- **C++ (Arduino)** – Sensor programming  
- **JavaScript** – Node-RED logic  
- **DHT11 Sensor** – Temperature & humidity  
- **Water Level Sensors** – Liquid detection  
- **Water Atomisers** – Oil diffusion  
- **LEDs** – Status indicators  

---

## ✨ Key Features  

- Automated **dual-pod aromatherapy system**  
- Real-time **humidity and temperature monitoring**  
- Node-RED **dashboard with gauges and controls**  
- **Circadian-based automation** (day/night oil switching)  
- User-defined **humidity threshold control**  
- Water level monitoring with **refill alerts**  
- Hybrid system using **Raspberry Pi + Arduino**  

---

## ⚙️ System Architecture  

The system uses a **hybrid IoT architecture**:

- **Arduino** reads sensor data (humidity, temperature, water levels)  
- **Raspberry Pi** processes logic and controls actuators  
- **Node-RED** provides a visual dashboard and automation  

Due to voltage limitations (3.3V vs 5V), actuators were powered via Arduino while still being controlled by the Raspberry Pi.

---

## 📝 Schematic

---

## 💻 Node-RED Dashboard

---

## 🟥 Node-RED

---

## 🔄 How It Works  

1. Sensors collect environmental data  
2. Arduino sends data via serial communication  
3. Node-RED processes and displays data  
4. System triggers atomisers based on:
   - Humidity levels  
   - Time of day (sun position logic)  
5. User can override settings via dashboard  

---

## 📊 Testing  

All system features were tested successfully, including:

- Pod refill detection  
- Humidity and temperature display  
- Automated pod activation (day/night cycle)  
- User-controlled humidity thresholds  
- Atomiser functionality  

---

## 🔐 Security Considerations  

The project explored key IoT security risks and mitigation strategies:

- Protection against **device tampering**  
- Firmware security and update validation  
- Encryption for secure data transmission  
- Access control for user permissions  
- Protection against replay and network attacks  

---

## 📡 Data Transmission  

The system evaluated multiple IoT communication protocols:

- Bluetooth (BLE)  
- ZigBee  
- LoRaWAN  

Bluetooth was identified as the most practical due to low power usage and mobile compatibility, though security considerations remain important.

---

## 📦 What I Learned  

### 🌐 IoT Development  
- Integration of sensors, actuators, and interfaces  
- Designing real-world IoT solutions  

### 🔄 Automation & Data Processing  
- Building Node-RED flows  
- Handling real-time sensor data  

### 🧠 Embedded Systems  
- Arduino programming (C++)  
- Serial communication with Raspberry Pi  

### 🔐 IoT Security  
- Risks in IoT environments  
- Methods to secure devices and data  

---

## 🧩 Areas for Improvement  

- Replace DHT11 with **DHT22 for higher accuracy**  
- Add **mobile app integration**  
- Implement **wireless communication (Bluetooth/LoRaWAN)**  
- Improve **power efficiency**  
- Enhance **security mechanisms (encryption & authentication)**  
- Add **cloud storage and analytics**  

---

## 🛠 Setup Instructions  

### Prerequisites  

- Raspberry Pi (with Node-RED installed)  
- Arduino Uno  
- Arduino IDE  
- Required sensors and components  

---

### Installation  

```bash
git clone https://github.com/yourusername/iot-aromatherapy-diffuser.git
cd iot-aromatherapy-diffuser
