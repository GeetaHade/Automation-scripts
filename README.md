# **Automation Scripts Repository**

This repository contains a collection of Python-based automation scripts designed for directory management, process monitoring, and system task automation. The scripts focus on improving productivity by automating repetitive tasks such as detecting and removing duplicate files, logging process information, and handling file system operations.


## **Overview**

This repository includes several automation scripts that help manage directories, identify and remove duplicate files, monitor system processes, and send log files via email. Each script performs a specific task, and they are designed to be modular, with clear separation of concerns. The tasks range from basic directory management (such as checking checksums) to more complex process monitoring and automation tasks.

---

## **Directory Contents**

The repository contains the following Python scripts:

- `DirectoryChecksum.py`: Calculates and displays checksums of all files in a given directory.
- `DirectoryDuplicate.py`: Identifies duplicate files in a directory based on their checksums and logs them.
- `DirectoryDuplicateRemoval.py`: Deletes duplicate files from a directory and logs the deleted file names.
- `ProcInfo.py`: Displays information of running processes including process name, PID, and username.
- `ProcInfoLog.py`: Logs running processes into a file in the specified directory.
- `DuplicateFileRemoval.py`: Removes duplicate files from a specified directory, logs the operation, and sends an email with the log.

---

## **List of Tasks Performed**

Here’s a list of tasks performed by each of the scripts:

### 1. **DirectoryChecksum.py**
- Accepts a directory name as input.
- Displays the checksum (hash) of all files in the directory, helping in verifying file integrity or detecting duplicates.

### 2. **DirectoryDuplicate.py**
- Accepts a directory name as input.
- Searches for duplicate files based on checksum comparison.
- Logs the names of duplicate files in a `Log.txt` file.

### 3. **DirectoryDuplicateRemoval.py**
- Accepts a directory name as input.
- Identifies duplicate files based on checksums.
- Deletes duplicate files and logs the names of deleted files in a `Log.txt` file.

### 4. **ProcInfo.py**
- Displays details of currently running processes.
- Shows process name, PID, and username for each running process.

### 5. **ProcInfoLog.py**
- Accepts a directory name as input.
- Logs details of currently running processes (name, PID, username) into a log file located in the specified directory.

### 6. **DuplicateFileRemoval.py**
- Accepts a directory name, time interval (in minutes), and email address as inputs.
- Periodically removes duplicate files from the specified directory.
- Logs the removal process and sends the log file via email with statistics on the operation.

---

