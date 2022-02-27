const int sensorPin = A0;
const float baselineTemp = 21.0;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // set pins as output and off
  for (int pinNumber = 0; pinNumber < 5; pinNumber++){
    pinMode(pinNumber, OUTPUT);
    digitalWrite(pinNumber, LOW);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  int sensorVal = analogRead(sensorPin);

  // convert ADC reading to voltage
  float voltage = (sensorVal/1024.0) * 5.0;
  
  // convert to Celsius 
  float temperature = (voltage - .5) * 100;
  //temperature = (temperature * (9/5)) + 32;
  Serial.print("Temperature: ");
  Serial.print(temperature);

  // led control
  if (temperature < baselineTemp+2){
    digitalWrite(2, LOW);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }
  else if (temperature >= baselineTemp+2 && temperature < baselineTemp+4){
    digitalWrite(2, HIGH);
    digitalWrite(3, LOW);
    digitalWrite(4, LOW);
  }
  else if (temperature >= baselineTemp+4 && temperature < baselineTemp+6) {
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, LOW);
  }
  else if (temperature >= baselineTemp + 6){
    digitalWrite(2, HIGH);
    digitalWrite(3, HIGH);
    digitalWrite(4, HIGH);
  }
  delay(1);
}
