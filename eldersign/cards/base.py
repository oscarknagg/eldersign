from eldersign.core import Task, EmptyMonsterTask, HealthCost, SanityCost
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion
from eldersign import effect
from eldersign import item


ancient_relics = UnorderedAdventure(
    name="Ancient Relics",
    tasks=[
        Task([Scroll(), Investigation(3)], monster_slot=0),
        Task([Scroll(), Investigation(3)]),
    ],
    trophy_value=1,
    terror_effect=effect.AddSanity(-1),
    rewards=[
        effect.AddItem(item.Clue),
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

a_terrible_discovery = UnorderedAdventure(
    name="A Terrible Discovery",
    tasks=[
        Task([Investigation(3), Terror()], [SanityCost(1)]),
        Task([Scroll(), Scroll()], [SanityCost(1)]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.Clue, 2),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddSanity(-2),
    ],
)

did_you_hear_that = UnorderedAdventure(
    # Lock green dice
    name="Did you hear that?",
    tasks=[
        Task([Skull()], monster_slot=0),
        Task([Skull(), Skull()]),
    ],
    trophy_value=2,
    terror_effect=effect.DiscardAllTerrorDice(),
    rewards=[
        effect.AddItem(item.Spell),
        effect.AddItem(item.UniqueItem),
        effect.MonsterAppears()
    ],
    penalties=[
        effect.AddHealth(-1),
    ],
)

the_loading_dock = UnorderedAdventure(
    name="The Loading Dock",
    tasks=[
        Task([Skull()]),
        Task([Skull(), Investigation(3)]),
    ],
    trophy_value=1,
    terror_effect=effect.DiscardAllTerrorDice(),
    rewards=[
        effect.AddItem(item.CommonItem),
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddHealth(-1),
    ],
)

the_storage_closet = OrderedAdventure(
    name="The Storage Closet",
    tasks=[
        Task([Investigation(3)], monster_slot=0),
        Task([Investigation(3)]),
        Task([Scroll(), Scroll()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.Clue),
        effect.AddItem(item.UniqueItem),
        effect.OpenGate(),
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddDoomToken(1),
    ],
)

the_key_to_the_beyond = OrderedAdventure(
    name="The Key to the Beyond",
    tasks=[
        Task([Investigation(3)]),
        Task([Scroll(), Skull(), Investigation(2)]),
    ],
    trophy_value=2,
    terror_effect=effect.AddSanity(-1),
    rewards=[
        effect.AddItem(item.Clue, 2),
        effect.OpenGate(),
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

riot_in_the_streets = OrderedAdventure(
    name="Riot in the Street",
    tasks=[
        Task([Investigation(3)]),
        Task([Investigation(9)]),
    ],
    trophy_value=2,
    terror_effect=effect.AddHealth(-1),
    rewards=[
        effect.AddElderSign(1),
        effect.AddItem(item.UniqueItem),
        effect.AddItem(item.CommonItem),
    ],
    penalties=[
        effect.AddDoomToken(1),
    ],
)

unnatural_habitat = UnorderedAdventure(
    name="Unnatural Habitat",
    tasks=[
        EmptyMonsterTask(),
        Task([Skull(), Skull(), Investigation(3)]),
    ],
    trophy_value=2,
    terror_effect=effect.AddSanity(-1),
    rewards=[
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddHealth(-1),
    ],
)

don_t_fall_asleep = UnorderedAdventure(
    name="Don't fall asleep",
    tasks=[
        Task([Terror()]),
        Task([Terror(), Terror()]),
    ],
    trophy_value=2,
    at_midnight_effect=effect.EachInvestigator(effect.AddSanity(-1)),
    rewards=[
        effect.AddItem(item.Clue),
        effect.AddItem(item.Spell),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

the_hidden_passage = OrderedAdventure(
    name="Something has broken free",
    tasks=[
        Task([Investigation(3)]),
        Task([Skull(), Investigation(3)]),
        Task([Scroll()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(2),
    ],
    penalties=[
        effect.AddHealth(-2),
    ],
)

something_has_broken_free = OrderedAdventure(
    name="Something has broken free",
    tasks=[
        Task([Skull()], monster_slot=0),
        Task([Terror(), Terror()]),
    ],
    trophy_value=1,
    terror_effect=effect.ImmediatelyFail(),
    rewards=[
        effect.MonsterAppears(),
        effect.AddItem(item.Clue),
        effect.AddItem(item.Spell),
        effect.AddItem(item.UniqueItem),
    ],
    penalties=[
        effect.AddHealth(-1),
    ],
)

hallway_on_fire = OrderedAdventure(
    name="Hallway on Fire",
    tasks=[
        Task([Skull()], [HealthCost(1)]),
        Task([Skull()], [HealthCost(1)]),
    ],
    trophy_value=2,
    terror_effect=effect.AddHealth(-1),
    rewards=[
        effect.AddItem(item.UniqueItem),
        effect.AddItem(item.UniqueItem),
    ],
    penalties=[
        effect.AddHealth(-2),
    ],
)

horrible_visions = UnorderedAdventure(
    name="Horrible Visions",
    tasks=[
        Task([Investigation(3)], monster_slot=0),
        Task([Investigation(6)]),
    ],
    trophy_value=1,
    at_midnight_effect=effect.AddDoomToken(2),
    rewards=[
        effect.AddItem(item.UniqueItem),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddHealth(-2),
        effect.AddSanity(-2),
    ],
)

late_night_break_in = UnorderedAdventure(
    name="Late night Break-in",
    tasks=[
        Task([Investigation(3)], monster_slot=0),
        Task([Investigation(6)]),
    ],
    trophy_value=1,
    terror_effect=effect.SpendTrophies(1),
    rewards=[
        effect.AddItem(item.Clue),
    ],
    penalties=[
        effect.AddHealth(-1),
    ],
)

there_s_something_in_the_basement = UnorderedAdventure(
    name="There's something in the basement",
    tasks=[
        Task([Investigation(6)], monster_slot=0),
        Task([Scroll()]),
        Task([Terror()]),
    ],
    trophy_value=1,
    rewards=[
        effect.AddItem(item.Clue),
        effect.AddItem(item.UniqueItem),
    ],
    penalties=[
        effect.AddHealth(-1),
        effect.AddSanity(-1),
    ],
)

tempest_in_a_teapot = OrderedAdventure(
    name="Tempest in a Teapot",
    tasks=[
        Task([Investigation(4)], monster_slot=0),
        Task([Terror()]),
        Task([Skull(), Scroll()]),
    ],
    trophy_value=1,
    rewards=[
        effect.AddItem(item.Clue),
        effect.AddItem(item.UniqueItem),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddHealth(-1),
        effect.AddDoomToken(1),
        effect.AddSanity(-1),
    ],
)

a_secret_gathering = UnorderedAdventure(
    name="A Secret Gathering",
    tasks=[
        Task([Investigation(6)]),
        Task([Scroll(), Scroll()]),
    ],
    trophy_value=1,
    terror_effect=effect.AddSanity(-1),
    rewards=[
        effect.MonsterAppears(),
        effect.AddItem(item.Clue),
        effect.OpenGate(),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddHealth(-2),
    ],
)

the_missing_records = UnorderedAdventure(
    name="The missing records",
    tasks=[
        Task([Investigation(6)]),
        Task([Scroll(), Investigation(3)]),
    ],
    trophy_value=1,
    rewards=[
        effect.AddItem(item.Clue, 2),
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

vermin_in_the_pipes = UnorderedAdventure(
    name="Vermin in the pipes",
    tasks=[
        Task([Investigation(3)]),
        Task([Investigation(3)]),
        Task([Investigation(3), Skull()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.CommonItem, 2),
        effect.AddItem(item.Clue),
    ],
    penalties=[
        effect.AddHealth(-1),
    ],
)

the_archives = UnorderedAdventure(
    name="The Archives",
    tasks=[
        Task([Scroll()], monster_slot=0),
        Task([Scroll(), Investigation(3)]),
        Task([Scroll(), Skull()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.UniqueItem, 2),
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

stay_away_from_the_windows = UnorderedAdventure(
    name="Stay Away From the Windows",
    tasks=[
        Task([Investigation(8)]),
        Task([Skull(), Skull()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(2),
    ],
    penalties=[
        effect.AddDoomToken(1),
        effect.AddSanity(-1),
        effect.AddHealth(-2),
    ],
)

gate_to_elsewhere = UnorderedAdventure(
    name="Gate to Elsewhere",
    tasks=[
        Task([Scroll()], monster_slot=0),
        Task([Scroll(), Scroll()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.Clue, 2),
        effect.OpenGate(),
    ],
    penalties=[
        effect.AddDoomToken(1),
    ],
)

administration_office = UnorderedAdventure(
    name="We need to find help",
    tasks=[
        Task([Scroll()]),
        Task([Investigation(9)]),
    ],
    trophy_value=1,
    rewards=[
        effect.AddItem(item.Clue, 2),
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddItem(item.Clue, -1),
    ],
)

we_need_to_find_help = UnorderedAdventure(
    # Lock red dice
    name="We need to find help",
    tasks=[
        EmptyMonsterTask(),
        Task([Skull(), Skull(), Scroll(), Investigation(3)]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddSanity(-2),
        effect.AddHealth(-1),
    ],
)

a_peculiar_specimen = OrderedAdventure(
    name="Mysterious Tome",
    tasks=[
        Task([Investigation(3)]),
        Task([Investigation(6)]),
        Task([Skull()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(1),
        effect.MonsterAppears(),
    ],
    penalties=[
        effect.AddHealth(-1),
    ],
)

mysterious_tome = UnorderedAdventure(
    name="Mysterious Tome",
    tasks=[
        Task([Investigation(3), Terror()]),
        Task([Scroll(), Scroll()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.Clue),
        effect.OpenGate(),
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddDoomToken(1),
    ],
)

lights_out = OrderedAdventure(
    name="Lights Out",
    tasks=[
        Task([Investigation(3)]),
        Task([Skull(), Skull()]),
        Task([Scroll(), Scroll()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(1),
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddHealth(-1),
        effect.AddDoomToken(1),
        effect.AddHealth(-1),
    ],
)

the_elder_sign = OrderedAdventure(
    name="The Elder Sign",
    tasks=[
        Task([Scroll()], [SanityCost(1)]),
        Task([Scroll()], [HealthCost(1)]),
        Task([Investigation(2), Scroll()]),
    ],
    trophy_value=2,
    terror_effect=effect.SpendTrophies(1),
    rewards=[
        effect.AddDoomToken(-1),
        effect.AddElderSign(1),
        effect.AddItem(item.Clue),
        effect.AddItem(item.Clue),
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

the_writing_on_the_wall = UnorderedAdventure(
    name="The Writing on the Wall",
    tasks=[
        EmptyMonsterTask(),
        Task([Scroll(), Skull(), Investigation(3)]),
    ],
    trophy_value=2,
    terror_effect=effect.SpendTrophies(1),
    rewards=[
        effect.AddItem(item.Spell),
        effect.OpenGate(),
        effect.AddItem(item.CommonItem),
        effect.MonsterAppears(),
    ],
    penalties=[
        effect.AddDoomToken(1),
    ],
)

gala_in_the_great_hall = UnorderedAdventure(
    # Yellow dice lock
    name="Gala in the Great Hall",
    tasks=[
        Task([Investigation(2), Scroll()]),
        Task([Investigation(3)], [SanityCost(1)]),
    ],
    trophy_value=2,
    terror_effect=effect.AddDoomToken(1),
    rewards=[
        effect.AddItem(item.Clue),
        effect.AddItem(item.Clue),
        effect.AddItem(item.Spell),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddDoomToken(1),
    ],
)

please_do_not_touch_the_exhibits = UnorderedAdventure(
    name="Medusa Exhibit",
    tasks=[
        Task([Terror(), Terror()], [SanityCost(1)]),
        Task([Skull(), Skull()], [HealthCost(1)]),
    ],
    trophy_value=2,
    terror_effect=effect.AddDoomToken(1),
    rewards=[
        effect.AddElderSign(2),
    ],
    penalties=[
        effect.AddHealth(-1),
        effect.AddDoomToken(1),
        effect.AddSanity(-1),
    ],
)

medusa_exhibit = OrderedAdventure(
    name="Medusa Exhibit",
    tasks=[
        Task([Terror()], [SanityCost(1)]),
        Task([Scroll()], [SanityCost(1)]),
        Task([Investigation(7)]),
    ],
    trophy_value=2,
    terror_effect=effect.DiscardAllTerrorDice(),
    rewards=[
        effect.MonsterAppears(),
        effect.AddItem(item.Spell),
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.Clue),
    ],
    penalties=[
        effect.AddSanity(-2),
    ],
)

the_guided_tour = OrderedAdventure(
    name="The Guided Tour",
    tasks=[
        Task([Investigation(2)]),
        Task([Investigation(4)]),
        Task([Scroll()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.Clue),
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.Clue),
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddHealth(-1),
    ],
)

you_become_that_which_you_fear_most = UnorderedAdventure(
    name="You Become that which you Fear Most",
    tasks=[
        EmptyMonsterTask(),
        Task([Terror(), Terror(), Terror()]),
    ],
    trophy_value=2,
    at_midnight_effect=effect.MonsterAppears(),
    rewards=[
        effect.MonsterAppears(),
        effect.AddItem(item.Clue),
        effect.AddItem(item.UniqueItem),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

the_curator = UnorderedAdventure(
    name="The Curator",
    tasks=[
        Task([Scroll(), Scroll(), Scroll()]),
        Task([Scroll(), Investigation(2)]),
    ],
    trophy_value=2,
    at_midnight_effect=effect.EachInvestigator(
        effect.InvestigatorEffectChoice([
            effect.SpendTrophies(2),
            effect.UnionEffect([
                effect.AddHealth(-1),
                effect.AddSanity(-1)
            ])
        ])
    ),
    rewards=[
        effect.AddItem(item.Clue),
        effect.AddItem(item.CommonItem),
        effect.AddElderSign(12),
    ],
    penalties=[
        effect.AddSanity(-2),
    ],
)

the_hedge_maze = UnorderedAdventure(
    name="The Hedge Maze",
    tasks=[
        EmptyMonsterTask(),
        EmptyMonsterTask(),
        Task([Skull(), Scroll(), Scroll()]),
    ],
    trophy_value=2,
    at_midnight_effect=effect.EachInvestigator(effect.AddHealth(-1)),
    rewards=[
        effect.MonsterAppears(),
        effect.MonsterAppears(),
        effect.AddElderSign(2),
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddHealth(-1)
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
        effect.AddElderSign(2),
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddHealth(-1)
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
        effect.AddItem(item.Spell),
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddSanity(-1)
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
        effect.AddItem(item.Clue),
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.UniqueItem),
    ],
    penalties=[
        effect.AddHealth(-1)
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
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.UniqueItem),
        effect.OpenGate(),
    ],
    penalties=[
        effect.AddSanity(-1)
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
        effect.AddItem(item.Ally),
    ],
    penalties=[
        effect.AddSanity(-2)
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
        effect.AddItem(item.Spell),
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddDoomToken(1),
        effect.AddSanity(-1)
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
        effect.AddItem(item.Clue),
        effect.AddItem(item.UniqueItem),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddSanity(-2),
        effect.AddHealth(-2)
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
        effect.AddItem(item.UniqueItem),
    ],
    penalties=[
        effect.AddSanity(-1)
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
        effect.AddItem(item.Clue),
        effect.AddItem(item.UniqueItem),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddSanity(-2)
    ],
)


koi_pond = UnorderedAdventure(
    name="Koi Pond",
    tasks=[
        Task([Terror()], monster_slot=0),
        Task([Terror(), Skull(), Skull()]),
    ],
    trophy_value=2,
    terror_effect=effect.ImmediatelyFail(),
    rewards=[
        effect.MonsterAppears(),
        effect.AddItem(item.Clue),
        effect.AddItem(item.CommonItem),
        effect.AddElderSign(1)
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddHealth(-2)
    ]
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
        effect.AddItem(item.Clue),
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddHealth(-1)
    ]
)

blood_on_the_floor = OrderedAdventure(
    name="Blood on the Floor",
    tasks=[
        Task([Investigation(2)]),
        Task([Investigation(3)]),
        Task([Terror(), Skull()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.Clue),
        effect.AddItem(item.CommonItem),
        effect.AddElderSign(1),
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddHealth(-1),
    ]
)

the_dreamlands = UnorderedAdventure(
    name='The Dreamlands',
    other_world=True,
    tasks=[
        Task([Skull(), Scroll(), Investigation(3)]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.Clue, 2),
        effect.AddElderSign(1)
    ],
    penalties=[
        effect.AddSanity(-1)
    ]
)

city_of_the_great_race = UnorderedAdventure(
    name='City of the Great Race',
    other_world=True,
    tasks=[
        Task([Investigation(3)], monster_slot=0),
        Task([Terror(), Scroll(), Skull()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(1),
        effect.AddItem(item.UniqueItem, 3)
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddHealth(-2)
    ]
)

great_hall_of_celeano = UnorderedAdventure(
    name="Great Hall of Celeano",
    other_world=True,
    tasks=[
        Task([Terror()], monster_slot=0),
        Task([Scroll()]),
        Task([Investigation(6)]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(1),
        effect.AddItem(item.Spell),
        effect.AddDoomToken(-1)
    ],
    penalties=[
        effect.AddSanity(-1)
    ]
)

plateau_of_leng = UnorderedAdventure(
    name='Plateau of Leng',
    other_world=True,
    tasks=[
        Task([Scroll(), Terror()]),
        Task([Terror(), Skull(), Terror()]),
    ],
    trophy_value=2,
    terror_effect=effect.AddSanity(-1),
    rewards=[
        effect.AddDoomToken(-1),
        effect.AddElderSign(1),
        effect.AddItem(item.Clue, 2)
    ],
    penalties=[
        effect.AddSanity(-2)
    ]
)

another_dimension = UnorderedAdventure(
    name="Another Dimension",
    other_world=True,
    tasks=[
        Task([Scroll(), Investigation(1)], monster_slot=1),
        Task([Terror(), Skull()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddSanity(-1),
        effect.AddHealth(-2),
    ],
    penalties=[
        effect.AddItem(item.Spell),
        effect.AddItem(item.CommonItem),
        effect.AddElderSign(1)
    ]
)

yuggoth = UnorderedAdventure(
    name='Yuggoth',
    other_world=True,
    tasks=[
        Task([Skull(), Terror()], monster_slot=1),
        Task([Investigation(8)]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(2),
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.UniqueItem),
    ],
    penalties=[
        effect.AddSanity(-2),
        effect.AddHealth(-1)
    ]
)

r_lyeh = UnorderedAdventure(
    name="R'lyeh",
    other_world=True,
    tasks=[
        Task([Investigation(1), Investigation(1)], monster_slot=1),
        Task([Scroll(), Scroll(), Skull(), Terror()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.Ally),
        effect.AddElderSign(3)
    ],
    penalties=[
        effect.AddSanity(-2),
        effect.AddHealth(-2),
    ]
)

print(r_lyeh.to_art())
# print(there_s_something_in_the_basement.to_art())