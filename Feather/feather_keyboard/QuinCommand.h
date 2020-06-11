#include "Blue.h"
#ifndef QuinCommand_h
#define QuinCommand_h

class QuinCommand
{
  public:
    QuinCommand(char keys[]);
    QuinCommand(char keys1[], char keys2[]);
    QuinCommand(char keys1[], char keys2[], char keys3[]);
    QuinCommand(char keys1[], char keys2[], char keys3[], char keys4[]);
    QuinCommand(char keys1[], char keys2[], char keys3[], char keys4[], char keys5[]);
    void invoke();
    void setBlue(Blue blue);

  protected:
    Blue* _blue;
    char _keys1[9];
    char _keys2[9];
    char _keys3[9];
    char _keys4[9];
    char _keys5[9];

    int _keys2Exists;
    int _keys3Exists;
    int _keys4Exists;
    int _keys5Exists;
};

#endif
