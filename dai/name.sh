num=0
for clothes in '/home/xia/1-huafei/tianchi/bu/fs/fs_test_yolo';
do
    echo $clothes
            num=$(expr $num + 1)
            echo $num
            find ${clothes}/ -name \*.jpg > test_${num}.txt
            cat test*.txt > z_rank.txt

done
rm -rf test*.txt
