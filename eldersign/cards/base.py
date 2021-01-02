from eldersign.core import Task
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion


the_dreamlands = UnorderedAdventure([
    Task([Skull(), Scroll(), Investigation(3)]),
])

city_of_the_great_race = UnorderedAdventure([
    Task([Investigation(3)]),
    Task([Terror(), Scroll(), Skull()]),
])

the_abyss = UnorderedAdventure([
    Task([Skull(), Terror()]),
    Task([Scroll(), Scroll(), Skull()]),
])

great_hall_of_celeano = UnorderedAdventure([
    Task([Terror()]),
    Task([Scroll()]),
    Task([Investigation(6)]),
])

plateau_of_leng = UnorderedAdventure([
    Task([Scroll(), Terror()]),
    Task([Terror(), Skull(), Terror()]),
])

another_dimension = UnorderedAdventure([
    Task([Scroll(), Investigation(1)]),
    Task([Terror(), Skull()]),
])

yuggoth = UnorderedAdventure([
    Task([Skull(), Terror()]),
    Task([Investigation(8)]),
])

r_lyeh = UnorderedAdventure(
    tasks=[
        Task([Investigation(1), Investigation(1)]),
        Task([Scroll(), Scroll(), Skull(), Terror()]),
    ]
)
