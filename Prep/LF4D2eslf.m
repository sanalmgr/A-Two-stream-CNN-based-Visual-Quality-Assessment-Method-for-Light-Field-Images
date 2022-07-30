function eslf=LF4D2eslf(y,x,t,s, fileList) 
%[listimagename, paths] = uigetfile('MultiSelect', 'on' ,'*.png' );

clear LF4D
% load all images into LF4D format I(y,x,t,s)
numim=0;
for itervertview=1:t
    for iterhorview=1:s
        numim = numim+1;
        tempim = double(imread([fileList(numim).folder, '\', fileList(numim).name]));
        %pth2Dest = strcat('G:/Projects/4/convert_sais_to_mlis/mlis_valid/', num2str(numim), '.png');
        %imwrite(tempim, pth2Dest);
        LF4D(:,:,:,itervertview,iterhorview) = tempim;
    end
end

% create output image size with 3 colour channels, type same with ori im
% (uint8 in this case)
eslf=double(zeros(y*t,x*s,3));

% run through all pixels y,x
for y_pos=1:y
    for x_pos=1:x
        %         pick the same position pixel from all views
        temppx=LF4D(y_pos,x_pos,:,:,:);
        % transform the view dimension t,s to y,x dimension
        temppx=permute(temppx,[4,5,3,1,2]);
        % put the pixels to the output image
        eslf( (y_pos-1)*t +1 : y_pos*t , (x_pos-1)*s +1 : x_pos*s , :) = temppx;
    end
end
% imtool(eslf,[])