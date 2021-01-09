from eldersign.core import Task, EmptyMonsterTask, HealthCost, SanityCost
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion
from eldersign import effect
from eldersign import item


the_hidden_temple = OrderedAdventure(
    name="The Hidden Temple",
    tasks=[
        Task([Investigation(5)]),
        Task([Investigation(3), Scroll(), Skull()]),
    ],
    trophy_value=3,
    entry_effect=effect.AddDoomToken(1),
    rewards=[
        effect.OpenGate(),
        effect.OpenGate(),
        effect.AddItem(item.Spell),
        effect.AddItem(item.UniqueItem),
    ],
    penalties=[
        effect.AddDoomToken(1),
    ],
)

slithering_shadows = UnorderedAdventure(
    name="Slithering Shadows",
    tasks=[
        Task([Investigation(5)]),
        Task([Skull(), Skull(), Skull()]),
    ],
    trophy_value=2,
    at_midnight_effect=effect.ThreeDoomsIfAnyMonster(),
    rewards=[
        effect.AddItem(item.UniqueItem),
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.Spell),
        effect.MonsterAppears(),
    ],
    penalties=[
        effect.AddHealth(-1),
        effect.AddSanity(-1),
    ],
)

in_the_stacks = UnorderedAdventure(
    name="In the Stacks",
    tasks=[
        Task([Skull(), Terror()]),
        Task([Terror()], [HealthCost(1)]),
    ],
    trophy_value=2,
    terror_effect=effect.MonsterAppears(),
    rewards=[
        effect.AddItem(item.UniqueItem),
        effect.AddItem(item.CommonItem, 2),
    ],
    penalties=[
        effect.AddHealth(-1),
        effect.AddSanity(-1),
    ],
)

strange_robberies = UnorderedAdventure(
    name="Strange Robberies",
    tasks=[
        Task([Investigation(4)]),
        Task([Skull(), Scroll(), Skull()]),
    ],
    trophy_value=3,
    entry_effect=effect.union_effects([
        effect.AddHealth(-1),
        effect.AddSanity(-1),
    ]),
    rewards=[
        effect.AddItem(item.UniqueItem),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddDoomToken(1),
    ],
)

the_director_s_safe = UnorderedAdventure(
    name="The Director's Safe",
    tasks=[
        Task([Investigation(2), Skull()]),
        Task([Skull(), Skull()]),
    ],
    trophy_value=1,
    rewards=[
        effect.AddItem(item.UniqueItem),
        effect.NotImplementedEffect("Draw the top 2 cards of the Adventure deck and claim them as trophies as well")
    ],
    penalties=[
        effect.AddHealth(-2),
    ],
)

bloody_footprints = UnorderedAdventure(
    name="Bloody Footprints",
    tasks=[
        Task([Skull(), Skull()]),
        Task([Scroll(), Scroll()]),
        Task([Terror()]),
    ],
    trophy_value=1,
    terror_effect=effect.AddHealth(-1),
    rewards=[
        effect.AddElderSign(1),
        effect.AddItem(item.Clue),
        effect.AddItem(item.Clue),
        effect.MonsterAppears(),
    ],
    penalties=[
        effect.AddSanity(-2),
    ],
)

under_construction = UnorderedAdventure(
    name="Under Construction",
    tasks=[
        Task([Skull()]),
        Task([Scroll(), Scroll()]),
    ],
    trophy_value=1,
    terror_effect=effect.AddHealth(-1),
    rewards=[
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.Clue),
    ],
    penalties=[
        effect.AddDoomToken(1),
        effect.AddSanity(-1),
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
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.UniqueItem),
        effect.OpenGate(),
        effect.AddItem(item.Ally),
    ],
    penalties=[
        effect.AddDoomToken(1),
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
        effect.AddElderSign(1),
        effect.OpenGate(),
        effect.MonsterAppears(),
    ],
    penalties=[
        effect.AddSanity(-2),
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
        effect.AddElderSign(1),
        effect.OpenGate(),
        effect.MonsterAppears(),
    ],
    penalties=[
        effect.AddSanity(-1),
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
        effect.AddDoomToken(1),
        effect.MonsterAppears()
    ]),
    rewards=[
        effect.AddElderSign(1),
        effect.AddItem(item.UniqueItem),
    ],
    penalties=[
        effect.AddHealth(-1),
        effect.AddDoomToken(1),
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
        effect.AddItem(item.UniqueItem),
    ],
    penalties=[
        effect.AddHealth(-1)
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
    terror_effect=effect.union_effects([effect.AddSanity(-1), effect.AddHealth(-1)]),
    rewards=[
        effect.AddElderSign(1),
        effect.AddItem(item.Clue),
        effect.AddItem(item.Clue),
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
        effect.AddElderSign(1),
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddDoomToken(1)
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
        effect.AddItem(item.UniqueItem),
        effect.AddItem(item.UniqueItem),
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddHealth(-1),
        effect.AddSanity(-2)
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
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.Clue),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddHealth(-2),
        effect.AddSanity(-1)
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
        effect.AddItem(item.Clue),
        effect.AddItem(item.Clue),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddDoomToken(1)
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
        effect.AddItem(item.UniqueItem),
        effect.AddItem(item.CommonItem),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddHealth(-2)
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
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddHealth(-1)
    ],
    terror_effect=effect.AddSanity(-1)
)

vision_of_demise = UnorderedAdventure(
    name='Vision of Demise',
    tasks=[
        Task([Scroll(), Scroll()]),
        Task([Terror(), Terror()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(1),
        effect.AddItem(item.Spell),
        effect.NotImplementedEffect("After successfully resolving this adventure, look at the top 3 cards of the "
                                    "mythos deck. Discard 1 and return the other 2 to the top of the deck in any order.")

    ],
    penalties=[
        effect.AddSanity(-1)
    ]
)
