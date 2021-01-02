from eldersign.core import Task
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion


prisoner_of_a_madman = UnorderedAdventure([
    Task([Skull()]),
    Task([Investigation(5), Terror()]),
])

dark_dealings = UnorderedAdventure([
    Task([Skull()]),
    Task([Investigation(3), Investigation(3), Scroll()]),
])

founders_rock = UnorderedAdventure([
    Task([Investigation(3)]),
    Task([Investigation(5), Terror()]),
    Task([Scroll(), Terror()]),
])

the_dean = UnorderedAdventure([
    Task([Investigation(2), Scroll(), Scroll()]),
])

cryptic_messages = UnorderedAdventure([
    Task([Investigation(1)]),
    Task([Investigation(4), Scroll()]),
])

# Other worlds
unknown_kadath = OrderedAdventure(
    tasks=[
        Task([Terror(), SymbolUnion([Terror(), Skull()])]),
        Task([Terror(), Terror()]),
        Task([Scroll(), SymbolUnion([Terror(), Scroll()])]),
    ]
)

city_of_gugs = UnorderedAdventure(
    tasks=[
        Task([Investigation(3), Investigation(3), Skull()]),
        Task([Skull(), Skull(), Terror()]),
    ]
)

the_great_temple = UnorderedAdventure(
    tasks=[
        Task([Skull(), Skull()]),
        Task([Skull(), Skull(), SymbolUnion([Terror(), Skull()])]),
    ]
)

ancient_sarnath = UnorderedAdventure(
    tasks=[
        Task([Investigation(4), Terror()]),
        Task([Investigation(3), Terror(), Scroll()]),
    ]
)

far_side_of_the_moon = UnorderedAdventure(
    tasks=[
        Task([Investigation(6)]),
        Task([Investigation(6), Scroll()]),
    ]
)

the_vaults_of_zin = UnorderedAdventure(
    tasks=[
        Task([Scroll()]),
        Task([Skull(), Terror(), Terror()]),
    ]
)

lost_in_time_and_space = UnorderedAdventure(
    tasks=[
        Task([Investigation(5)]),
        Task([Investigation(3), Terror()]),
    ]
)

ancient_egypt = UnorderedAdventure(
    tasks=[
        Task([Investigation(3), Scroll()]),
        Task([Investigation(4), Scroll()]),
    ]
)

