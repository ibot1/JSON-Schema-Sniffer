from solution.src.json_schema_extractor import JsonSchemaExtractor
import json
import unittest


class TestJsonSchemaExtractor(unittest.TestCase):
    def test_success_case1(self):
        input_file_path = "solution/tests/resources/test_1.json"
        output_file_path = "schema/schema_test_1.json"
        expected_output_file_path = "solution/tests/resources/expected_1.json"
        status = JsonSchemaExtractor.process_file(input_file_path)
        self.assertEqual(True, status, "Operation should succeed")
        self.assertDataFromFiles(expected_output_file_path, output_file_path)

    def test_success_case2(self):
        input_file_path = "solution/tests/resources/test_2.json"
        output_file_path = "schema/schema_test_2.json"
        expected_output_file_path = "solution/tests/resources/expected_2.json"
        status = JsonSchemaExtractor.process_file(input_file_path)
        self.assertEqual(True, status, "Operation should succeed")
        self.assertDataFromFiles(expected_output_file_path, output_file_path)

    def assertDataFromFiles(
        self, expected_output_file_path: str, actual_output_file_path: str
    ):
        try:
            actual_data, expected_data = None, None
            with open(actual_output_file_path, "r") as file:
                actual_data = json.load(file)
            with open(expected_output_file_path, "r") as file:
                expected_data = json.load(file)
            self.assertDictEqual(
                expected_data, actual_data, "JSON data should match as expected"
            )
        except Exception:
            self.fail("Unable to assert data from file")


if __name__ == "__main__":
    unittest.main()
