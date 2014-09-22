#from models import Document
import xml.etree.ElementTree as ET

int_names = ['ISPIN', 'IBRION', 'ISIF', 'ISYM', 'ISMEAR', 'LDAUTYPE', 'IALGO', 'NBANDS',
                 'ISMEAR', 'IDIPOL', 'NFREE', 'ICORELEVEL', 'I_CONSTRAINED_M', 'VOSKOWN', 'NKREDX', 
                 'NKREDY', 'NKREDZ', 'NOMEGA']
float_names = ['EDIFF', 'EDIFFG', 'ENCUT', 'SIGMA', 'NELECT', 'NUPDOWN', 'EPSILON', 'EFIELD', 'PSTRESS',
                   'AEXX', 'HFSCREEN', 'CSHIFT', 'OMEGAMAX', 'ENCUTGW', 'volume', 'e_wo_entrp', 'efermi']
string_names = ['GGA', 'PRECFOCK']
logical_names = ['LOPTICS', 'LPEAD', 'LMETAGGA', 'LDAU', 'LNONCOLLINEAR', 'LSORBIT', 'LDIPOL', 
                     'LMONO', 'LBERRY', 'LHFCALC', 'ODDONLY', 'EVENONLY', 'LEPSILON', 'LRPA', 'LSPECTRAL', 
                     'ODDONLYGW', 'EVENONLYGW', 'LVDW']
array_names = ['LDAUL', 'LDAUU', 'LDAUJ', 'MAGMOM', 'DIPOL', 'atomtypes', 'MAGDIPOLOUT']
varray_names = ['basis', 'stress']

