import os
import sys
import getopt
import random as r
from PIL import Image
from pixelsort import pixelsort

# --- DEFINE ARGS AND SET DEFAULTS ---
count = 0
in_path = 'images/'
out_path = 'generated/'
argumentList = sys.argv[1:]
options = 'hi:n:'

# --- DEFINE TERMINAL ARG OPERATIONS ---
try:
    args, values = getopt.getopt(argumentList, options)
    for currentArgument, currentValue in args:
        if currentArgument in ('-h'):
            print('-'*30)
            print('-h : args description')
            print('-i : pass location of input img-file')
            print('-n : number of outputs required')
            print('-'*30)
        if currentArgument in ('-i'):
            print('-'*30)
            in_path += currentValue
            print(f'[+] Input-file: {in_path}')
        if currentArgument in ('-n'):
            count = int(currentValue)
            print(f'[+] Output-Count: {currentValue}')
            print('-'*30)

except getopt.error as e:
    print(str(e))

# --- DELETE PREVIOUS RESULTS ---
for f in os.listdir(out_path):
    os.remove(os.path.join(out_path, f)) 

for index in range(count):

    angle = r.randint(90, 359)

    # --- DEFINE ALL PARAMETERS ---
    params = {
        1: 'interval_function',
        2: 'randomness',
        3: 'lower_threshold',
        4: 'upper_threshold',
        5: 'sorting_function',
    }

    # --- RANDOMIZE COUNT AND CHOICE OF PARAMS ---
    param_count = r.randint(1, 5)
    selected_params = []
    for _ in range(param_count):
        param_choice = r.randint(1, 5)
        if params[param_choice] not in selected_params:
            selected_params.append(params[param_choice])

    # --- SET DEFAULTS FOR PARAMS ---
    args = {}
    args['angle'] = angle
    args['interval_function'] = 'threshold'
    args['lower_threshold'] = 0.5
    args['upper_threshold'] = 0.8
    args['randomness'] = 0.5
    args['sorting_function'] = 'lightness'

    # --- UPDATE WITH RANDOMIZED VALUES ---
    for param in selected_params:
        if param == 'interval_function':
            interval_fns = ['random', 'threshold', 'waves']
            args['interval_function'] = r.choice(interval_fns)
        if param == 'randomness':
            args['randomness'] = r.uniform(0.5, 1)
        if param == 'sorting_function':
            sorting_fns = ['lightness', 'hue', 'saturation', 'intensity', 'minimum']
            args['sorting_function'] = r.choice(sorting_fns)
        if param == 'lower_threshold':
            args['lower_threshold'] = r.uniform(0.5, 1)
        if param == 'upper_threshold':
            up_thresh = r.uniform(0.6, 1)
            if up_thresh <= args['lower_threshold']:
                up_thresh += r.uniform(0.1, 1 - args['lower_threshold'])
            args['upper_threshold'] = up_thresh
        if args['upper_threshold'] - args['lower_threshold'] < 0.25:
            args['lower_threshold'] -= 0.25

    # --- PRINT THE RANDOMIZED CHOICES ---
    for arg in args:
        print(arg, ':', args[arg])

    # --- DEFINE LOCATIONS FOR LOAD AND SAVE ---
    in_file = in_path
    out_file = out_path + f'result-0{index + 1}.png'
    img = Image.open(in_file)

    # --- PERFORM PIXELSORT WITH RANDOMIZED PARAMS ---
    new_img = pixelsort(
        image = img,
        angle = args['angle'],
        interval_function = args['interval_function'],
        lower_threshold = args['lower_threshold'],
        upper_threshold = args['upper_threshold'],
        randomness = args['randomness'],
        sorting_function = args['sorting_function']
    )

    # --- SAVE NEW FILE ---
    new_img.save(out_file)
    print('-'*30)