import os
import argparse
import master


class Tracker2DConversion(object):

    def __init__(self):
        self.parser = argparse.ArgumentParser()
        self.support_list = ['syntheyes', '3de', 'pftrack', 'boujou', 'syn']
        self.add_argus()
        # self.parser.parse_args()
        self.args = self.parser.parse_args()

    def add_argus(self):
        self.parser.add_argument('file_path', help='Specify the source file path.')
        self.add_source_option()
        self.add_target_option()
        self.add_size_option()
        self.add_offset_option()
        self.add_clip_option()

    def add_source_option(self):
        self.parser.add_argument('-s', '--source',
                                 help='Specify the source 2D point type.',
                                 choices=self.support_list,
                                 dest='source_type',
                                 type=str,
                                 default='3de',
                                 action='store')

    def add_target_option(self):
        self.parser.add_argument('-t', '--target',
                                 help='Specify the target 2D point type.',
                                 choices=self.support_list,
                                 dest='target_type',
                                 type=str,
                                 default='syn',
                                 action='store')

    def add_size_option(self):
        self.parser.add_argument('-wh', '--widthHeight',
                                 help='Set image size',
                                 dest='size',
                                 type=str,
                                 default='1920x1080',
                                 action='store')

    def add_offset_option(self):
        self.parser.add_argument('-o', '--offset',
                                 help='Set offset value',
                                 dest='offset',
                                 type=int,
                                 default=0,
                                 action='store')

    def add_clip_option(self):
        self.parser.add_argument('-c', '--clip',
                                 help='Set PFTrack clip number',
                                 dest='clip_num',
                                 type=str,
                                 default='1',
                                 action='store')

    def get_res_xy(self):
        x_res, y_res = self.args.size.split('x')
        return float(x_res), float(y_res)

    def get_source_data(self, source_type):
        file_path = self.args.file_path
        x_res, y_res = self.get_res_xy()
        offset = self.args.offset
        command = {'syn': 'master.from_syn(file_path, x_res, y_res, offset)',
                   'syntheyes': 'master.from_syn(file_path, x_res, y_res, offset)',
                   '3de': 'master.from_3de(file_path, offset)',
                   'pftrack': 'master.from_pft(file_path, offset)',
                   'boujou': 'master.from_bju(file_path, x_res, offset)'
                   }.get(source_type)
        return eval(command)

    def get_target_data(self, target_type, tracker_data):
        x_res, y_res = self.get_res_xy()
        clip_num = self.args.clip_num
        command = {'syn': 'master.to_syn(tracker_data, x_res, y_res)',
                   'syntheyes': 'master.to_syn(tracker_data, x_res, y_res)',
                   '3de': 'master.to_3de(tracker_data)',
                   'pftrack': 'master.to_pft(tracker_data, clip_num)',
                   'boujou': 'master.to_bju(tracker_data, y_res)'
                   }.get(target_type)
        return eval(command)


def main():
    tk = Tracker2DConversion()
    file_path = tk.args.file_path
    source_type = tk.args.source_type
    target_type = tk.args.target_type

    source_data = tk.get_source_data(source_type)
    target_data = tk.get_target_data(target_type, source_data)

    output_file = os.path.splitext(file_path)[0] + '_to{0}.txt'.format(target_type)
    master.save_file(target_data, output_file)
    print 'Done.'
    print output_file


if __name__ == '__main__':
    main()
