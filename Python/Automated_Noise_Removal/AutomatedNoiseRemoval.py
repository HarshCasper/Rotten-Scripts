import sys
import os
import glob
import subprocess
from pydub import AudioSegment

# Sox path is DIFFERENT FOR EACH SYSTEM!! (install sox if you haven't using link in README.md)
MYSOX_PATH = '"C:\\Users\\Rahul Rana\\OneDrive - Microsoft Student Ambassadors\\Azure Applications\\sox\\sox.exe"' 

MYTESTING_FILE = "test.wav"
MYSILENCING_FILE = "silence.wav"
MYSILENCING_PROFILE = "silence.prof"


def performOperations(operations, parameters):
    """
    Operating on given inputs and tracking them in a list
    """
    
    trackedInputs = glob.glob(os.path.join(parameters["root"],"*.wav"))
    frequency = 1
    
    for f in trackedInputs:
        
        myprint("[{}/{}] Going on : {}".format(frequency, len(trackedInputs), f), 4)
        frequency += 1
        
        if "noiseProfile" in operations:
            noiseProfile(f)
        
        if "denoiseCall" in operations:
            denoiseCall(f)
    
    if "cleanDir" in operations:
        cleanDir()


def denoiseCall(fileInput):	
    """ 
    takes file as input then generates a profile based on the input file
    takes file and profile as input and gives the output file with 0.3 profile set 
    0.3 setting is what I liked the most. User can play around with this value and can increase decrease it according to taste
    """
    
    mySoundOne = AudioSegment.from_file(MYSILENCING_FILE, format="wav")
    partLen = len(mySoundOne) / 1000.0
    
    instruction = '{sox} "{wav_in}" -n Trimming 0 {silence_len} --Noise Profile-- {prof_out}'.format(sox=MYSOX_PATH, wav_in=MYSILENCING_FILE, silence_len=partLen, prof_out=MYSILENCING_PROFILE)
    
    myprint(instruction, 0)
    myprint(subprocess.call(instruction), 1)
    
    out_file = os.path.join(os.path.dirname(fileInput), " --Now Cleaned-- ", os.path.basename(fileInput))
    
    if not os.path.exists(os.path.dirname(out_file)):
        os.makedirs(os.path.dirname(out_file))
    
    instruction = '{sox} "{wav_in}" "{wav_out}" --Reduce Noise-- {prof_in} 0.3'.format(sox=MYSOX_PATH, wav_in=fileInput, wav_out=out_file, prof_in=MYSILENCING_PROFILE)
    
    myprint(instruction, 0)
    myprint(subprocess.call(instruction), 1)


def noiseProfile(fileInput):
    """
    To find part where there is silence that can be later used for profiling
    """

    mySoundOne = AudioSegment.from_file(fileInput, format="wav")
    
    milliSec = 0
    silenceFound = 0
    maxTimeFound = 500
    maxValue = None
    
    for var in mySoundOne:
        if var.dBFS > -38.0:
            length = milliSec - silenceFound
            if length > maxTimeFound:
                maxValue = mySoundOne[silenceFound : milliSec]
                maxTimeFound = length
            silenceFound = milliSec + 1
        milliSec += 1
    
    myprint(" --Longest Segment-- " + str(maxTimeFound / 1000.0) + " Seconds ", 2)
    
    maxValue[200:-200].export(MYSILENCING_FILE, format="wav")


def cleanDir():
    """
    To remove files that are no longer needed once the script has done work
    """

    os.remove(MYSILENCING_FILE)
    os.remove(MYSILENCING_PROFILE)	
                

PRINT_LEVEL=2 # for organising output
def myprint(str, level=0):
    """
    To organise output prints
    """

    if (level >= PRINT_LEVEL):
        print(str)


if __name__ == '__main__':

    # write this code in your main in case you are importing this file
    
    operations = [
    
        "noiseProfile",
        "denoiseCall",
        "cleanDir",
        "blankCall" 
    
        # Last file does not have to do with anything!
    
    ]
    
    
    parameters = {
    
        "root" : sys.argv[1],
        "blankCall" : None 
        # [SAME] Last file does not have to do with anything!
    
    }

    performOperations(operations, parameters)
    
    sys.exit(0)
