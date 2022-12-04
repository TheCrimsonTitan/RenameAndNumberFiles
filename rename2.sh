
echo "What is the path?"
read PathToFiles
echo $PathToFiles

echo "What is base name?"
read NameOfFile
echo $NameOfFile

echo "How many do we already have?"
read offset

FILES=$PathToFiles*


cd $PathToFiles

for f in $FILES
do
	if [[ $f == *".jpg"* ]]; then
	   mv -n "$f" "$NameOfFiles ($offset).jpg"
	fi
	offset=$((offset+1))	
done
