# BashTesterMaker

Please follow the structure of tests.json.

For each test:
- test_name: Name for the test.
- points: What is the score this test worth.
- input_data:
  - If this test aims to run python script, this is the input.
  - If this test aims to run python script as a module, there are the 'main' commands (separated by '\n').
  - If this test aims to run shell script, this it the command.
- expected_output: The output you wish to get from running the shell/py script.
- comparison_method: Currently supports "exact", "contains".
- mode:
  - If set to script, will run the task as python file.
  - If set to import, will use the task as a module.
  - If you wish to run a shell script, mode should be empty.
- input_type: If set to "sys" will use the input_data as arguments and not as input. Otherwise - set to none.
