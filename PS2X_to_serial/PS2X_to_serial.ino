#include <PS2X_lib.h>

PS2X ps2x; // create PS2 Controller Class

//right now, the library does NOT support hot pluggable controllers, meaning
//you must always either restart your Arduino after you conect the controller,
//or call config_gamepad(pins) again after connecting the controller.
int error = 0;
byte type = 0;

bool debug = false;

void setup() {
  Serial.begin(57600);
  error = ps2x.config_gamepad(5, 8, 7, 9, false, true); //GamePad(clock, command, attention, data, Pressures?, Rumble?) check for error

  if (debug) {
    if (error == 0)
      Serial.println("Found Controller, configured successful");
    else if (error == 1)
      Serial.println("No controller found, check wiring, see readme.txt to enable debug. visit www.billporter.info for troubleshooting tips");
    else if (error == 2)
      Serial.println("Controller found but not accepting commands. see readme.txt to enable debug. Visit www.billporter.info for troubleshooting tips");
    else if (error == 3)
      Serial.println("Controller refusing to enter Pressures mode, may not support it. ");
  }
}

void loop() {
  /* You must Read Gamepad to get new values
    Read GamePad and set vibration values
    ps2x.read_gamepad(small motor on/off, larger motor strenght from 0-255)
    if you don't enable the rumble, use ps2x.read_gamepad(); with no values

    you should call this at least once a second
  */

  if (error == 1) //skip loop if no controller found
    return;

  ps2x.read_gamepad(false, 0);

  Serial.print(ps2x.Button(PSB_START));
  Serial.print(ps2x.Button(PSB_SELECT));

  Serial.print(ps2x.Button(PSB_PAD_UP));
  Serial.print(ps2x.Button(PSB_PAD_RIGHT));
  Serial.print(ps2x.Button(PSB_PAD_DOWN));
  Serial.print(ps2x.Button(PSB_PAD_LEFT));
    
  Serial.print(ps2x.Button(PSB_L3));
  Serial.print(ps2x.Button(PSB_R3));

  Serial.print(ps2x.Button(PSB_L2));
  Serial.print(ps2x.Button(PSB_R2));

  Serial.print(ps2x.Button(PSB_L1));
  Serial.print(ps2x.Button(PSB_R1));

  Serial.print(ps2x.Button(PSB_GREEN)); // triangle
  Serial.print(ps2x.Button(PSB_RED)); // circle
  Serial.print(ps2x.Button(PSB_PINK)); // square
  Serial.print(ps2x.Button(PSB_BLUE)); // x

  Serial.print(",");
  Serial.print(ps2x.Analog(PSS_LY), DEC); //Left stick, Y axis. Other options: LX, RY, RX
  Serial.print(",");
  Serial.print(ps2x.Analog(PSS_LX), DEC);
  Serial.print(",");
  Serial.print(ps2x.Analog(PSS_RY), DEC);
  Serial.print(",");
  Serial.println(ps2x.Analog(PSS_RX), DEC);

  delay(50);
}
