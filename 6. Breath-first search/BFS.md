# Breadth-First Search

A graph models is a set of connections. The graphas are made up of nodes and edges. A node can be directly connected to many other nodes (called neighbors).
This algorith search entire network. 

* Create a queue
* create array to keep the peoplr checked
* While the search queue is not empty run
  * Set the person to the first from the left
  * if person is not in the searched list
    * if person is a seller return true
    * else add neighbors of last person to the queue and add peson to the seached list
