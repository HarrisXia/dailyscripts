num=0
for clothes in /home/xia/huafei/tianchi/bu/test_a;
do
    echo $clothes
            num=$(expr $num + 1)
            echo $num
            find ${clothes}/ -name \*.jpg > test_${num}.txt
            cat test*.txt > z_rank.txt

done
rm -rf test*.txt
