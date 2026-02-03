```python
# Example
def chat_task(ctx, pipe, n, group):  # function name is chat_task
```
```python
def get_peer_node(username): # function name is get_peer_node
```
```python
def join_group(node, group): # function name is join_group
```
```python
def get_channel(node, group): # function name is get_channel
```

```shell    
# Example
ctx: This is a ZeroMQ Connection Context
pipe: This is a communications pipe polled by ZeroMQ for messages.
n: This is the peer to peer node my chat app is connected as
group: This is the peer chat group I wanted to join
# Example
The chat_task method does not return anything, it appears to be the send/recieve manager.
```
```shell    
username: Didn't catch the answer, proff keeps switching tabs. 
The get_peer_node method returns the node. 
```
```shell
node: 
group: 
The join_group method does not return anything, it is the comand that allows you to join or create a group. 
```
```shell
node: 
group: 
The get_channel method returns zhelper.zthread_fork(ctx, chat_task, n=node, group=group)
```


