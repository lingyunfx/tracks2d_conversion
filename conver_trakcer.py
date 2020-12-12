import argparse
support_list = ['syn', '3de', 'pft', 'bju']
parser = argparse.ArgumentParser()
parser.add_argument('file_path')
parser.add_argument('-s', '--source',
                    help='Specify the source 2D point type.',
                    choices=support_list,
                    dest='source_type',
                    type=str,
                    action='store')

parser.add_argument('-t', '--target',
                    help='Specify the target 2D point type.',
                    choices=support_list,
                    dest='target_type',
                    type=str,
                    action='store')

parser.parse_args()
args = parser.parse_args()
print args.source_type
print args.target_type
print args.file_path
