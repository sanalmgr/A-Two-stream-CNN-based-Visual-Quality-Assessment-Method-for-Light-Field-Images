clear all
close all

rootPath = 'path_2_light_field_images/';
dirList = dir(fullfile(rootPath));
%organization of directories:
%path_2_light_field_images/
%      light_field_image_1/
%            sai_1.png
%            sai_2.png
%            ...
%     light_field_image_2/
%           sai_1.png
%            sai_2.png
%            ...
%      ...
%      light_field_image_n/
%            sai_1.png
%            sai_2.png
%            ...

outputPath = '/media/sanaalamgeer/Seagate Expansion Drive/Projects/4/convert_sais_to_mlis/mlis_mpi/';

% input parameter
%load('zig_zag_array.mat');
%[t, s] = size(index);
s=10; %horizontal view
t=10; %vertical view
x=960; % width image resolution
y=720; % height image resolution

%start from 3 as 1 and 2 elements are null
for i=301:length(dirList)
    disp(i);
    path2file = strcat(rootPath, '/', dirList(i).name);
    fileList = dir(fullfile(path2file, '*.png'));
    % select all SAIs that will be processed to MLI
    %eslf = zig_zag_LF4D2eslf(y,x,t,s, fileList, index);
    eslf = LF4D2eslf(y, x, t, s, fileList);
    pth2Dest = strcat(outputPath, dirList(i).name, '.png');
    imwrite(eslf, pth2Dest);
end

