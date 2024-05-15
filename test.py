import os
from hdp import run_cairo

def test_run_cairo(capsys):
    input_file = 'tests/test_file/input.json'
    output_file = 'tests/test_file/output.zip'
    
    output = run_cairo(input_file, output_file)
    
  