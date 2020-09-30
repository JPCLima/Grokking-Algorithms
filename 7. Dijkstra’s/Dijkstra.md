# Dijkstra’s

* Find the "cheapest" node. This is the node you can get to in the least amount of time
* Update the costs of the neighbors of the node.
* Repeat until you're done this for every node in the graph
* Calculate the final path


Terminology:
- In Dijkstra’s graphas has a number associated with it, it's calleded weights.
- A graph with weights is called weighted graph.
- A graph with weights is called unweigthed graph.

Code Logic:
* While we have nodes to process
  * Grab the node is closest to the start
  * Update costs for its neighbors
  * If any of the neighbors costs were updated, update the parent too
  * Mark this node processed
