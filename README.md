# longevity-problem
Problem to be completed during Industry Prep - Interview Prep activity time

## Problem Statement

You are given a data structure containing information about albums that artists have released. It will be an unordered list of tuples, where each tuple will represent a single album. The tuple will have three elements in this order: artist name, album name, and release year. Note that the list is NOT in chronological order.

For example:

```py
[
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
```

The difference in time between Shakira's first released album and last released album is 26 years (1991 to 2017). This is the largest difference of any of the listed artists. Thus, we say that Shakira has the most longevity of any of the listed artists.

Write a function that accepts a list of albums and returns a tuple containing the artist with the most longevity and difference in time between their first and last album.

## Examples

### Example 1
```py
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

longest_career(albums_1)
```
Produces
```py
("Shakira", 26)
```

### Example 2
```py
albums_2 = [
    ("Skylar Kergil", "Tell Me a Story", 2015),
    ("Lil Nas X", "Old Town Road", 2018),
    ("Skylar Kergil", "Thank You", 2013),
    ("Lil Nas X", "Montero", 2021),
]

longest_career(albums_2)
```
Produces
```py
("Lil Nas X", 3)
```

## Notes for the Interviewer

### Clarifying Questions

#### Q: How should I handle invalid input?
A: You can assume the input will be valid.

#### Q: Will there be duplicate albums in the input?
A: No.

#### Q: Will there be any albums released by the same artist in the same year?
A: No.

#### Q: How should I handle empty input? Or an artist with only one album?
A: You can assume the input will be non-empty and each artist will have at least two albums.

### Hints

- If your candidate is struggling to form an algorithm, encourage them to explain how they would do it by hand. Afterwards help them to see what data structures might be useful.

- If your candidate is struggling with a subpart of the problem (e.g. finding the longest span), encourage them to first focus on writing a solution to a simpler version of the problem that does not include those requirements.

- There are other solid approaches to finding the earliest and last album, for example, sorting each persons list of years and selecting the first and last element.