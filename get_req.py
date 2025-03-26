def clean_dependencies(file_path, output_path):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    # Clean lines by stripping leading spaces and dash
    cleaned_lines = [line.lstrip("- ").strip() for line in lines]

    # Write the cleaned lines to a new file
    with open(output_path, 'w') as f:
        f.write('\n'.join(cleaned_lines))

    print("Dependencies cleaned and saved to", output_path)

# Usage: Provide input and output file paths
input_file = "D:\drug_modelling\prelim_req.txt"  # Replace with your input file path
output_file = "D:\drug_modelling\\req.txt"   # Replace with your output file path

clean_dependencies(input_file, output_file)
