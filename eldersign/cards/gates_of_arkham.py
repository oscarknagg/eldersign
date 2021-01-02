from eldersign.core import Task
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion


_monster = Task([Skull(), Investigation(1)])

the_psychic_skull = OrderedAdventure(
    tasks=[
        Task([Scroll(), Scroll()]),
        Task([Scroll()]),
        Task([Scroll()]),
    ],
    trophy_value=2,
)

a_play_in_the_park = OrderedAdventure(
    tasks=[
        Task([Terror(), Terror(), Scroll()]),
        Task([Terror(), Scroll()]),
    ],
    trophy_value=2,
    event=True
)

lost_in_the_brambles = OrderedAdventure(
    tasks=[
        Task([Investigation(2), Investigation(2), Terror()]),
        Task([Investigation(2), Skull()]),
    ],
    trophy_value=2,
)

rats_in_the_walls = UnorderedAdventure(
    tasks=[
        Task([Investigation(3)]),
        Task([Investigation(2), Terror(), Terror()]),
    ],
    trophy_value=2,
)

the_coven = UnorderedAdventure(
    tasks=[
        Task([Investigation(8), Terror(), Skull()]),
    ],
    trophy_value=2,
)

lost_in_the_dark = OrderedAdventure(
    tasks=[
        Task([Investigation(1), Terror(), Skull()]),
        Task([Investigation(2), Investigation(2)]),
    ],
    trophy_value=2,
)

gypsy_curse = UnorderedAdventure(
    tasks=[
        Task([Terror()]),
        Task([Scroll()]),
        Task([Scroll(), Scroll()]),
    ],
    trophy_value=2,
    event=True
)

run_for_your_life = OrderedAdventure(
    tasks=[
        Task([Skull(), Terror(), Scroll()]),
        _monster,
    ],
    trophy_value=2,
)

prisoner_of_a_madman = UnorderedAdventure(
    tasks=[
        Task([Skull()]),
        Task([Investigation(5), Terror()]),
    ],
    trophy_value=2,
)

booth_in_the_back = UnorderedAdventure(
    tasks=[
        Task([Investigation(3)]),
        Task([Scroll()]),
        Task([Scroll(), Terror()]),
    ],
    trophy_value=2
)

alien_dissection = OrderedAdventure(
    tasks=[
        Task([Terror()]),
        Task([Investigation(2)]),
        Task([Investigation(3), SymbolUnion([Scroll(), Skull()])]),
    ],
    trophy_value=2,
    event=True
)

chants_and_incantations = OrderedAdventure(
    tasks=[
        Task([Investigation(3)]),
        Task([Scroll(), Scroll()]),
        Task([Terror(), ], membership='silver_twilight'),
    ],
    trophy_value=2,
    event=True
)

standing_stones = UnorderedAdventure(
    tasks=[
        # Monster slot, silver_twilight
        Task([Investigation(3), Scroll(), Terror()]),
    ],
    trophy_value=1
)

initiation_into_the_mysteries = OrderedAdventure(
    tasks=[
        Task([Investigation(3), Scroll()]),
        Task([Investigation(2)]),
        Task([Investigation(1), ], membership='silver_twilight'),
    ],
    trophy_value=2
)

late_night_visitor = UnorderedAdventure(
    tasks=[
        Task([Terror()]),
        Task([Terror(), Skull()]),
        Task([Skull(), ], membership='sheldon_gang'),
    ],
    trophy_value=2,
    event=True
)

the_lecture = OrderedAdventure(
    tasks=[
        Task([Investigation(3)]),
        Task([Scroll()]),
        Task([Investigation(4)]),
    ],
    trophy_value=1
)

death_at_the_docks = UnorderedAdventure(
    tasks=[
        Task([Investigation(3), Terror()], membership='sheldon_gang'),
        Task([Scroll(), Skull()]),
    ],
    trophy_value=1,
    event=True
)

private_meetings = UnorderedAdventure(
    tasks=[
        Task([Investigation(2)], membership='silver_twilight'),
        Task([Investigation(3), Scroll(), Scroll()]),
    ],
    trophy_value=2
)

