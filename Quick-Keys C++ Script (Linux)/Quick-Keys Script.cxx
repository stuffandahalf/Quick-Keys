#include <iostream>
#include <stdio.h>
#include <unistd.h>
#include <fcntl.h>
#include <pthread.h>

#ifdef __linux__
    #include <X11/Xlib.h>
    #include <X11/keysym.h>
    #include <X11/extensions/XTest.h>
#endif

using namespace std;

void main_script(const char *portname);

int main(int argc, char **argv)
{
    const char *serial_port = "/dev/ttyUSB0";
    //pthread_create(
    main_script(serial_port);
	return 0;
}

void main_script(const char *portname)
{
    string symbols[6] = {"\u03c0", "\u03b1", "\u03a3", "\u0394", "\u03b2", "\u03a9"};
    int ser = open(portname, O_RDONLY);
    char byte[2];
    while(true)
    {
        int size = read(ser, &byte, 1);
        if(size > 0) {
            cout << byte[0];
            int i = (int) byte[0];
            cout << symbols[i];
        }
    }
}
