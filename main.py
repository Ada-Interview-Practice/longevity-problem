def longest_career(albums):
    # Dictionary to summarize artist info
    # Key will be name of artist
    # Value will be 2 element list containing the earliest and last year
    # e.g. {"Shakira": [1991, 2017]}
    artist_spans = {}

    # Iterate over each album, unpacking the needed values
    for artist, _, year in albums:
        # if this is the first time we've seen the artist
        if artist not in artist_spans:
            # The first seen album starts off as both min and max
            artist_spans[artist] = [year, year]
        # if we have seen the artist before
        else:
            # Find the earliest and latest release for the arist so far
            prev_min = artist_spans[artist][0]
            prev_max = artist_spans[artist][1]

            # Update the min or max if the new year is higher or lower
            if year < prev_min:
                artist_spans[artist][0] = year
            if year > prev_max:
                artist_spans[artist][1] = year

    best_artist = None
    best_duration = None
    for artist, span in artist_spans.items():
        # Duration is latest year minus earliest year
        duration = span[1] - span[0]
        # If this is the longest duration we've seen
        if best_duration is None or duration > best_duration:
            # Update the best seen
            best_duration = duration
            best_artist = artist
    
    return (best_artist, best_duration)


# Test cases
albums_1 = [
    ("Rodrigo y Gabriela", "9 Dead Alive", 2014),
    ("Shakira", "El Dorado", 2017),
    ("Janelle Monáe", "The ArchAndroid", 2010),
    ("Shakira", "Magia", 1991),
    ("Shakira", "She Wolf", 2009),
    ("Rodrigo y Gabriela", "11:11", 2009),
    ("Rodrigo y Gabriela", "Rodrigo y Gabriela", 2006),
    ("Rodrigo y Gabriela", "Mettavolution", 2019),
    ("Janelle Monáe", "Dirty Computer", 2018)
]
assert longest_career(albums_1) == ("Shakira", 26)


albums_2 = [
    ("Skylar Kergil", "Tell Me a Story", 2015),
    ("Lil Nas X", "Old Town Road", 2018),
    ("Skylar Kergil", "Thank You", 2013),
    ("Lil Nas X", "Montero", 2021),
]
assert longest_career(albums_2) == ("Lil Nas X", 3)

print("All test cases passed!")
print("Finished early? Discuss time & space complexity")
