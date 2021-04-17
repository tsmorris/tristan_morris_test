import redis

#Using redis since it's pretty fast at read/writes and it's got a nice python library so why not



class ClientNode(object):
    #Node to be deployed at each geo-location
    #Maintains its own cache and communicates with the network to retrieve data and maintain consistency

    def __init__(self, expiry):
        #Connect to local redis server
        self.cache = redis.Redis()
        #set expiry time to desired value
        self.expiry = expiry


    def __get_data(key):
        #function to get data that doesn't exist in the cache
        #retrieves it from the network
        #since we don't know what data is where, it should send out the request to the network as a whole
        #and wait for the first response, which should automatically be the nearest with the requested data,
        #due to the latency of the request/response
        pass

    def __send_data(key, value):
        #function to send data back to the network
        pass


    def get_data(self, key):
        #function to get data
        if self.cache.exists(key):
            #if it's in the cache, reset the expiry and return the value
            self.cache.expire(key, self.expiry)
            return self.cache.get(key)
        else:
            #if it's not in the cache, get it from the nearest location, add to cache, then return it
            data = __get_data(key)
            self.cache.setex(key, self.expiry, data)
            return data

    def add_data(self, key, value):
        #add new data to the network
        #add to local cache as well as propogating across the network for consistency
        self.cache.setex(key, self.expiry, value)
        __send_data(key, value)

class ServerNode(object):
    #Node to be deployed at the server level

    def __init__(self):
        pass

    def send_data(key, node):
        #function to send data associated with the key to the specified client node
        pass

    def add_data(key, value):
        #function to add new data to the network, setting the value of a key to the given value
        pass

    def watcher():
        #function to wait around for something to happen, at which point
        #the server will respond with one of its other methods
        pass



