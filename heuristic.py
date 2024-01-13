def heuristic(key_heuristic, new_cost, distance, energy, charge_time, neighbor):
    idx = step_map.get(neighbor)
    distance_need = sum(step['distance'] / 1000 for step in steps[idx:])
    if key_heuristic == 1:
        return distance + distance_need  # khoảng cách
    if key_heuristic == 2:
        return energy + distance_need * 0.3  # năng lượng tiêu thụ
    if key_heuristic == 3:
        return charge_time + distance_need / 40 * 60  # thời gian sạc
    return new_cost + distance_need / 40 * 60  # thời gian



def find_router1(key_heuristic):
    G = nx.MultiDiGraph()
    # inti edge
    # init search
    start_node = 0
    end_node = 1
    pq = [(0, 0, 0, 0, start_node, [start_node])]
    while pq:
        cost_h, cost, charge_time, distance_result, energy, current_node, path = (
            heapq.heappop(pq))
        if current_node == end_node:
            if current_soc >= SOC_MIN_GOAL:
                print(f"Found path: {path}")
                break
            else:
                continue

        for u, neighbor, data in G.out_edges(current_node, data=True):
            if charging:
                print()
            else:
                print()
            
            heapq.heappush(pq, (
                heuristic(key_heuristic,
                          cost + current_cost,
                          distance_result + current_distance,
                          energy + current_energy,
                          charge_time + current_charge_time,
                          neighbor),
                cost + current_cost, 
                distance_result + current_distance,
                energy + current_energy,
                charge_time + current_charge_time,
                neighbor, 
                path + [neighbor])

