from channelConfiguration import channelConfiguration
from ddsConfiguration import ddsConfiguration
# TODO: Does this really need to be imported, looks unused
# Double checked this by searching for remoteChannel in the project
from remoteChannel import remoteChannel

class hardwareConfiguration(object):
    channelTotal = 32
    timeResolution = '40.0e-9' #seconds
    timeResolvedResolution = 10.0e-9
    maxSwitches = 1022
    resetstepDuration = 2 #duration of advanceDDS and resetDDS TTL pulses in units of timesteps
    collectionTimeRange = (0.010, 5.0) #range for normal pmt counting
    sequenceTimeRange = (0.0, 85.0) #range for duration of pulse sequence
    isProgrammed = False
    sequenceType = None #none for not programmed, can be 'one' or 'infinite'
    collectionMode = 'Normal' #default PMT mode
    collectionTime = {'Normal':0.100,'Differential':0.100} #default counting rates
    okDeviceID = 'Pulser'
    okDeviceFile = 'pulser_2013_06_05.bit'
    lineTriggerLimits = (0, 15000)#values in microseconds
    secondPMT = False
    DAC = False

    #name: (channelNumber, ismanual, manualstate,  manualinversion, autoinversion)
    channelDict = {
                   'ch1':channelConfiguration(1, False, True, False, True),
                   'ch2':channelConfiguration(2, False, True, False, True),
                   'ch3':channelConfiguration(3, False, True, False, True),
                   'ch4':channelConfiguration(4, False, True, False, True),
                   'ch5':channelConfiguration(5, False, True, False, True),
                   'ch6':channelConfiguration(6, False, True, False, True),
                   'ch7':channelConfiguration(7, False, True, False, True),
                   'ch8':channelConfiguration(8, False, True, False, True),
                   'ch9':channelConfiguration(9, False, True, False, True),
                   'ch10':channelConfiguration(10, False, True, False, True),
                   'ch11':channelConfiguration(11, False, True, False, True),
                   'ch12':channelConfiguration(12, False, True, False, True),
                   'ch13':channelConfiguration(13, False, True, False, True),
                   'ch14':channelConfiguration(14, False, True, False, True),
                   'ch15':channelConfiguration(15, False, True, False, True),
#                   'ch16':channelConfiguration(16, False, True, False, True),
#                   '866DP':channelConfiguration(12, False, True, False, True),
#                   'crystallization':channelConfiguration(1, True, False, False, False),
#                   'bluePI':channelConfiguration(2, True, False, True, False),
#                   'camera':channelConfiguration(5, False, False, True, True),
#                   'coil_dir':channelConfiguration(6, False, False, True, True),
                   #------------INTERNAL CHANNEgiLS----------------------------------------#
                   'Internal866':channelConfiguration(0, False, False, False, False),
                   'DiffCountTrigger':channelConfiguration(16, False, False, False, False),
                   'TimeResolvedCount':channelConfiguration(17, False, False, False, False),
                   'AdvanceDDS':channelConfiguration(18, False, False, False, False),
                   'ResetDDS':channelConfiguration(19, False, False, False, False),
                   'ReadoutCount':channelConfiguration(20, False, False, False, False),
                }
    #address, allowedfreqrange, allowedamplrange, frequency, amplitude, **args):
    ddsDict =   {
                '866DP':ddsConfiguration(        0,  (70.0,90.0),    (-63.0,-5.0),   80.0,   -33.0),
                'global397':ddsConfiguration(    1,  (70.0,100.0),   (-63.0,-12.0),  90.0,   -33.0),
                'radial':ddsConfiguration(       2,  (90.0,130.0),   (-63.0,-12.0),   110.0,  -63.0),
#                  'radial':ddsConfiguration(       2,  (74.0,74.0),   (-63.0,-5.0),   74.0,  -63.0),
                '854DP':ddsConfiguration(        3,  (70.0,90.0),    (-63.0,-4.0),   80.0,   -33.0),
                '729DP':ddsConfiguration(        4,  (150.0,250.0),  (-63.0,-5.0),   220.0,  -33.0),
                }
    remoteChannels = {}