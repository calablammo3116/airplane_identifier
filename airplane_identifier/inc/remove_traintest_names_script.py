import os
import re

def rename_files(root_directory):
    # Regular expression patterns to match 'train_{number}' or 'test_{number}'
    train_pattern = re.compile(r'(.*)_train_(\d+)(.*)')
    test_pattern = re.compile(r'(.*)_test_(\d+)(.*)')
    
    for subdir, _, files in os.walk(root_directory):
        for file in files:
            old_file_path = os.path.join(subdir, file)
            
            # Check if file name matches the train or test pattern
            train_match = train_pattern.match(file)
            test_match = test_pattern.match(file)

            # Help with numbers for file renaming
            initial_offset = 7
            
            if train_match:
                new_file_name_attempt_p1 = f"{train_match.group(1)}_{train_match.group(2)}{train_match.group(3)}"
                new_file_path = os.path.join(subdir, new_file_name_attempt_p1)
                new_file_name = f"{train_match.group(1)}_{str(int(train_match.group(2)) + initial_offset) if os.path.exists(new_file_path) else train_match.group(2)}{train_match.group(3)}"
                new_file_path = os.path.join(subdir, new_file_name)
                while os.path.exists(new_file_path):
                    initial_offset += 1
                    new_file_name = f"{train_match.group(1)}_{str(int(train_match.group(2)) + initial_offset)}{train_match.group(3)}"
                    new_file_path = os.path.join(subdir, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")
                
            elif test_match:
                new_file_name_attempt_p1 = f"{test_match.group(1)}_{test_match.group(2)}{test_match.group(3)}"
                new_file_path = os.path.join(subdir, new_file_name_attempt_p1)
                new_file_name = f"{test_match.group(1)}_{str(int(test_match.group(2)) + initial_offset) if os.path.exists(new_file_path) else test_match.group(2)}{test_match.group(3)}"
                new_file_path = os.path.join(subdir, new_file_name)
                while os.path.exists(new_file_path):
                    initial_offset += 1
                    new_file_name = f"{test_match.group(1)}_{str(int(test_match.group(2)) + initial_offset)}{test_match.group(3)}"
                    new_file_path = os.path.join(subdir, new_file_name)
                os.rename(old_file_path, new_file_path)
                print(f"Renamed: {old_file_path} -> {new_file_path}")

if __name__ == "__main__":
    # Specify the root directory
    root_directory = os.getcwd()  # Or specify a different directory
    rename_files(root_directory)
