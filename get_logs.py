import os

import paramiko


def get_logs():
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ips = ['4', '5', '6']

    for ip in ips:
        ssh.connect('10.130.0.' + ip, username='admin', password='test@2022')

        ftp = ssh.open_sftp()
        # ftp.chdir('/var/log/hadoop-hdfs')
        hadoob_path = '/var/log/hadoop-'
        hadoob_paths = ['hdfs', 'mapreduce', 'yarn']

        for i in hadoob_paths:
            path = hadoob_path + i
            print(ip, os.path.join(hadoob_path, path))
            for filename in ftp.listdir(path):
                try:
                    if filename not in ['userlogs', 'SecurityAuth-hdfs.audit']:
                        for foldername in os.listdir('./logs'):
                            if foldername in filename:
                                ftp.get(os.path.join(path, filename), os.path.join('logs', foldername, filename))
                        # else:
                        #     ftp.get(os.path.join(path, filename),
                        #             os.path.join('logs', 'namenode', filename))

                except IOError:
                    pass

# node_param = ['datanode', 'namenode', '']
# rashir = ['.log', 'out', 'out.1', 'out.2', 'out.3', 'out.4']

# flask написать и как-то там легче делается...хрен его как, надо бы

# exceptions and errors вытаскивать все лог файлы "error hadoob hdfs", "error hadoob mapreduce", "error hadoob yarn"
