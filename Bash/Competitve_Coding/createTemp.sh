
#!/bin/bash
name=$1
mkdir $name
cd $name
touch code.cpp input.txt output.txt

cat ~/template.cpp >> code.cpp


#Choose your editor of choice

#vim .
code .
