import pprint


def load_file(file_path):
    with open(file_path) as f:
        line_list = f.readlines()
    line_list = [x.strip() for x in line_list]
    return line_list


def save_file(data, output_path):
    print data
    with open(output_path, 'w') as f:
        for d in data:
            f.write(d + '\n')


def from_3de(file_path, offset):
    tracker_data = {}
    line_list = load_file(file_path)
    switch = True
    for line in line_list[1:]:
        if len(line.split()) == 1:
            if switch:
                name = line
                tracker_data.setdefault(name, {})
                switch = False
            continue

        frame, x_pos, y_pos = line.split()
        tracker_data[name].setdefault(int(frame) + offset, [x_pos, y_pos])
        switch = True
    return tracker_data


def from_syn(file_path, height=0.0, width=0.0, offset=0):
    tracker_data = {}
    line_list = load_file(file_path)
    for line in line_list:
        name, frame, x_pos, y_pos, ref = line.split()
        frame = int(frame) + offset
        x_pos = float(x_pos+1)/2 * int(width)
        y_pos = 1 - float(y_pos)/2 * int(height)
        if name in tracker_data.keys():
            tracker_data[name].setdefault(frame, [x_pos, y_pos])
        else:
            tracker_data.setdefault(name, {})
            tracker_data[name].setdefault(frame, [x_pos, y_pos])
    return tracker_data


def from_pft(file_path, offset=0):
    tracker_data = {}
    line_list = load_file(file_path)
    for line in line_list:
        if line.startswith('"'):
            name = line.replace('"', '')
            tracker_data.setdefault(name, {})
        if len(line.split()) == 4:
            frame, x_pos, y_pos, score = line.split()
            tracker_data[name].setdefault(int(frame) + offset, [x_pos, y_pos])
    return tracker_data


def from_bju(file_path, width=0.0, offset=0):
    tracker_data = {}
    line_list = load_file(file_path)
    for line in line_list:
        if line.startswith('#'):
            continue
        name, frame, x_pos, y_pox = line.split()
        frame = int(frame) + offset
        y_pox = float(float(width)-float(y_pox))
        if name in tracker_data.keys():
            tracker_data[name].setdefault(frame, [x_pos, y_pox])
        else:
            tracker_data.setdefault(name, {})
            tracker_data[name].setdefault(frame, [x_pos, y_pox])
    return tracker_data


def to_3de(tracker_data):
    frame_count = len(tracker_data.keys())
    result_data = [str(frame_count)]
    for name, frames in tracker_data.iteritems():
        result_data.append(name)
        result_data.append('0')
        result_data.append(str(len(frames.keys())))
        for frame in sorted(frames.keys()):
            x_pos = frames[frame][0]
            y_pos = frames[frame][1]
            result_data.append('{0} {1} {2}'.format(frame, x_pos, y_pos))
    return result_data


def to_pft(tracker_data):
    result_data = []
    clip_number = '1'
    for name, frames in tracker_data.iteritems():
        result_data.append('"{0}"'.format(name))
        result_data.append(clip_number)
        result_data.append(str(len(frames.keys())))
        for frame in sorted(frames.keys()):
            x_pos = frames[frame][0]
            y_pos = frames[frame][1]
            result_data.append('{0} {1} {2} 1.000000'.format(frame, x_pos, y_pos))
    return result_data


def to_syn(tracker_data):
    result_data = []
