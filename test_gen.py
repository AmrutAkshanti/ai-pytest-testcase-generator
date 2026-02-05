import argparse
import os
import sys
from pathlib import Path
from generate_from_prompt import generate_tests


def extract_function_from_file(file_path: str) -> str:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"Input file not found: {path.absolute()}")

    try:
        content = path.read_text()
        if not content.strip():
            raise ValueError("Input file is empty")
        return content
    except Exception as e:
        raise RuntimeError(f"Failed to read input file: {str(e)}")


def clean_generated_code(raw_code: str) -> str:
    """Remove all non-test content from generated output"""
    lines = []
    capture = False

    for line in raw_code.splitlines():
        if not capture and line.strip().startswith(('import ', 'def test_', 'from ')):
            capture = True

        if capture and any(line.strip().startswith(s) for s in ('#', 'Note:', 'Tips:')):
            break

        if capture:
            lines.append(line)

    return '\n'.join(lines).strip()


def save_tests_to_file(test_code: str, input_file: str, output_file: str):
    path = Path(output_file)
    try:
        if not test_code.strip():
            raise ValueError("Generated test code is empty")

        path.parent.mkdir(parents=True, exist_ok=True)

        # Calculate relative import path
        rel_path = str(Path(input_file).with_suffix('')).replace(os.sep, '.')

        header = f"""# Auto-generated tests for {Path(input_file).name}
# To execute: pytest {path}

from {rel_path} import *

"""
        path.write_text(header + test_code)
        return str(path.absolute())
    except Exception as e:
        raise RuntimeError(f"Failed to save test file: {str(e)}")


def main():
    parser = argparse.ArgumentParser(
        description='Generate test cases with proper imports',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument("--file", default="examples/sample_func.py",
                        help="Python file containing the function to test")
    parser.add_argument("--output",
                        help="Output path for generated tests (default: tests/test_<input>.py)")
    args = parser.parse_args()

    # Set default output path if not provided
    if not args.output:
        input_stem = Path(args.file).stem
        args.output = f"tests/test_{input_stem}.py"

    try:
        print(f"⚙️ Extracting function from {args.file}...")
        func_str = extract_function_from_file(args.file)

        print("⚙️ Generating test cases...")
        raw_test_code = generate_tests(func_str)
        test_code = clean_generated_code(raw_test_code)

        print("\n=== Cleaned Test Code ===")
        print(test_code[:500] + ("..." if len(test_code) > 500 else ""))
        print("=======================")

        saved_path = save_tests_to_file(test_code, args.file, args.output)
        print(f"✅ Successfully saved to: {saved_path}")
        print(f"\nTo run these tests:\npytest {saved_path}")

    except Exception as e:
        print(f"❌ Error: {str(e)}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()




#python test_gen.py --file examples/multi_funcs.py --output output/test_multi_funcs.py
#pytest output/test_multi_funcs.py