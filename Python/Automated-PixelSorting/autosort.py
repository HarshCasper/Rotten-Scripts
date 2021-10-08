import os
import sys
import getopt
import random as r
from PIL import Image
from pixelsort import pixelsort

def randomize_params():
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
        elif param == 'randomness':
            args['randomness'] = r.uniform(0.5, 1)
        elif param == 'sorting_function':
            sorting_fns = ['lightness', 'hue', 'saturation', 'intensity', 'minimum']
            args['sorting_function'] = r.choice(sorting_fns)
        elif param == 'lower_threshold':
            args['lower_threshold'] = r.uniform(0.5, 1)
        elif param == 'upper_threshold':
            up_thresh = r.uniform(0.6, 1)
            if up_thresh <= args['lower_threshold']:
                up_thresh += r.uniform(0.1, 1 - args['lower_threshold'])
            args['upper_threshold'] = up_thresh
        elif args['upper_threshold'] - args['lower_threshold'] < 0.25:
            args['lower_threshold'] -= 0.25
    return args

def perform_sorting(args, img):
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
    return new_img

def Main():
    # --- DEFINE ARGS AND SET DEFAULTS ---
    count = 0
    in_path = 'images/'
    out_path = 'generated/'
    argument_list = sys.argv[1:]
    options = 'hi:n:'

    # --- DEFINE TERMINAL ARG OPERATIONS ---
    try:
        args, _ = getopt.getopt(argument_list, options)
        for current_argument, current_value in args:
            if current_argument in ('-h'):
                print('-'*30)
                print('-h : args description')
                print('-i : pass location of input img-file')
                print('-n : number of outputs required')
                print('-'*30)
            if current_argument in ('-i'):
                print('-'*30)
                in_path += current_value
                print(f'[+] Input-file: {in_path}')
            if current_argument in ('-n'):
                count = int(current_value)
                print(f'[+] Output-Count: {current_value}')
                print('-'*30)

    except getopt.error as error:
        print(str(error))

    # --- DELETE PREVIOUS RESULTS ---
    for file in os.listdir(out_path):
        os.remove(os.path.join(out_path, file))

    # --- GENERATE 'N=COUNT' INSTANCES ---
    for index in range(count):

        # --- CALL PARAMETER FUNCTION ---
        args = randomize_params()

        # --- PRINT RANDOMIZED CHOICES ---
        for arg in args.items():
            print(arg[0], ':', arg[1])

        # --- DEFINE LOCATIONS FOR LOAD AND SAVE ---
        in_file = in_path
        out_file = out_path + f'result-0{index + 1}.png'
        img = Image.open(in_file)

        # --- CALL SORT FUNCTION ---
        new_img = perform_sorting(args, img)
        
        # --- SAVE NEW FILE ---
        new_img.save(out_file)
        print('-'*30)

if __name__ == "__main__":
    Main()
