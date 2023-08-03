import argparse

def main():
    parser = argparse.ArgumentParser(description='A simple program with argparse.')
    
    # Adding a positional argument
    parser.add_argument('input_file', help='Path to the input file.')
    
    # Adding an optional argument (flag)
    parser.add_argument('--output', '-o', help='Path to the output file.')
    
    # Adding an optional argument with default value
    parser.add_argument('--count', '-c', type=int, default=1, help='Number of times to process the input.')
    
    # Parsing the arguments
    args = parser.parse_args()

    # Accessing the parsed arguments
    print(f"Input file: {args.input_file}")
    print(f"Output file: {args.output}")
    print(f"Count: {args.count}")

if __name__ == '__main__':
    main()
 