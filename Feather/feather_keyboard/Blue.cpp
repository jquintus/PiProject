#include "Adafruit_BluefruitLE_SPI.h"
#include "Blue.h"
#include <SPI.h>
#include "Adafruit_BLE.h"
#include "Adafruit_BluefruitLE_UART.h"

#include "BluefruitConfig.h"

#define FACTORYRESET_ENABLE         0
#define MINIMUM_FIRMWARE_VERSION    "0.6.6"

Adafruit_BluefruitLE_SPI ble(
        BLUEFRUIT_SPI_CS, 
        BLUEFRUIT_SPI_IRQ, 
        BLUEFRUIT_SPI_RST);

Blue::Blue(int x) 
{
    // Comment
}

void Blue::setup()
{
  int waitcnt = 0;
  while(!Serial && (waitcnt++ < 10))  // wait (only so long) for serial port to connect.
  {
    delay(100);
  }

  Serial.begin(115200);
  Serial.println(F("Adafruit Bluefruit HID Control Key Example"));
  Serial.println(F("---------------------------------------"));

  // Initialise the module
  Serial.print(F("Initialising the Bluefruit LE module: "));

  digitalWrite(LED_BUILTIN, 1);

  if ( !ble.begin(VERBOSE_MODE) )
  {
    error(F("Couldn't find Bluefruit, make sure it's in CoMmanD mode & check wiring?"));
  }
  Serial.println( F("OK!") );

  if ( FACTORYRESET_ENABLE )
  {
    // Perform a factory reset to make sure everything is in a known state
    Serial.println(F("Performing a factory reset: "));
    if ( ! ble.factoryReset() ){
      error(F("Factory reset failed!"));
    }
  }

  // Disable command echo from Bluefruit
  ble.echo(false);

  Serial.println("Requesting Bluefruit info:");
  // Print Bluefruit information
  ble.info();

  // This demo only works with firmware 0.6.6 and higher!
  // Request the Bluefruit firmware rev and check if it is valid
  if ( !ble.isVersionAtLeast(MINIMUM_FIRMWARE_VERSION) )
  {
    error(F("This sketch requires firmware version " MINIMUM_FIRMWARE_VERSION " or higher!"));
  }

  Serial.println(F("Setting device name to 'Master Board LE': "));
  if (! ble.sendCommandCheckOK(F( "AT+GAPDEVNAME=Master Board LE")) ) {
    error(F("Could not set device name?"));
  }

  // Enable HID Service
  Serial.println(F("Enable HID Services (including Control Key): "));
  if (! ble.sendCommandCheckOK(F( "AT+BLEHIDEN=On"  ))) {
    error(F("Failed to enable HID (firmware >=0.6.6?)"));
  }

  // Adding or removing services requires a reset
  Serial.println(F("Performing a SW reset (service changes require a reset): "));
  if (! ble.reset() ) {
    error(F("Couldn't reset??"));
  }
}

void Blue::sendKeyboardCode(char code[])
{
    ble.print("AT+BleKeyboardCode=");
    ble.println(code);
}

void Blue::sendControlKey(char keys[])
{
    ble.print("AT+BleHidControlKey=");
    ble.println(keys);
}

void Blue::error(const __FlashStringHelper*err) {
  Serial.println(err);
  while (1);
}

void Blue::foo(){
  Serial.println("Got here");
}
