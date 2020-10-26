# File Monitoring System for Unix Based Systems

This system simply monitors the files or directories from the base directories
you set and then records all the operations like file creation, deletion and modification and 
access those action to know which files or directories are compromised.
We also provide the Basic Flags which you can set upon file creation which will 
add a new configuration when accessing the validity of actions on the concerned file.

LIst of those flags are:

`[read_only, fullScan, nonScan, system_file, executable, hidden_files]`

Systems main menu looks like this:
```
Basic Tripwire model:
    1. Update model working path (current : ~)
    2. Start service
    3. Generate Report
    4. Exit
Select option (1/2/3/4) :
```
Options are very obvious to use.

## Signatures used 
We have used **alder32** and **crc32** concatinated to get the final checksum or signature
for a file. We chose these two because we want he signature 
function to be light weight and also strong enough
for our need. The hash function formed is now a 64 bit hash probability of getting 
collision for having 10000 hashes in the database the chances of 
collision is 2.710234×10<sup>-12</sup>. ([source](http://davidjohnstone.net/pages/hash-collision-probability))

## Report Generation 
The report we generate is appended to the `report.txt` present at the 
root of the project and format for a typical report looks like:

```
----------------------------------------
Report generated on Mon Oct 26 17:30:22 2020

	 Action Type : MODIFIED
	 Time : Mon Oct 26 13:47:32 2020
	 Concerned File : /home/ace201m/Study/ASE/semesterLong/project/demo_dir/file.txt1
	 User Responsible : ace201m

	 Action Type : MODIFIED
	 Time : Mon Oct 26 13:47:32 2020
	 Concerned File : /home/ace201m/Study/ASE/semesterLong/project/demo_dir/file.txt1
	 User Responsible : ace201m

----------------------------------------

```
