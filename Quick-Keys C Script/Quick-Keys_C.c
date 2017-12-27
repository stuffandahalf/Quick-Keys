#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

#ifdef __linux__
    #include <X11/Xlib.h>
    #include <X11/keysym.h>
    #include <X11/extensions/XTest.h>
#elif defined __macintosh__

#elif defined _WIN32

#endif

void main_script(char *port_name);

int main(int argc, char **argv)
{
    char *port_name = "/dev/ttyUSB1";
    //char *port_name = "test";
	main_script(port_name);
	return 0;
}

void main_script(char *port_name)
{
    for(int i = 0; i < 1000000; i++)
    {
        printf("test\n");
    }
    if(access(port_name, F_OK) != -1)
    {   
        Display *display;
        unsigned int keycode;
        display = XOpenDisplay(NULL);
        FILE *port = fopen(port_name, "r");
        char *symbols[6] = {"\u03c0", "\u03b1", "\u03a3", "\u0394", "\u03b2", "\u03a9"};
        int data;
        while(fscanf(port, "%d", &data) != EOF)
        {
            printf("%d\t", data-1);
            printf("%s\n", symbols[data-1]);
            keycode = XKeysymToKeycode(display, XK_A);
            XTestFakeKeyEvent(display, keycode, True, 0);
            XTestFakeKeyEvent(display, keycode, False, 0);
        }
        XFlush(display);
    }
    else
    {
        printf("Port does not exist");
    }
}
