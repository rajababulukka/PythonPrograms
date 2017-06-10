def movies(flight_lengths, movie_lengths):
    lengths={}

    for length in movie_lengths:
        for movie in range(int(len(movie_lengths)/2)):
            print(movie_lengths[movie])

            if (movie_lengths[movie] + length == flight_lengths) and (movie_lengths[movie]!=length):
                lengths.append(movie_lengths[movie],length)
            else:
                continue
            print(lengths)
        
        if lengths:
            return True
        else:
            return False


flight_length = 180
movie_lengths = [60,30,60,120]
print(movies(flight_length,movie_lengths))
