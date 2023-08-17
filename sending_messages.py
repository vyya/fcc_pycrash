def send_messages(messages, sent_messages):
        while messages:
                outbox = messages.pop()
                sent_messages.append(outbox)
        print(messages)
        print(sent_messages)
            

messages = ['Hi there!', 'Look out!', 'Morning sir', 'Astalavista baby']
sent_messages = []
send_messages(messages[:], sent_messages)
print(messages)
