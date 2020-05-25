/*********************************************************************
 This is an example for our nRF51822 based Bluefruit LE modules

 Pick one up today in the adafruit shop!

 Adafruit invests time and resources providing this open source code,
 please support Adafruit and open-source hardware by purchasing
 products from Adafruit!

 MIT license, check LICENSE for more information
 All text above, and the splash screen below must be included in
 any redistribution
*********************************************************************/

// https://github.com/adafruit/Adafruit_BluefruitLE_nRF51/tree/master/examples

/*
  This example shows how to send HID Consumer Control Keys,
  ncluding the following control key definitions:

  System Control (works on most systems: Windows/OS X/Android/iOS)
    - Sound Mute
    - Brightness Increase, decrease
  Media Control (works on most systems)
    - PlayPause
    - MediaNext
  Application Launchers (works mainly on Windows 8/10)
    - EmailReader
    - Calculator
  Browser Specific (Firefox, file explorer: mainly on Windows 8/10)
    - Back
    - Forward
    - Refresh
    - Search
*/

#include <Arduino.h>
#include <SPI.h>
#include "Adafruit_BLE.h"
#include "Adafruit_BluefruitLE_SPI.h"
#include "Adafruit_BluefruitLE_UART.h"

#include "BluefruitConfig.h"

#if SOFTWARE_SERIAL_AVAILABLE
  #include <SoftwareSerial.h>
#endif

/*=========================================================================
    APPLICATION SETTINGS

    FACTORYRESET_ENABLE       Perform a factory reset when running this sketch
   
                              Enabling this will put your Bluefruit LE module
                              in a 'known good' state and clear any config
                              data set in previous sketches or projects, so
                              running this at least once is a good idea.
   
                              When deploying your project, however, you will
                              want to disable factory reset by setting this
                              value to 0.  If you are making changes to your
                              Bluefruit LE device via AT commands, and those
                              changes aren't persisting across resets, this
                              is the reason why.  Factory reset will erase
                              the non-volatile memory where config data is
                              stored, setting it back to factory default
                              values.
       
                              Some sketches that require you to bond to a
                              central device (HID mouse, keyboard, etc.)
                              won't work at all with this feature enabled
                              since the factory reset will clear all of the
                              bonding data stored on the chip, meaning the
                              central device won't be able to reconnect.
    MINIMUM_FIRMWARE_VERSION  Minimum firmware version to have some new features
    -----------------------------------------------------------------------*/
    #define FACTORYRESET_ENABLE         0
    #define MINIMUM_FIRMWARE_VERSION    "0.6.6"
/*=========================================================================*/


// Create the bluefruit object, either software serial...uncomment these lines
/*
SoftwareSerial bluefruitSS = SoftwareSerial(BLUEFRUIT_SWUART_TXD_PIN, BLUEFRUIT_SWUART_RXD_PIN);

Adafruit_BluefruitLE_UART ble(bluefruitSS, BLUEFRUIT_UART_MODE_PIN,
                      BLUEFRUIT_UART_CTS_PIN, BLUEFRUIT_UART_RTS_PIN);
*/

/* ...or hardware serial, which does not need the RTS/CTS pins. Uncomment this line */
// Adafruit_BluefruitLE_UART ble(BLUEFRUIT_HWSERIAL_NAME, BLUEFRUIT_UART_MODE_PIN);

/* ...hardware SPI, using SCK/MOSI/MISO hardware SPI pins and then user selected CS/IRQ/RST */
Adafruit_BluefruitLE_SPI ble(BLUEFRUIT_SPI_CS, BLUEFRUIT_SPI_IRQ, BLUEFRUIT_SPI_RST);

/* ...software SPI, using SCK/MOSI/MISO user-defined SPI pins and then user selected CS/IRQ/RST */
//Adafruit_BluefruitLE_SPI ble(BLUEFRUIT_SPI_SCK, BLUEFRUIT_SPI_MISO,
//                             BLUEFRUIT_SPI_MOSI, BLUEFRUIT_SPI_CS,
//                             BLUEFRUIT_SPI_IRQ, BLUEFRUIT_SPI_RST);