ink_blots = UnorderedAdventure(
    tasks=[
        Task([Investigation(1)]),
        Task([Investigation(2)]),
        Task([Terror()]),
    ],
    trophy_value=1
)

ramblings_of_the_mad = UnorderedAdventure(
    tasks=[
        Task([Investigation(1)]),
        Task([Investigation(2), Scroll()]),
    ],
    trophy_value=1
)

psychiatric_assistance = UnorderedAdventure(
    tasks=[
        Task([Investigation(1), Investigation(2)]),
        Task([Investigation(3)]),
    ],
    trophy_value=1
)

prayers_for_the_lost = UnorderedAdventure(
    tasks=[
        Task([Investigation(1)]),
        Task([Investigation(1)]),
        Task([Investigation(1), Investigation(2)]),
    ],
    trophy_value=1
)

last_words = UnorderedAdventure(
    tasks=[
        Task([Investigation(2)]),
        Task([Investigation(2)]),
        Task([Investigation(3)]),
    ],
    trophy_value=1
)

gruesome_autopsy = OrderedAdventure(
    tasks=[
        Task([Investigation(1), SymbolUnion([Terror(), Skull()])]),
        _monster,  # Simulating a monster
    ],
    trophy_value=1
)

pursuing_leads = UnorderedAdventure(
    tasks=[
        Task([Investigation(1)]),
        Task([Investigation(2)]),
        Task([Investigation(3)]),
    ],
    trophy_value=1,
    event=True
)

registration_day = UnorderedAdventure(
    tasks=[
        Task([Investigation(2)]),
        Task([Investigation(3)]),
    ],
    trophy_value=1
)

cryptic_messages = UnorderedAdventure(
    tasks=[
        Task([Investigation(1)]),
        Task([Investigation(4), Scroll()]),
    ],
    trophy_value=1
)

the_dean = UnorderedAdventure(
    tasks=[
        Task([Investigation(2), Scroll(), Scroll()]),
    ],
    trophy_value=2
)

dark_dealings = UnorderedAdventure(
    tasks=[
        Task([Skull()], membership='sheldon_gang'),
        Task([Investigation(3), Investigation(3), Scroll()]),
    ],
    trophy_value=2
)

founders_rock = UnorderedAdventure(
    tasks=[
        Task([Investigation(3)], membership='silver_twilight'),
        Task([Investigation(5), Terror()]),
        Task([Scroll(), Terror()]),
    ],
    trophy_value=3,
    event=True
)


# Other worlds
unknown_kadath = OrderedAdventure(
    tasks=[
        Task([Terror(), SymbolUnion([Terror(), Skull()])]),
        Task([Terror(), Terror()]),
        Task([Scroll(), SymbolUnion([Terror(), Scroll()])]),
    ],
    trophy_value=3
)

city_of_gugs = UnorderedAdventure(
    tasks=[
        Task([Investigation(3), Investigation(3), Skull()]),
        Task([Skull(), Skull(), Terror()]),
    ],
    trophy_value=3
)

the_great_temple = UnorderedAdventure(
    tasks=[
        Task([Skull(), Skull()]),
        Task([Skull(), Skull(), SymbolUnion([Terror(), Skull()])]),
    ],
    trophy_value=2
)

ancient_sarnath = UnorderedAdventure(
    tasks=[
        Task([Investigation(4), Terror()]),
        Task([Investigation(3), Terror(), Scroll()]),
    ],
    trophy_value=3
)

far_side_of_the_moon = UnorderedAdventure(
    tasks=[
        Task([Investigation(6)]),
        Task([Investigation(6), Scroll()]),
    ],
    trophy_value=2,
    event=True
)

the_vaults_of_zin = UnorderedAdventure(
    tasks=[
        Task([Scroll()]),
        Task([Skull(), Terror(), Terror()]),
    ],
    trophy_value=3,
    event=True
)

lost_in_time_and_space = UnorderedAdventure(
    tasks=[
        Task([Investigation(5)]),
        Task([Investigation(3), Terror()]),
    ],
    trophy_value=2,
    event=True
)

ancient_egypt = UnorderedAdventure(
    tasks=[
        Task([Investigation(3), Scroll()]),
        Task([Investigation(4), Scroll()]),
    ],
    trophy_value=2,
    event=True
)

