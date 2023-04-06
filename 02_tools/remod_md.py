import argparse
import glob

parser = argparse.ArgumentParser(
    description='Remodelling the notion md files to go in a obsidian doc')

parser.add_argument(
    "--in_f", help="Targeted MD file  used.", default="No Input Directory Arguments provided.")
parser.add_argument(
    "--out_p", help="The place the new file needs to go.", default="No Output Directory Arguments provided.")

args = parser.parse_args()

flag = True
line_num = 0
file_title = ""

if args.in_f == "No Input Directory Arguments provided." or args.out_p == "No Output Directory Arguments provided.":
    flag = False

if flag:
    print("Program is running...")

    target_file = open(args.in_f, "r")

    # Make out file's name
    for line in target_file:
        if "#" in line:
            file_title = line.removeprefix("# ").replace(" ", "_").rstrip()
        elif "Start Time:" in line:
            file_title = file_title + \
                line.removeprefix("Start Time:").replace(
                    ",", "").replace(" ", "_").rstrip() + ".md"

    print("HERE IS OUR NEW FILE TITLE:   " + file_title)
