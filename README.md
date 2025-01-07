# uuid-replacer
A Python script that identifies and replaces UUIDs in text files with newly generated UUIDs. This tool is useful for scenarios where UUIDs need to be anonymized, updated, or randomized in datasets or configuration files. It supports command-line usage with customizable input and output file paths for flexible processing.

# Story
While working on a job that involved creating workflows based on designs, one of the most repetitive and time-consuming tasks was duplicating similar cases and reliably replacing UUIDs in the process. This often meant manually ensuring every UUID was unique and valid, which was both tedious and error-prone.

Initially, tools like ChatGPT were explored for automation, but they frequently generated invalid UUIDs or failed to handle duplicated UUIDs correctly, leaving gaps in the workflow. To solve this, I wrote this script, which automates the replacement of UUIDs in text files. It guarantees that each UUID is valid and unique, making it a reliable tool for repetitive tasks involving UUID management.

This script significantly reduced my workload and might help others facing similar challenges in their projects. Whether you're working on workflows, data anonymization, or updating configuration files, this tool ensures accuracy and saves time.
