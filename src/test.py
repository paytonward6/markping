import subprocess

#ping_results = subprocess.run(["ping",  "-c", "4", "google.com"])

#print(f"The exit code was: {ping_results.returncode}")
messages = b'PING wayfair.com (151.101.193.252): 56 data bytes\n64 bytes from 151.101.193.252: icmp_seq=0 ttl=59 time=12.278 ms\n64 bytes from 151.101.193.252: icmp_seq=1 ttl=59 time=19.571 ms\n64 bytes from 151.101.193.252: icmp_seq=2 ttl=59 time=19.598 ms\n64 bytes from 151.101.193.252: icmp_seq=3 ttl=59 time=19.791 ms\n\n--- wayfair.com ping statistics ---\n4 packets transmitted, 4 packets received, 0.0% packet loss\nround-trip min/avg/max/stddev = 12.278/17.809/19.791/3.195 ms\n'

messages = messages.decode('UTF-8')

messages = messages.split("\n")
for message in messages:
    print(message)
