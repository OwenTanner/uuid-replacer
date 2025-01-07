from re import sub
import uuid
import argparse

def replace_uuids_in_text(input_text: str) -> str:
    """Replace all UUIDs in the given text with newly generated UUIDs, maintaining consistency for duplicates.

    Args:
        input_text (str): The input text containing UUIDs.

    Returns:
        str: The text with UUIDs replaced by new ones.
    """
    uuid_mapping = {}

    def replace_match(match):
        original_uuid = match.group(0)
        if original_uuid not in uuid_mapping:
            uuid_mapping[original_uuid] = str(uuid.uuid4())
        return uuid_mapping[original_uuid]

    return sub(
        r'\b[0-9a-fA-F]{8}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{4}-[0-9a-fA-F]{12}\b',
        replace_match,
        input_text
    )

def process_uuid_replacement(input_file: str, output_file: str) -> None:
    """Read from the input file, replace UUIDs, and write to the output file.

    Args:
        input_file (str): Path to the input file containing text with UUIDs.
        output_file (str): Path to the output file where processed text will be saved.
    """
    try:
        with open(input_file, "r") as file:
            input_text = file.read()
        output_text = replace_uuids_in_text(input_text)
        with open(output_file, "w") as file:
            file.write(output_text)
        print(f"UUID replacement completed. Check '{output_file}' for the result.")
    except FileNotFoundError:
        print(f"Error: '{input_file}' not found.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Replace UUIDs in a text file with new UUIDs.")
    parser.add_argument("input_file", type=str, help="Path to the input file containing text with UUIDs.")
    parser.add_argument("output_file", type=str, help="Path to the output file to save the modified text.")
    args = parser.parse_args()

    process_uuid_replacement(args.input_file, args.output_file)
