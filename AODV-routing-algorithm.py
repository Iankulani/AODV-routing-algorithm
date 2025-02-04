# -*- coding: utf-8 -*-
"""
Created on Tue Fe 04 07:28:25 2025

@author: IAN CARTER KULANI

"""

import random
import time

# A simple class for representing a node in the FANET
class Node:
    def __init__(self, node_id, position):
        self.node_id = node_id
        self.position = position  # (x, y) coordinates
        self.routing_table = {}  # Stores known routes {destination: (next_hop, hops)}

    def add_route(self, destination, next_hop, hops):
        self.routing_table[destination] = (next_hop, hops)
    
    def delete_route(self, destination):
        if destination in self.routing_table:
            del self.routing_table[destination]
    
    def get_route(self, destination):
        return self.routing_table.get(destination, None)

# A function to simulate the AODV route discovery process
def route_discovery(source, destination, nodes):
    print(f"Node {source.node_id} is trying to discover a route to Node {destination.node_id}.")

    # Simulate broadcasting a Route Request (RREQ)
    visited_nodes = set()
    rreq_queue = [source]
    
    while rreq_queue:
        current_node = rreq_queue.pop(0)
        print(f"Node {current_node.node_id} broadcasting RREQ.")
        
        # Check if we have already visited this node
        if current_node.node_id in visited_nodes:
            continue
        visited_nodes.add(current_node.node_id)

        # Check if current node is the destination
        if current_node.node_id == destination.node_id:
            print(f"Destination Node {destination.node_id} reached!")
            # Route Reply (RREP) would be sent back along the reverse path.
            return f"Route found via Node {current_node.node_id}."
        
        # Propagate RREQ to neighboring nodes (simulated by checking all other nodes)
        for neighbor in nodes:
            if neighbor != current_node and neighbor.node_id not in visited_nodes:
                rreq_queue.append(neighbor)

    return "Route discovery failed. No route found."

# Simulating the FANET routing operation
def main():
    print("FANET Routing Algorithm Simulation (AODV-like)")

    # Number of nodes in the FANET (can be drones or other mobile nodes)
    num_nodes = int(input("Enter the number of nodes in the FANET: "))
    
    # Create the nodes with random positions (x, y)
    nodes = []
    for i in range(num_nodes):
        position = (random.randint(0, 100), random.randint(0, 100))  # Random positions
        nodes.append(Node(i, position))
    
    # Get the source and destination node IDs from the user
    source_id = int(input("Enter the source node ID: "))
    destination_id = int(input("Enter the destination node ID: "))

    # Get the source and destination nodes
    source_node = nodes[source_id]
    destination_node = nodes[destination_id]
    
    # Start the route discovery process
    result = route_discovery(source_node, destination_node, nodes)
    print(result)

if __name__ == "__main__":
    main()
