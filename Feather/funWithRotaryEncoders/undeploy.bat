@ECHO OFF
REM ************************************
REM Pulls the code file from the board
REM
REM This is useful if you've been writing
REM and debugging code directly to a 
REM CircuitPython board and now want
REM to check it in to git
REM ************************************

copy /Y d:\code.py .\code.py
