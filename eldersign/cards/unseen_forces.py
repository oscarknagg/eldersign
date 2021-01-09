from eldersign.core import Task, EmptyMonsterTask, HealthCost, SanityCost
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion
from eldersign import effect
from eldersign import item


the_true_history = UnorderedAdventure(
    name="The True History",
    tasks=[
        Task([Investigation(2), Scroll()], [SanityCost(1)]),
        Task([Scroll(), Scroll], [SanityCost(1)]),
    ],
    trophy_value=2,
    rewards=[
        effect.ElderSignEffect(1),
        effect.ItemReward(item.CommonItem),
        effect.ItemReward(item.CommonItem),
        effect.ItemReward(item.Spell),
    ],
    penalties=[
        effect.DoomTokenEffect(1)
    ],
)

visiting_antiquarian = UnorderedAdventure(
    # Lock red and yellow dice
    name="Visiting Antiquarian",
    tasks=[
        Task([Scroll(), Skull()]),
        Task([Scroll()]),
    ],
    trophy_value=2,
    rewards=[
        effect.ItemReward(item.UniqueItem),
        effect.ItemReward(item.UniqueItem),
        effect.ItemReward(item.Spell),
    ],
    penalties=[
        effect.HealthEffect(-1),
        effect.SanityEffect(-2)
    ],
)

walking_the_ledge = OrderedAdventure(
    name="Walking the Ledge",
    tasks=[
        Task([Skull()]),
        Task([Skull()]),
        Task([Skull(), Skull()]),
    ],
    trophy_value=2,
    terror_effect=effect.MonsterAppearsOnEveryMonsterTask(),
    at_midnight_effect=effect.NotImplementedEffect("Discard this adventure and do not replace it"),
    rewards=[
        effect.ItemReward(item.CommonItem),
        effect.ItemReward(item.CommonItem),
        effect.ItemReward(item.Clue),
        effect.ElderSignEffect(1),
    ],
    penalties=[
        effect.HealthEffect(-2),
        effect.SanityEffect(-1)
    ],
)

it_s_quiet = UnorderedAdventure(
    name="It's Quiet",
    tasks=[
        Task([Investigation(12)]),
    ],
    trophy_value=1,
    terror_effect=effect.MonsterAppearsOnEveryMonsterTask(),
    at_midnight_effect=effect.NotImplementedEffect("Discard this adventure and do not replace it"),
    rewards=[
        effect.ItemReward(item.Clue),
        effect.ItemReward(item.Clue),
        effect.ElderSignEffect(1),
    ],
    penalties=[
        effect.DoomTokenEffect(1)
    ],
)


sudden_attack = UnorderedAdventure(
    name='Sudden Attack',
    tasks=[
        Task([Skull()]),
        Task([Investigation(3), Skull()]),
    ],
    trophy_value=1,
    terror_effect=effect.MonsterAppearsOnEveryMonsterTask(),
    rewards=[
        effect.ItemReward(item.UniqueItem),
        effect.ItemReward(item.CommonItem),
        effect.ElderSignEffect(1),
    ],
    penalties=[
        effect.HealthEffect(-2)
    ],
)


balancing_mind_and_body = UnorderedAdventure(
    name='Balancing Mind and Body',
    tasks=[
        Task([Scroll(), Skull()]),
        Task([Skull(), Scroll()]),
    ],
    trophy_value=2,
    rewards=[
        effect.ItemReward(item.CommonItem),
        effect.ItemReward(item.Spell),
    ],
    penalties=[
        effect.HealthEffect(-1)
    ],
    terror_effect=effect.SanityEffect(-1)
)

vision_of_demise = UnorderedAdventure(
    name='Vision of Demise',
    tasks=[
        Task([Scroll(), Scroll()]),
        Task([Terror(), Terror()]),
    ],
    trophy_value=2,
    rewards=[
        effect.ElderSignEffect(1),
        effect.ItemReward(item.Spell),
        effect.NotImplementedEffect("After successfully resolving this adventure, look at the top 3 cards of the "
                                    "mythos deck. Discard 1 and return the other 2 to the top of the deck in any order.")

    ],
    penalties=[
        effect.SanityEffect(-1)
    ]
)
