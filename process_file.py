def identify_object_type(obj):
    if obj.isdigit():
        return "Integer"
    try:
        float_obj = float(obj)
        return "Real Number" if '.' in obj else "Integer"
    except ValueError:
        pass
    
    if any(char.isalnum() for char in obj):
        return "Alphanumeric"
    
    return "String"

def process_file(input_filename, output_filename):
    with open(input_filename, 'r') as file:
        content = file.read().strip()
        objects = content.split(',')
        
        with open(output_filename, 'w') as output_file:
            for obj in objects:
                stripped_obj = obj.strip()
                output_file.write(f"Object: {stripped_obj}, Type: {identify_object_type(stripped_obj)}\n")

# Process the input file and write the output to a file
process_file("random_objects.txt", "output.txt")
