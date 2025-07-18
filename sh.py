from PyQt5 import QtCore, QtGui, QtWidgets
import paramiko, os
import threading

class Ui_Sh(object):
    def setupUi(self, Form, parameter=None):
        Form.setObjectName("Form")
        Form.setStyleSheet("background-color: #f5f5f5;")  # 设置背景色为浅灰色
        ui_width = 2000
        ui_height = 1000
        Form.resize(ui_width, ui_height)
        Form.setMinimumSize(QtCore.QSize(ui_width, ui_height))
        Form.setMaximumSize(QtCore.QSize(ui_width, ui_height))

        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(30, 10, ui_width-60, 40))
        self.label.setObjectName("label")
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(12)  # 增加标题字体大小
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet("color: #333333;")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setGeometry(QtCore.QRect(30, 60, ui_width-60, ui_height-120))
        self.textBrowser.setObjectName("textBrowser")
        
        self.testname = {
            2:"Binary FC-3算法识别准确率",
            # 3:"RRAM芯片 能效测试",
            4:"<font color='orange'>MRAM</font>芯片 容量测试",
            # 5:"MRAM芯片 1-8bit位宽乘加计算测试",
            # 6:"MRAM芯片 算力测试",
            # 7:"MRAM芯片 单阵列核心计算能效测试",
            # 8:"MRAM芯片 全芯片处理能效测试",
            # 9:"MRAM芯片 与GPU的能效对比测试",
            10:"<font color='blue'>RRAM</font>芯片 算力测试",
            11:"<font color='blue'>RRAM</font>芯片 1、8、16bit位宽乘加计算测试",
            12:"<font color='blue'>RRAM</font>芯片 容量测试",
            13:"Binary LeNet-5算法识别准确率",
            14:"Naive Bayes算法识别准确率",
        }

        self.parameter = parameter
        self.process = QtCore.QProcess(self)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        # 根据传入的参数来执行逻辑
        if self.parameter:
            self.run_stuff(self.parameter)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "脚本运行窗口"))
        self.label.setText(_translate("Form", f"当前正在运行{self.testname.get(self.parameter, None)}"))

    def run_stuff(self, parameter):
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
            #self.executable = "/home/zhaoyuhang/work_space/BYO-PiM/GUI/bin/TOPSTest"# 算力
            self.executable = "/home/luhongye/workspaces/software/GUI/bin/TOPSTest"
        elif parameter == 11:
            #self.executable = "/home/zhaoyuhang/work_space/BYO-PiM/GUI/bin/computeCorrectnessTest"# 乘加计算
            self.executable = "/home/luhongye/workspaces/software/GUI/bin/computeCorrectnessTest"
        elif parameter == 12:
            #self.executable = "/home/zhaoyuhang/work_space/BYO-PiM/GUI/bin/allRRAMTest"# 容量
            self.executable = "/home/luhongye/workspaces/software/GUI/bin/allRRAMTest"
        else:
            return
        
        self.process = QtCore.QProcess(self)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        print(self.executable)
        self.process.start("sudo",[self.executable])

    def run_script(self, parameter):
        if self.process:
            if self.process.state() == QtCore.QProcess.Running:
                self.kill_process()

        scripts_dic = {
            4: "/home/dengyao/workspace/cpp/MRAM_Driver/test/mram_test.py",# 容量
            5: "test.py",# 乘加计算
            6: "",# 算力
            7: "",# 单阵列核心计算能效
            8: "",# 全芯片处理能效
            9: "",# 与GPU能效对比
        }
        script = scripts_dic.get(parameter, None)
        if not script:
            return
        self.process = QtCore.QProcess(self)
        self.process.setProcessChannelMode(QtCore.QProcess.MergedChannels)
        self.process.readyReadStandardOutput.connect(self.on_readyReadStandardOutput)
        self.process.finished.connect(self.on_finished)
        self.process.start("sudo", ["/usr/bin/python3.8", script])# 使用对应环境的python
        if not self.process.waitForStarted():
            print("Error: Fail to start!")

    def on_readyReadStandardOutput(self):
        if self.process == None:
            return
        output = self.process.readAllStandardOutput().data().decode()
        self.textBrowser.append(output)  # 实时更新textBrowser

    def on_finished(self):
        self.textBrowser.append('<span style = "color: green; font-weight: bold;">The subprocess has completed. You may exit now</span>')
    
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
                self.kill_process()
        if self.parameter in [2, 13, 14]:
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
