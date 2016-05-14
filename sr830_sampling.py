# This a very basic scipt designed to collect data from the SR830
# lockin amplifier using PyVisa.
#
# Programmed user-specified parameters are:
# 1) Sampling rate
# 2) Sampling time
#
# A few other parameters can be specified using the 'SR830_parameters.py'
# scipt if choosen (or use the lockin front panel). 
#
# The main point of this script is to illustrate the process for
# data collection and transfer.
#
# Note that one-shot data collection is used, so you will have a problem if
# you attempt to collect more than 16383 data points.
#
# Also note that if you are using a 512Hz sampling rate then at 6dB/oct your 
# time constant should be: Tau < 5/512Hz ~= 10ms.
#
# Levi Smith - April 13, 2016


import visa
import sys
import scipy as sp
import time
import struct
import SR830_parameters
import matplotlib.pyplot as plt


### user-specified parameters ###
sample_time = 5   # Sample time in seconds
sample_freq = 32  # Select a valid sampling rate (see SR830 manual) [i.e. 1,2,4,8,16,32,64,...]Hz

# check if the one-shot sampling will work
if sample_time*sample_freq >= 16383:
    print('One-shot data collection will not work for you, change the sampling rate or implement loop mode.')
    sys.exit()

# Open a resource manager
rm = visa.ResourceManager()
print(rm.list_resources())

# You may need to change this if your address was changed from the default
sr830 = rm.open_resource('GPIB0::8::INSTR')

# Configure the SR830
sr830.write('REST') # Reset the buffer
sr830.timeout = 1100*sample_time # Set the timeout
SR830_parameters.set_sampling_rate(sr830, sample_freq) # Set the sampling rate
sr830.write('SEND 0')  # One-shot data collection
sr830.write('OUTX 1')  # SR830 responds to GPIB port
sr830.write('FAST 0')  # Fast mode off

# Sample for the specified time
print('Starting scan...', flush=True)
sr830.write('STRT')      # Start scan
time.sleep(sample_time)  # Wait for the scan time (not very elegant...)
sr830.write('PAUS')      # Pause the scan
print('Completed.', flush=True)

# Retrieve the data from the buffer
N = int(sr830.query('SPTS?'))              # How many data points were collected?
print('Transferring X-Data...', flush=True)
sr830.write('TRCB?1,0,%d' % N)             # Request binary data (channel 1)
retByteX = bytearray(sr830.read_raw())     # Collect data
vx = sp.asarray(struct.unpack('<%df' % N,retByteX)) # Unpack into Numpy array
print('Completed.', flush=True)
print('Transferring Y-Data...', flush=True)
sr830.write('TRCB?2,0,%d' % N)             # Request binary data (channel 2)
retByteY = bytearray(sr830.read_raw())     # Collect data
vy = sp.asarray(struct.unpack('<%df' % N,retByteY)) # Unpack into Numpy array
print('Completed.', flush=True)

# Plot the data
t = sp.linspace(0,sample_time,N)
plt.figure(1)
plt.plot(t, vx,'b',t, vy,'r')
plt.xlabel('time')
plt.ylabel('ampltiude')
plt.legend(['X', 'Y'])