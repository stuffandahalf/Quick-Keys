#include <iostream>
#include <iomanip>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#include "variables.h"

#include <X11/Xlib.h>
#include <X11/keysym.h>
#include <X11/extensions/XTest.h>

using namespace std;

/* EXTERNAL VARIABLES */
//extern string symbols[];
//extern const char* serial_port;

/* PROTOTYPES */
void type_symbol(wchar_t symbol);
void load_initial_symbols();
void main_script(const char *portname);
void save_preferences();

/* MAIN FUNCTION */
int main(int argc, char **argv)
{
    //type_symbol(symbols[0]);
    //type_symbol(testsym);
    type_symbol(testchar);
    //type_symbol("π");
    
    profile test;
    test.name = "This is a test";
    for(int i = 0; i < BUTTONNUM; i++)
    {
        test.symbols[i] = symbols[i];
        cout << symbols[i] << '\n';
    }
    cout << '\n';
    
    main_script(serial_port);
    
	return 0;
}

void type_symbol(wchar_t symbol)
{
    Display *display;
    unsigned int keycode;
    display = XOpenDisplay(NULL);

    //KeySym sym = XStringToKeysym(symbol.c_str());
    //cout << sym;
    //keycode = XKeysymToKeycode(display, sym);
    //cout << keycode << '\n';
    cout << XK_Greek_pi << '\n';
    //cout << XK_A << '\n';
    cout << (int)symbol << '\n';
    //UnicodeString::ToInt(symbol);
    //const char *symarr = symbol.c_str();
    sleep(5);
    //int i = 0;
    //while(symarr[i] != '\0')
    //{
        //cout << XK_Greek_pi << '\n';
        //keycode = XKeysymToKeycode(display, (int)'a');
        //keycode = XKeysymToKeycode(display, XK_A);
        //keycode = XKeysymToKeycode(display, (int)symarr[i]);
    //KeySym sym = XStringToKeysym(symbol);
    //keycode = XKeysymToKeycode(display, sym);
    //keycode = XKeysymToKeycode(display, XK_Greek_pi);
    //keycode = XKeysymToKeycode(display, XK_A);
    //cout << keycode << '\n';
    //XTestFakeKeyEvent(display, keycode, True, 0);
    //XTestFakeKeyEvent(display, keycode, False, 0);
        //i++;
    //}
    XFlush(display);
}

/* LOAD INITIAL SYMBOLS */
void load_initial_symbols()
{
    string new_symbols[BUTTONNUM] = {"\u03c0",      //pi
                                     "\u03b1",      //alpha
                                     "\u03a3",      //sigma
                                     "\u0394",      //delta
                                     "\u03b2",      //beta
                                     "\u03a9"};     //omega
                      
    for(int i = 0; i < BUTTONNUM; i++)
    {
        symbols[i] = new_symbols[i];
    }
}

/* MAIN SCRIPT */
void main_script(const char *portname)
{
    int ser = open(portname, O_RDONLY);
    char byte[1];
    while(access(portname, F_OK) != -1)
    {
        int size = read(ser, &byte, 1);
        if(size > 0)
        {
            int i = (int) byte[0] - (int) '0' - 1;
            if(i >= 0)
            {
                cout << symbols[i];
                cout << '\n';
            }
        }
        sleep(.75);
    }
}

/* FUNCTION TO SAVE PREFERENCES */
void save_preferences()
{
    
}
