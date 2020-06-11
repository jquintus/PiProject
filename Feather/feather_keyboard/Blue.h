#ifndef Blue_h
#define Blue_h

class Blue
{
    public:
        Blue(int x);
        void setup();
        void sendKeyboardCode(char code[]);
        void sendControlKey(char keys[]);
        void foo();
    private:
        void error (const __FlashStringHelper*err);
};

#endif
