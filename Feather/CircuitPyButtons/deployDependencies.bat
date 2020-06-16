@ECHO OFF
REM ************************************
REM Deploy the Python dependencies to the
REM CircuitPython device.
REM
REM This only has to happen once each time
REM dependencies have changes.
REM ************************************

xcopy .\lib d:\lib /sY
