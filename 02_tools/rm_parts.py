import argparse

parser = argparse.ArgumentParser(description='Removing Parts of a txt doc.')

parser.add_argument(
    "--file", help="The file you wish to mod.", default="No Arguments provided.")
parser.add_argument(
    "--rl", help="The line you wish to remove.", default="No Arguements provided")


args = parser.parse_args()

flag = True
num_count = 0

if args.file == "No Arguments provided." or args.rl == "No Arguments provided.":
    flag = False

if flag:
    print("Program is running...")

    with open(args.file, "r") as f:
        lines = f.readlines()

    with open(args.file, "w") as f:
        for line in lines:
            if line.strip("\\n") != args.rl:
                f.write(line)
            else:
                num_count += 1

print("Total lines removed: " + str(num_count))
