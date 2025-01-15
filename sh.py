from PyQt5 import QtCore, QtGui, QtWidgets
import paramiko, os
import threading

class Ui_Sh(object):
    def setupUi(self, Form, parameter=None):
        Form.setObjectName("Form")
        Form.setStyleSheet("background-color: #f5f5f5;")  # 设置背景色为浅灰色
        ui_width = 500
        ui_height = 500
        Form.resize(ui_width, ui_height)
        Form.setMinimumSize(QtCore.QSize(ui_width, ui_height))
        Form.setMaximumSize(QtCore.QSize(ui_width, ui_height))

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, 401, 41))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(14)  # 增加标题字体大小
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #333333;")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 60, 430, 400))
        self.textBrowser.setObjectName("textBrowser")
        
        self.testname = ""
        self.process = QtCore.QProcess(self)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 根据传入的参数来执行逻辑
        if parameter:
            self.run_script(parameter)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "脚本运行窗口"))
        self.label.setText(_translate("Form", f"当前正在运行{self.testname}"))

    def run_script(self, parameter):
        if parameter in [2, 13, 14]:
            # 启动一个新线程来执行脚本
            self.thread = ScriptExecutionThread(parameter, self.textBrowser)
            self.thread.start()
        elif parameter in [3, 10, 11, 12]:
            self.run_executable(parameter)
        elif parameter in [4, 5, 6, 7, 8, 9]:
            self.run_script(parameter)
        else:
            return

    def run_executable(self, parameter):
        if self.process:
            if self.process.state() == QtCore.QProcess.Running:
                self.kill_process()

        if parameter == 3:
            self.executable = ""# 能效
        elif parameter == 10:
            self.executable = ""# 算力
        elif parameter == 11:
            self.executable = ""# 乘加计算
        elif parameter == 12:
            self.executable = ""# 容量
        else:
            return
        
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.start( [self.executable])

    def run_script(self, parameter):
        if self.process:
            if self.process.state() == QtCore.QProcess.Running:
                self.kill_process()

        scripts_dic = {
            4: "",# 容量
            5: "",# 乘加计算
            6: "",# 算力
            7: "",# 单阵列核心计算能效
            8: "",# 全芯片处理能效
            9: "",# 与GPU能效对比
        }
        script = scripts_dic.get(parameter, None)
        if not script:
            return
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.start("python", [script])# 使用对应环境的python

    def on_readyReadStandardOutput(self):
        if self.process == None:
            return
        output = self.process.readAllStandardOutput().data().decode()
        self.textBrowser.append(output)  # 实时更新textBrowser
    
    def kill_process(self):
        if self.process:
            pid = self.process.processId()
            print(f"Now killing the subprocess {pid} of compiler window")
            if pid:
                os.system(f"sudo kill -9 {pid}")
            self.process = None

    def closeEvent(self, event):
        # check if subprocess exists
        if self.process:
            if self.process.state() == QtCore.QProcess.Running:
                self.process.kill()
        if parameter in [2, 13, 14]:
            self.sever = connect_ssh(self.textBrowser)
            if hasattr(self, 'sever') and self.sever.target_ssh:
                try:
                    # 获取进程 PID 并杀掉进程              
                    self.sever.execute('pkill -f bnn_mnist.py')  
                    self.sever.execute('pkill -f func_test.py')
                    self.sever.execute('pkill -f naive_bayes.py')  
                    print("相关进程已终止。")
                except Exception as e:
                    print(f"终止进程时发生错误: {e}")
    
            # 关闭 SSH 连接
            if hasattr(self, 'sever'):
                self.sever.close()            
        event.accept()

