
# colors - you may add more colors
WHITE='\[\033[1;37m\]'
LIGHTGRAY='\[\033[0;37m\]'
GRAY='\[\033[1;30m\]'
BLACK='\[\033[0;30m\]'
RED='\[\033[0;31m\]'
LIGHTRED='\[\033[1;31m\]'
GREEN='\[\033[0;32m\]'
LIGHTGREEN='\[\033[1;32m\]'
BROWN='\[\033[0;33m\]'
YELLOW='\[\033[1;33m\]'
BLUE='\[\033[0;34m\]'
LIGHTBLUE='\[\033[1;34m\]'
PURPLE='\[\033[0;35m\]'
PINK='\[\033[1;35m\]' 
CYAN='\[\033[0;36m\]'
LIGHTCYAN='\[\033[1;36m\]'
DEFAULT='\[\033[0m\]'
VIOLET='\[\033[01;35m\]'

# change colors for different components here
cARROW=$VIOLET
cLINES=$GRAY #Lines and Arrow
cBRACKETS=$GRAY # Brackets around each data item
cERROR=$LIGHTRED # Error block when previous command did not return 0
cSUCCESS=$GREEN  # When last command ran successfully and return 0
cTIME=$LIGHTGRAY # The current time
cUSR=$LIGHTBLUE # Color of user
cUHS=$CYAN # Color of the user and hostname separator, probably '@'
cSSH=$PINK # Color for brackets if session is an SSH session
cHST=$LIGHTGREEN # Color of hostname
cRWN=$RED # Color of root warning
cPWD=$BLUE # Color of current directory
cCMD=$DEFAULT # Color of the command you type

# seperator, default '@' you may use any ASCII character
UHS="@"

# parse git branch - install git beforehand
function parse_git_branch() {
    git branch 2> /dev/null | sed -e '/^[^*]/d' -e 's/* \(.*\)/(\1)/'
}

function command_prompt() {
    # get error code of previous command
    PREVIOUS=$?

    # insert a new line to clear space from previous command
    PS1="\n"

    # First line - arrow wrap around and color
    PS1="${PS1}${cARROW}\342\224\214\342\224\200"

    # First line - show if previous command was successful
    if [ $PREVIOUS -ne 0 ] ; then
        PS1="${PS1}${cBRACKETS}[${cERROR}:(${cBRACKETS}]${cLINES}\342\224\200"
    else
        PS1="${PS1}${cBRACKETS}[${cSUCCESS}:)${cBRACKETS}]${cLINES}\342\224\200"
    fi

    # First line - current time
    PS1="${PS1}${cBRACKETS}[${cTIME}\D{%H:%M}${cBRACKETS}]${cLINES}\342\224\200"

    # First line - set color of brackets if its an SSH session
    if [[ $SSH_CLIENT ]] || [[ $SSH2_CLIENT ]]; then
                sesClr="$cSSH"
        else
                sesClr="$cBRACKETS"
    fi

    # First line - Dont display user if its root
    if [ $EUID -eq 0 ] ; then
                PS1="${PS1}${sesClr}[${cRWN}!"
        else
                PS1="${PS1}${sesClr}[${cUHS}\u"
    fi

    # First line - Host session
    PS1="${PS1}${cUHS}${UHS}\h${sesClr}]${cLINES}\342\224\200"

    # First line - current Directory
    PS1="${PS1}[${cPWD}\w${cBRACKETS}]"

    #First line - Conda and Git information
    if [[ ! -z "$CONDA_DEFAULT_ENV" ]]; then
                PS1="${PS1} ${cSUCCESS}$(parse_git_branch) ${cBRACKETS}venv:${VIOLET}${CONDA_DEFAULT_ENV}"
        else
                PS1="${PS1} ${cSUCCESS}$(parse_git_branch)"
    fi

    # Second line - arrow ending 
    PS1="${PS1}\n${cARROW}\342\224\224\342\224\200\342\224\200> ${cCMD}"
}

# load your custom prompt
function load_prompt () {
    PROMPT_COMMAND=command_prompt
    export PS1 PROMPT_COMMAND
}

load_prompt