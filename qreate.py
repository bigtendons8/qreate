
import argparse
import os

def main():
    DEFAULT_DIRECTORY = "/Users/james/Documents/Home/codering/python/"

    parser = argparse.ArgumentParser(description="create python project")
    parser.add_argument("name", type=str, nargs=1)
    parser.add_argument("-g", "--git", action="store_true", help="create git repository")

    args = parser.parse_args()
    name = args.name[0]

    created_directory = DEFAULT_DIRECTORY+name

    os.system(f"mkdir -p {created_directory}")
    print(f"Created directory \"{args.name[0]}\"")
    os.chdir(created_directory)
    os.system("touch main.py")
    os.system("echo \"def main():\n\nif __name__ == \"__main__\":\n    main()\" > main.py")
    if args.git is True:
        os.system("git init")
        os.system("git add main.py")
        os.system("git commit -m \"initial commit\"")

if __name__ == "__main__":
    main()

