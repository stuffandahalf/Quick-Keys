#include <iostream>

#include "quickkeys.hxx"

QuickKeys::QuickKeys()
{
    this->port = "/dev/ttyUSB0";
    this->profile = new Profile();
}

QuickKeys::QuickKeys(Profile prof)
{
    this->port = "/dev/ttyUSB0";
    this->profile = &prof;
}

QuickKeys::~QuickKeys()
{
    std::cout << "Deleted Quick Keys Object" << std::endl;
    delete(this->profile);
}
