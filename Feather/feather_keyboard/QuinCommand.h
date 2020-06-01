#include "Blue.h"
#ifndef QuinCommand_h
#define QuinCommand_h

class QuinCommand
{
  public:
    QuinCommand(int x);
    void invoke();
    void setBlue(Blue blue);
  protected:
    Blue* _blue;
};

#endif
