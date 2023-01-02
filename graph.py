import matplotlib.pyplot as plt
import numpy as np
import LoadBalancer

t_l = [10, 100, 500, 1000, 2000, 2500]
times_list = np.array(t_l)
wait_times = np.zeros(6, dtype=float)
avg_wait_time = 0

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

for i in range(len(times_list)):
    for _ in range(10):
        total_time = times_list[i]
        load_balancer = LoadBalancer.LoadBalancer(total_time, num_of_servers, probs, lamb,
                                     queue_sizes, queue_mus)
        load_balancer.run()
        # print(load_balancer.get_wait_time())
        avg_wait_time += load_balancer.get_wait_time()
    avg_wait_time = avg_wait_time / 10
    print(f"Time: {times_list[i]}, wait time: {avg_wait_time}")
    wait_times[i] = avg_wait_time
    avg_wait_time = 0

plt.plot(times_list, wait_times)
plt.show()
