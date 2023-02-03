// Imports
#include <ESP8266WiFi.h> 
#include <Pinger.h>

extern "C"
{
  #include <lwip/icmp.h> // needed for icmp packet definitions
}

// Constant Globals
const char* host = "sump_ping"; // The hostname to ping
const char* ssid = "TwoCrazyDucks";         // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "CrispyChickenSandwhich17";     // The password of the Wi-Fi network

void connect_to_wifi(){
  // Init connection
  WiFi.hostname(host);
  WiFi.begin(ssid, password);
  Serial.print("Connecting to "); Serial.print(ssid); Serial.println(" ...");

  // Wait for WiFi to connect
  int i = 0;
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
    Serial.print(++i); Serial.print(' ');
  }

  Serial.println('\n'); Serial.println("Connection established!");  Serial.print("IP address:\t"); Serial.println(WiFi.localIP());         // Send the IP address of the ESP8266 to the computer
}


void setup() {
  Serial.begin(9600);
  connect_to_wifi();
}

void loop() {
  // nothing to see here
}
