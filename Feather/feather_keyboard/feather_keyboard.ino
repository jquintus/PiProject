#include <Arduino.h>

#include "QuinCommand.h"
#include "CommandsConstants.h"
#include "Blue.h"

#if SOFTWARE_SERIAL_AVAILABLE
  #include <SoftwareSerial.h>
#endif

// A small helper

int inputPins[6] = { 5, 6, 9, 10, 11, 12};
int buttonsPressedLastTime;

Blue blue(0);  // The int is ignored
QuinCommand greenTop(
  CMD_ZOOM_START_MEETING
  );

QuinCommand greenBottom(
  CMD_ZOOM_END_MEETING,
  CMD_ENTER
  );

QuinCommand yellowTop(
  CMD_ZOOM_GALLERY_VIEW
  );

QuinCommand yellowBottom(
  CMD_ZOOM_START_SHARE,
  CMD_ARROW_RIGHT,
  CMD_ENTER
  );

QuinCommand redTop(
  CMD_ZOOM_TOGGLE_VIDEO
  );

QuinCommand redBottom(
  CMD_ZOOM_TOGGLE_MUTE
  );

void setup(void)
{
  setupButtons();
  blue.setup();
}

void setupButtons(void)
{
  for(int i=0; i< 6; i++)
  {
    pinMode(inputPins[i], INPUT_PULLUP);
  }
}


void loop(void)
{
  handleKeyPress();
  delay(10);
}

void handleKeyPress(void)
{
  int pressed = 0;
  int playPressed = false;
  if ( digitalRead(5) == LOW )
  {
    pressed++;
    greenBottom.invoke();
  }
  if ( digitalRead(6) == LOW )
  {
    pressed++;
    greenTop.invoke();
  }
  if ( digitalRead(9) == LOW )
  {
    pressed++;
    yellowTop.invoke();
  }
/*
  if ( digitalRead(10) == LOW )
  {
    playPressed = true;
    if (!playButtonPressedLastTime)
    {
      printControlKey("PLAY");
    }
  }
*/
  if ( digitalRead(10) == LOW )
  {
    pressed++;
    yellowBottom.invoke();
  }
  if ( digitalRead(11) == LOW )
  {
    pressed++;
    redBottom.invoke();
  }
  if ( digitalRead(12) == LOW )
  {
    pressed++;
    redTop.invoke();
  }

  if (pressed < 1 && buttonsPressedLastTime > 0){
    // send the key-up command
    blue.sendKeyboardCode(CMD_KEYS_UP);
  }

  buttonsPressedLastTime = pressed;
}
