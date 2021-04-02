import pandas as pd
import argparse

from eldersign import cards


def main(args):
    adventure_cards_to_process = [
        (
            adventure_id,
            adventure,
        )
        for expansion in args.expansions
        for adventure_id, adventure in cards.expansions[expansion].items()
    ]

    rows = []
    for adventure_id, adventure in adventure_cards_to_process:
        for i, task in enumerate(adventure.tasks):
            for symbol in task.symbols:
                rows.append({
                        'adventure_id': adventure_id,
                        'task': i,
                        'symbol': symbol.__class__.__name__,
                        'value': getattr(symbol, 'value', None)
                    })

    df = pd.DataFrame(rows)
    df.to_csv(args.output, index=False)


if __name__ == '__main__':

    parser = argparse.ArgumentParser()
    parser.add_argument('--output', default='card_details.csv')
    parser.add_argument('--expansions', nargs='+', default=['base', 'unseen_forces'])
    args = parser.parse_args()

    main(args)
