import time
import sys

informations = {
    "Name": "Sensei-CHO",
    "Age": "16",
    "Location": "N/A",
    "Working on": "https://github.com/Sensei-CHO/HomeCloud",
}

for x in informations:
    for y in range(len(informations[x]) + 1):
        time.sleep(0.1)
        sys.stdout.write("\r" + f"{x}: {informations[x][0:y]}")
        sys.stdout.flush()
    sys.stdout.write("\n")
    sys.stdout.flush()
