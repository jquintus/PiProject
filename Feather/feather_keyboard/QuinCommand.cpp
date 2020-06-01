#include <Arduino.h>
#include "Blue.h"
#include "QuinCommand.h"

QuinCommand::QuinCommand(int x)
{
  // _blue = blue;
}

void QuinCommand::setBlue(Blue blue)
{
  _blue = &blue;
  _blue->foo();
}

void QuinCommand::invoke()
{
  // Serial.println( F("Invoking QuinCommand!") );
}

