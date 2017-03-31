OBJS = Quick-Keys\ Script.o
CC = g++
DEBUG = -g
CFLAGS = -Wall -c $(DEBUG)
LFLAGS = -Wall $(DEBUG)

Quick-Keys\ Script: $(OBJS) 
	$(CC) $(LFLAGS) $(OBJS) `python2-config --cflags --ldflags` -lX11 -lXtst -o Quick-Keys\ Script
	
Quick-Keys\ Script.o: Quick-Keys\ Script.cxx variables.h
	$(CC) $(CFLAGS) Quick-Keys\ Script.cxx

clean:
	\rm *.o *~ Quick-Keys\ Script
