#ifndef QUICKKEYS_HXX
#define QUICKKEYS_HXX

#include <iostream>

#define BUTTONNUM 6

typedef std::string String;

class Profile
{
    public:
    String prefFile;
    String name;
    char *symbols[BUTTONNUM];
    
    //Constructors
    Profile();
    //Profile();
};

class QuickKeys
{
    public:
    String port;
    Profile *profile;
    
    //Constructors
    QuickKeys();
    QuickKeys(Profile prof);
    
    
    //Desctructor
    ~QuickKeys();
};

void mainScript(QuickKeys *qk);
void loadPrefFile(String fname);

#endif
