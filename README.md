# cs_prediction
Scripts to perform predictions with several empirical and qm-based chemical shift predictors.
Run the .sh files to get instructions

# Notes
As far as I can tell, there's a bug in the shAIC program, where HA2 is used instead of HA3 in some parts of the program.
I don't know if the error will be lesser or greater if it's corrected.
To fix it, change 2HA to 1HA in lines 20850, 20915, 20968 and 21180 in the shAIC program.
