#include "Adafruit_BluefruitLE_SPI.h"

class Blue
{
    public:
        Blue(int x);
        void setup();
        void sendKeyboardCode(char code[]);
        void sendControlKey(char keys[]);
    private:
        void error (const __FlashStringHelper*err);
};
