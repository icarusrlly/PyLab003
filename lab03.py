import lab_chat as lc

def get_group():
   return get_input_upper("Enter your group: ")

def get_input(mesg):
    str_in = input(mesg)
    return str_in.strip()

def get_input_upper(mesg):
    return get_input(mesg).upper()

def get_message():
    return get_input("Enter your message: ")

def get_username():
    return get_input_upper("Enter your username: ")

# print(get_username())
# print(get_group())
# print(get_message())

def initialize_chat():
    user_name = get_username()
    group = get_group()
    node = lc.get_peer_node(user_name)
    lc.join_group(node, group)
    return lc.get_channel(node, group)

def start_chat():
    channel = initialize_chat()

    while True:
        try:
            msg = get_message()
            channel.send(msg.encode('utf_8'))
        except (KeyboardInterrupt, SystemExit):
            break
    channel.send("$$STOP".encode('utf_8'))
    print("FINISHED")

start_chat()








