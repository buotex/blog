#!/bin/zsh
a=""
b=""
for i in $(seq 0 7)
do
    #echo git diff --shortstat "master@{ $i+1 day ago }..master@{$i day ago}"
    b=$(git diff --shortstat "master@{ $(($i+1)) day ago 23:59:59 }..master@{$i day ago 23:59:59 }")
    if [[ "$b" != "$a" ]]; then
    echo $(date --date="$i days ago" +%F) $b
    else
        echo $(date --date="$i days ago" +%F) 0 files changed, 0 insertions\(+\), 0 deletions\(-\)
    fi
    #a=$b
done
