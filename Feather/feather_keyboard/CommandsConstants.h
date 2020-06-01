#ifndef CommandConstants_h
#define CommandConstants_h

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

/* Zoom Key Bindings */
// https://support.zoom.us/hc/en-us/articles/205683899-Hot-Keys-and-Keyboard-Shortcuts-for-Zoom
const char CMD_ZOOM_TOGGLE_MUTE[9]   = "82-00-04"; // Command + Shift + A
const char CMD_ZOOM_TOGGLE_VIDEO[9]  = "82-00-19"; // Command + Alt + V
const char CMD_ZOOM_END_MEETING[9]   = "80-00-1A"; // Command + W
const char CMD_ZOOM_START_MEETING[9] = "81-00-19"; // Command + Control + V
const char CMD_ZOOM_START_SHARE[9]   = "82-00-16"; // Command + Shift + S
const char CMD_ZOOM_GALLERY_VIEW[9]  = "82-00-1A"; // Command + Shift + W

/* Mac Key Bindings */
char CMD_MISSION_CONTROL[9]    = "01-00-52"; // (Left) Control + Arrow Up
char CMD_APP_WINDOWS[9]        = "01-00-51"; // (Left) Control + Arrow Down
char CMD_SHOW_DESKTOP[9]       = "08-00-07"; // (Left) Window + D

/* Media Key Bindings */
char CMD_VOLUME_UP[9]          = "00-00-80"; // Volume Up
char CMD_VOLUME_DOWN[9]        = "00-00-81"; // Volume Down
char CMD_VOLUME_MUTE[9]        = "00-00-7F"; // Volume Mute

/* Other Key Bindings */
char CMD_F14[9]                = "00-00-69";
char CMD_ENTER[9]              = "00-00-28";
char CMD_KEYS_UP[9]            = "00-00-00"; // No keys held

#endif
