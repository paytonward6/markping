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

    def ping_command(to_ping):
        return subprocess.run(["ping",  "-c", str(markping.ping_count), "-i", str(markping.ping_wait_duration), to_ping],
                                                  capture_output=True)
    def write_ping_result(ping_result, ping_record_file):
            stdout = ping_result.stdout.decode('UTF-8')
            stdout = stdout.split("\n")
            stderr = ping_result.stderr.decode('UTF-8')
            
            if "Unknown host" in stderr:
                ping_record_file.write(stderr)
            else:
                for output in stdout:
                    ping_record_file.write(output)
                    ping_record_file.write("\n")

    def write_results(ping_file, markdown_file, ping_list):
        with open(markdown_file, "w") as ping_record:
            ping_record.write("# Ping results from: "+ ping_file.name + "\n") # creates the title of the .md file

            print("\nPinging " + str(len(ping_list)) + " items in " + ping_file.name)
            
            for i in tqdm(range(len(ping_list))):
                    ping_record.write("\n## " + ping_list[i] + "\n") # heading for a specific ping
                    result = markping.ping_command(ping_list[i])
                    markping.write_ping_result(result, ping_record)

    def ping_list(ping_path, markdown_file):
        ## Open File that contains IPs, DNS Servers, and Domain Names
        with open(ping_path, "r") as ping_file:

            to_ping = []
            for line in ping_file:
                line = line[:-1] # removes newline character from ping list
                to_ping.append(line)
            markping.write_results(ping_file, markdown_file, to_ping)

    def results_to_markdown(markdown_lines, line):
            if line[0] == "#" or line[0] == "P":
                markdown_lines.append(line)
            elif line == '\n' or "statistics" in line:
                pass
            elif line[0] == str(markping.ping_count) or line[0] == 'r':
                line = "\t- " + line # additional list indentation for Roung Trip results
                markdown_lines.append(line)
            elif "icmp_seq" or "Unknown host" in line:
                markdown_lines.append("- " + line)

    def format_results(md):
        markdown_lines = []
        with open(md, "r") as markdown_file:
            raw_lines = markdown_file.readlines()
            ## Creates a .md list out of the ping results ##
            for line in raw_lines:
                markping.results_to_markdown(markdown_lines, line)  ## Applies final changs to the ping results ##
        with open(md, "w") as final_md_file:
            for line in markdown_lines:
                final_md_file.write(line)

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
        markping.format_results(md)

if __name__ == "__main__":
    count = 4
    wait = 0.1
    test = markping(count, wait)
    test.run() 
