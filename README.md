# WynnSorceryMajorID
Ported to GitHub. Created August 4th 2022.

Proving the average number of free-casts provided by Major Identification roll called Sorcery with simulation and taylor series.

In Wynncraft, there is a Major Identification called Sorcery such that upon casting any spell, there is a 30% chance to cast another spell. A spell casted for free by Sorcery can proc Sorcery again and again, infinitely if that lucky.

The goal is to determine, on average, how many total casts per manual cast the user gets when using Sorcery.

This was solved by Simulation, and Taylor series.

Taylor series: .3**0 + .3**1 + .3**2 + .3**3 + .3**4 + .3**5 + .3**6 + .3**7 = ~1.428 casts per cast
