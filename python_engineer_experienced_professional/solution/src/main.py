from json_schema_extractor import JsonSchemaExtractor


def main():
    # get file path from the caller
    file_path = input("Please enter input file path:")

    # process the file
    JsonSchemaExtractor.process_file(file_path)


if __name__ == "__main__":
    main()
