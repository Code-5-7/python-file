def file_processor():
    """Read a file, modify its content, and write to a new file with error handling."""
    
    print("📝 File Processor - Read, Modify, and Write Files 📝")
    
    # Get input filename with error handling
    while True:
        input_filename = input("\nEnter the name of the file to read: ")
        try:
            # Try to open the file for reading
            with open(input_filename, 'r') as file:
                content = file.read()
            break  # Exit loop if file was successfully read
        except FileNotFoundError:
            print(f"❌ Error: The file '{input_filename}' does not exist. Please try again.")
        except PermissionError:
            print(f"❌ Error: Permission denied when trying to read '{input_filename}'. Please try another file.")
        except IOError as e:
            print(f"❌ Error: Unable to read file '{input_filename}': {str(e)}. Please try again.")
    
    # Modify the content (example: convert to uppercase and add line numbers)
    modified_content = []
    lines = content.split('\n')
    for i, line in enumerate(lines, 1):
        modified_line = f"{i}. {line.upper()}"
        modified_content.append(modified_line)
    modified_content = '\n'.join(modified_content)
    
    # Get output filename with validation
    while True:
        output_filename = input("\nEnter the name of the output file: ")
        if output_filename.strip() == "":
            print("❌ Error: Output filename cannot be empty. Please try again.")
            continue
        
        if output_filename == input_filename:
            print("❌ Warning: Output file would overwrite input file. Please choose a different name.")
            continue
        
        try:
            # Try to open the file for writing to check permissions
            with open(output_filename, 'x') as file:
                pass  # Just testing if we can create the file
            break  # Exit loop if file can be created
        except FileExistsError:
            overwrite = input(f"⚠️ Warning: '{output_filename}' already exists. Overwrite? (y/n): ").lower()
            if overwrite == 'y':
                break
        except PermissionError:
            print(f"❌ Error: Permission denied when trying to write to '{output_filename}'. Please try another filename.")
        except IOError as e:
            print(f"❌ Error: Unable to write to file '{output_filename}': {str(e)}. Please try again.")
    
    # Write the modified content to the new file
    try:
        with open(output_filename, 'w') as file:
            file.write(modified_content)
        print(f"\n✅ Success! Modified content written to '{output_filename}'")
    except Exception as e:
        print(f"\n❌ Unexpected error while writing to file: {str(e)}")
    finally:
        print("\nOperation completed. Thank you for using the File Processor!")

if __name__ == "__main__":
    file_processor()
