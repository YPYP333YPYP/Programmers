def solution(cacheSize, cities):
    answer = 0
    cache = []
    if cacheSize == 0:
        answer = len(cities) * 5
    else:
        for city in cities:
            city = city.lower()
            if city in cache:
                answer+=1
                cache.remove(city)
                cache.append(city)
            else:
                if len(cache) >= cacheSize:
                    cache.pop(0)
                cache.append(city)
                answer+=5

    return answer