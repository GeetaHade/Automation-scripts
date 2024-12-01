# **Automation Scripts Repository** 🤖

Welcome to the **Automation Scripts Repository**! 🚀 This repository contains a collection of **Python-based automation scripts** designed for **directory management**, **process monitoring**, and **system task automation**. These scripts are crafted to help you improve productivity by automating repetitive tasks such as:

- Detecting and removing **duplicate files**
- Logging **process information**
- Handling various **file system operations**

---

## **Overview** 📝

This repository includes several powerful automation scripts that simplify the management of directories, the removal of duplicate files, and the monitoring of system processes. Each script is designed to be **modular** with a clear separation of concerns, allowing you to easily integrate or modify them based on your needs. The tasks range from simple directory management tasks (like checking file checksums) to more complex process monitoring and automation operations.

---

## **Directory Contents** 📂

The repository includes the following Python scripts, each serving a unique purpose:

- **`DirectoryChecksum.py`**: Calculates and displays the checksum (hash) of all files in a given directory.
- **`DirectoryDuplicate.py`**: Identifies duplicate files in a directory based on checksums and logs them.
- **`DirectoryDuplicateRemoval.py`**: Deletes duplicate files from a directory and logs the names of deleted files.
- **`ProcInfo.py`**: Displays information about currently running processes, including process name, PID, and username.
- **`ProcInfoLog.py`**: Logs details of running processes (name, PID, username) into a specified log file.
- **`DuplicateFileRemoval.py`**: Removes duplicate files from a specified directory, logs the operation, and sends the log file via email.

---

## **List of Tasks Performed** 🛠️

Below is a breakdown of the tasks performed by each of the scripts:

### 1. **`DirectoryChecksum.py`** 💻
- **Purpose**: Accepts a directory name as input and calculates the checksum (hash) of all files in that directory.
- **Use Case**: Helps verify file integrity and detect duplicate files.

### 2. **`DirectoryDuplicate.py`** 📑
- **Purpose**: Accepts a directory name as input and searches for duplicate files based on their checksums.
- **Output**: Logs the names of duplicate files into a file called `Log.txt`.

### 3. **`DirectoryDuplicateRemoval.py`** 🗑️
- **Purpose**: Identifies duplicate files in a directory and deletes them.
- **Output**: Logs the names of deleted duplicate files in a `Log.txt` file.

### 4. **`ProcInfo.py`** 🔍
- **Purpose**: Displays details of all currently running processes.
- **Output**: Shows the **process name**, **PID**, and **username** for each running process.

### 5. **`ProcInfoLog.py`** 📝
- **Purpose**: Accepts a directory name as input and logs the details of running processes into a log file in that directory.
- **Output**: A log file that records the **name**, **PID**, and **username** for each running process.

### 6. **`DuplicateFileRemoval.py`** ✂️
- **Purpose**: Accepts a directory name, time interval (in minutes), and email address as inputs.
- **Functionality**:
  - Periodically removes duplicate files from the specified directory.
  - Logs the details of the operation.
  - Sends an email with the log file as an attachment, including operation statistics.

---

## **Usage Instructions** 📖

### **Setup** 🛠️

1. **Install Dependencies**:
   To run the scripts, make sure you have Python 3.x installed, and then install the required libraries:
   ```bash
   pip install psutil schedule
