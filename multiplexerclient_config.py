class multiplexer_config(object):
    '''
    configuration file for multiplexer client
    info is the configuration dictionary in the form
    {channel_name: (port, hint, display_location, stretched)), }
    '''
    info = {'Repump'              : (1, '384.232000', (1,1), True),
            'Pebbles - MOT light' : (3, '384.229085', (1,3), True),
            'Bamm-Bamm'           : (4, '384.228903', (5,1), True),
            'Ti:Sapph'            : (5, '385.284', (5,3), True),
            }
