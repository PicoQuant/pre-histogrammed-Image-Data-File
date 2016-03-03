#!/usr/bin/python
import struct
import sys

if len(sys.argv) != 2:
    sys.exit('Error missing bin file as argument')
    print


fin=open(sys.argv[1])

# PixX	int32	pixels in X-direction
PixX = struct.unpack('i',fin.read(4))[0]
print 'PixX: ' + str(PixX)
# PixY	int32	pixels in Y-direction
PixY = struct.unpack('i',fin.read(4))[0]
print 'PixY: ' + str(PixY)
# PixResol	float32	spatial pixel resolution in micrometer
PixResol = struct.unpack('f',fin.read(4))[0]
print 'PixResol: '+ str(PixResol)
# TCSPCChannels	int32	number of TCSPC channels per pixel
TCSPCChannels = struct.unpack('i',fin.read(4))[0]
print 'TCSPCChannels: '+  str(TCSPCChannels)
# TimeResol	float32	time resolution of the TCSPC histograms in ns
TimeResol = struct.unpack('f',fin.read(4))[0]
print 'TimeResol: '+ str(TimeResol)

DecayFormatString = str(TCSPCChannels)+'i'

for y in range(PixY+):
    for x in range(PixX):
        TCSPCDecay=struct.unpack(DecayFormatString,fin.read(TCSPCChannels*4))
        # Now do something with the TCSPCDecay of that specific pixel
fin.close()
