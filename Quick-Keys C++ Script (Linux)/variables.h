#ifndef VARIABLES_H
#define VARIABLES_H
#endif

#include <iostream>

using namespace std;

#define BUTTONNUM 6

const char *serial_port = "/dev/ttyUSB0";
string symbols[BUTTONNUM] = {"\u03c0",      //pi
                             "\u03b1",      //alpha
                             "\u03a3",      //sigma
                             "\u0394",      //delta
                             "\u03b2",      //beta
                             "\u03a9"};     //omega;

string testsym = "\u03c0";
wchar_t testchar = '\u03c0';

struct profile
{
    string name;
    string symbols[BUTTONNUM];
};
