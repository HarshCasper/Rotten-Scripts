#!/bin/bash

# Author: Muhammad Galhoum

  echo $'\n\n\n\n\n\n
                        ==============================
                            Welcome to my Program 
                        ==============================
                          |Author: Muhammad Galhoum|'
  sleep 5
  clear;

  echo $'\n\n\n\n\n\n
                        ==============================
                            How to use my program
                        =============================='
  sleep 2
  clear;

function startMenu {
  echo "========== Start Menu ==========="
  echo "# 1. Instructions               #"
  echo "# 2. I already know             #"
  echo "# 3. Exit                       #"
  echo "================================="
  echo -e "Choose One Choice From Above : \c"
  read choice
  case $choice in
    1) clear; instructions ;;
    2) clear ; dbMenu ;;
    3) exitProgram ;;
    *) echo " Wrong Choice, Enter Any Number From {1..3} " ; startMenu;
  esac
}

function instructions {
	clear;
	echo $'\n\n\n\n\n\n
              ===========================================================
                  All names in our program like Database name,Table name
                  and Column name must not contain any space, I advise
                  you to write any name consists of one word or you can 
                  follow camelCase or snake_case ways like the following
                  examples: student, dbOne, my_table
              =========================================================== '
	sleep 10;
	clear;
  startMenu ;
}


mkdir -p DataBases 2>> ./.errors
clear
function dbMenu {
  echo "=========== Main Menu ============"
  echo "# 1. Create DataBase             #"
  echo "# 2. List DataBase               #"
  echo "# 3. Connect to DataBase         #"
  echo "# 4. Drop DataBase               #"
  echo "# 5. Clear the screen            #"
  echo "# 6. Exit                        #"
  echo "=================================="
  echo -e "Choose only one Choice from Main Menu: \c"
  read choice
  case $choice in
    1)  createDataBase ;;
    2)  cd ./DataBases 2>>./.errors; ls ; dbMenu;;
    3)  selectDataBase ;;
    4)  dropDataBase ;;
    5)  chooseMenu ;;
    6)  exitProgram ;;
    *) echo " Wrong Choice, please Enter any number from {1..6} " ; dbMenu;
  esac
}

function createDataBase {
  echo -e "Enter Database Name: \c"
  read DBName
  mkdir -p ./DataBases/$DBName
  if [[ $? == 0 ]]
  then
    echo "Database Created Successfully"
  else
    echo "Error When Try To Create Database $DBName"
  fi
  dbMenu
}

function selectDataBase {
  echo -e "Enter Database Name To Select It : \c"
  read DBName
  cd ./DataBases/$DBName 2>>./.errors
  if [[ $? == 0 ]]; then
    echo "Database $DBName was Successfully Selected"
    tablesMenu
  else
    echo "Database $DBName wasn't found, Try To Select Another One"
    dbMenu
  fi
}

function dropDataBase {
  echo -e "Enter Database Name To Drop It : \c"
  read DBName
  rm -r ./DataBases/$DBName 2>>./.errors
  if [[ $? == 0 ]]; then
    echo "Database Dropped Successfully"
  else
    echo "Database Not found, Try To Select Another"
  fi
  dbMenu
}

function tablesMenu {
  echo "========== Tables Menu ==========="
  echo "# 1. Create Table                #"
  echo "# 2. List Tables                 #"
  echo "# 3. Drop Table                  #"
  echo "# 4. insert Into Table           #"
  echo "# 5. Select From Table(2 Choices)#"
  echo "# 6. Delete From Table           #"
  echo "# 7. Update Table                #"
  echo "# 8. Back To Main Menu           #"
  echo "# 9. Clear the screen            #"
  echo "# 10.Exit                        #"
  echo "=================================="
  echo -e "Choose One Choice From Above : \c"
  read ch
  case $ch in
    1)  createTable ;;
    2)  ls .; tablesMenu ;;
    3)  dropTable;;
    4)  insertIntoTable;;
    5)  clear; selectMenu ;;
    6)  deleteFromTable;;
    7)  updateTable;;
    8)  clear; cd ../.. 2>>./.errors; dbMenu ;;
    9)  chooseMenu ;;
    10) exitProgram ;;
    *) echo " Wrong Choice,Please Choose Any Number From {1..10} " ; tablesMenu;
  esac

}

