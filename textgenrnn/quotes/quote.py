# -*- coding: utf-8 -*-

import os

import textgenrnn as tg

temperature = 0.35

dirname = os.path.dirname(os.path.realpath(__file__))
quote_gen = tg.textgenrnn(
    weights_path=os.path.join(dirname, 'quotes_weights.hdf5'),
    vocab_path=os.path.join(dirname, 'quotes_vocab.json'),
    config_path=os.path.join(dirname, 'quotes_config.json')
)


def get_quote():
    return quote_gen.generate(n=1, temperature=temperature,
                              progress=False, return_as_list=True)[0]
