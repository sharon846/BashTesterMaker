import os
import json

import json

def convert_json_to_shell(json_file):
    with open(json_file, 'r') as file:
        data = json.load(file)

    shell_script = []

    for task in data['tasks']:
        task_file = task['task_file']
        shell_script.append(f'if [ -f "{task_file}" ]; then')

        preset_tests = [test for test in task['tests'] if 'preset' in test['test_name'].lower()]
        if preset_tests:
            for test in preset_tests:
                test_name = test['test_name']
                points = test['points']
                input_data = test['input_data'].replace("\n", "\\n")
                expected_output = test['expected_output'].replace("\n", "\\n")
                comparison_method = test['comparison_method']

                shell_script.append(
                    f'  run_preset_test "{test_name}" {points} "{input_data}" "{expected_output}" "{comparison_method}"'
                )

        normal_tests = [test for test in task['tests'] if 'preset' not in test['test_name'].lower()]
        if normal_tests:
            shell_script.append(f'  run_task "{task_file}" \\')
            for test in normal_tests:
                test_name = test['test_name']
                points = test['points']
                input_data = test['input_data'].replace("\n", "\\n")
                expected_output = test['expected_output'].replace("\n", "\\n")
                comparison_method = test['comparison_method']
                mode = test['mode']
                input_type = test['input_type']

                shell_script.append(
                    f'    "{test_name}" {points} "{input_data}" "{expected_output}" "{comparison_method}" "{mode}" "{input_type}" \\'
                )

            shell_script[-1] = shell_script[-1].rstrip(' \\')  # Remove trailing backslash from the last test

        shell_script.append(f'else')
        shell_script.append(f'  echo "{task_file} does not exist, skipping"')
        shell_script.append(f'fi\n')

    return "\n".join(shell_script)

with open('shell_template', 'r') as file:
    text = file.read()

json_file = 'tests.json'
shell_script_content = convert_json_to_shell(json_file)

text = text.replace('INSERT_HERE', shell_script_content)

with open('tester.sh', 'w') as shell_file:
    shell_file.write(text)