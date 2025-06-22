import sys
import subprocess
import argparse


def parseTeamsList():
    # opening the file
    file_obj = open("teams.txt", "r")

    # reading the data from the file
    file_data = file_obj.read()
    file_obj.close()
    # splitting the file data into lines
    return file_data.split(',')
    
def generateSchedule(numTeams, numRounds):
    # Generate a schedule for a set number of teams and rounds
    if sys.platform == 'win32':
        with open("matches.txt", "w") as outfile:
            subprocess.run(["./matchMakerFiles/MatchMaker.exe", "-t", str(numTeams), "-r", str(numRounds)], stdout=outfile)

    elif sys.platform =='darwin':
        return 0
    elif sys.platform == 'linux':
        return 0

def extractSchedule(file_path):
    schedule = []
    capture = False

    with open(file_path, 'r') as f:
        for line in f:
            line = line.strip()

            # Start capturing after we see the header line
            if line.startswith("Match Schedule"):
                capture = True
                continue
            elif line.startswith("Schedule Statistics"):
                break  # Stop capturing at this section

            if capture:
                # Match lines like '  1:   17    30    28    22    12    21'
                if line and line[0].isdigit():
                    parts = line.split(":")
                    if len(parts) == 2:
                        match_num = int(parts[0].strip())
                        teams = list(map(int, parts[1].strip().split()))
                        schedule.append([match_num] + teams)
    # Returns a list of list, first char is match number, then red teams and then blue teams
    return schedule

def replaceTeams(matchSchedule, teamsList):

    for match in matchSchedule:
        match[1] = teamsList[match[1] -1]
        match[2] = teamsList[match[2] -1]
        match[3] = teamsList[match[3] -1]
        match[4] = teamsList[match[4] -1]
        match[5] = teamsList[match[5] -1]
        match[6] = teamsList[match[6] -1]

    return matchSchedule

def createCodeBlock(matchSchedule):

    outputStr = ""
    for match in matchSchedule:
        outputStr += "generateMatch(" + str(match[0]) + ", " + str(0) + ", " + "Match.Type.QUALIFICATION" + ", [" + str(match[1]) + ", " + str(match[2]) + ", " + str(match[3]) + "]" + ", [" + str(match[4]) + ", " + str(match[5]) + ", " + str(match[6]) + "]," " 1, 8);\n"

    return outputStr

def createShareableSchedule(matchSchedule):
    headers = ["Match #", "Red 1", "Red 2", "Red 3", "Blue 1", "Blue 2", "Blue 3"]
    markdown = "| " + " | ".join(headers) + " |\n"
    markdown += "| " + " | ".join(["---"] * len(headers)) + " |\n"

    # Add the rows
    for row in matchSchedule:
        markdown += "| " + " | ".join(map(str, row)) + " |\n"

    with open("matchSchedule.md", "w") as f:
        f.write(markdown)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='Match Schedule Generator')
    
    parser.add_argument('-r', '--numRounds', help="Number of rounds, matches for each team")
    args = parser.parse_args()

    teamsList = parseTeamsList()
    numTeams = len(teamsList)


    if numTeams > len(set(teamsList)):
        print("teamsList.txt file has team numbers duplicated")
        exit()
    else:
        print("Generating schedule for "+ str(numTeams) + " teams, "+ str(args.numRounds)+ " rounds")
        generateSchedule(numTeams, args.numRounds)
        prelimSchedule = extractSchedule("matches.txt")
        fullSchedule = replaceTeams(prelimSchedule, teamsList)
        createShareableSchedule(fullSchedule)
        codeBlock = createCodeBlock(fullSchedule)
        print(codeBlock)
        with open("generateCode.txt", "w") as text_file:
            text_file.write(codeBlock)
