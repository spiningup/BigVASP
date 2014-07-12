#BigVASP

##Science Motivation
In material science, the Vienna ab-initio Simulations Package (VASP) has emerged as the dominant standard tool for performing materials simulations from first principles.  As a whole, the material science community has generated tens of thousands of VASP datasets - but in the absence of a useful cataloging and distribution system, this massive resource remains fragmented and inaccessible.

Due to VASP's popularity, a unifying platform for registering and distributing VASP simulation results has the potential to dramatically promote collaboration and cross-pollination in material science.  Researchers at the Colorado School of Mines have decided to take advantage of this opportunity to promote open data, by seeking to develop and host just such a VASP platform, called BigVASP.

Researchers in this project would like developer guidance in beginning the infrastructure for this project by way of implementing a bare-bones Django web app capable of allowing a user to upload a collection of VASP output (plain text) files, register some metadata about those files in a database (probably SQL), as well as supporting searching and downloading VASP files from the same.

##Mozilla Science Sprint
We're hoping to get a start on BigVASP at the upcoming [Mozilla Science Sprint](http://mozillascience.org/prepping-for-our-first-global-sprint-july-10-11-et/) - we've got a few foundational goals to shoot for there:

####Basic Goals
 - *Set up a Django app*: The materials science community would like to work in Python, and Django is an excellent choice for a project like this.  To start, all we need is a bare-bones interface in the frontend that allows a user to upload a set of files to the server, and just enough backend to park those files somewhere reasonable.
 - *Update an SQL database*: Every batch of files uploaded will contain one particular metadata file, named `vasprun.xml`; some of the metadata in this xml file needs to be scraped out and put in an SQL database - details in the 'Search Database' section below.
 - *Search & Download*: Finally, we need enough functionality to query the metadata database and offer matching sets of files for download.

####Stretch Goals
Done already?  Throw these in too:
 - *User Auth*: we'll need off-the-shelf user auth for handling logins before people can upload to the BigVASP server.
 - *Data QC*: need to check received files for data quality.
 
###Search Database
The basic vision for the searchable database is as a MySQL database with one or two simple tables, as described below; other suggestions for database technology and structure are welcome, please open an issue!

Each dataset comes with an xml metadata file called `vasprun.xml`; the following are the fields that should be registered to an SQL table as an item corresponding to this dataset, with name, type and value preserved:

```
<i type="int" name="ISPIN"> 1</i>

 <i type="int" name="IBRION"> -1</i>

 <i name="EDIFF"> 0.00000100</i>

 <i name="EDIFFG"> -0.05000000</i>

 <i type="int" name="ISIF"> 2</i>

 <i type="int" name="ISYM"> 0</i>

 <i name="ENCUT"> 340.00000000</i>

 <i type="int" name="ISMEAR"> 0</i>

 <i name="SIGMA"> 0.01000000</i>

 <i type="logical" name="LOPTICS"> F </i>

 <i type="logical" name="LPEAD"> F </i>

 <i type="logical" name="LMETAGGA"> F </i>

 <i type="logical" name="LDAU"> T </i>

 <v type="int" name="LDAUTYPE"> 2</v>

 <v type="int" name="LDAUL"> -1 -1 2</v>

 <v name="LDAUU"> 0.00000000 0.00000000 5.00000000</v>

 <v name="LDAUJ"> 0.00000000 0.00000000 0.00000000</v>

 <i type="int" name="IALGO"> 68</i>

 <i type="int" name="NBANDS"> 96</i>

 <i name="NELECT"> 158.00000000</i>

 <i type="int" name="ISMEAR"> 0</i>

 <i name="SIGMA"> 0.01000000</i>

 <i type="logical" name="LNONCOLLINEAR"> F </i>

 <v name="MAGMOM"> 1.00000000 1.00000000 </v>

 <i name="NUPDOWN"> -1.00000000</i>

 <i type="logical" name="LSORBIT"> F </i>

 <i type="logical" name="LDIPOL"> F </i>

 <i type="logical" name="LMONO"> F </i>

 <i type="int" name="IDIPOL"> 0</i>

 <i name="EPSILON"> 1.00000000</i>

 <v name="DIPOL"> -100.00000000 -100.00000000 -100.00000000</v>

 <i name="EFIELD"> 0.00000000</i>

 <i name="PSTRESS"> 0.00000000</i>

EDIFFG

 <i type="int" name="NFREE"> 0</i>

 <i type="logical" name="LOPTICS"> F </i>

 <i type="logical" name="LBERRY"> F </i>

 <i type="int" name="ICORELEVEL"> 0</i>

 <i type="int" name="I_CONSTRAINED_M"> 0</i>

 <i type="string" name="GGA">--</i>

 <i type="int" name="VOSKOWN"> 0</i>

 <i type="logical" name="LHFCALC"> F </i>

 <i type="string" name="PRECFOCK"></i>

 <i name="AEXX"> 0.00000000</i>

 <i type="int" name="NKREDX"> 1</i>

 <i type="int" name="NKREDY"> 1</i>

 <i type="int" name="NKREDZ"> 1</i>

 <i type="logical" name="ODDONLY"> F </i>

 <i type="logical" name="EVENONLY"> F </i>

 <i name="HFSCREEN"> 0.00000000</i>

 <i type="logical" name="LEPSILON"> F </i>

 <i type="logical" name="LRPA"> F </i>

 <i name="CSHIFT"> 0.10000000</i>

 <i name="OMEGAMAX"> -1.00000000</i>

 <i name="ENCUTGW"> -2.00000000</i>

 <i type="int" name="NOMEGA"> 0</i>

 <i type="logical" name="LSPECTRAL"> F </i>

 <i type="logical" name="ODDONLYGW"> F </i>

 <i type="logical" name="EVENONLYGW"> F </i>

 <array name="atomtypes" >

 </array>

<structure name="initialpos" >

 <crystal>

 <varray name="basis" >

 <v> 8.46878006 -0.00000094 -0.00000190 </v>

 <v> -0.00000514 8.46877926 -0.00000098 </v>

 <v> -0.00000092 -0.00000023 5.37411607 </v>

 </varray>

 <i name="volume"> 385.43283447 </i>

<varray name="forces" >

 <varray name="stress" >

 <v> 1.79816953 0.00018066 0.00051208 </v>

 <v> 0.00025570 1.79794929 0.00026502 </v>

 <v> 0.00021029 0.00028367 1.22115689 </v>

 </varray>

 <separator name="dft+d2" >

 <i type="logical" name="LVDW"> F </i>

 </separator>

 <v name="MAGDIPOLOUT"> 0.00000000 0.00000000 

0.00000000</v>

 <i name="e_wo_entrp"> -70.72311261 </i>

 <i name="efermi"> 3.79419797 </i>
```

In addition to the fields pulled from `vasprun.xml`, 8 more should be available per dataset (values TBD):

 - name=”direct_bandgap”,	type=”float”
 - name=”indirect_bandgap”,	type=”float”
 - name=”energyperatom”,	type=”float”
 - name=”initial_spacegroup”,	type=”string”
 - name=”final_spacegroup”,	type=”string”
 - name=”formula”,	type=”string”
 - name=”contributor”,	type=”string”
 - name=”email”,	type=”string”

In addition to this searchable metadata, the database will also have to know where the corresponding files have been stored on disk.
