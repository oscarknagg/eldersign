from eldersign.core import Task
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion
from eldersign import effect
from eldersign import item


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
