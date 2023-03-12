import argparse
import glob
from pdfminer.high_level import extract_text

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument(
    "--in_file", help="Targeted PDF file  used.", default="No Input Directory Arguments provided.")
parser.add_argument(
    "--out_file", help="Text placed in this file.", default="No Output Directory Arguments provided.")

args = parser.parse_args()

flag = True

if args.in_file == "No Input Directory Arguments provided." or args.out_file == "No Output Directory Arguments provided.":
    flag = False

if flag:
    print("Program is running...")

    target_file = glob.glob(args.in_file)

    write_file = open(
        args.out_file + "/replace_title_with_book_and_chapter_title.txt", "a")

    for f in target_file:
        text = extract_text(f)
        write_file.writelines(text)

    write_file.close()
    print("Program is done.")

else:
    print("Unable to run Program with out correct arguments.")
