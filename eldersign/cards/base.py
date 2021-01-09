from eldersign.core import Task
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion
from eldersign import effect
from eldersign import item


haunted_by_a_shadowy_figure = UnorderedAdventure(
    name='Haunted by a Shadowy Figure',
    tasks=[
        Task([Skull()]),
        Task([Scroll(), Investigation(6)]),
    ],
    trophy_value=2,
    terror_effect=effect.MonsterAppears(),
    rewards=[
        effect.MonsterAppears(),
        effect.ItemReward(item.Clue),
        effect.ItemReward(item.UniqueItem),
        effect.ElderSignEffect(1),
    ],
    penalties=[
        effect.SanityEffect(-2)
    ],
)


the_koi_pond = UnorderedAdventure(
    tasks=[
        Task([Terror()]),
        Task([Terror(), Skull(), Skull()]),
    ],
    trophy_value=2,
    terror_effect=effect.ImmediatelyFail()
)

remains_of_the_high_priest = UnorderedAdventure(
    name='Remains of the High Priest',
    tasks=[
        Task([Skull()]),
        Task([Scroll(), Investigation(6)]),
    ],
    trophy_value=1,
    terror_effect=effect.DiscardAllTerrorDice(),
    rewards=[
        effect.ItemReward(item.Clue),
        effect.ItemReward(item.Spell),
    ],
    penalties=[
        effect.HealthEffect(-1)
    ]
)

the_curator = UnorderedAdventure(
    tasks=[
        Task([Scroll(), Scroll(), Scroll()]),
        Task([Scroll(), Investigation(3)]),
    ],
    trophy_value=2
)

blood_on_the_floor = OrderedAdventure(
    tasks=[
        Task([Investigation(2)]),
        Task([Investigation(3)]),
        Task([Terror(), Skull()]),
    ],
    trophy_value=2
)

the_dreamlands = UnorderedAdventure(
    tasks=[
        Task([Skull(), Scroll(), Investigation(3)]),
    ],
    trophy_value=2
)

city_of_the_great_race = UnorderedAdventure(
    tasks=[
        Task([Investigation(3)]),
        Task([Terror(), Scroll(), Skull()]),
    ],
    trophy_value=2
)

the_abyss = UnorderedAdventure(
    tasks=[
        Task([Skull(), Terror()]),
        Task([Scroll(), Scroll(), Skull()]),
    ],
    trophy_value=2
)

great_hall_of_celeano = UnorderedAdventure(
    tasks=[
        Task([Terror()]),
        Task([Scroll()]),
        Task([Investigation(6)]),
    ],
    trophy_value=2
)

plateau_of_leng = UnorderedAdventure(
    tasks=[
        Task([Scroll(), Terror()]),
        Task([Terror(), Skull(), Terror()]),
    ],
    trophy_value=2
)

another_dimension = UnorderedAdventure(
    tasks=[
        Task([Scroll(), Investigation(1)]),
        Task([Terror(), Skull()]),
    ],
    trophy_value=2
)

yuggoth = UnorderedAdventure(
    tasks=[
        Task([Skull(), Terror()]),
        Task([Investigation(8)]),
    ],
    trophy_value=2
)

r_lyeh = UnorderedAdventure(
    tasks=[
        Task([Investigation(1), Investigation(1)]),
        Task([Scroll(), Scroll(), Skull(), Terror()]),
    ],
    trophy_value=2
)
