// Includes the 'DHT.h' library
#include "DHT.h"

// Defines the digital pin that's connected to the DHT sensor
#define DHTPIN 7

// Defines the DHT11 sensor
#define DHTTYPE DHT11

// Creates an LCD object
DHT dht(DHTPIN, DHTTYPE);

// Code that runs at the start of the program 
void setup() {
  // Initalises and begins the dht object
  dht.begin();
  // Initialises serial port and exchanges at 9600 bits per second with the serial monitor 
  Serial.begin(9600);
}

// Looping timeframe
void loop() {
  // Reads humidity
  float H = dht.readHumidity();  
  //Reads temperature as Celsius
  float T = dht.readTemperature();    

  // Check if readings failed
  if (isnan(H) || isnan(T)){
    Serial.println("Failed to read from DHT sensor!");
    return;
  }

  // Combines humidity and temperature into single string
  String dhtData = String(H) + "," + String(T);
  Serial.println(dhtData);

  // Reads the input on the analog pin 0 and 2
  int waterLevelSensorValueOne = analogRead(A0);
  int waterLevelSensorValueTwo = analogRead(A2);

  // Prints the water level sensor values
  Serial.print("{\"PodOne\":");
  Serial.print(waterLevelSensorValueOne);
  Serial.print("{\"PodTwo\":");
  Serial.print(waterLevelSensorValueTwo);
  
  // Waits two seconds between taking measurements
  delay(2000);
}
