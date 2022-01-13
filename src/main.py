from pythonping import ping

##### REMOVE AFTER COMPLETION ####
##### USED FOR CODE WRITING AND DEBUGGING PURPOSES #####
import os
import traceback

md = "ping_results.md"

if os.path.exists(md):
    os.remove(md)
else:
    print("\nFile: " + md + " does not exist. No file deleted")
#################################

## Open File that contains IPs, DNS Servers, and Domain Names
ping_file = open("./to_ping.txt", "r")

to_ping = []
for line in ping_file:
    line = line[:-1] # removes newline character from ping list
    to_ping.append(line)
try: 
    ping_record = open(md, "w")
    ping_record.write("# Ping results from: "+ ping_file.name + "\n") # creates the title of the .md file

    print("\nPinging " + str(len(to_ping)) + " items in " + ping_file.name)

    for i in range(len(to_ping)):
        print("\n" + str(i + 1) + ": " + to_ping[i]) 

        ping_record.write("\n## " + to_ping[i] + "\n") # heading for a specific ping
        message = str(ping(to_ping[i], verbose=True))
        message = message.replace("\r", "")

        ping_record.write(message)
        ping_record.write("\n")

except: 
    print(f"File {ping_record_filename} already exists.")
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
    for line in  md_lines:
        if line[0] == "R":
            if "min/avg/max" in line:
                line = "\t- " + line # additional list indentation for Roung Trip results
            else:
                line = "- " + line
            altered_md_lines.append(line)
        else:
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
