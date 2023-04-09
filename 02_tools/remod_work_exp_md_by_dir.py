import argparse
import glob

parser = argparse.ArgumentParser(
    description='Remodelling the notion md files to go in a obsidian doc')

parser.add_argument(
    "--in_dir", help="Targeted dir to get the md files.", default="No Input Directory Arguments provided.")
parser.add_argument(
    "--out_dir", help="Ouput dir for mod md files.", default="No Output Directory Arguments provided.")

args = parser.parse_args()

flag = True
file_title_list = []

if args.in_dir == "No Input Directory Arguments provided." or args.out_dir == "No Output Directory Arguments provided.":
    flag = False


def get_file_list(read_path):
    return glob.glob(read_path + '/*.md', recursive=True)


def get_file_name_list(file_list):
    out_list = []
    for read_file_path in file_list:
        out_list.append(build_file_title(read_file_path))
    return out_list


def remod_all_files(read_path_list, write_file_path, file_name_list):
    index_position = 0

    for read_path in read_path_list:
        write_final_file(read_path, write_file_path,
                         file_name_list[index_position])
        index_position += 1


def build_file_title(read_file_path):
    read_file_path = open(read_file_path, "r")
    first_hash = True
    num = 1
    out_name = ""

    for line in read_file_path:
        if "#" in line and first_hash == True:
            first_hash = False
            new_line = line.removeprefix("# ").replace(
                " ", "_").replace("\\", "_").replace("/", "_").rstrip()

            if new_line not in file_title_list:
                file_title_list.append(new_line)
                out_name = new_line
            else:
                while new_line + "_" + str(num) in file_title_list:
                    num += 1
                file_title_list.append(new_line + "_" + str(num))
                out_name = new_line + "_" + str(num)
    read_file_path.close()
    return out_name


def better_date_output(line):
    no_coma_line = line.replace(",", "")
    parts = no_coma_line.split(" ")
    day = int(parts[2].rstrip())
    return parts[3].rstrip() + " " + get_month_number(parts[1]).rstrip() + " " + str("{:02d}".format(day))


def get_month_number(month):

    if month == "January":
        return "01"
    elif month == "February":
        return "02"
    elif month == "March":
        return "03"
    elif month == "April":
        return "04"
    elif month == "May":
        return "05"
    elif month == "June":
        return "06"
    elif month == "July":
        return "07"
    elif month == "August":
        return "08"
    elif month == "September":
        return "09"
    elif month == "October":
        return "10"
    elif month == "November":
        return "11"
    elif month == "December":
        return "12"
    else:
        return "Missing"


def reconstruct_line(line):
    part_01 = ""
    part_02 = ""
    line_parts = line.split(":")

    part_01 = line_parts[0].replace(" ", "_").replace(
        "(1)_", "").replace("(2)_", "").replace("(3)_", "") + ":: "
    part_02 = line_parts[1]

    if "Start_Date" in part_01 or "End_Date" in part_01:
        part_02 = better_date_output(part_02) + "\n"

    return part_01 + part_02.replace("'", "")


def write_final_file(read_file_path, write_file_path, file_title):
    read_file = open(read_file_path, "r")
    write_file = open(write_file_path + "/" + file_title + ".md", "w")
    heading_line = True
    to_many_blank_lines = 0

    for line in read_file:
        if "[" in line or "---" in line:
            continue
        elif "#" in line and heading_line == True:
            heading_line = False
            to_many_blank_lines = 0
            write_file.writelines(line)
        elif "#" in line and heading_line == False:
            write_file.writelines("##" + line)
            to_many_blank_lines = 0
        elif ":" in line:
            write_file.writelines(reconstruct_line(line) + "\n")
            to_many_blank_lines = 0
        elif "EXP" in line:
            write_file.writelines("---\n")
            write_file.writelines(
                '<small style="color:grey">' + line + '</small>\n')
            to_many_blank_lines = 0
        elif "\n" == line:
            if to_many_blank_lines <= 1:
                write_file.writelines(line)
                to_many_blank_lines += 1
            else:
                continue
        else:
            write_file.writelines(line)

    read_file.close()
    write_file.close()


if flag:
    print("Program is running...")

    read_path = args.in_dir
    write_path = args.out_dir

    read_path_list = get_file_list(read_path)
    file_name_list = get_file_name_list(read_path_list)

    remod_all_files(read_path_list, write_path, file_name_list)


print("\nCompleted")
