import os
import subprocess

# Path where the malware samples are located
malware_path = "/home/abc/Documents/satvikdataset/malwares"

# Check if Cuckoo is running
try:
    subprocess.check_call(["pgrep", "-f", "cuckoo"])
except subprocess.CalledProcessError:
    print("Cuckoo is not running. Please start Cuckoo before running this script.")
    exit()

# List all files in the directory
malware_files = os.listdir(malware_path)

# Counter for submitted files
submitted_files = 0

# Loop through each file and submit it to Cuckoo for analysis
for malware in malware_files:
    # Construct the full path of the file
    file_path = os.path.join(malware_path, malware)
    
    # Check if the file exists and is a file
    if os.path.isfile(file_path):
        try:
            # Submit the file to Cuckoo for analysis
            subprocess.check_call(["cuckoo", "submit", file_path])
            submitted_files += 1
        except subprocess.CalledProcessError as e:
            print(f"An error occurred while submitting {file_path} to Cuckoo: {str(e)}")
    else:
        print(f"{file_path} is not a valid file.")

print(f"Submitted {submitted_files} out of {len(malware_files)} files to Cuckoo.")
