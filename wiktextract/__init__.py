# This file defines the public exports from the wiktextract module.
#
# Copyright (c) 2018-2021 Tatu Ylonen.  See LICENSE and https://ylonen.org

from .wiktionary import parse_wiktionary, reprocess_wiktionary
from .config import WiktionaryConfig
from .page import clean_value, parse_page
from .parts_of_speech import PARTS_OF_SPEECH
from .thesaurus import extract_thesaurus_data

__all__ = (
    "WiktionaryConfig",
    "parse_wiktionary",
    "reprocess_wiktionary",
    "PARTS_OF_SPEECH",
    "parse_page",
    "extract_thesaurus_data",
)
