#!/bin/zsh
echo $PWD
a=""
b=""
for i in $(seq 0 30)
do
    echo 'git diff --shortstat "master@{ $i day ago }..master@{now}"'
    b=$(git diff --shortstat "master@{ $i day ago }..master@{now}")
    if [[ "$b" != "$a" ]]; then
        echo $(date --date="$i days ago" +%F) $b
    else
        echo $(date --date="$i days ago" +%F) 0 files changed, 0 insertions\(+\), 0 deletions\(-\)
    fi
    a=$b
done
