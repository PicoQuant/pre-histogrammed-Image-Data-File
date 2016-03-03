#!/usr/bin/python
import struct
import sys

if len(sys.argv) != 2:
    sys.exit('Error missing bin file as argument')
    print


fin=open(sys.argv[1])

# PixX pixels in X-direction (int32)
PixX = struct.unpack('i',fin.read(4))[0]
print 'PixX: ' + str(PixX)
# PixY pixels in Y-direction (int32)
PixY = struct.unpack('i',fin.read(4))[0]
print 'PixY: ' + str(PixY)
# PixResol spatial pixel resolution in micrometer (float32)
PixResol = struct.unpack('f',fin.read(4))[0]
print 'PixResol: '+ str(PixResol)
# TCSPCChannels number of TCSPC channels per pixel (float32)
TCSPCChannels = struct.unpack('i',fin.read(4))[0]
print 'TCSPCChannels: '+  str(TCSPCChannels)
# TimeResol	time resolution of the TCSPC histograms in ns (float32)
TimeResol = struct.unpack('f',fin.read(4))[0]
print 'TimeResol: '+ str(TimeResol)

# the histogram is composed of TCSPCChannels int32 values
DecayFormatString = str(TCSPCChannels)+'i'

for y in range(PixY+):
    for x in range(PixX):
        TCSPCDecay=struct.unpack(DecayFormatString,fin.read(TCSPCChannels*4))
        # Now do something with the TCSPCDecay of that specific pixel
fin.close()
