import queue
import numpy as np
import LoadBalancer


class Server:
    def __init__(self, queue_size, mu):
        self.queue = queue.Queue()
        self.max_size = queue_size
        self.proc_rate = 1 / mu
        self.is_working = False
        self.failed = 0
        self.packets_processed = 0
        self.total_waiting_time = 0
        self.total_process_time = 0
        self.last_processed = 0

    # def to enter
    def handle_packet(self, time_received, load_balancer):
        if self.queue.empty() and not self.is_working:
            self.total_waiting_time += LoadBalancer.Time() - time_received
            rate = np.random.exponential(scale=self.proc_rate)
            self.total_process_time += rate
            self.is_working = True
            load_balancer.s.enter(rate, 1, self.switch_packet, argument=(load_balancer,))
        elif self.queue.qsize() < self.max_size:
            self.queue.put(time_received)
        else:
            self.failed += 1

    def switch_packet(self, load_balancer: LoadBalancer):
        self.packets_processed += 1
        self.last_processed = LoadBalancer.Time()
        if not self.queue.empty():
            # TODO: if doesn't perform change to constant
            rate = np.random.exponential(scale=self.proc_rate)
            curPacketTime = self.queue.get()
            self.total_waiting_time += LoadBalancer.Time() - curPacketTime
            self.is_working = True
            self.total_process_time += rate
            load_balancer.s.enter(rate, 1, self.switch_packet, argument=(load_balancer,))
        else:
            self.is_working = False

