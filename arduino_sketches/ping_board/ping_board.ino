// Imports
#include <ESP8266WiFi.h> 
#include <ESP8266Ping.h>

extern "C"
{
  #include <lwip/icmp.h> // needed for icmp packet definitions
}

// Constant Globals
const int MAX_RETRIES = 60;
const int WAIT_MILLISECONDS = 1 * 1000;
const int BACKOFF_MILLISECONDS = 3600 * 1000;
const bool VERBOSE = true; // print successful pings

const char* host = "sump_ping"; // The hostname to ping
const char* ssid = "TwoCrazyDucks";         // The SSID (name) of the Wi-Fi network you want to connect to
const char* password = "CrispyChickenSandwhich17";     // The password of the Wi-Fi network

// IFTTT
const char* ifttt_host = "maker.ifttt.com";
const char* url = "https://maker.ifttt.com/trigger/sump_pump_ping_error/json/with/key/YL6PcwlZULPTvflrExH5k";
const byte port = 80;
WiFiClient client;    // wifi client object



// Dynamic Globals
int cur_retries = 0;


void connect_to_wifi(){
  // Init connection
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

bool ping() {
  bool state = Ping.ping(host);
  return state;
}

void alarm(){
  Serial.print("Sending email via ifttt.com");
  if (!client.connect(ifttt_host, port)) {             // connect to ifttt.com
      Serial.println("Connection failed.");
      return;
  }

  client.print(String("GET ") + url + " HTTP/1.1\r\n" +
                 "Host: " + ifttt_host + "\r\n" +
                 "Connection: close\r\n\r\n");

  delay(100);  // without the delay, the request may not be completed
  Serial.println("\nDisconnecting from ifttt.com");
  client.stop();
  
}

void loop() {
  // Check if backoff time
  if (cur_retries >= MAX_RETRIES){
    cur_retries = 0;
    alarm();
    Serial.println("Backoff limit hit. Waiting...");
    delay(BACKOFF_MILLISECONDS);
  }
  else {
    // Ping
    bool successfull_ping = ping();
    if (successfull_ping){
      cur_retries = 0;
      if (VERBOSE){
        Serial.println("Pinging host succeeded."); Serial.println("\n");
      }
    }
    else{
      cur_retries++;
      Serial.println("Pinging host failed. "); Serial.print("Retry attempt #"); Serial.print(cur_retries); Serial.println("\n");
    }
    delay(WAIT_MILLISECONDS);
  }
}
