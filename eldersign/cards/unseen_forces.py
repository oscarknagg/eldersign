from eldersign.core import Task, EmptyMonsterTask, HealthCost, SanityCost
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion
from eldersign import effect
from eldersign import item


bloody_footprints = UnorderedAdventure(
    name="Bloody Footprints",
    tasks=[
        Task([Skull(), Skull()]),
        Task([Scroll(), Scroll()]),
        Task([Terror()]),
    ],
    trophy_value=1,
    terror_effect=effect.HealthEffect(-1),
    rewards=[
        effect.ElderSignEffect(1),
        effect.ItemReward(item.Clue),
        effect.ItemReward(item.Clue),
        effect.MonsterAppears(),
    ],
    penalties=[
        effect.SanityEffect(-2),
    ],
)

under_construction = UnorderedAdventure(
    name="Under Construction",
    tasks=[
        Task([Skull()]),
        Task([Scroll(), Scroll()]),
    ],
    trophy_value=1,
    terror_effect=effect.HealthEffect(-1),
    rewards=[
        effect.ItemReward(item.CommonItem),
        effect.ItemReward(item.Clue),
    ],
    penalties=[
        effect.DoomTokenEffect(1),
        effect.SanityEffect(-1),
    ],
)

dreaming_of_a_stranger = OrderedAdventure(
    name="Dreaming of a Stranger",
    tasks=[
        Task([], [HealthCost(1), SanityCost(1)]),
        Task([Scroll(), Scroll(), Skull()]),
        Task([Terror()]),
    ],
    trophy_value=2,
    rewards=[
        effect.ItemReward(item.CommonItem),
        effect.ItemReward(item.UniqueItem),
        effect.OpenGate(),
        effect.ItemReward(item.Ally),
    ],
    penalties=[
        effect.DoomTokenEffect(1),
    ],
)

repugnant_tome = OrderedAdventure(
    name="Repugnant Tome",
    tasks=[
        Task([Scroll(), Scroll()]),
        Task([Scroll()]),
    ],
    trophy_value=2,
    terror_effect=effect.NotImplementedEffect("Discard 1 spell or be devoured."),
    rewards=[
        effect.ElderSignEffect(1),
        effect.OpenGate(),
        effect.MonsterAppears(),
    ],
    penalties=[
        effect.SanityEffect(-2),
    ],
)

the_door_is_ajar = UnorderedAdventure(
    name="The Door is Ajar",
    tasks=[
        Task([Skull()]),
        Task([Investigation(2)]),
        Task([Investigation(7)]),
    ],
    trophy_value=2,
    rewards=[
        effect.ElderSignEffect(1),
        effect.OpenGate(),
        effect.MonsterAppears(),
    ],
    penalties=[
        effect.SanityEffect(-1),
    ],
)

too_quiet = UnorderedAdventure(
    name="Too Quiet",
    tasks=[
        Task([Scroll(), Terror()]),
        Task([Terror(), Terror()]),
    ],
    trophy_value=2,
    # at_midnight_effect=effect.UnionEffect([
    #     effect.DoomTokenEffect(1),
    #     effect.MonsterAppears()
    # ]),
    at_midnight_effect=effect.union_effects([
        effect.DoomTokenEffect(1),
        effect.MonsterAppears()
    ]),
    rewards=[
        effect.ElderSignEffect(1),
        effect.ItemReward(item.UniqueItem),
    ],
    penalties=[
        effect.HealthEffect(-1),
        effect.DoomTokenEffect(1),
    ],
)

prized_display = UnorderedAdventure(
    name="Prized Display",
    tasks=[
        Task([Terror()], monster_slot=0),
        Task([Skull()]),
        Task([Scroll()]),
    ],
    trophy_value=1,
    rewards=[
        effect.MonsterAppears(),
        effect.ItemReward(item.UniqueItem),
    ],
    penalties=[
        effect.HealthEffect(-1)
    ],
)

wicked_old_man = UnorderedAdventure(
    name="Wicked Old Man",
    tasks=[
        Task([Investigation(1), Scroll(), Terror()]),
        Task([Investigation(3), Terror()]),
    ],
    trophy_value=3,
    # terror_effect=effect.UnionEffect([effect.SanityEffect(-1), effect.HealthEffect(-1)]),
    terror_effect=effect.union_effects([effect.SanityEffect(-1), effect.HealthEffect(-1)]),
    rewards=[
        effect.ElderSignEffect(1),
        effect.ItemReward(item.Clue),
        effect.ItemReward(item.Clue),
    ],
    penalties=[
        effect.Curse()
    ],
)

the_true_history = UnorderedAdventure(
    name="The True History",
    tasks=[
        Task([Investigation(2), Scroll()], [SanityCost(1)]),
        Task([Scroll(), Scroll()], [SanityCost(1)]),
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
