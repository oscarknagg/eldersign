from eldersign.core import Task, EmptyMonsterTask, HealthCost, SanityCost
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion
from eldersign import effect
from eldersign import item


the_hedge_maze = UnorderedAdventure(
    name="The Hedge Maze",
    tasks=[
        EmptyMonsterTask(),
        EmptyMonsterTask(),
        Task([Skull(), Scroll(), Scroll()]),
    ],
    trophy_value=2,
    at_midnight_effect=effect.EachInvestigator(effect.HealthEffect(-1)),
    rewards=[
        effect.MonsterAppears(),
        effect.MonsterAppears(),
        effect.ElderSignEffect(2),
    ],
    penalties=[
        effect.SanityEffect(-1),
        effect.HealthEffect(-1)
    ],
)

public_lavatory = UnorderedAdventure(
    name="Public Lavatory",
    tasks=[
        EmptyMonsterTask(),
        EmptyMonsterTask(),
        Task([Skull(), Scroll(), Scroll()]),
    ],
    trophy_value=2,
    rewards=[
        effect.MonsterAppears(),
        effect.MonsterAppears(),
        effect.ElderSignEffect(2),
    ],
    penalties=[
        effect.SanityEffect(-1),
        effect.HealthEffect(-1)
    ],
)

forgotten_knowledge = UnorderedAdventure(
    name="Forgotten Knowledge",
    tasks=[
        Task([Scroll()]),
        Task([Terror(), Investigation(8)]),
    ],
    trophy_value=1,
    rewards=[
        effect.ItemReward(item.Spell),
        effect.ItemReward(item.CommonItem),
        effect.ItemReward(item.Spell),
    ],
    penalties=[
        effect.SanityEffect(-1)
    ],
)

the_hall_of_the_dead = UnorderedAdventure(
    name="The Hall of the Dead",
    tasks=[
        Task([Scroll()]),
        Task([Skull(), Skull]),
        Task([Investigation(5)]),
    ],
    trophy_value=1,
    rewards=[
        effect.ItemReward(item.Clue),
        effect.ItemReward(item.CommonItem),
        effect.ItemReward(item.UniqueItem),
    ],
    penalties=[
        effect.HealthEffect(-1)
    ],
)

the_graveyard = UnorderedAdventure(
    name="The Graveyard",
    tasks=[
        Task([Skull()]),
        Task([Terror()]),
        Task([Investigation(7)]),
    ],
    trophy_value=1,
    terror_effect=effect.DiscardAllTerrorDice(),
    rewards=[
        effect.ItemReward(item.CommonItem),
        effect.ItemReward(item.UniqueItem),
        effect.OpenGate(),
    ],
    penalties=[
        effect.SanityEffect(-1)
    ],
)

the_security_office = OrderedAdventure(
    name="The Security Office",
    tasks=[
        Task([Investigation(2)]),
        Task([Investigation(3)]),
        Task([Investigation(6)]),
    ],
    trophy_value=1,
    rewards=[
        effect.ItemReward(item.Ally),
    ],
    penalties=[
        effect.SanityEffect(-2)
    ],
)

transported_by_magic = UnorderedAdventure(
    name="Transported by Magic",
    tasks=[
        Task([Investigation(6)]),
        Task([Scroll(), Scroll()]),
    ],
    trophy_value=2,
    at_midnight_effect=effect.NotImplementedEffect("For each Other World card in play, add 1 doom token to "
                                                   "the doom track"),
    rewards=[
        effect.OpenGate(),
        effect.ItemReward(item.Spell),
        effect.ItemReward(item.Spell),
    ],
    penalties=[
        effect.DoomTokenEffect(1),
        effect.SanityEffect(-1)
    ],
)


when_night_falls = UnorderedAdventure(
    name='When Night Falls',
    tasks=[
        EmptyMonsterTask(),
        Task([Terror()]),
        Task([Skull(), Scroll(), Scroll()]),
    ],
    trophy_value=2,
    terror_effect=effect.MonsterAppears(),
    rewards=[
        effect.ItemReward(item.Clue),
        effect.ItemReward(item.UniqueItem),
        effect.ElderSignEffect(1),
    ],
    penalties=[
        effect.SanityEffect(-2),
        effect.HealthEffect(-2)
    ],
)


the_gift_shop = OrderedAdventure(
    name='The Gift Shop',
    tasks=[
        Task([Investigation(3)]),
        Task([Scroll(), Investigation(3)]),
    ],
    trophy_value=1,
    terror_effect=effect.MonsterAppears(),
    rewards=[
        effect.ItemReward(item.UniqueItem),
    ],
    penalties=[
        effect.SanityEffect(-1)
    ],
)


haunted_by_a_shadowy_figure = UnorderedAdventure(
    name='Haunted by a Shadowy Figure',
    tasks=[
        EmptyMonsterTask(),
        Task([Skull(), Terror()]),
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