class ScriptExecutionThread(QtCore.QThread):
    def __init__(self, parameter, textBrowser):
        super().__init__()
        self.parameter = parameter
        self.textBrowser = textBrowser

    def run(self):
        # 创建 SSH 连接类并连接
        self.ssh_connection = connect_ssh(self.textBrowser)  # 传递 textBrowser
        print('连接成功')

        if self.parameter == 2:  # Binary FC-3算法识别准确率
            self.ssh_connection.execute('cd /home/wangyufei/ProgramTest/FADESim_project_test/ir_drop/pimfixedpoint/')
            # 确保cd命令正确执行，并打印当前工作目录
            cd_cmd = 'cd /home/wangyufei/ProgramTest/FADESim_project_test/ir_drop/pimfixedpoint/ && ./ui_fc3.sh'
            self.ssh_connection.execute_real_time(cd_cmd)

        elif self.parameter == 13:  # Binary LeNet-5算法识别准确率
            self.ssh_connection.execute('cd /home/wangyufei/ProgramTest/FADESim_project_test/ir_drop/pimfixedpoint/')
            # 确保cd命令正确执行，并打印当前工作目录
            cd_cmd = 'cd /home/wangyufei/ProgramTest/FADESim_project_test/ir_drop/pimfixedpoint/ && ./ui_lenet5.sh'
            self.ssh_connection.execute_real_time(cd_cmd)

        elif self.parameter == 14:  # Naive Bayes算法识别准确率
            self.ssh_connection.execute('cd /home/wangyufei/ProgramTest/FADESim_project_test/ir_drop/pimfixedpoint/')
            # 确保cd命令正确执行，并打印当前工作目录
            cd_cmd = 'cd /home/wangyufei/ProgramTest/FADESim_project_test/ir_drop/pimfixedpoint/ && ./ui_nb.sh'
            self.ssh_connection.execute_real_time(cd_cmd)

        else:
            return "Unknown script"

class connect_ssh:

    def __init__(self, textBrowser):
        jumpbox_host_ip = "222.20.98.67"  # 跳板机
        ssh_user = "wangyufei"
        ssh_key_filename = 'id_rsa'
        target_host_ip = '192.168.33.2'  # 目的服务器

        # 创建一个实例化
        jumpbox_ssh = paramiko.SSHClient()
        jumpbox_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        jumpbox_ssh.connect(hostname=jumpbox_host_ip, port=5088, username=ssh_user, key_filename=ssh_key_filename)

        jumpbox_transport = jumpbox_ssh.get_transport()
        src_addr = (jumpbox_host_ip, 5088)
        dest_addr = (target_host_ip, 5011)
        jumpbox_channel = jumpbox_transport.open_channel(kind="direct-tcpip", dest_addr=dest_addr, src_addr=src_addr)

        target_ssh = paramiko.SSHClient()
        target_ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        target_ssh.connect(hostname=target_host_ip, port=5011, username=ssh_user, key_filename=ssh_key_filename,
                           sock=jumpbox_channel)

        self.target_ssh = target_ssh
        self.textBrowser = textBrowser  # 保存 textBrowser 供后续更新使用

    def execute(self, cmd):
        # 在执行命令前，先激活 conda 环境
        conda_activate_cmd = "source ~/miniconda3/etc/profile.d/conda.sh && conda activate pimtorch && " + cmd
        stdin, stdout, stderr = self.target_ssh.exec_command(conda_activate_cmd)

        # 获取标准输出和标准错误
        stdout_data = stdout.read().decode('utf-8')  # 远程命令的标准输出
        stderr_data = stderr.read().decode('utf-8')  # 远程命令的标准错误输出

        # 输出标准输出和标准错误
        print("标准输出：")
        print(stdout_data)

        if stderr_data:
            print("标准错误：")
            print(stderr_data)

    def execute_real_time(self, cmd):
        # 实时执行命令并读取输出
        conda_activate_cmd = "source ~/miniconda3/etc/profile.d/conda.sh && conda activate pimtorch && " + cmd
        stdin, stdout, stderr = self.target_ssh.exec_command(conda_activate_cmd)

        # 实时读取输出并更新文本框
        while True:
            output = stdout.readline()
            if output == '' and stdout.channel.exit_status_ready():
                break
            if output:
                self.update_output(output)

        # 获取错误输出并处理
        stderr_data = stderr.read().decode('utf-8')
        if stderr_data:
            self.update_output(stderr_data)

    def update_output(self, output):
        # 更新界面上的 QTextBrowser 内容
        QtWidgets.QApplication.processEvents()  # 更新GUI
        self.textBrowser.append(output)  # 将输出添加到 textBrowser
        self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())  # 滚动到底部

    def close(self):
        self.target_ssh.close()
