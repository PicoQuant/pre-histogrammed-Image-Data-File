#!/usr/bin/python
import struct
import sys

if len(sys.argv) != 2:
    sys.exit('Error missing bin file as argument')
    print


fin=open(sys.argv[1])

# PixX	int32	pixels in X-direction
print 'PixX: ' + str(struct.unpack('i',fin.read(4))[0])
# PixY	int32	pixels in Y-direction
print 'PixY: ' + str(struct.unpack('i',fin.read(4))[0])
# PixResol	float32	spatial pixel resolution in micrometer
print 'PixResol: '+ str(struct.unpack('f',fin.read(4))[0])
# TCSPCChannels	int32	number of TCSPC channels per pixel
print 'TCSPCChannels: '+  str(struct.unpack('i',fin.read(4))[0])
# TimeResol	float32	time resolution of the TCSPC histograms in ns
print 'TimeResol: '+ str(struct.unpack('f',fin.read(4))[0])

fin.close()
