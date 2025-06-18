from lru import LRUCache


def test_lru():
    cache = LRUCache(2)

    cache.put(1, 100)      # cache = {1=100}
    cache.put(2, 200)      # cache = {1=100, 2=200}
    print(cache.get(1))    # returns 100 (1 becomes most recently used)
    assert cache.get(1) == 100

    cache.put(3, 300)      # evicts key 2; cache = {1=100, 3=300}
    print(cache.get(2))    # returns -1 (2 was evicted)
    assert cache.get(2) == -1

    print(cache.get(3))    # returns 300
    assert cache.get(3) == 300

    print(cache.get(1))    # returns 100
    assert cache.get(1) == 100


    cache.put(4, 400)      # evicts key 3; cache = {1=100, 4=400}
    print(cache.get(3))    # returns -1
    assert cache.get(3) == -1

    print(cache.get(4))    # returns 400
    assert cache.get(4) == 400
    print(cache.get(1))    # returns 100
    assert cache.get(1) == 100


    # Overwrite an existing key
    cache.put(1, 111)      # updates value; 1 is most recently used
    print(cache.get(1))    # returns 111
    assert cache.get(1) == 111

    # Re-eviction
    cache.put(5, 500)      # evicts key 4; cache = {1=111, 5=500}
    print(cache.get(4))    # returns -1
    assert cache.get(4) == -1
    print(cache.get(5))    # returns 500
    assert cache.get(5) == 500

    print(cache.get(1))    # returns 111
    assert cache.get(1) == 111
