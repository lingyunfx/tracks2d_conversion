import os
import argparse
import master


def main():
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

    parser.add_argument('-wh', '--widthHeight',
                        help='Set image size',
                        dest='size',
                        type=str,
                        default='1920x1080',
                        action='store')

    parser.add_argument('-o', '--offset',
                        help='Set offset value',
                        dest='offset',
                        type=int,
                        default=0,
                        action='store')

    parser.add_argument('-n', '--name',
                        help='Set tracks name',
                        dest='tracker_name',
                        type=str,
                        action='store')
    parser.parse_args()
    args = parser.parse_args()

    file_path = args.file_path
    source_type = args.source_type
    target_type = args.target_type
    x_res, y_res = args.size.split('x')
    offset = args.offset
    x_res = float(x_res)
    y_res = float(y_res)
    tracker_name = args.tracker_name

    if source_type == '3de':
        tracker_data = master.from_3de(file_path, offset)
    elif source_type == 'syn':
        tracker_data = master.from_syn(file_path, x_res, y_res, offset)
    elif source_type == 'pft':
        tracker_data = master.from_pft(file_path, offset)
    elif source_type == 'bju':
        tracker_data = master.from_bju(file_path, x_res, offset)
    else:
        tracker_data = None

    if target_type == '3de':
        result_data = master.to_3de(tracker_data)
    elif target_type == 'pft':
        result_data = master.to_pft(tracker_data)
    elif target_type == 'syn':
        pass
    elif target_type == 'bju':
        pass

    print result_data
    output_file = os.path.splitext(file_path)[0] + '_to{0}.txt'.format(source_type)
    master.save_file(result_data, output_file)
    print output_file

if __name__ == '__main__':
    main()
