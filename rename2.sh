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

ChangeJPG "$NameOfFile" "$offset"

function ChangeMp4 {

        for f in $files/*.mp4
        do
            mv -n "$f" "$nameoffile ($offset).mp4"
        offset=$((offset+1))

        done
}

#       fi

