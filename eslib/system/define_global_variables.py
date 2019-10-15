#this module will be used to define all the global variable with consideration of cross platform
import os #retrieve existing system variables
import sys #used to add system path
import platform  #determine the platform this package is running at
from pathlib import Path #get the home directory

sPlatform_os = platform.system()
sCluster = os.environ['SYSTEM_NAME']
sWorkspace_home = str(Path.home())

sWorkspace_configuration = sWorkspace_home
if sPlatform_os == 'Windows':  #windows
    slash = '\\'
    sMachine ='None'
    
    sWorkspace_code = 'C:' + slash + 'workspace'
    sWorkspace_scratch = 'D:'    
else:  #linux or unix
    slash = '/'    
    sWorkspace_code = sWorkspace_home + slash + 'workspace'
    if (sPlatform_os == 'Linux'):
        if( 'compy' in sCluster):
            sMachine='compy'           
            sPython2 = '/share/apps/anaconda2/2019.03/bin/python' #this is used for mixture of python2/3
            sWorkspace_scratch = slash + 'compyfs' + slash + 'liao313'            
        else:
            if( 'constance' in sCluster ):
                sMachine='constance'
                sAccount='e3sm'
                sPython2 = '/share/apps/python/anaconda2.7/bin/python'
                sWorkspace_scratch = slash + 'pic' + slash + 'scratch' + slash + 'liao313'
            else:
                if( 'marianas' in sCluster ):
                    sMachine='marianas'
                    sWorkspace_scratch = slash + 'pic' + slash + 'scratch' + slash + 'liao313'                    
                else:
                    pass
            #more cluster can be added here            
    else:
        if (sPlatform_os == 'Darwin'):
            sWorkspace_scratch = slash + 'Users' + slash + 'liao313' + slash + 'tmp'  
        else:
            pass

sWorkspace_data = sWorkspace_home + slash + 'data'

#now we will start define major global variables
#data file type
sExtension_txt = '.txt'
sExtension_envi = '.dat'
sExtension_tiff = '.tif'
sExtension_header ='.hdr'
sExtension_netcdf = '.nc'
sExtension_shapefile = '.shp'

#graphics
sExtension_png = '.png'
sExtension_jpg = '.jpg'

sFilename_config = sMachine + '_configuration' + sExtension_txt

#constant values
missing_value = -9999.0
mms2mmd = 24 * 3600.0
nmonth = 12
iMonth_start = 1
iMonth_end = 12
