#ifndef VARIABLES_H
#define VARIABLES_H

#include <iostream>

using namespace std;

#define BUTTONNUM 6

const char *serial_port = "/dev/ttyUSB1";
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

#define UINPUT_MAX_NAME_SIZE    80
/*struct uinput_user_dev {
    char name[UINPUT_MAX_NAME_SIZE];
    struct input_id id;
        int ff_effects_max;
        int absmax[ABS_MAX + 1];
        int absmin[ABS_MAX + 1];
        int absfuzz[ABS_MAX + 1];
        int absflat[ABS_MAX + 1];
};*/

#endif
