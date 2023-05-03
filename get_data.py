import os


def get_data(data_name: str):
    line_param = data_name.split('_')[-1].split('s')[0]
    if line_param == 'warning':
        line_params = ['warning', ' warn ']
    elif line_param == 'error':
        line_params = ['error', ' err ']
    rez = []
    if 'all' in data_name:
        for folder in os.listdir('./logs'):
            data_name += folder
    for foldername in os.listdir('./logs'):
        if foldername in data_name:
            for file in os.listdir(os.path.join('./logs', foldername)):
                with open(os.path.join('./logs', foldername, file), 'r') as f:
                    lines = f.readlines()

                    # итерация по строкам
                    for line in lines:
                        for param in line_params:
                            if param in line.lower():
                                rez.append(line+'\n')

    return rez


if __name__ == '__main__':
    print(get_data('datanode_errors'))
