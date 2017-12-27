#include <iostream>
#include <fcntl.h>
#include <unistd.h>
//#include <libxml.parser.h>

#include "quickkeys.hxx"

void mainScript(QuickKeys *qk)
{
    /*int ser = open(qk->port, O_RDONLY);
    char byte[1];
    while(access(qk->port, F_OK) != -1)
    {
        int size = read(ser, &byte, 1);
        if(size > 0)
        {
            int i = (int) byte[0] - (int) '0' - 1;
            if(i >= 0)
            {
                //cout << symbols[i];
                std::cout << i << std::endl;
                //type_symbol(symbols[i]);
            }
        }
        sleep(.75);
    }*/
}
