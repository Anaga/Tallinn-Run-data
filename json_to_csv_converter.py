import json
import csv
import re
import argparse
import sys
import os

def convert_json_to_csv(json_file_path, csv_file_path):
    """
    Converts JSON file with race results to CSV format
    """
    try:
        # Check if input file exists
        if not os.path.exists(json_file_path):
            print(f"Error: File {json_file_path} not found")
            return False
        
        # Read JSON file
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract labels (column headers)
        labels = data.get('labels', [])
        headers = [label['label'] for label in labels]
        
        # Extract participant data
        participants = data.get('arr', [])
        
        if not participants:
            print("No participant data found in JSON file")
            return False
        
        # Create output directory if it doesn't exist
        output_dir = os.path.dirname(csv_file_path)
        if output_dir and not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Create CSV file
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write headers
            writer.writerow(headers)
            
            # Write data for each participant
            for participant in participants:
                row = []
                for label in labels:
                    key = label['key']
                    value = participant.get(key, '')
                    
                    # Handle team names with <br> tags - often duplicated content
                    if isinstance(value, str) and '<br>' in value:
                        # Split by <br> and clean up parts
                        parts = [part.strip() for part in value.split('<br>') if part.strip()]
                        
                        if len(parts) == 0:
                            value = ""
                        elif len(parts) == 1:
                            value = parts[0]
                        else:
                            # Remove duplicates while preserving order (case-insensitive comparison)
                            seen = set()
                            unique_parts = []
                            for part in parts:
                                # Normalize for comparison (lowercase, remove extra spaces)
                                normalized = ' '.join(part.lower().split())
                                if normalized not in seen and normalized:
                                    seen.add(normalized)
                                    unique_parts.append(part)
                            
                            # If we have duplicates, use the first occurrence
                            # If we have genuinely different parts, join them
                            if len(unique_parts) == 1:
                                value = unique_parts[0]
                            else:
                                value = ' '.join(unique_parts)
                    
                    # Clean remaining HTML tags if present (e.g. in certificate field)
                    if isinstance(value, str) and '<' in value:
                        value = re.sub(r'<[^>]+>', '', value)
                    
                    row.append(value)
                
                writer.writerow(row)
        
        print(f"✓ CSV file successfully created: {csv_file_path}")
        print(f"✓ Processed participants: {len(participants)}")
        print(f"✓ Columns: {', '.join(headers)}")
        return True
        
    except FileNotFoundError:
        print(f"Error: File {json_file_path} not found")
        return False
    except json.JSONDecodeError:
        print("Error: Invalid JSON file format")
        return False
    except Exception as e:
        print(f"Error: {e}")
        return False

def main():
    # Setup command line argument parser
    parser = argparse.ArgumentParser(
        description='Converts JSON file with race results to CSV format',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog='''
Usage examples:
  python json_to_csv_converter.py -i input.json -o output.csv
  python json_to_csv_converter.py --input data.json --output results.csv
        '''
    )
    
    parser.add_argument(
        '-i', '--input',
        required=True,
        help='Path to input JSON file'
    )
    
    parser.add_argument(
        '-o', '--output',
        required=True,
        help='Path to output CSV file'
    )
    
    # Parse arguments
    args = parser.parse_args()
    
    # Display file information
    print(f"Input file: {args.input}")
    print(f"Output file: {args.output}")
    print("-" * 50)
    
    # Perform conversion
    success = convert_json_to_csv(args.input, args.output)
    
    # Return appropriate exit code
    sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()