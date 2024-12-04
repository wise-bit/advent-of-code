def find_differences(file1_path, file2_path):
  with open(file1_path, 'r') as file1, open(file2_path, 'r') as file2:
    file1_lines = set(file1.readlines())
    file2_lines = set(file2.readlines())

  unique_to_file1 = file1_lines - file2_lines

  for line in unique_to_file1:
    print(line.strip())


# Example usage
file1 = 'test_output_1.txt'
file2 = 'test_output_2.txt'
find_differences(file1, file2)
