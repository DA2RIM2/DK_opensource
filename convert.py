#!/usr/bin/env python3
"""
Convert a binary P6 PPM file to an ASCII P3 PPM file.
Usage:
    python3 ppm_converter.py input.ppm output.ppm
"""
import sys

def convert_p6_to_p3(input_path, output_path):
    with open(input_path, 'rb') as fin:
        # Read magic number
        magic = fin.readline().strip()
        if magic != b'P6':
            print(f"Error: Expected P6 format, found {magic.decode()}")
            return

        # Helper to read next non-comment line
        def read_non_comment():
            line = fin.readline()
            while line.startswith(b'#'):
                line = fin.readline()
            return line

        # Read width and height
        dims = read_non_comment().strip().split()
        width, height = map(int, dims)

        # Read max color value
        maxval = int(read_non_comment().strip())

        # Read pixel data
        pixel_data = fin.read()

    # Write P3 ASCII PPM
    with open(output_path, 'w') as fout:
        fout.write('P3\n')
        fout.write(f"{width} {height}\n")
        fout.write(f"{maxval}\n")

        # Write pixels, 3 values per pixel, newline every row
        for i in range(0, len(pixel_data), 3):
            r = pixel_data[i]
            g = pixel_data[i+1]
            b = pixel_data[i+2]
            fout.write(f"{r} {g} {b} ")
            # Newline at end of each row
            if ((i // 3 + 1) % width) == 0:
                fout.write('\n')


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python3 ppm_converter.py input.ppm output.ppm")
        sys.exit(1)

    inp, outp = sys.argv[1], sys.argv[2]
    convert_p6_to_p3(inp, outp)
