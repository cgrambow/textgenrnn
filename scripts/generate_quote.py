#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os

import textgenrnn as tg

quote_gen = tg.textgenrnn(
    weights_path=os.path.join(os.path.dirname(tg.__file__),
                              'quotes', 'quotes_weights.hdf5'),
    vocab_path=os.path.join(os.path.dirname(tg.__file__),
                            'quotes', 'quotes_vocab.json'),
    config_path=os.path.join(os.path.dirname(tg.__file__),
                             'quotes', 'quotes_config.json')
)
quote_gen.generate(n=1, temperature=0.35, progress=False)
