from pythonping import ping

##### REMOVE AFTER COMPLETION ####
import os
import traceback

if os.path.exists("ping_record.md"):
    os.remove("ping_record.md")
else:
    print("File does not exist")
#################################

## Open File that contains IPs, DNS Servers, and Domain Names
ping_file = open("./to_ping.txt", "r")

to_ping = []
for line in ping_file:
    line = line[:-1]
    to_ping.append(line)

try: 
    ping_record_filename = "ping_record.md"
    ping_record = open(ping_record_filename, "w")
    ping_record.write("# Ping results from: "+ ping_file.name + "\n")

    print("Pinging items in " + ping_file.name)

    for i in range(len(to_ping)):
        print("\n" + str(i + 1) + ": " + to_ping[i]) 

        ping_record.write("\n## " + to_ping[i] + "\n")
        message = str(ping(to_ping[i], verbose=True))
        message = message.replace("\r", "")
        message.splitlines()
#        print(message)

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

