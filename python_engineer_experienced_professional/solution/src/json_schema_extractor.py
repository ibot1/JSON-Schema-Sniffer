from pathlib import Path
from typing import Any
import json
import logging

# define logger settings
logging.basicConfig(
    filename="logs/app.log",
    filemode="a",
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

# acquire logger
logger = logging.getLogger(__name__)


"""
This class provides utility functions to extract the schema from an input file
"""


class JsonSchemaExtractor:
    @staticmethod
    def process_file(input_file_path: str) -> bool:
        try:
            schema_buffer, message = {}, {}

            # get message data from input file
            # Note: no validation (like validating file type) is done before opening the input file
            # because that doesn't prevent future errors (like invalid json content)
            # Hence: all files with valid json content will be processed successfully
            with open(input_file_path, "r") as file:
                message = json.load(file).get("message") or message

            # populate the schema buffer with the attributes and their entries
            for att in message.keys():
                att_type = JsonSchemaExtractor.__type_of(message[att])
                schema_buffer[att] = JsonSchemaExtractor.__create_att_entry(att_type)

            # create schema file name from input file name
            output_file_name = f"schema/schema_{Path(input_file_path).stem}.json"

            # write the schema to the output file
            with open(output_file_name, "w") as file:
                json.dump(
                    schema_buffer, file, sort_keys=True, indent=4, ensure_ascii=False
                )

            logger.info(
                "Successfully processed input file '%s' to schema ouput file '../../%s'",
                input_file_path,
                output_file_name,
            )

            return True
        except (OSError, json.JSONDecodeError) as e:
            logger.error(
                "Failed to process input file '%s' with error: %s", input_file_path, e
            )
            return False

    @staticmethod
    def __create_att_entry(att_type: str) -> dict[str, str | bool]:
        return {
            "type": att_type,
            "tag": "",
            "description": "",
            "required": False,
        }

    # I added the extra rule types aside the ones mentioned in the PROBLEM.MD because
    # I think they are valid scenarios
    @staticmethod
    def __type_of(obj: Any) -> str:
        if obj is None:
            return "null"
        if isinstance(obj, bool):
            return "boolean"
        if isinstance(obj, int):
            return "integer"
        if isinstance(obj, float):
            return "float"
        if isinstance(obj, str):
            return "string"
        if not isinstance(obj, list):
            return "json"
        return "enum" if obj and isinstance(obj[0], str) else "array"
