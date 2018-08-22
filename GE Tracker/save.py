import pickle

def save(watchingItemsPrice):
    output_file = ('save.bin')
    with open(output_file, 'wb') as output:
        pickle.dump(watchingItemsPrice, output)

def load():
    watchingItemsPrice = []
    input_file = 'save.bin'
    try:
        with open(input_file, 'rb') as input:
            watchingItemsPrice = pickle.load(input)
    except:
        print('something went wrong loading items')
    return watchingItemsPrice
