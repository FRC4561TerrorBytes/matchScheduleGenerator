# Match Schedule Generator 

This script takes in a teams.txt file that details all teams in a competition and creates a code block for use in the MiniFRC FMS

## teams.txt format

Format the file with the numbers of all teams, separated by commas
Example:
``1,2,3,4,5,6,7,99,9,10,11,12,13,14,15,16,17,18,19,20,21,22,67,24,25,26,27,28,29,30``

## Running and using the Script

Call the script from the folder it is in like this, specifying the number of matches for each team (rounds). This example generates a schedule of 8 matches per team.

``Python generateSchedule.py -r 8 ``

The output code block is found in the generateCode.txt file, formatted like so:

``    generateMatch(1, 0, Match.Type.QUALIFICATION, [20, 1, 99], [29, 27, 7], 1, 8);  
    generateMatch(2, 0, Match.Type.QUALIFICATION, [10, 15, 16], [19, 11, 4], 1, 8);  
    generateMatch(3, 0, Match.Type.QUALIFICATION, [24, 6, 26], [30, 2, 12], 1, 8);  
    generateMatch(4, 0, Match.Type.QUALIFICATION, [25, 21, 13], [5, 14, 22], 1, 8);  
    generateMatch(5, 0, Match.Type.QUALIFICATION, [3, 28, 18], [9, 67, 17], 1, 8);  
    generateMatch(6, 0, Match.Type.QUALIFICATION, [7, 19, 15], [20, 12, 26], 1, 8);  
    generateMatch(7, 0, Match.Type.QUALIFICATION, [27, 99, 21], [24, 14, 2], 1, 8);``