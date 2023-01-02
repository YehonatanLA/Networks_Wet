import sched
import sys
import Server
import LoadBalancer


#
# def main():
#     print("hello")
#     s = sched.scheduler(Time, zero)
#     s.enterabs(10, 1, printer, argument=("first",))
#     s.enterabs(3, 2, printer, argument=("second",))
#     s.run()


def main():
    # total_time = int(sys.argv[1])
    total_time = 2500  # 5000
    # num_of_servers = int(sys.argv[2])
    num_of_servers = 1  # 2
    # probs = [float(sys.argv[3 + i]) for i in range(num_of_servers)]
    probs = [1]  # [0.2, 0.8]
    # lamb = int(sys.argv[3 + num_of_servers])
    lamb = 9  # 200
    # queue_sizes = [int(sys.argv[4 + num_of_servers + i]) for i in range(num_of_servers)]
    queue_sizes = [5]  # [2, 10]
    # queue_mus = [int(sys.argv[4 + 2 * num_of_servers + i]) for i in range(num_of_servers)]
    queue_mus = [12]  # [20, 190]
    load_balancer = LoadBalancer.LoadBalancer(total_time, num_of_servers, probs, lamb,
                                              queue_sizes, queue_mus)
    load_balancer.run()
    load_balancer.print_data()


if __name__ == "__main__":
    main()
