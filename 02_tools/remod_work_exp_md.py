import argparse
import glob

parser = argparse.ArgumentParser(
    description='Remodelling the notion md files to go in a obsidian doc')

parser.add_argument(
    "--in_f", help="Targeted file.", default="No Input Directory Arguments provided.")
parser.add_argument(
    "--out_p", help="Ouput dir for mod md file.", default="No Output Directory Arguments provided.")

args = parser.parse_args()

flag = True
file_list = []
file_title_list = []

if args.in_f == "No Input Directory Arguments provided." or args.out_p == "No Output Directory Arguments provided.":
    flag = False


def build_file_title(read_file):
    read_file = open(read_file, "r")
    first_hash = True
    num = 1

    for line in read_file:
        if "#" in line and first_hash == True:
            first_hash = False
            new_line = line.removeprefix("# ").replace(" ", "_").rstrip()

            if new_line not in file_title_list:
                file_title_list.append(new_line)
            else:
                while new_line + "_" + str(num) in file_title_list:
                    num += 1
                file_title_list.append(new_line + "_" + str(num))

    for i in file_title_list:
        print(i)

    read_file.close()


def better_date_output(line):
    no_coma_line = line.replace(",", "")
    parts = no_coma_line.split(" ")
    day = int(parts[2].rstrip())
    return parts[3].rstrip() + get_month_number(parts[1]).rstrip() + str("{:02d}".format(day))


def get_month_number(month):

    if month == "January":
        return "_01_"
    elif month == "February":
        return "_02_"
    elif month == "March":
        return "_03_"
    elif month == "April":
        return "_04_"
    elif month == "May":
        return "_05_"
    elif month == "June":
        return "_06_"
    elif month == "July":
        return "_07_"
    elif month == "August":
        return "_08_"
    elif month == "September":
        return "_09_"
    elif month == "October":
        return "_10_"
    elif month == "November":
        return "_11_"
    elif month == "December":
        return "_12_"
    else:
        return "_Missing_"


def reconstruct_line(line):
    part_01 = ""
    part_02 = ""
    if ":" in line:
        line_parts = line.split(":")
        part_01 = line_parts[0].replace(" ", "_") + ":"

        if "_/" in part_01:
            part_01 = part_01.replace("_/", "")

        part_02 = line_parts[1]
    return part_01 + part_02


def write_final_file(read_file_path, write_file_path, file_title):
    read_file = open(read_file_path, "r")
    write_file = open(write_file_path + "/" + file_title, "w")
    heading_line = True
    first_blank_line = True

    hash_title = ""

    write_file.writelines("---\n")

    for line in read_file:
        if "[" in line or "---" in line or "#" in line:
            continue
        elif ":" in line:
            write_file.writelines(reconstruct_line(line))
        elif line == "\n" and first_blank_line:
            first_blank_line = False
            continue
        else:
            if heading_line:
                write_file.writelines("\n---\n")
                write_file.writelines("# " + hash_title(file_title) + "\n\n")
                write_file.writelines("### Job Duties\n")
                heading_line = False
            else:
                write_file.writelines(line)

    read_file.close()
    write_file.close()


def remod_all_in_file_list(file_list, out_p):
    write_file_path = out_p

    for file in file_list:
        read_file_path = file

        file_title = build_file_title(read_file_path)
        write_final_file(read_file_path, write_file_path, file_title)


if flag:
    print("Program is running...")

    read_file = args.in_f

    build_file_title(read_file)

    # file_list = get_file_list(args.in_f)


print("\nCompleted")
