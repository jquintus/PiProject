#include <Arduino.h>
#include "Blue.h"
#include "QuinCommand.h"

QuinCommand::QuinCommand(char keys[])
{
    memcpy(_keys1, keys, 9);
    _keys2Exists = false;
    _keys3Exists = false;
    _keys4Exists = false;
    _keys5Exists = false;
}
QuinCommand::QuinCommand(char keys1[], char keys2[])
{
    memcpy(_keys1, keys1, 9);
    memcpy(_keys2, keys2, 9);
    _keys2Exists = true;
    _keys3Exists = false;
    _keys4Exists = false;
    _keys5Exists = false;
}
QuinCommand::QuinCommand(char keys1[], char keys2[], char keys3[])
{
    memcpy(_keys1, keys1, 9);
    memcpy(_keys2, keys2, 9);
    memcpy(_keys3, keys3, 9);
    _keys2Exists = true;
    _keys3Exists = true;
    _keys4Exists = false;
    _keys5Exists = false;
}
QuinCommand::QuinCommand(char keys1[], char keys2[], char keys3[], char keys4[])
{
    memcpy(_keys1, keys1, 9);
    memcpy(_keys2, keys2, 9);
    memcpy(_keys3, keys3, 9);
    memcpy(_keys4, keys4, 9);

    _keys2Exists = true;
    _keys3Exists = true;
    _keys4Exists = true;
    _keys5Exists = false;
}
QuinCommand::QuinCommand(char keys1[], char keys2[], char keys3[], char keys4[], char keys5[])
{
    memcpy(_keys1, keys1, 9);
    memcpy(_keys2, keys2, 9);
    memcpy(_keys3, keys3, 9);
    memcpy(_keys4, keys4, 9);
    memcpy(_keys5, keys5, 9);

    _keys2Exists = true;
    _keys3Exists = true;
    _keys4Exists = true;
    _keys5Exists = true;
}

void QuinCommand::setBlue(Blue blue)
{
    Serial.println("Setting the blue");
    _blue = &blue;
}

void QuinCommand::invoke()
{
  _blue->sendKeyboardCode(_keys1);
  if (_keys2Exists) _blue->sendKeyboardCode(_keys2);
  if (_keys3Exists) _blue->sendKeyboardCode(_keys3);
  if (_keys4Exists) _blue->sendKeyboardCode(_keys4);
  if (_keys5Exists) _blue->sendKeyboardCode(_keys5);
}

