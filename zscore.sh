cd dirtree
FILES=*
for f in $FILES
do
  echo "Processing $f"
  head -3 $f/$f/report.tbl|tail -1|echo -e "$f\t$(cut -f 4)" >> zscore.txt
done
sort -k2 -n -r zscore.txt -o zscore.txt
mv zscore.txt ../

  
  
