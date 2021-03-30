from eldersign.core import Task, EmptyMonsterTask, HealthCost, SanityCost, TimeCost
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion
from eldersign import effect
from eldersign import item


heroic_rescue = OrderedAdventure(
    name="Heroic Rescue",
    tasks=[
        Task([Skull()]),
        Task([], [SanityCost(1)]),
        Task([Terror(), Terror(), Terror()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.Ally),
        effect.Bless(),
    ],
    penalties=[
        effect.AddHealth(-1),
    ],
)

break_on_through = UnorderedAdventure(
    # Lock green dice
    name="Break On Through",
    tasks=[
        Task([Scroll()], [SanityCost(1)]),
        Task([Investigation(3), Scroll()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.UniqueItem),
        effect.OpenGate(),
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddHealth(-1),
    ],
)

lingering_curse = UnorderedAdventure(
    name="Lingering Curse",
    tasks=[
        Task([Investigation(3)]),
        Task([Scroll(), Scroll(), Skull()]),
    ],
    trophy_value=2,
    terror_effect=effect.InvestigatorAttemptingAdventure(effect.SetHealthSanity(health=1, sanity=1)),
    rewards=[
        effect.AddItem(item.UniqueItem, 2),
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddHealth(-1),
    ],
)

mysterious_puzzle_box = UnorderedAdventure(
    name="Mysterious Puzzle Box",
    tasks=[
        Task([Scroll()]),
    ],
    trophy_value=2,
    entry_effect=effect.UnionEffect([
        effect.MonsterAppears(),
        effect.MonsterAppears()
    ]),
    rewards=[
        effect.AddElderSign(1),
        effect.MonsterAppears()
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddHealth(-2),
    ],
)

recruiting_aid = OrderedAdventure(
    name="Recruiting Aid",
    tasks=[
        Task([Investigation(3)]),
        Task([Investigation(6)]),
        Task([Investigation(9)]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.Ally, 2),
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

seeking_leads = OrderedAdventure(
    name="Seeking Leads",
    tasks=[
        Task([Investigation(1)], monster_slot=0),
        Task([Skull()]),
        Task([Skull(), Scroll()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.Spell),
        effect.AddItem(item.Clue),
    ],
    penalties=[
        effect.AddHealth(-2),
    ],
)

midnight_visitor = UnorderedAdventure(
    name="Grazed Writings",
    tasks=[
        Task([Skull(), Skull()]),
        Task([Skull(), Terror()], [HealthCost(1)]),
    ],
    trophy_value=2,
    terror_effect=effect.InvestigatorAttemptingAdventure(effect.AddHealth(-1)),
    rewards=[
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.UniqueItem),
        effect.AddItem(item.Clue),
    ],
    penalties=[
        effect.AddHealth(-2),
        effect.AddDoomToken(1),
    ],
)

grazed_writings = UnorderedAdventure(
    name="Grazed Writings",
    tasks=[
        Task([Investigation(4)], monster_slot=0),
        Task([Terror()]),
        Task([Scroll()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(1)
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

fragments_of_knowledge = UnorderedAdventure(
    name="Fragments of Knowledge",
    tasks=[
        Task([Investigation(6)]),
        Task([Terror()]),
        Task([Scroll(), Scroll()], monster_slot=0),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.Spell),
        effect.AddItem(item.Clue),
        effect.AddElderSign(1)
    ],
    penalties=[
        effect.AddSanity(-2),
    ],
)

rite_of_passage = OrderedAdventure(
    name="Rite of Passage",
    tasks=[
        Task([Skull()], [SanityCost(1)]),
        Task([Scroll()], [HealthCost(1)]),
        Task([Investigation(3), Terror()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.Spell),
        effect.AddItem(item.Clue),
        effect.AddElderSign(1)
    ],
    penalties=[
        effect.AddDoomToken(1),
        effect.AddHealth(-2),
    ],
)

up_on_the_roof = UnorderedAdventure(
    name="Up on the Roof",
    tasks=[
        EmptyMonsterTask(),
        Task([Terror(), Skull(), Scroll()]),
    ],
    trophy_value=2,
    entry_effect=effect.NotImplementedEffect("If there is no monster on this adventure place 1 monster on the task"
                                             "below."),
    rewards=[
        effect.AddItem(item.Spell),
        effect.AddDoomToken(-1),
        effect.AddElderSign(1),
        effect.MonsterAppears()
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddHealth(-1),
    ],
)

it_s_got_me = UnorderedAdventure(
    name="It's got me!",
    tasks=[
        Task([Investigation(3), Skull(), Terror()], [HealthCost(1)]),
    ],
    trophy_value=2,
    terror_effect=effect.InvestigatorAttemptingAdventure(effect.ItsGotMe()),
    rewards=[
        effect.AddItem(item.Spell),
        effect.AddItem(item.Clue),
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

the_boiler_room = UnorderedAdventure(
    name="Just Sign Here",
    tasks=[
        Task([Investigation(4), Terror()]),
        Task([Skull(), Terror()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddDoomToken(-1),
        effect.AddElderSign(1),
        effect.AddItem(item.Spell),
    ],
    penalties=[
        effect.AddSanity(-1),
        effect.AddHealth(-1),
    ],
)

just_sign_here = UnorderedAdventure(
    name="Just Sign Here",
    tasks=[
        Task([Scroll()]),
        Task([Skull()]),
        Task([Investigation(3)]),
    ],
    trophy_value=2,
    rewards=[
        effect.OpenGate(),
        effect.AddItem(item.Spell),
        effect.Curse(),
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

test_of_faith = UnorderedAdventure(
    name="Test of Faith",
    tasks=[
        Task([Investigation(6)]),
        Task([Investigation(3), Skull()]),
    ],
    trophy_value=2,
    rewards=[
        effect.Bless(),
    ],
    penalties=[
        effect.Curse(),
    ],
)

walled_up = UnorderedAdventure(
    name="Walled up",
    tasks=[
        Task([Investigation(2), Terror()], [SanityCost(1)]),
        Task([Investigation(6)],),
    ],
    trophy_value=2,
    terror_effect=effect.InvestigatorAttemptingAdventure(effect.Curse()),
    rewards=[
        effect.AddItem(item.Clue),
        effect.AddElderSign(2),
        effect.MonsterAppears(),
    ],
    penalties=[
        effect.AddSanity(-2),
    ],
)

fickle_fates = UnorderedAdventure(
    name="Fickle Fates",
    tasks=[
        EmptyMonsterTask(),
        Task([Scroll(), Scroll()]),
        Task([Investigation(2), Scroll()],),
    ],
    trophy_value=1,
    rewards=[
        effect.Bless(),
        effect.MonsterAppears(),
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

vital_information = OrderedAdventure(
    name="Vital Information",
    tasks=[
        Task([Terror()], monster_slot=0),
        Task([Scroll()]),
        Task([Skull()], [SanityCost(1)]),
    ],
    trophy_value=1,
    rewards=[
        effect.AddElderSign(1),
        effect.AddItem(item.Clue, 3),
    ],
    penalties=[
        effect.AddSanity(-1),
    ],
)

the_night_watchman = UnorderedAdventure(
    # Lock green dice
    name="The Night Watchman",
    tasks=[
        Task([Skull(), Skull()]),
        Task([Skull()], [HealthCost(1)]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(1),
        effect.AddItem(item.CommonItem),
        effect.AddItem(item.CommonItem),
    ],
    penalties=[
        effect.AddDoomToken(1),
        effect.AddHealth(-3),
    ],
)

ominous_portents = OrderedAdventure(
    name="Ominous portents",
    tasks=[
        Task([], [SanityCost(2)]),
        Task([Scroll(), Scroll(), Scroll()]),
    ],
    trophy_value=2,
    at_midnight_effect=effect.EachInvestigator(effect.Curse()),
    rewards=[
        effect.Bless(),
        effect.AddElderSign(1),
        effect.AddItem(item.Clue),
    ],
    penalties=[
        effect.Curse(),
    ],
)

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
    entry_effect=effect.UnionEffect([
       effect.InvestigatorAttemptingAdventure(effect.AddHealth(-1)),
       effect.InvestigatorAttemptingAdventure(effect.AddSanity(-1)),
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
        # Approximation of "Draw the top 2 cards of the Adventure deck and claim them as trophies as well"
        effect.AddTrophies([1, 2])
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
    terror_effect=effect.InvestigatorAttemptingAdventure(effect.AddHealth(-1)),
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
    terror_effect=effect.InvestigatorAttemptingAdventure(effect.AddHealth(-1)),
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
    at_midnight_effect=effect.UnionEffect([
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
    terror_effect=effect.UnionEffect([
        effect.InvestigatorAttemptingAdventure(effect.AddSanity(-1)),
        effect.InvestigatorAttemptingAdventure(effect.AddHealth(-1))
    ]),
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
    terror_effect=effect.InvestigatorAttemptingAdventure(effect.AddSanity(-1))
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

another_time = UnorderedAdventure(
    name='Another Time',
    other_world=True,
    tasks=[
        Task([Scroll(), Scroll()], [TimeCost(1)]),
        Task([Investigation(3)], [TimeCost(1)]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(2),
        effect.AddItem(item.Clue, 2),

    ],
    penalties=[
        effect.AddHealth(-1),
        effect.AddTime(1)
    ]
)

the_abyss = UnorderedAdventure(
    name='The Abyss',
    other_world=True,
    tasks=[
        Task([Skull(), Terror()], monster_slot=0),
        Task([Scroll(), Scroll(), Skull()]),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(2),
        effect.AddItem(item.Spell),
        effect.AddItem(item.CommonItem)
    ],
    penalties=[
        effect.AddSanity(-2),
        effect.AddHealth(-1),
    ]
)

lost_carcosa = UnorderedAdventure(
    name='Lost Carcosa',
    other_world=True,
    tasks=[
        Task([Terror(), Terror(), Terror()]),
        Task([Investigation(5)], monster_slot=0),
    ],
    trophy_value=2,
    rewards=[
        effect.AddElderSign(2),
        effect.AddItem(item.Spell),
        effect.AddItem(item.Clue)
    ],
    penalties=[
        effect.AddSanity(-3),
    ]
)