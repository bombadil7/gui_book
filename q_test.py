from queue import Queue

def useQueues():
    guiQueue = Queue()
    print(guiQueue)
    for idx in range(10):
        guiQueue.put('Message from a queue' + str(idx))
    guiQueue.put(None)

    for m in iter(guiQueue.get, None):
        print(m)

useQueues()
