% Reads PicoQuant bin files exported from SymPhoTime64
% This is demo code. Use at your own risk.
% No warranties and no support.
% Peter Kapusta, PicoQuant GmbH, January 22th, 2018
 
    clear all;
    close all;
    
    [filename, pathname]=uigetfile('*.bin', 'Exported binary file:');
    fid=fopen([pathname filename]);

    PixX = fread(fid, 1, 'int32')
    PixY = fread(fid, 1, 'int32')
    PixResol = fread(fid, 1, 'float32')
    TCSPCChannels = fread(fid, 1, 'int32')
    TimeResol = fread(fid, 1, 'float32')
    
    HistogramData=zeros(PixX,PixY,TCSPCChannels);
    
    for x=1:PixX
        for y=1:PixY
            HistogramData(x,y,:)=fread(fid, TCSPCChannels, 'int32');
        end;
    end;    
    fclose(fid);
    
    % The FLIM image is now a 3D matrix (array):
    % HistogramData(PixX, PixY, TCSPCChannels)    
    
    
    % Just as a check, we integrate the 3rd dimension (time)
    % and plot a greyscale (intensity only) image:
    
    BWImage=sum(HistogramData, 3);
    colormap('gray');    
    imagesc(BWImage);
    axis image;
    
    
