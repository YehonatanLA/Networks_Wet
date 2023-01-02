import Server
import sched
import random as rnd
from numpy import random

t = 0


def Time():
    global t
    return t


def inc_time(arg):
    global t
    t += arg


class LoadBalancer:
    def __init__(self, TT, server_num, probs, lamb, queues, mus):
        self.servers = [Server.Server(queues[i], mus[i]) for i in range(server_num)]
        self.server_num = server_num
        self.total_time = TT
        self.rate_of_packages = lamb
        self.server_probs = probs
        self.s = sched.scheduler(Time, inc_time)

    def run(self):
        global t
        temp_time = 0
        while temp_time <= self.total_time:
            server = rnd.choices(self.servers, self.server_probs, k=1)[0]
            time_to_spare = random.exponential(scale=1/self.rate_of_packages)
            self.s.enterabs(temp_time, 1, server.handle_packet, argument=(temp_time, self))
            temp_time += time_to_spare

        self.s.run()
        t = 0

    def print_data(self):
        failed = 0
        packets_processed = 0
        total_waiting_time = 0
        total_proc_time = 0
        last_packet_time = 0

        for server in self.servers:
            failed += server.failed
            packets_processed += server.packets_processed
            total_waiting_time += server.total_waiting_time
            total_proc_time += server.total_process_time

            if last_packet_time < server.last_processed:
                last_packet_time = server.last_processed

        avg_waiting_time = total_waiting_time / packets_processed
        avg_proc_time = total_proc_time / packets_processed
        print(packets_processed, failed, last_packet_time, avg_waiting_time, avg_proc_time)

    def get_wait_time(self):
        failed = 0
        packets_processed = 0
        total_waiting_time = 0
        total_proc_time = 0
        last_packet_time = 0

        for server in self.servers:
            failed += server.failed
            packets_processed += server.packets_processed
            total_waiting_time += server.total_waiting_time
            total_proc_time += server.total_process_time

            if last_packet_time < server.last_processed:
                last_packet_time = server.last_processed

        avg_waiting_time = total_waiting_time / packets_processed
        avg_proc_time = total_proc_time / packets_processed
        print(avg_waiting_time + avg_proc_time)
        return avg_waiting_time + avg_proc_time
