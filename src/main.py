from pythonping import ping

##### REMOVE AFTER COMPLETION ####
import os
import traceback

md = "ping_record.md"

if os.path.exists(md):
    os.remove(md)
else:
    print("File does not exist")
#################################

## Open File that contains IPs, DNS Servers, and Domain Names
ping_file = open("./to_ping.txt", "r")

to_ping = []
for line in ping_file:
    line = line[:-1]
    to_ping.append(line)
print(to_ping)
try: 
    ping_record = open(md, "w")
    ping_record.write("# Ping results from: "+ ping_file.name + "\n")

    print("Pinging items in " + ping_file.name)

    for i in range(len(to_ping)):
        print("\n" + str(i + 1) + ": " + to_ping[i]) 

        ping_record.write("\n## " + to_ping[i] + "\n")
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
    for line in  md_lines:
        if line[0] == "R":
            if "min/avg/max" in line:
                line = "\t- " + line
            else:
                line = "- " + line
            altered_md_lines.append(line)
        else:
            altered_md_lines.append(line)
    print(altered_md_lines)
except:
    traceback.print_exc()
finally:
    markdown_file.flush()
    markdown_file.close()

try:
    final_md_file = open(md, "w")
    for line in altered_md_lines:
        final_md_file.write(line)
except:
    traceback.print_exc()
finally:
    final_md_file.flush()
    final_md_file.close()
