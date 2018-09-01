#!/bin/bash


wd=`pwd`


find ${wd}/divided_img_gray_400_200 -name \*.tiff > test2.txt
find ${wd}/divided_img_gray_400_200 -name \*.tif > test3.txt
cat test2.txt test3.txt > test_gray_400_200.txt

