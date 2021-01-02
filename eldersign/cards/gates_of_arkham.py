from eldersign.core import Task
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion


_monster = Task([Skull(), Investigation(1)])

the_psychic_skull = OrderedAdventure([
    Task([Scroll(), Scroll()]),
    Task([Scroll()]),
    Task([Scroll()]),
])

a_play_in_the_park = OrderedAdventure([
    Task([Terror(), Terror(), Scroll()]),
    Task([Terror(), Scroll()]),
])

lost_in_the_brambles = OrderedAdventure([
    Task([Investigation(2), Investigation(2), Terror()]),
    Task([Investigation(2), Skull()]),
])

rats_in_the_walls = UnorderedAdventure([
    Task([Investigation(3)]),
    Task([Investigation(2), Terror(), Terror()]),
])

the_coven = UnorderedAdventure([
    Task([Investigation(8), Terror(), Skull()]),
])

lost_in_the_dark = OrderedAdventure([
    Task([Investigation(1), Terror(), Skull()]),
    Task([Investigation(2), Investigation(2)]),
])

gypsy_curse = UnorderedAdventure([
    Task([Terror()]),
    Task([Scroll()]),
    Task([Scroll(), Scroll()]),
])

run_for_your_life = OrderedAdventure([
    Task([Skull(), Terror(), Scroll()]),
    _monster,
])

prisoner_of_a_madman = UnorderedAdventure([
    Task([Skull()]),
    Task([Investigation(5), Terror()]),
])

booth_in_the_back = UnorderedAdventure([
    Task([Investigation(3)]),
    Task([Scroll()]),
    Task([Scroll(), Terror()]),
])

alien_dissection = OrderedAdventure([
    Task([Terror()]),
    Task([Investigation(2)]),
    Task([Investigation(3), SymbolUnion([Scroll(), Skull()])]),
])

chants_and_incantations = OrderedAdventure([
    Task([Investigation(3)]),
    Task([Scroll(), Scroll()]),
    Task([Terror(), ], membership='silver_twilight'),
])

standing_stones = UnorderedAdventure([
    # Monster slot, silver_twilight
    Task([Investigation(3), Scroll(), Terror()]),
])

initiation_into_the_mysteries = OrderedAdventure([
    Task([Investigation(3), Scroll()]),
    Task([Investigation(2)]),
    Task([Investigation(1), ], membership='silver_twilight'),
])

late_night_visitor = UnorderedAdventure([
    Task([Terror()]),
    Task([Terror(), Skull()]),
    Task([Skull(), ], membership='sheldon_gang'),
])

the_lecture = OrderedAdventure([
    Task([Investigation(3)]),
    Task([Scroll()]),
    Task([Investigation(4)]),
])

death_at_the_docks = UnorderedAdventure([
    Task([Investigation(3), Terror()], membership='sheldon_gang'),
    Task([Scroll(), Skull()]),
])

private_meetings = UnorderedAdventure([
    # Task([Investigation(2)], membership='silver_twilight'),
    Task([Investigation (3), Scroll(), Scroll()]),
])

ink_blots = UnorderedAdventure([
    Task([Investigation(1)]),
    Task([Investigation(2)]),
    Task([Terror()]),
])

ramblings_of_the_mad = UnorderedAdventure([
    Task([Investigation(1)]),
    Task([Investigation(2), Scroll()]),
])

psychiatric_assistance = UnorderedAdventure([
    Task([Investigation(1), Investigation(2)]),
    Task([Investigation(3)]),
])

prayers_for_the_lost = UnorderedAdventure([
    Task([Investigation(1)]),
    Task([Investigation(1)]),
    Task([Investigation(1), Investigation(2)]),
])

last_words = UnorderedAdventure([
    Task([Investigation(2)]),
    Task([Investigation(2)]),
    Task([Investigation(3)]),
])

gruesome_autopsy = OrderedAdventure([
    Task([Investigation(1), SymbolUnion([Terror(), Skull()])]),
    _monster,  # Simulating a monster
])

pursuing_leads = UnorderedAdventure([
    Task([Investigation(1)]),
    Task([Investigation(2)]),
    Task([Investigation(3)]),
])

dark_dealings = UnorderedAdventure([
    Task([Skull()], membership='sheldon_gang'),
    Task([Investigation(3), Investigation(3), Scroll()]),
])

founders_rock = UnorderedAdventure([
    Task([Investigation(3)], membership='silver_twilight'),
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

