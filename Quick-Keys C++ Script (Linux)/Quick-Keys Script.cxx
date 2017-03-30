#include <iostream>
#include <unistd.h>
#include <fcntl.h>

using namespace std;

void main_script(char *portname);

int main(int argc, char **argv)
{
    main_script("/dev/ttyUSB0");
	return 0;
}

void main_script(string portname)
{
    portname = portname.c_str();
    int ser = open(portname, O_RDONLY);
    char byte[2];
    while(true)
    {
        int size = read(ser, &byte, 1);
        if(size > 0) {
            cout << byte;
        }
    }
}
