import argparse
import glob

parser = argparse.ArgumentParser(description='Removing Parts of a txt doc.')

parser.add_argument(
    "--focus_file", help="The file you wish to mod.", default="No Arguments provided.")
parser.add_argument(
    "--rm_line", help="The line you wish to remove.", default="No Arguements provided")


args = parser.parse_args()

flag = True

if args.focus_file == "No Arguments provided." or args.rm_line == "No Arguments provided.":
    flag = False

if flag:
    print("Program is running...")

    with open(args.focus_file, "r") as f:
        lines = f.readlines()

    with open(args.focus_file, "w") as f:
        for line in lines:
            if line.strip("/n") != args.rm_line:
                f.write(line)