// A small helper
void error(const __FlashStringHelper*err) {
  Serial.println(err);
  while (1);
}

int inputPins[6] = { 
 5,    // Mission Control
 6,    // App Window
 9,    // Show Desktop
 10,   // Play/Pause
 11,   // Volume Up
 12};  // Volume Down

/* 
 * For full list of commands look at section 12
 * http://www.freebsddiary.org/APC/usb_hid_usages.php
 *
 * For explanation on how to interpret these strings look at
 * https://learn.adafruit.com/introducing-adafruit-ble-bluetooth-low-energy-friend/ble-services#at-plus-blekeyboardcode-14-25
 * 
 * ----------------------------------
 * Basic format
 * ----------------------------------
 * Byte 0: Modifier
 * Byte 1: Reserved (should always be 00)
 * Bytes 2..7: Hexadecimal value(s) corresponding to the 
 *             HID keys (if no character is used you can 
 *             enter '00' or leave trailing characters empty)
 * 
 * ----------------------------------
 * Modifier
 * ----------------------------------
 * Bit 0 (0x01): Left Control
 * Bit 1 (0x02): Left Shift
 * Bit 2 (0x04): Left Alt
 * Bit 3 (0x08): Left Window / Command
 * 
 * Bit 4 (0x10): Right Control
 * Bit 5 (0x20): Right Shift
 * Bit 6 (0x40): Right Alt
 * Bit 7 (0x80): Right Window / Command
 *
 * ----------------------------------
 * Keys (sample)
 * ----------------------------------
 * 0x04	Keyboard a and A
 * 0x05	Keyboard b and B
 * 0x06	Keyboard c and C
 * 0x07	Keyboard d and D
 * ...
 * 0x1D	Keyboard z and Z
 * 0x1E	Keyboard 1 and !
 * 0x1F	Keyboard 2 and @
 * 0x20	Keyboard 3 and #
 * 0x21	Keyboard 4 and $
 * 0x22	Keyboard 5 and %
 * 0x23	Keyboard 6 and ^
 * 0x24	Keyboard 7 and &
 * 0x25	Keyboard 8 and *
 * 0x26	Keyboard 9 and (
 * 0x27	Keyboard 0 and )
 * 0x28	Keyboard Return (ENTER)
 * 0x29	Keyboard ESCAPE
 * ...
 * 0x3A	Keyboard F1
 * 0x3B	Keyboard F2
 * 0x3C	Keyboard F3
 * ...
*/

/* Mac Key Bindings */
char CMD_MISSION_CONTROL[]    = "01-00-52"; // (Left) Control + Arrow Up
char CMD_APP_WINDOWS[]        = "01-00-51"; // (Left) Control + Arrow Down
char CMD_SHOW_DESKTOP[]       = "08-00-07"; // (Left) Window + D

/* Media Key Bindings */
char CMD_VOLUME_UP[]          = "00-00-80"; // Volume Up
char CMD_VOLUME_DOWN[]        = "00-00-81"; // Volume Down
char CMD_VOLUME_MUTE[]        = "00-00-7F"; // Volume Mute

/* Zoom Key Bindings */
// https://support.zoom.us/hc/en-us/articles/205683899-Hot-Keys-and-Keyboard-Shortcuts-for-Zoom
char CMD_ZOOM_TOGGLE_MUTE[]   = "82-00-04"; // Command + Shift + A
char CMD_ZOOM_TOGGLE_VIDEO[]  = "82-00-19"; // Command + Alt + V
char CMD_ZOOM_END_MEETING[]   = "80-00-1A"; // Command + W
char CMD_ZOOM_START_MEETING[] = "81-00-19"; // Command + Control + V
char CMD_ZOOM_START_SHARE[]   = "82-00-16"; // Command + Shift + S
char CMD_ZOOM_GALLERY_VIEW[]  = "82-00-1A"; // Command + Shift + W

