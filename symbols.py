import utils

hps = utils.get_hparams()


symbols=set()

if hps.data.cleaned_text:
    with open(hps.data.training_files, 'r') as inputs:
        lines=inputs.readlines()
        for line in lines:
            text=line.split('|')[2]
            for letter in text:
                symbols.add(letter)
    with open(hps.data.validation_files, 'r') as inputs:
        lines=inputs.readlines()
        for line in lines:
            text=line.split('|')[2]
            for letter in text:
                symbols.add(letter)


print(f'use following symbols: {sorted(list(symbols))}')