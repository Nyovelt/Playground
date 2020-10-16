//DFRobot.com
//Compatible with the Arduino IDE 1.0 & 1.8
//Library version:1.2
#include <Wire.h>
#include <LiquidCrystal_I2C.h>
#include <IRremote.h>
#include "SCoop.h"
#if defined(ARDUINO) && ARDUINO >= 100
#define printByte(args)  write(args);
#else
#define printByte(args)  print(args,BYTE);
#endif

uint8_t bell[8]  = {0x4, 0xe, 0xe, 0xe, 0x1f, 0x0, 0x4};
uint8_t note[8]  = {0x2, 0x3, 0x2, 0xe, 0x1e, 0xc, 0x0};
uint8_t clock[8] = {0x0, 0xe, 0x15, 0x17, 0x11, 0xe, 0x0};
uint8_t heart[8] = {0x0, 0xa, 0x1f, 0x1f, 0xe, 0x4, 0x0};
uint8_t duck[8]  = {0x0, 0xc, 0x1d, 0xf, 0xf, 0x6, 0x0};
uint8_t check[8] = {0x0, 0x1, 0x3, 0x16, 0x1c, 0x8, 0x0};
uint8_t cross[8] = {0x0, 0x1b, 0xe, 0x4, 0xe, 0x1b, 0x0};
uint8_t retarrow[8] = {	0x1, 0x1, 0x5, 0x9, 0x1f, 0x8, 0x4};

const int RECV_PIN = 11;
const int LED_PIN = 10;
IRrecv irrecv(RECV_PIN);
decode_results results;
LiquidCrystal_I2C lcd(0x20, 16, 2); // set the LCD address to 0x27 for a 16 chars and 2 line display

int led_flag = 0;




defineTask(TaskTest);
void TaskTest::setup()
{
  pinMode(LED_PIN, OUTPUT);
}
void TaskTest::loop()
{
  if (led_flag) {
    digitalWrite(LED_PIN, HIGH);
    sleep(100);
    digitalWrite(LED_PIN, LOW);
    sleep(100);
  }
  else
  {
    digitalWrite(LED_PIN, HIGH);
    sleep(200);
    digitalWrite(LED_PIN, LOW);
    sleep(200);
    digitalWrite(LED_PIN, HIGH);
    sleep(200);
    digitalWrite(LED_PIN, LOW);
    sleep(1000);
  }
}



void print_Hello() {
  lcd.clear();
  lcd.print("XDDDDDD");
  lcd.setCursor(0, 1);
  lcd.print("    i ");
  lcd.printByte(3);
  lcd.print(" arduinos!");
  delay(5000);

}

void print_Coming() {
  lcd.clear();
  lcd.print("Hello ...... ");
  lcd.setCursor(0, 1);
  lcd.print("How are you today?");
  delay(5000);
}

void print_GoodBye() {
  lcd.clear();
  lcd.print("Software unstable");
  lcd.setCursor(0, 1);
  for (int i=0; i<8; i++){
    lcd.printByte(i);
    delay(300);
  }
  delay(1000);
}

void print_nose() {
  lcd.clear();
  lcd.print("Hey!");
  lcd.setCursor(0, 1);
  lcd.print("Dont touch myHAT!");
  delay(5000);
}

void print_face() {
  int randomNumber = random(1, 6);
  lcd.clear();
  switch (randomNumber) {
    case 1:
      lcd.print("  >         <  ");
      lcd.setCursor(0, 1);
      lcd.print("       o       ");
      break;
    case 2:
      lcd.print("  @         @  ");
      lcd.setCursor(0, 1);
      lcd.print("       づ       ");
      break;
    case 3:
      lcd.print("  ^         ^  ");
      lcd.setCursor(0, 1);
      lcd.print("       o       ");
      break;
    case 4:
      lcd.print("   o        o  ");
      lcd.setCursor(0, 1);
      lcd.print("        --      ");
      break;
    case 5:
      lcd.print("  -         -  ");
      lcd.setCursor(0, 1);
      lcd.print("        --      ");
      break;
  }
  delay(3000);
}

void(* resetFunc) (void) = 0;

void setup()
{
  lcd.init();                      // initialize the lcd
  lcd.backlight();

  lcd.createChar(0, bell);
  lcd.createChar(1, note);
  lcd.createChar(2, clock);
  lcd.createChar(3, heart);
  lcd.createChar(4, duck);
  lcd.createChar(5, check);
  lcd.createChar(6, cross);
  lcd.createChar(7, retarrow);
  lcd.home();
  print_Hello();
  Serial.begin(9600);
  irrecv.enableIRIn();
  mySCoop.start();
}


void loop()
{
  //  if (irrecv.decode(&results)) {
  //    Serial.println(results.value, HEX);
  //    irrecv.resume(); // Receive the next value
  //  }
  led_flag = 0;
  yield();
  print_face();
  if (irrecv.decode(&results)) {
    Serial.println(results.value, HEX);
    if (results.value == 0xFD00FF) {
      led_flag = 1;
      print_GoodBye();
      resetFunc();
      irrecv.resume(); // Receive the next value
    }
    else if (results.value == 0xFD30CF) {
      uint16_t val;
      double dat;
      val = analogRead(A2); //Connect LM35 on Analog 0
      dat = (double) val * (5 / 10.24);
      Serial.print("Tep:"); //Display the temperature on Serial monitor
      Serial.print(dat);
      Serial.println("C");
      lcd.clear();
      lcd.print("Tep:"); //Display the temperature on Serial monitor
      lcd.print(dat);
      lcd.print("C");
      delay(2000);
      if(dat <= 20 ){
        lcd.clear();
        lcd.print("It's cold."); //Display the temperature on Serial monitor
        lcd.setCursor(0, 1);
        lcd.print("Take some clothes.");
        delay(2000);
      }
      else if( dat >= 20 && dat <= 40 ){
        lcd.clear();
        lcd.print("It's comfortable."); //Display the temperature on Serial monitor
        lcd.setCursor(0, 1);
        lcd.print("Have a nice day.");
        delay(2000);
      }
      else if(  dat > 40 ){
        lcd.clear();
        lcd.print("It's hot."); //Display the temperature on Serial monitor
        lcd.setCursor(0, 1);
        lcd.print("Protect yourself.");
        delay(2000);
      }
    }
    irrecv.resume();
  }
  int init_value = analogRead(A3);
  //Serial.println(init_value);
  delay(10);
  int final_value = analogRead(A3);
  Serial.println(abs(init_value - final_value));
  if (abs(init_value - final_value) >= 10) {
    Serial.println("nose");
    led_flag = 1;
    print_nose();
  }
}
