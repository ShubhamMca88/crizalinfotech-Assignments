import subprocess

# Path to the trained Naive Bayes model
model_path = "trained_model.bin"

# Path to the test dataset
test_data_path = "test_data.txt"

# MeTA command to perform classification
meta_command = f"classify naive-bayes {model_path} {test_data_path}"

# Execute MeTA command and capture the output
output = subprocess.check_output(meta_command, shell=True).decode("utf-8")

# Parse output to get accuracy
accuracy_line = output.split("\n")[-2]  # Second last line contains accuracy
accuracy = float(accuracy_line.split()[-1])

# Print the accuracy
print("Classification Accuracy:", accuracy)
