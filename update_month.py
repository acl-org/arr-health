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

if not os.path.exists(args.month) or args.full_copy:
    print("Performing full copy")
    shutil.copytree(template_folder, args.month)
else:
    print("Performing template copy")
    shutil.copy(os.path.join(template_folder, "index.html"), args.month)
