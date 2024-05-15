import os
from pathlib import Path
from hdp import run_cairo

def test_run_cairo():
    input_file = 'test_fixture/input.json'
    output_file = 'test_fixture/output.zip'
    
    output = run_cairo(input_file, output_file)
    print(output)

test_run_cairo()