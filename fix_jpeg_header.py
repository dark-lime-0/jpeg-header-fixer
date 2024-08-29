jpeg_header = b'\xFF\xD8\xFF\xE0'  # JPEG header (SOI marker + JFIF APP0 marker)
jpeg_identifier = b'\x00\x10JFIF\x00\x01\x02\x00\x00\x01\x00\x01\x00\x00'

# Open the file in binary mode and replace the header
with open('your_image_file.jpg', 'r+b') as f:
    # Read the current header
    current_header = f.read(len(jpeg_header))
    
    # Move to the beginning of the file
    f.seek(0)
    
    # Replace with the correct JPEG header
    f.write(jpeg_header + jpeg_identifier)
