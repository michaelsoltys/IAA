# Problem 5.13, Page 108 — FIFO-Cache
# Label: exr:belady
# An Introduction to the Analysis of Algorithms (4th Edition)

def FIFO_cache(stream, cache_size):
    """
    Simulates a FIFO cache replacement policy.
    :param stream: sequence of page requests
    :param cache_size: number of slots in the cache
    Each iteration prints out cache information.
    """
    cache = []
    misses = 0
    for item in stream:
        if item not in cache:
            cache.append(item)
            misses += 1
        if len(cache) > cache_size:
            cache.pop(0)
        print(str.format("cache: {},misses: {}", cache, misses))




