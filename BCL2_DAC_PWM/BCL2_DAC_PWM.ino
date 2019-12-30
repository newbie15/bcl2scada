#include <PWM.h>
#include <Adafruit_MCP4725.h>


#define INV1 5
#define INV2 5
#define INV3 5
#define INV4 5
#define INV5 9
#define INV6 10
#define INV7 5

#define HR 0
int led = 9;                // the pin that the LED is attached to
int brightness = 0;         // how bright the LED is
int fadeAmount = 1;         // how many points to fade the LED by
int32_t frequency = 3000; //frequency (in Hz)

String data;
float volt_target[7];

int out1,dac_value1 ;
int out2,dac_value2 ;
int out3,dac_value3 ;
int out4,dac_value4 ;
int out5,dac_value5 ;
int out6,dac_value6 ;
int out7,dac_value7 ;


Adafruit_MCP4725 dac1; // constructor
Adafruit_MCP4725 dac2; // constructor
Adafruit_MCP4725 dac3; // constructor
Adafruit_MCP4725 dac4; // constructor
Adafruit_MCP4725 dac5; // constructor
Adafruit_MCP4725 dac6; // constructor
Adafruit_MCP4725 dac7; // constructor


void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  // dac1.begin(0x60);
  // dac2.begin(0x61);
  dac3.begin(0x60);
  dac4.begin(0x61);
  // dac5.begin(0x62);
  // dac6.begin(0x63);
  // dac7.begin(0x63);

  InitTimersSafe(); 

  //sets the frequency for the specified pin
  bool success = SetPinFrequencySafe(led, frequency);
 
  //if the pin frequency was set successfully, turn pin 13 on
  if(success) {
    pinMode(13, OUTPUT);
    digitalWrite(13, HIGH);    
  }
}

void loop() {

  char inc = 0;
  if ( Serial.available()) {
    String serialResponse = Serial.readStringUntil('\r\n');

    // Convert from String Object to String.
    char buf[64];
    serialResponse.toCharArray(buf, sizeof(buf));
    char *p = buf;
    char *str;
    while ((str = strtok_r(p, ";", &p)) != NULL){ // delimiter is the semicolon
      Serial.println(str);
      String d = str;
      volt_target[inc++] = d.toFloat();
    }
    control_inverter();
  }
  

}

float voltage_lin(float x){
//  float y = 0.000909850357*x*x + 0.0506284093*x +0.4165844525;
  float y = (-1.0*(0.83002151*x*x)) + (14.42224643*x) - 3.413639126;
  return y/10;
}


void control_inverter(){
  if(HR==0){
    out1 = 255 * (volt_target[0]/5.0);
    out2 = 255 * (volt_target[1]/5.0);
    out3 = 255 * (volt_target[2]/5.0);
    out4 = 255 * (volt_target[3]/5.0);
    out5 = 255 * (volt_target[4]/5.0);
    out6 = 255 * (volt_target[5]/5.0);
    out7 = 255 * (volt_target[6]/5.0);
  
    pwmWrite(INV1,out1);
    pwmWrite(INV2,out2);
    pwmWrite(INV3,out3);
    pwmWrite(INV4,out4);
    pwmWrite(INV5,out5);
    pwmWrite(INV6,out6);
    pwmWrite(INV7,out7);

    Serial.println("OK");
  }else{
    out1 = 65535 * (volt_target[0]/5.0);
    out2 = 65535 * (volt_target[1]/5.0);
    out3 = 65535 * (volt_target[2]/5.0);
    out4 = 65535 * (volt_target[3]/5.0);
    out5 = 65535 * (volt_target[4]/5.0);
    out6 = 65535 * (volt_target[5]/5.0);
    out7 = 65535 * (volt_target[6]/5.0);

    pwmWriteHR(INV1,out1);
    pwmWriteHR(INV2,out2);
    pwmWriteHR(INV3,out3);
    pwmWriteHR(INV4,out4);
    pwmWriteHR(INV5,out5);
    pwmWriteHR(INV6,out6);
    pwmWriteHR(INV7,out7);

  }

  // dac_value1 = 4096 * (volt_target[0]/5.0);
  // dac_value2 = 4096 * (volt_target[1]/5.0);
  dac_value3 = 4095 * (volt_target[2]/5.0);
  dac_value4 = 4095 * (volt_target[3]/5.0);
  // dac_value5 = 4096 * (volt_target[4]/5.0);
  // dac_value6 = 4096 * (volt_target[5]/5.0);
  // dac_value7 = 4096 * (volt_target[6]/5.0);

  // dac1.setVoltage(dac_value1, false);
  // dac2.setVoltage(dac_value2, false);
  dac3.setVoltage(dac_value3, false);
  dac4.setVoltage(dac_value4, false);
  // dac5.setVoltage(dac_value5, false);
  // dac6.setVoltage(dac_value6, false);
  // dac7.setVoltage(dac_value7, false);

//  Serial.println(dac_value3);

}
