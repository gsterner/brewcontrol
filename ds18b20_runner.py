import os
import glob
import time
import csv

UPPER_BOUND = 23
LOWER_BOUND = 19
MAX_POINTS = 200

# These tow lines mount the device:
os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

base_dir = '/sys/bus/w1/devices/'
# Get all the filenames begin with 28 in the path base_dir.
device_folder = glob.glob(base_dir + '28*')[0]
device_file = device_folder + '/w1_slave'
def read_rom():
    name_file=device_folder+'/name'
    f = open(name_file,'r')
    return f.readline()

def read_temp_raw():
    f = open(device_file, 'r')
    lines = f.readlines()
    f.close()
    return lines

def read_temp():
    lines = read_temp_raw()
    # Analyze if the last 3 characters are 'YES'.
    while lines[0].strip()[-3:] != 'YES':
        time.sleep(0.2)
        lines = read_temp_raw()
    # Find the index of 't=' in a string.
    equals_pos = lines[1].find('t=')
    if equals_pos != -1:
        # Read the temperature .
        temp_string = lines[1][equals_pos+2:]
        temp_c = float(temp_string) / 1000.0
        temp_f = temp_c * 9.0 / 5.0 + 32.0
        return temp_c, temp_f

def write_csv(data_rows):
    with open('tempdata.csv', 'w') as outfile:
        writer = csv.writer(outfile)
        for row in data_rows:
            writer.writerow(row)


def add_point(current_data, new_point):
    if len(current_data) > MAX_POINTS:
        current_data.pop(0)
    current_data.append(new_point)
    write_csv(current_data)

data_points = []
print(' rom: '+ read_rom())
while True:
    time_stamp = time.strftime("%H:%M:%S", time.localtime())
    celsius, farenheit = read_temp()
    add_point(data_points, [time_stamp, celsius, UPPER_BOUND, LOWER_BOUND])
    print(time_stamp, ' C=%3.3f  F=%3.3f'% (celsius, farenheit))
time.sleep(1)
