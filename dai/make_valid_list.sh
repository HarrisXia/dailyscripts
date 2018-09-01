#!/bin/bash
num=0
for clothes in ./train_valid/*;
do
    echo $clothes
    for trainval in ${clothes}/*
    do
        for classes in ${trainval}/*
        do
            num=$(expr $num + 1)
            echo $num
            find ${classes}/ -name \*.jpg > test_${num}.txt
            cat test*.txt > all.txt
 
        done
    done
done
rm -rf test*.txt
# num=0
# for clothes in ./rank/Images/*;
# do
#     echo $clothes
#             num=$(expr $num + 1)
#             echo $num
#             find ${clothes}/ -name \*.jpg > test_${num}.txt
#             cat test*.txt > rank.txt

# done
# rm -rf test*.txt