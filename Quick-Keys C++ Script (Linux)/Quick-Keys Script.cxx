#include <iostream>
#include <stdlib.h>
#include <unistd.h>
#include <fcntl.h>

#include "variables.h"

#include <X11/Xlib.h>
#include <X11/keysym.h>
#include <X11/extensions/XTest.h>

using namespace std;

/* EXTERNAL VARIABLES */
extern string symbols[];
extern const char* port_name;

/* PROTOTYPES */
void load_initial_symbols();
void main_script(const char *portname);

/* MAIN FUNCTION */
int main(int argc, char **argv)
{
    load_initial_symbols();
    main_script(serial_port);
    
	return 0;
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
    while(true)
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
