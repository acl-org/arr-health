import argparse
import shutil
import os

def get_argparser():
    parser = argparse.ArgumentParser(description='OpenReview venue management')
    parser.add_argument('--month', required=True, help='which month?')
    parser.add_argument('--full_copy', action='store_true', help='when creating new, otherwise only need to copy template')
    return parser

args = get_argparser().parse_args()
template_folder = "pMQseJPcaH"

if args.month == "all":
    months = [a for a in os.listdir() if os.path.isdir(a)]
    months.remove(template_folder)
    months.remove(".git")
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
