## Authentication Log Storage Estimator

# Assume there is a log file on your system that records all the user logins and logouts.

# You (playing the role of a network administrator) need to estimate how large the log file
# will grow as the number of users (and login/logouts) increase, to ensure that you do not
# run out of disk space. The script you will write to automate this estimation should perform
# the following steps:

# 1. Read (using the input() function) the number of log entries per second
# 2. Read (using the input() function) the average size of a log entry in bytes
# 3. Display:
# a) The storage required for 1 minutes worth of log entries, in KB
# b) The storage required for 1 hours worth of log entries, in MB
# c) The storage required for 1 days worth of log entries, in GB

# To finish the assignment, complete the following tasks:

# - Correct the error(s) in the provided code
# - Implement the remaining functionality

KB = 1024
MB = (KB * 1024)
GB = (MB * 1024)

num_entries = int(input("Please enter the number of entries per second: "))
entry_size = int(input("Please enter the average number of bytes per entry: "))

kb_size_per_sec = (num_entries * entry_size) / KB
mb_size_per_sec = (num_entries * entry_size) / MB
gb_size_per_sec = (num_entries * entry_size) / GB

print("Storage Estimates")
print(f"Per minute: {kb_size_per_sec * 60}KB")
print(f"Per hour: {mb_size_per_sec * 60 * 60}MB")
print(f"Per day: {gb_size_per_sec * 60 * 60 * 24}GB")