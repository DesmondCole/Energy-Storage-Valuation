import pandas as pd
import numpy as np
from src import PySSC

class Solar:
    '''
    simul: Obtain generation data using NREL's SAM.
    simple: Use actual generation data.
    '''
    def __init__(self, *, type):
        if type == 'simul':
            self.data = self._genvals()
        if type == 'simple':
            data = pd.read_csv('../data/generation.csv', parse_dates=['LocalTime'])
            data['date'] = data['LocalTime'].dt.date
            data['month'] = data['LocalTime'].dt.month
            self.data = data.groupby(['date','month','hour']).mean().reset_index()
        return None

    def _genvals(self):
        '''
        Add in SAM code.
        '''
        ssc = PySSC.PySSC()
        ssc.module_exec_set_print(0)
        data = ssc.data_create()
        ssc.data_set_string( data, b'solar_resource_file', b'C:/SAM/2018.11.11/solar_resource/phoenix_az_33.450495_-111.983688_psmv3_60_tmy.csv' );
        ssc.data_set_number( data, b'system_capacity', 4 )
        ssc.data_set_number( data, b'module_type', 0 )
        ssc.data_set_number( data, b'dc_ac_ratio', 1.2000000476837158 )
        ssc.data_set_number( data, b'inv_eff', 96 )
        ssc.data_set_number( data, b'losses', 14.075660705566406 )
        ssc.data_set_number( data, b'array_type', 0 )
        ssc.data_set_number( data, b'tilt', 20 )
        ssc.data_set_number( data, b'azimuth', 180 )
        ssc.data_set_number( data, b'gcr', 0.40000000596046448 )
        ssc.data_set_number( data, b'adjust:constant', 0 )
        module = ssc.module_create(b'pvwattsv5')
        ssc.module_exec_set_print( 0 );
        if ssc.module_exec(module, data) == 0:
    	    print ('pvwattsv5 simulation error')
    	    idx = 1
    	    msg = ssc.module_log(module, 0)
    	    while (msg != None):
    		    print ('	: ' + msg.decode("utf - 8"))
    		    msg = ssc.module_log(module, idx)
    		    idx = idx + 1
    	    SystemExit( "Simulation Error" );
        ssc.module_free(module)
        annual_energy = ssc.data_get_number(data, b'annual_energy');
        print ('Annual energy (year 1) = ', annual_energy)
        capacity_factor = ssc.data_get_number(data, b'capacity_factor');
        print ('Capacity factor (year 1) = ', capacity_factor)
        kwh_per_kw = ssc.data_get_number(data, b'kwh_per_kw');
        print ('Energy yield (year 1) = ', kwh_per_kw)
        ssc.data_free(data)
        ssc.data_get_array(data, b'gen');
        return True
