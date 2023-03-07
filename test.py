import argparse

parser = argparse.ArgumentParser(description='A test program.')

parser.add_argument(
    "--in_dir", help="Directory used to scrape PDF files.", default="A random string.")
parser.add_argument(
    "--out_dir", help="Directory were the text file is placed.")

args = parser.parse_args()

print(args.in_dir)
print(args.out_dir)
