from eldersign.core import Task
from eldersign.adventure import UnorderedAdventure, OrderedAdventure
from eldersign.symbol import Terror, Scroll, Skull, Investigation, SymbolUnion
from eldersign import effect
from eldersign import item


balancing_mind_and_body

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
