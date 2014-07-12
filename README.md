#BigVASP

In material science, the Vienna ab-initio Simulations Package (VASP) has emerged as the dominant industry standard tool for performing materials simulations from first principles.  As a whole, the material science community has generated tens of thousands of VASP datasets - but in the absence of a useful cataloging and distribution system, this massive resource remains fragmented and inaccessible.

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
