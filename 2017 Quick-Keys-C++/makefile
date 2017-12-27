OBJS = QuickKeys.o QKLib.o QuickKeysImpl.o ProfileImpl.o UInputLib.o
CCA = g++
CCB = gcc
DEBUG = -g
CFLAGS = -Wall -c $(DEBUG)
LFLAGS = -Wall $(DEBUG)

QuickKeys: $(OBJS) 
	$(CCA) $(LFLAGS) $(OBJS) -o QuickKeys
	
QuickKeys.o: QuickKeys.cxx
	$(CCA) $(CFLAGS) QuickKeys.cxx
	
QKLib.o: QKLib.cxx
	$(CCA) $(CFLAGS) QKLib.cxx
	
ProfileImpl.o: ProfileImpl.cxx
	$(CCA) $(CFLAGS) ProfileImpl.cxx
	
QuickKeysImpl.o: QuickKeysImpl.cxx
	$(CCA) $(CFLAGS) QuickKeysImpl.cxx
	
UInputLib.o: UInputLib.c
	$(CCB) $(CFLAGS) UInputLib.c

clean:
	rm *.o

