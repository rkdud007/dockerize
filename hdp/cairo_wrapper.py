import os
from pathlib import Path
import subprocess

def run_cairo(input_file, output_file):
    # Set the paths to the compiled Cairo files, build files, tools, and packages
    # Get the current directory
    package_dir = Path(__file__).parent.resolve()
    print(package_dir)
    compiled_cairo_path = os.path.join(package_dir, 'compiled_cairo', 'hdp.json')
    print(compiled_cairo_path)
    build_path = os.path.join(package_dir, 'build', 'compiled_cairo_files', 'simple_linear_regression.sierra.json')
    tools_path = os.path.join(package_dir, 'tools', 'py')
    print(tools_path)
    packages_path = os.path.join(package_dir, 'packages', 'hdp_bootloader')
    
    # Set the environment variables for the cairo-run command
    env = os.environ.copy()
    env['PYTHONPATH'] = f"{tools_path}:{packages_path}:{env.get('PYTHONPATH', '')}"
    
    try:
        # Run the cairo-run command and capture the output
        result = subprocess.run(
            [
                'cairo-run',
                '--program', './hdp/compiled_cairo/hdp.json',
                '--layout', 'starknet_with_keccak',
                '--program_input', input_file,
                '--cairo_pie_output', output_file,
                '--print_info'
            ],
            env=env,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            text=True
        )

        print(result.stdout)
        
        # Check the return code
        if result.returncode == 0:
            print("cairo-run executed successfully.")
            print("Output:")
            print(result.stdout)
            return result.stdout
        else:
            print(f"cairo-run execution failed with return code: {result.returncode}")
            print("Error:")
            print(result.stderr)
            return None
    
    except FileNotFoundError:
        print("cairo-run command not found. Please make sure cairo-lang is installed.")
        return None
    
    except subprocess.CalledProcessError as e:
        print(f"cairo-run execution failed with error: {e}")
        print("Error output:")
        print(e.output)
        return None