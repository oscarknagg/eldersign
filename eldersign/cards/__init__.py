import eldersign.cards.base
import eldersign.cards.unseen_forces

expansions = {
    'base': {
        i: getattr(base, i)
        for i in dir(base)
        if not i.startswith('__') and isinstance(getattr(base, i), base.AbstractAdventure)
    },
    'unseen_forces': {
        i: getattr(unseen_forces, i)
        for i in dir(unseen_forces)
        if not i.startswith('__') and isinstance(getattr(unseen_forces, i), base.AbstractAdventure)
    }
}
