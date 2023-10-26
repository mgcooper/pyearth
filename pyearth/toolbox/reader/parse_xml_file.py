import os
import numpy as np
import xml.etree.ElementTree as ET

def parse_xml_file(sFilename_xml_in):
    """
    Parse an XML file

    Args:
        sFilename_xml_in (string): The XML filename

    Returns:
        dict: The content in the XML file
    """

    if os.path.exists(sFilename_xml_in):
        pass
    else:
        print('The xml file does not exist!')
        return
    tree = ET.parse(sFilename_xml_in)
    root = tree.getroot()
    namelist = {}
    keys_str = []

    for entry in root.findall('./group/entry'):
        key = entry.get('id')
        dtype = entry.find('type').text
        if dtype=='char':
            keys_str.append(key)
        if 'value' in entry.keys():
            # single value setting
            if dtype=='integer':
                value = int(entry.get('value'))
            elif dtype=='real':
                value = float(entry.get('value'))
            elif dtype=='logical':
                if entry.get('value')=='TRUE':
                    value = True
                else:
                    value = False
            else:
                value = entry.get('value')
            namelist[key] = value
        else:
            # value is an array
            values = []
            for value in entry.findall('./values'):
                key = entry.get('id')
                dtype = entry.find('type').text
                if dtype=='integer':
                    values.append(int(value.text))
                elif dtype=='real':
                    values.append(float(value.text))
                elif dtype=='logical':
                    if value.text=='TRUE':
                        values.append(True)
                    else:
                        values.append(False)
                else:
                    values.append(value.text)
            namelist[key] = np.array(values, dtype=np.float64, order='F')

    # fill environment variable values
    for key in keys_str:
        keys_str_iter = list(set(keys_str)-set([key]))
        for okey in keys_str_iter:
            string = namelist[okey]
            if string.find('$'+key)>=0:
                new_string = string.replace('$'+key, namelist[key])
                namelist[okey] = new_string
                
    return namelist

def parse_xml_file_atm(sFilename_xml_in, sVariable_in):
    """
    Parse an XML file

    Args:
        sFilename_xml_in (string): The XML filename

    Returns:
        dict: The content in the XML file
    """

    if os.path.exists(sFilename_xml_in):
        pass
    else:
        print('The xml file does not exist!')
        return
    tree = ET.parse(sFilename_xml_in)
    root = tree.getroot()
    namelist = {}
    keys_str = []

    entry = root.findall('./fieldInfo/filePath')
    sFolder = (entry[0].text).strip()

    entry = root.findall('./fieldInfo/variableNames')
    dummy = (entry[0].text).strip()
    aField0 = dummy.split('\n')  #(dummy.split(" "))
    aField = list()
    for sField in aField0:
        d = sField.strip()
        e = d.split()
        aField.append(e[0])

    entry = root.findall('./fieldInfo/fileNames')
    dummy = (entry[0].text).strip()
    aFilename = dummy.split('\n')

    nf = len(aFilename)
    aFile=list()
    for i in range(nf):
        aFile.append( os.path.join( sFolder ,aFilename[i] ) )
       
    return sFolder, aField, aFile

def parse_xml_file_lnd(sFilename_xml_in):
    """
    Parse an XML file

    Args:
        sFilename_xml_in (string): The XML filename

    Returns:
        dict: The content in the XML file
    """

    if os.path.exists(sFilename_xml_in):
        pass
    else:
        print('The xml file does not exist!')
        return
    tree = ET.parse(sFilename_xml_in)
    root = tree.getroot()

    entry = root.findall('./domainInfo/filePath')
    sFolder_domain = (entry[0].text).strip()
    entry = root.findall('./domainInfo/variableNames')
    dummy = (entry[0].text).strip()
    aField0 = dummy.split('\n')  #(dummy.split(" "))
    aField_domain = list()
    for sField in aField0:
        d = sField.strip()
        e = d.split()
        aField_domain.append(e[0])
        pass

    entry = root.findall('./domainInfo/fileNames')
    dummy = (entry[0].text).strip()
    sFilename_domain = dummy.split('\n')
    sFilename_domain = os.path.join( sFolder_domain ,sFilename_domain[0] )
   

    entry = root.findall('./fieldInfo/filePath')
    sFolder = (entry[0].text).strip()

    entry = root.findall('./fieldInfo/variableNames')
    dummy = (entry[0].text).strip()
    aField0 = dummy.split('\n')  #(dummy.split(" "))
    aField = list()
    for sField in aField0:
        d = sField.strip()
        e = d.split()
        aField.append(e[0])

    entry = root.findall('./fieldInfo/fileNames')
    dummy = (entry[0].text).strip()
    aFilename = dummy.split('\n')

    nf = len(aFilename)
    aFile=list()
    for i in range(nf):
        aFile.append( os.path.join( sFolder ,aFilename[i] ) )
       
    return sFilename_domain,aField_domain, sFolder, aField, aFile