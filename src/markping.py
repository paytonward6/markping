import sys
from tqdm import tqdm
import os
import traceback
import subprocess

class markping:
    def __init__(self, ping_count, ping_wait_duration):
        markping.ping_count = ping_count
        markping.ping_wait_duration = ping_wait_duration
     
    def initial_prompt(markdown_file):
        if os.path.exists(markdown_file):
            while True:
                user_input = str(input(f"Would you like to replace file {markdown_file} (y/n/q)? "))
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
            print("\nFile: " + markdown_file + " will be created since it does not exist.")

    def ping_list(ping_path, markdown_file):
        ## Open File that contains IPs, DNS Servers, and Domain Names
        with open(ping_path, "r") as ping_file:

            to_ping = []
            for line in ping_file:
                line = line[:-1] # removes newline character from ping list
                to_ping.append(line)
            with open(markdown_file, "w") as ping_record:
                ping_record.write("# Ping results from: "+ ping_file.name + "\n") # creates the title of the .md file

                print("\nPinging " + str(len(to_ping)) + " items in " + ping_file.name)
                
                for i in tqdm(range(len(to_ping))):
                        ping_record.write("\n## " + to_ping[i] + "\n") # heading for a specific ping
                        result = subprocess.run(["ping",  "-c", str(markping.ping_count), "-i", str(markping.ping_wait_duration), to_ping[i]],
                                                      capture_output=True)
                        stdout = result.stdout.decode('UTF-8')
                        stdout = stdout.split("\n")
                        stderr = result.stderr.decode('UTF-8')
                        
                        if "Unknown host" in stderr:
                            ping_record.write(stderr)
                        else:
                            for output in stdout:
                                ping_record.write(output)
                                ping_record.write("\n")



    def run(self):
        md = ""
        ping_filepath  = ""

        if len(sys.argv) < 2:
            print("Usage: python3 main.py <input> <output>")
        else:
            ping_filepath = sys.argv[1]
            md = sys.argv[2]
    
        markping.initial_prompt(md)
        markping.ping_list(ping_filepath, md)




        ##########################################
        altered_md_lines = []
        try:
            markdown_file = open(md, "r")
            md_lines = markdown_file.readlines()

            ## Creates a .md list out of the ping results ##
            for line in md_lines:
                if line[0] == "#" or line[0] == "P":
                    altered_md_lines.append(line)
                elif line == '\n' or "statistics" in line:
                    continue
                elif line[0] == str(markping.ping_count) or line[0] == 'r':
                    line = "\t- " + line # additional list indentation for Roung Trip results
                    altered_md_lines.append(line)
                elif "icmp_seq" or "Unknown host" in line:
                    altered_md_lines.append("- " + line)
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


if __name__ == "__main__":
    count = 4
    wait = 0.1
    test = markping(count, wait)
    test.run() 