function createTable {
  echo -e "Please Enter Table Name: \c"
  read tableName
  if [[ -f $tableName ]]; then
    echo "This Table Is already existed ,choose another name"
    tablesMenu
  fi
  echo -e "Enter Number of Columns: \c"
  read colsNum
  counter=1
  fSep="|"
  rSep="\n"
  pKey=""
  metaData="Field"$fSep"Type"$fSep"key"            
  while [ $counter -le $colsNum ]
  do
    echo -e "Enter Name of Column No.$counter: \c"
    read colName

    echo -e "Enter Type of Column $colName: "
    select var in "int" "str"
    do
      case $var in
        int ) colType="int";break;;
        str ) colType="str";break;;
        *   ) echo "Wrong Choice" ;;
      esac
    done
    if [[ $pKey == "" ]]; then
      echo -e "Make This Column PrimaryKey ? "
      select var in "yes" "no"
      do
        case $var in
          yes ) pKey="PK";
          metaData+=$rSep$colName$fSep$colType$fSep$pKey;
          break;;
          no )
          metaData+=$rSep$colName$fSep$colType$fSep
          break;;
          * ) echo "Wrong Choice" ;;
        esac
      done
    else
      metaData+=$rSep$colName$fSep$colType$fSep
    fi
    if [[ $counter == $colsNum ]]; then
      temp=$temp$colName
    else
      temp=$temp$colName$fSep
    fi
    ((counter++))
  done
  touch .$tableName
  echo -e $metaData  >> .$tableName
  touch $tableName
  echo -e $temp >> $tableName
  if [[ $? == 0 ]]
  then
    echo "Good, Table Created Successfully"
    temp="" 
    tablesMenu

  else
    echo "Error When Try To Create Table $tableName"
    temp="" 
    tablesMenu
  fi
}

function dropTable {
  echo -e "Enter Table Name That u Wanna Drop It: \c"
  read tName
  rm $tName .$tName 2>>./.errors
  if [[ $? == 0 ]]
  then
    echo "Table Dropped Successfully"
  else
    echo "Error when we try to Drop Table $tName"
  fi
  tablesMenu
}

function insertIntoTable {
  echo -e "Enter Table Name That U Wanna Insert Into It: \c"
  read tableName
  if ! [[ -f $tableName ]]; then
    echo "Table $tableName isn't existed ,choose another Table"
    tablesMenu
  fi
  colsNum=`awk 'END{print NR}' .$tableName`
  fSep="|"
  rSep="\n"
  for (( i = 2; i <= $colsNum; i++ )); do
    colName=$(awk 'BEGIN{FS="|"}{ if(NR=='$i') print $1}' .$tableName)
    colType=$( awk 'BEGIN{FS="|"}{if(NR=='$i') print $2}' .$tableName)
    colKey=$( awk 'BEGIN{FS="|"}{if(NR=='$i') print $3}' .$tableName)
    echo "$colName ($colType) = "
    read data

    # Validate Input
    if [[ $colType == "int" ]]; then
      while ! [[ $data =~ ^[0-9]*$ ]]; do
        echo "invalid DataType !!"
        echo -e "$colName ($colType) = \c"
        read data
      done
    fi

    if [[ $colKey == "PK" ]]; then
      while [[ true ]]; do
        if [[ $data =~ ^[`awk 'BEGIN{FS="|" ; ORS=" "}{if(NR != 1)print $(('$i'-1))}' $tableName`]$ ]]; then
          echo "invalid input for Primary Key !!"
        else
          break;
        fi
        echo -e "$colName ($colType) = \c"
        read data
      done
    fi

    #Set row
    if [[ $i == $colsNum ]]; then
      row=$row$data$rSep
    else
      row=$row$data$fSep
    fi
  done
  echo -e $row"\c" >> $tableName
  if [[ $? == 0 ]]
  then
    echo "Well Done, Data inserted Successfully"
  else
    echo "Error When Try To Insert Into Table $tableName"
  fi
  row=""
  tablesMenu
}

