#!/bin/zsh
a=""
b=""
for i in $(seq 0 7)
do
    b=$(git diff --shortstat "master@{ $i+1 day ago }..master@{now}")
    if [[ "$b" != "$a" ]]; then
        echo $(date --date="$i days ago" +%F) $b
    else
        echo $(date --date="$i days ago" +%F) 0 files changed, 0 insertions\(+\), 0 deletions\(-\)
    fi
    a=$b
done
