'''
    You've built an inflight entertainment system with on-demand movie streaming.

'''

def flightSystem(fL, mL)-> bool:
    if fL < 2 or len(mL) < 2:
        return False
    
    movie_length = set()
    for movie in mL:
        movieMin = fL - movie
        
        if movieMin in movie_length:
            return True
        movie_length.add(movie)
    return False

print(flightSystem(5, [2, 3, 4, 5]))
 