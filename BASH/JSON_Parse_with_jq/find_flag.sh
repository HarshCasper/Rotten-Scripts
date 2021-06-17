#!/bin/bash

echo "##########################################################"
echo "### Let's check first few lines of the json file ..."
echo "##########################################################"
echo ""
echo "$ cat sample.json | jq \".\" | head -n 13"
echo ""
echo "Press any key to continue"
while [ true ] ; do
read -t 3 -n 1
if [ $? = 0 ] ; then
cat sample.json | jq "." | head -n 13
break
else
echo "..."
fi
done

echo ""
echo "##########################################################"
echo "### Now analyzing a couple of node objects under edges... "
echo "##########################################################"
echo ""
echo "$ cat sample.json | jq \".data.allPosts.edges[0:3]\""
echo ""
echo "Press any key to continue"
while [ true ] ; do
read -t 3 -n 1
if [ $? = 0 ] ; then
cat sample.json | jq ".data.allPosts.edges[0:3]"
break
else
echo "..."
fi
done

echo ""
echo "##########################################################"
echo "### We'll use grep to get a unique secret value..."
echo "##########################################################"
echo ""
echo "$ cat sample.json | jq \".data.allPosts.edges\" | grep -E -o 'RotteN{.*}' | grep -v 'harder'"
echo ""
echo "Press any key to continue"
while [ true ] ; do
read -t 3 -n 1
if [ $? = 0 ] ; then
cat sample.json | jq ".data.allPosts.edges" | grep -E -o "RotteN{.*}" | grep -v "harder"
exit
else
echo "..."
fi
done
