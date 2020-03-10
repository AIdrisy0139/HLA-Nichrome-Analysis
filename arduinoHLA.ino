float temp1=0;
int TempPin = A1;
float mission_time;

void setup() {
// Enable serial communication with a buad rate of 9600
Serial.begin(9600);
Serial1.begin(9600);


//Set digital i/o pins to outputs
pinMode(TempPin,OUTPUT);



}

void loop() {
 mission_time=millis(); // Start time
 // put your main code here, to run repeatedly:
 temp1=(analogRead(TempPin))*(5.0/1024.0)*100; // 10mv per degree celcusis
 Serial.println(temp1);
}
