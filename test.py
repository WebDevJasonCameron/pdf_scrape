import argparse
import glob
from pdfminer.high_level import extract_pages, extract_text

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument(
    "--in_dir", help="Directory used to scrape PDF files.", default="No Input Directory Arguments provided.")
parser.add_argument(
    "--out_dir", help="Directory were the text file is placed.", default="No Output Directory Arguments provided.")

args = parser.parse_args()

flag = True

if args.in_dir == "No Input Directory Arguments provided." or args.out_dir == "No Output Directory Arguments provided.":
    flag = False

if flag:
    print("Program is running...")

    files = glob.glob(args.in_dir + '/**/*.pdf', recursive=True)
    files.sort()

    write_file = open(
        args.out_dir + "/replace_title_with_book_title.md", "a")

    for f in files:
        text = extract_text(f)
        write_file.writelines(text)

    write_file.close()
    print("Program is done.")

else:
    print("Unable to run Program with out correct arguments.")
