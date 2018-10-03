import paramiko

self.ssh_conn_stress = paramiko.SSHClient()
self.ssh_conn_stress.set_missing_host_key_policy(paramiko.AutoAddPolicy())


self.ssh_conn_stress.connect(self.stress_host, username=self.stress_uname, password=self.stress_pwd)
                self.ssh_conn_stress.exec_command(
                    "cd /opt/tools/profiler/ise1.3 ; python new.py 10.197.88.138 DHCP 100 200 eth0 false")


stdin, stdout, stderr = self.ssh_conn_profilerLogs.exec_command(
                    "grep \"Redis get returns wrong object. Given mac:\" '/opt/CSCOcpm/logs/profiler.log' | tail -1")
                output = stdout.readlines()
                output = str(output)