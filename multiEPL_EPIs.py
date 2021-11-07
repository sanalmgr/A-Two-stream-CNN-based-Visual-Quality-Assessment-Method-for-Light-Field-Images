#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 12:51:38 2020

@author: sanaalamgeer
"""
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import os
import sys
import numpy as np
import scipy.misc
import cv2
from PIL import Image
import imageio

def loadlf(folder):
	filelist = sorted(os.listdir(folder))
	for img in filelist[:]:
		if not(img.endswith(".png")):
			filelist.remove(img)

	LF_r = list()
	LF_g = list()
	LF_b = list()

	for i in range(len(filelist)):
		filename = folder+"/"+filelist[i]
		img = imageio.imread(filename)
		LF_r.append(img[:, :, 0])
		LF_g.append(img[:, :, 1])
		LF_b.append(img[:, :, 2])

	return (LF_r, LF_g, LF_b)

def lf2epi(LF):
	return np.transpose(LF, (0, 2, 1))

def main():
	path2DB = 'path_to_SAIs/'
	DBDirs = os.listdir(path2DB)
	DBDirs.sort()
    
	for lf in DBDirs[:]:
		path2LF = path2DB + lf

		(LF_r, LF_g, LF_b) = loadlf(path2LF)
		height, width = LF_r[0].shape
		#np.median(list(range(0,720))) = 359.5 < MPI
		#np.median(list(range(0, 434))) = 216.5 < WIN5LID
		if height == 408:
			index_t = np.median(list(range(0, 408)))
		elif height == 512:
			index_t = np.median(list(range(0, 512)))
		print(index_t)

		list_of_epis = []
		#10 x 10 = MPI
		#9 x 9 = win5lid
		for i in range(14): #change here according to the number of rows
			row_start = i*14
			row_end = row_start+13 #row minus one

			LF_rt = lf2epi(LF_r[row_start:row_end+1])
			LF_gt = lf2epi(LF_g[row_start:row_end+1])
			LF_bt = lf2epi(LF_b[row_start:row_end+1])
			dims = LF_rt.shape
			
			for j in range(int(float(index_t)), int(float(index_t))+1):
				EPI_r = LF_rt[:, :, j]
				EPI_g = LF_gt[:, :, j]
				EPI_b = LF_bt[:, :, j]
				img = np.zeros((14, dims[1], 3), 'uint8') # change here the row
				img[:, :, 0] = EPI_r
				img[:, :, 1] = EPI_g
				img[:, :, 2] = EPI_b
    
				list_of_epis.append(img)
    
		row_epi = cv2.vconcat(list_of_epis)

		EPIfilename = 'path_to_output/' + lf +".png"   

		imageio.imwrite(EPIfilename, row_epi)

if __name__ == "__main__":
	main()


