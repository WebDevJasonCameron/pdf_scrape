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

# <F> BUILD FILE NAME


def build_file_name(read_file):
    read_file = open(read_file, "r")
    out_title = ""

    for line in read_file:
        if "#" in line:
            out_title = line.removeprefix("# ").replace(" ", "_").rstrip()
        elif "Start Time:" in line:
            out_title = out_title + "_" + \
                line.removeprefix("Start Time:").replace(
                    ",", "").replace(" ", "_").rstrip() + ".md"

    read_file.close()
    return out_title


# <F> RECONSTRUCT LINE
def reconstruct_line(line):
    part_01 = ""
    part_02 = ""
    if ":" in line:
        line_parts = line.split(":")
        part_01 = line_parts[0].replace(" ", "_") + ":"

        if "_/" in part_01:
            part_01 = part_01.replace("_/", "")

        if "POC_3_1:" in part_01:
            part_01 = "POC_3_Number"

        part_02 = line_parts[1]
    return part_01 + part_02


if flag:
    print("Program is running...")

    file_title = build_file_name(args.in_f)

    read_file = open(args.in_f, "r")

    for line in read_file:
        mod_line = reconstruct_line(line)
        print(mod_line)

    print("HERE IS OUR NEW FILE TITLE:   " + file_title)
