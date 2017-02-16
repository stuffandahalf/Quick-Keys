#include <iostream>
#include <unistd.h>
#include <fcntl.h>

using namespace std;

//char buffer[64];

int main(int argc, char **argv)
{
    int ser = open("/dev/ttyUSB0", O_RDONLY);
    //char byte[0x1000];
    char byte;
    while(true)
    {
        int size = read(ser, &byte, 1);
        if(size > 0) {
            cout << byte;
        }
    }
	return 0;
}

