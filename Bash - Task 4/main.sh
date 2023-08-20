awk -F'\t' 'BEGIN {OFS="\t"} $1 ~ /^Xerox/ {print $1, NR}' demo.tsv | sort -k1,1 > output.tsv

cat output.tsv | tee >(wc -l > final.txt) | tee >(sha1sum >> final.txt) | tail -5 >> final.txt

