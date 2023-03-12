import argparse

parser = argparse.ArgumentParser(description='Removing Parts of a txt doc.')

parser.add_argument(
    "--file", help="The file you wish to mod.", default="No Arguments provided.")

parser.add_argument(
    "--sw", help="The targeted line starts with this...", default="No Arugments provided."
)

args = parser.parse_args()

flag = True
num_count = 0


if args.file == "No Arguments provided." or args.sw == "No Arugments provided.":
    flag = False

if flag:
    print("Program is running...")

    with open(args.file, "r") as f:
        lines = f.readlines()

    with open(args.file, "w") as f:
        for line in lines:
            if len(line) > 1:
                if line.startswith(args.sw):
                    continue
                else:
                    f.write(line)
            else:
                continue
else:
    print("Unapble to run the program")
