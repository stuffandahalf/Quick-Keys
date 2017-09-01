#include <iostream>
#include <cstdio>
#include <string.h>
#include <iomanip>
#include <stdlib.h>
#include <unistd.h>
#include <linux/uinput.h>
#include <linux/input.h>
#include <fcntl.h>

#include "variables.h"

/*#include <X11/Xlib.h>
#include <X11/keysym.h>
#include <X11/extensions/XTest.h>
*/

using namespace std;

/* EXTERNAL VARIABLES */
//extern string symbols[];
//extern const char* serial_port;

/* PROTOTYPES */
int type_symbol(string symbol);
void load_initial_symbols();
void main_script(const char *portname);
void save_preferences();

/* MAIN FUNCTION */
int main(int argc, char **argv)
{
    //type_symbol(symbols[0]);
    //type_symbol(testsym);
    //type_symbol(testsym);
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

/* KEYBOARD EMULATION */
int type_symbol(string symbol)
{
    const char *symbol_array = symbol.c_str();
    
    int fd;
    struct uinput_user_dev uidev;
    struct input_event ev;
    
    fd = open("/dev/uinput", O_WRONLY | O_NONBLOCK);
    if(fd < 0)
    {
        return EXIT_FAILURE;
    }
    else
    {
        
        ioctl(fd, UI_SET_EVBIT, EV_KEY);
        ioctl(fd, UI_SET_KEYBIT, KEY_D);
        
        
        memset(&uidev, 0, sizeof(uidev));
        
        snprintf(uidev.name, UINPUT_MAX_NAME_SIZE, "uinput-sample");
        uidev.id.bustype = BUS_USB;
        uidev.id.vendor = 0x1234;
        uidev.id.product = 0xfedc;
        uidev.id.version = 1;
        
        write(fd, &uidev, sizeof(uidev));
        ioctl(fd, UI_DEV_CREATE);
        sleep(.5);
        
        memset(&ev, 0, sizeof(ev));
        ev.type = EV_KEY;
        ev.code = KEY_D;
        ev.value = 1;
        write(fd, &ev, sizeof(ev));
        
        memset(&ev, 0, sizeof(ev));
        ev.type = EV_KEY;
        ev.code = KEY_D;
        ev.value = 0;
        write(fd, &ev, sizeof(ev));
        
        memset(&ev, 0, sizeof(struct input_event));
        ev.type = EV_SYN;
        ev.code = 0;
        ev.value = 0;
        write(fd, &ev, sizeof(struct input_event));
        
        ioctl(fd, UI_DEV_DESTROY);
        close(fd);
        return EXIT_SUCCESS;
    }
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
                //type_symbol(symbols[i]);
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
