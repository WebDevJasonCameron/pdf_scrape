import argparse

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument(
    "--in_dir", help="Directory used to scrape PDF files.", default="No Input Directory Arguments provided.")
parser.add_argument(
    "--out_dir", help="Directory were the text file is placed.", default="No Output Directory Arguments provided.")

args = parser.parse_args()

print(args.in_dir)
print(args.out_dir)

flag = True

if args.in_dir == "No Input Directory Arguments provided." or args.out_dir == "No Output Directory Arguments provided.":
    flag = False

if flag:
    print("The program will not continue")
