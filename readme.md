## Web scraping of OSIRIS NAC images
### Author: Sergey Krasilnikov

Planetary Remote Sensing Laboratory / The Hong Kong Polytechnic University

---
### Overview
This program download data from the [Rosetta mission website](https://www.cosmos.esa.int/web/psa/rosetta "Rosetta"), in
particularly OSIRIS narrow-angle camera (OSINAC) - high-resolution images of the comet's nucleus and Rosetta's flyby 
targets.

---
### Running
The data is located at the: 
[.../INTERNATIONAL-ROSETTA-MISSION/OSINAC/](https://archives.esac.esa.int/psa/ftp/INTERNATIONAL-ROSETTA-MISSION/OSINAC/ "OSINAC data") 

, where subfolders (like *"RO-C-OSINAC-4-PRL-67PCHURYUMOV-M05-V1.0"*) is the stages of the mission. The initial data 
could be found in the subfolder *"BROWSE"*.

To reach the files that you need, set the ***url*** address in the ***main.py*** file.