/* Other Key Bindings */
char CMD_F14[]               = "00-00-69"; // F14
char CMD_KEYS_UP[]           = "00-00";    // No keys held

int buttonsPressedLastTime = 0;
bool playButtonPressedLastTime = false;
/**************************************************************************/
/*!
    @brief  Sets up the HW an the BLE module (this function is called
            automatically on startup)
*/
/**************************************************************************/

void setup(void)
{
  setupButtons();
  setupBluetooth();
}

void setupButtons(void)
{
  for(int i=0; i< 6; i++)
  {
    pinMode(inputPins[i], INPUT_PULLUP);
  }
}

void setupBluetooth(void)
{
  int waitcnt = 0;
  while(!Serial && (waitcnt++ < 10))  // wait (only so long) for serial port to connect.
  {
    delay(100);
  }

  Serial.begin(115200);
  Serial.println(F("Adafruit Bluefruit HID Control Key Example"));
  Serial.println(F("---------------------------------------"));

  /* Initialise the module */
  Serial.print(F("Initialising the Bluefruit LE module: "));

  digitalWrite(LED_BUILTIN, 1);

  if ( !ble.begin(VERBOSE_MODE) )
  {
    error(F("Couldn't find Bluefruit, make sure it's in CoMmanD mode & check wiring?"));
  }
  Serial.println( F("OK!") );

  if ( FACTORYRESET_ENABLE )
  {
    /* Perform a factory reset to make sure everything is in a known state */
    Serial.println(F("Performing a factory reset: "));
    if ( ! ble.factoryReset() ){
      error(F("Factory reset failed!"));
    }
  }

  /* Disable command echo from Bluefruit */
  ble.echo(false);

  Serial.println("Requesting Bluefruit info:");
  /* Print Bluefruit information */
  ble.info();

  // This demo only works with firmware 0.6.6 and higher!
  // Request the Bluefruit firmware rev and check if it is valid
  if ( !ble.isVersionAtLeast(MINIMUM_FIRMWARE_VERSION) )
  {
    error(F("This sketch requires firmware version " MINIMUM_FIRMWARE_VERSION " or higher!"));
  }

  /* Enable HID Service */
  Serial.println(F("Enable HID Services (including Control Key): "));
  if (! ble.sendCommandCheckOK(F( "AT+BLEHIDEN=On"  ))) {
    error(F("Failed to enable HID (firmware >=0.6.6?)"));
  }

  /* Adding or removing services requires a reset */
  Serial.println(F("Performing a SW reset (service changes require a reset): "));
  if (! ble.reset() ) {
    error(F("Couldn't reset??"));
  }
}

/**************************************************************************/
/*!
    @brief  Constantly poll for new command or response data
*/
/**************************************************************************/
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
    printKeyboardCode(CMD_ZOOM_END_MEETING);
  }
  if ( digitalRead(6) == LOW )
  {
    pressed++;
    printKeyboardCode(CMD_ZOOM_START_MEETING);
  }
  if ( digitalRead(9) == LOW )
  {
    pressed++;
    printKeyboardCode(CMD_ZOOM_GALLERY_VIEW);
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
    printKeyboardCode(CMD_ZOOM_START_SHARE);
  }
  if ( digitalRead(11) == LOW )
  {
    pressed++;
    printKeyboardCode(CMD_ZOOM_TOGGLE_MUTE);
  }
  if ( digitalRead(12) == LOW )
  {
    pressed++;
    printKeyboardCode(CMD_ZOOM_TOGGLE_VIDEO);
  }

  if (pressed < 1 && buttonsPressedLastTime > 0){
    // send the key-up command
    printKeyboardCode(CMD_KEYS_UP);
  }

  buttonsPressedLastTime = pressed;
  playButtonPressedLastTime = playPressed;
}

void printKeyboardCode(char keys[])
{
    ble.print("AT+BleKeyboardCode=");
    ble.println(keys);
}

void printControlKey(char keys[])
{
    ble.print("AT+BleHidControlKey=");
    ble.println(keys);
}
