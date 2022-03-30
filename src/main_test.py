#ping_results = subprocess.run(["ping",  "-c", "4", "google.com"])

import sys
from pythonping import ping
from tqdm import tqdm
import os
import traceback
import subprocess

md = ""
ping_filepath  = ""

if len(sys.argv) < 2:
    print("Usage: python3 main.py <input> <output>")
else:
    ping_filepath = sys.argv[1]
    md = sys.argv[2]

if os.path.exists(md):
    while True:
        user_input = str(input(f"Would you like to replace file {md} (y/n/q)? "))
        if user_input.__eq__('y'):
            break
        elif user_input.__eq__('n'):
            md = str(input(f"Provide name for ping results to be written to (foo.md): "))
            break
        elif user_input.__eq__('q'):
            sys.exit(0)
        else:
            print("Invalid input. Try again")
else:
    print("\nFile: " + md + " will be created since it does not exist.")

## Open File that contains IPs, DNS Servers, and Domain Names
ping_file = open(ping_filepath, "r")

to_ping = []
for line in ping_file:
    line = line[:-1] # removes newline character from ping list
    to_ping.append(line)
try: 
    ping_record = open(md, "w")
    ping_record.write("# Ping results from: "+ ping_file.name + "\n") # creates the title of the .md file

    print("\nPinging " + str(len(to_ping)) + " items in " + ping_file.name)
    
    c = 4
    wait = 0.2
    for i in tqdm(range(len(to_ping))):
        try:
            #print("\n" + str(i + 1) + ": " + to_ping[i]) 

            ping_record.write("\n## " + to_ping[i] + "\n") # heading for a specific ping
            messages = subprocess.run(["ping",  "-c", str(c), "-i", str(wait), to_ping[i]],
                                          stdout=subprocess.PIPE).stdout
            messages = messages.decode('UTF-8')

            messages = messages.split("\n")
            for message in messages:
                print(message)
                ping_record.write(message)
                ping_record.write("\n")
 
            #message = message.replace("\r", "")

        except:
            message = f"ping: cannot resolve {to_ping[i]}: Unknown host"
            message = message.replace("\r", "")

            ping_record.write(message)
            ping_record.write("\n")
            traceback.print_exc()

except: 
    traceback.print_exc()
finally:
    #Mandatory file stream operations
    ping_record.flush()
    ping_record.close()

    ping_file.close()

##########################################
altered_md_lines = []
try:
    markdown_file = open(md, "r")
    md_lines = markdown_file.readlines()

    ## Creates a .md list out of the ping results ##
    for line in md_lines:
        if line[0] == "#":
            altered_md_lines.append(line)
        else: 
            if line[0] == "P":
                altered_md_lines.append(line)
            elif "icmp_seq" in  line:
                altered_md_lines.append("- " + line)
            elif "min/avg/max" or "packets transmitted" in line:
                if line == '\n':
                    continue
                elif "statistics" in line:
                    continue
                else:
                    line = "\t- " + line # additional list indentation for Roung Trip results
                    altered_md_lines.append(line)
except:
    traceback.print_exc()
finally:
    markdown_file.flush()
    markdown_file.close()

## Applies final changs to the ping results ##
try:
    final_md_file = open(md, "w")
    for line in altered_md_lines:
        final_md_file.write(line)
except:
    traceback.print_exc()
finally:
    final_md_file.flush()
    final_md_file.close()
