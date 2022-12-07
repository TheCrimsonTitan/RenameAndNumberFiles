function ChangeJPG () {

        echo "Basename: $1"
        echo "Offset: $2"

        offset=$2

#       ls *.jpg

        for f in $PWD/*.jpg
        do
          mv -n "$f" "$1 ($offset).jpg"
        offset=$((offset+1))

        done
}

function ChangeMp4 {

        echo "Basename: $1"
        echo "Offset: $2"

        offset=$2


        for f in $PWD/*.mp4
        do
            mv -n "$f" "$1 ($offset).mp4"
        offset=$((offset+1))

        done
}


echo "What File Type are we renaming?"
echo "A) JPG"
echo "B) MP4"
read UserChoice

echo "What is the path?"
read PathToFiles
echo $PathToFiles

echo "What is base name?"
read NameOfFile
echo $NameOfFile

echo "How many do we already have?"
read offset

FILES=$PathToFiles


cd $PathToFiles
#echo "inside $PWD"


case $UserChoice in
	
	A)
	ChangeJPG "$NameOfFile" "$offset"
        ;;

	B)
	ChangeMp4 "$NameOfFile" "$offset"
	;;

esac
