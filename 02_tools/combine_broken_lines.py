import argparse

parser = argparse.ArgumentParser(description='Removing Parts of a txt doc.')

parser.add_argument(
    "--focus_file", help="The file you wish to mod.", default="No Arguments provided.")

args = parser.parse_args()

flag = True

if args.focus_file == "No Arguments provided.":
    flag = False

if flag:
    print("Program is running...")

    with open(args.focus_file, "r") as f:
        lines = f.readlines()

    with open(args.focus_file, "w") as f:
        for line in lines:
            if not line.endswith("."):
                line.replace("\\n", " ")
                f.write(line)
            else:
                f.write(line)