function updateTable {
  echo -e "Enter Table Name To Update It: \c"
  read tName
  if ! [[ -f $tName ]]; then
    echo "Table $tName isn't existed ,choose another Table"
    tablesMenu
  fi
  echo -e "Enter Column name That U want To update It's Value: \c"
  read field
  fid=$(awk 'BEGIN{FS="|"}{if(NR==1){for(i=1;i<=NF;i++){if($i=="'$field'") print i}}}' $tName)
  if [[ $fid == "" ]]
  then
    echo "Not Found"
    tablesMenu
  else
    echo -e "Enter The Old Value That Will be Updated: \c"
    read val
    res=$(awk 'BEGIN{FS="|"}{if ($'$fid'=="'$val'") print $'$fid'}' $tName 2>>./.errors)
    if [[ $res == "" ]]
    then
      echo "Value Not Found"
      tablesMenu
    else
      echo -e "Enter Field name again to set New Value to It: \c"
      read setField
      setFid=$(awk 'BEGIN{FS="|"}{if(NR==1){for(i=1;i<=NF;i++){if($i=="'$setField'") print i}}}' $tName)
      if [[ $setFid == "" ]]
      then
        echo "Not Found"
        tablesMenu
      else
        echo -e "Enter new Field Value to set it: \c"
        read newValue
        NR=$(awk 'BEGIN{FS="|"}{if ($'$fid' == "'$val'") print NR}' $tName 2>>./.errors)
        oldValue=$(awk 'BEGIN{FS="|"}{if(NR=='$NR'){for(i=1;i<=NF;i++){if(i=='$setFid') print $i}}}' $tName 2>>./.errors)
        echo $oldValue
        sed -i ''$NR's/'$oldValue'/'$newValue'/g' $tName 2>>./.errors
        echo "Row Updated Successfully"
        tablesMenu
      fi
    fi
  fi
}

function deleteFromTable {
  echo -e "Enter Table Name To Delete From It: \c"
  read tName
  if ! [[ -f $tName ]]; then
    echo "Table $tName isn't existed ,choose another Table"
    tablesMenu
  fi
  echo -e "Enter Column name: \c"
  read field
  fid=$(awk 'BEGIN{FS="|"}{if(NR==1){for(i=1;i<=NF;i++){if($i=="'$field'") print i}}}' $tName)
  if [[ $fid == "" ]]
  then
    echo "Not Found"
    tablesMenu
  else
    echo -e "Enter Value To Delete The Row Which Contains This Value : \c"
    read val
    res=$(awk 'BEGIN{FS="|"}{if ($'$fid'=="'$val'") print $'$fid'}' $tName 2>>./.errors)
    if [[ $res == "" ]]
    then
      echo "Value Not Found"
      tablesMenu
    else
      NR=$(awk 'BEGIN{FS="|"}{if ($'$fid'=="'$val'") print NR}' $tName 2>>./.errors)
      sed -i ''$NR'd' $tName 2>>./.errors
      echo "Row Deleted Successfully"
      tablesMenu
    fi
  fi
}

function selectMenu {
  echo "================== Select Menu =================="
  echo "# 1. Select All Columns from the Table          #"
  echo "# 2. Select Specific Column from the Table      #"
  echo "# 3. Back To Tables Menu                        #"
  echo "# 4. Back To Main Menu                          #"
  echo "# 5. Cleae the screen                           #"
  echo "# 6. Exit                                       #"
  echo "#===============================================#"
  echo  -e "Please Choose One From The Above : \c"
  read ch
  case $ch in
    1) selectAll ;;
    2) selectCol ;;
    3) clear; tablesMenu ;;
    4) clear; cd ../.. 2>>./.errors; dbMenu ;;
    5) chooseMenu ;;
    6) exitProgram ;;
    *) echo " Wrong Choice, Enter Any Number From {1..6} " ; selectMenu;
  esac
}

function selectAll {
  echo -e "Enter Table Name That U Wanna print all It's Data: \c"
  read tName
  column -t -s '|' $tName 2>>./.errors
  if [[ $? != 0 ]]
  then
    echo "Table $tName isn't existed"
  fi
  selectMenu
}

function selectCol {
  echo  -e "Enter Table Name That U Wanna Select Column From It: \c"
  read tName
  if ! [[ -f $tName ]]; then
    echo "Table $tName isn't existed ,choose another Table"
    tablesMenu
  fi
  echo "Enter Column Number: "
  read colNum
  awk 'BEGIN{FS="|"}{print $'$colNum'}' $tName
  selectMenu
}

function chooseMenu {
  clear;
  echo "========== Choose Menu ==========="
  echo "# 1. Main Menu                   #"
  echo "# 2. Table Menu                  #"
  echo "# 3. Exit                        #"
  echo "=================================="
  echo -e "Choose One Choice From Above : \c"
  read choice
  case $choice in
    1) clear; dbMenu ;;
    2) clear ; tablesMenu ;;
    3) exitProgram ;;
    *) echo " Wrong Choice, Enter Any Number From {1..3} " ; chooseMenu;
  esac
}

function exitProgram {
	clear;
	echo $'\n\n\n\n\n\n
                        ================================
                          Thanks for using my Program 
                        ================================ '
	sleep 2
	clear
	exit
}

startMenu 
