import serial
import threading

class SerialThread:
    """
    串口通信线程，包含读线程和写线程
    """
    def __init__(self, port, baudrate=9600, parity=None, bytesize=8, stopbits=1, timeout=1):
        self.my_serial = serial.Serial()
        self.my_serial.port = port              # 端口号
        self.my_serial.baudrate = baudrate      # 波特率
        self.my_serial.bytesize = bytesize      # 数据位
        self.my_serial.stopbits = stopbits      # 停止位
        self.my_serial.timeout = timeout

        self.alive = False                      # 当 alive 为 True，读写线程会进行
        self.wait_end = None                    # 用来控制主线程
        self.thread_read = None                 # 读线程
        self.thread_write = None                # 写线程

    def start(self):
        self.my_serial.open()
        if self.my_serial.isOpen():
            self.alive = True
            self.wait_end = threading.Event()

            self.thread_read = threading.Thread(target=self.read)
            self.thread_read.setDaemon(True)                        # 当主线程结束，读线程和主线程一并退出

            self.thread_write = threading.Thread(target=self.write)
            self.thread_write.setDaemon(True)                       # 当主线程结束，读线程和主线程一并退出

            self.thread_read.start()
            self.thread_write.start()

            return True

        else:
            return False

    def wait(self):
        if not self.wait_end is None:
            self.wait_end.wait()            # 阻塞主线程

    def stop(self):
        self.alive = False
        if self.my_serial.isOpen():
            self.my_serial.close()


    def read(self):
        while self.alive:
            try:
                n = self.my_serial.inWaiting()                       # 返回接收缓存中的字节数
                if n:
                    data = self.my_serial.read(n).decode("gbk")     # 解码成 gbk 码（处理中文字符问题）
                    if len(data) == 1 and ord(data[-1]) == 113:     # 当接收到“q”时，线程结束
                        break
                    print(data)
            except Exception as ex:
                print(ex)


        self.wait_end.set()
        self.alive = False

    def write(self):
        while self.alive:
            try:
                receive = input()
                self.my_serial.write(receive.encode("gbk"))     # 解码成 gbk 码（处理中文字符问题）
            except Exception as ex:
                print(ex)

        self.wait_end.set()
        self.alive = False

if __name__ == "__main__":
    my_serial = SerialThread("COM1")

    if my_serial.start():
        my_serial.wait()
        my_serial.stop()

    if my_serial.alive == True:
        my_serial.stop()

    print("END")

    del my_serial


