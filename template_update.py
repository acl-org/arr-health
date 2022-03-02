import argparse
import shutil
import os

def get_argparser():
    parser = argparse.ArgumentParser(description='OpenReview venue management')
    parser.add_argument('--month', required=True, help='which month?')
    parser.add_argument('--full_copy', action='store_true', help='when creating new, otherwise only need to copy template')
    return parser

args = get_argparser().parse_args()
iter_path = "iterations"
template_folder = "pMQseJPcaH"

os.chdir(os.path.join(os.getcwd(), iter_path))

if args.month == "all":
    years = os.listdir()
    years.remove(template_folder)
    months = [os.path.join(y,m) for y in years for m in os.listdir(y)]
    # months = [a for a in os.listdir() if os.path.isdir(a)]
else:
    months = [args.month]

print(months)

for month in months:
    if not os.path.exists(month) or args.full_copy:
        print("Performing full copy")
        shutil.copytree(template_folder, month)
    else:
        print("Performing template copy")
        shutil.copy(os.path.join(template_folder, "index.html"), month)
