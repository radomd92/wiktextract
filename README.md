# Wiktextract

This is a utility and Python package for for extracing data from Wiktionary.

**Version 1.99.5 is now on pypi and available for installation using
  pip (Python3).  Think of it as a beta version for 2.0.0.  There is
  also a new version of wikitextprocessor.**

The release won't address everything.  Especially linkages (hypernyms,
hyponyms, etc.) and disambiguation have issues that I'm postponing to
future releases.  This release is still a *major* improvement and
should handle non-English languages much better and be much more
maintainable.  Technically it is a nearly full rewrite and should now
handle almost any templates as well as text and encoding generated by
Lua modules.

Please report issues on github and I'll try to address them reasonably
soon.

The current extracted version is available for browsing and download
at: [https://kaikki.org/dictionary/](http://kaikki.org/dictionary/).
I plan to maintain an automatically updating version of the data at
this location.  For most people the preferred way to get the extracted
Wiktionary data will be to just take it from the web site.

Note: extracting all data for all languages from English Wiktionary
takes about 7 hours on a modern 24-core desktop.  You may want to
download the pre-extracted data rather than run it yourself.  If you
run it yourself, be prepared to wait from several hours to a couple of
days, depending on your computer.  Expanding Lua modules is not cheap,
but it enables superior extraction quality and maintainability!

## Overview

This is a Python package and tool for extracting information from
English Wiktionary (enwiktionary) data dumps.  Note that the English
Wiktionary contains extensive dictionaries and inflectional
information for many languages, not just English.  Only its glosses
and internal tagging are in English.

One thing that distinguishes this tool from any system I'm aware of is
that this tool expands templates and Lua macros in Wiktionary.  That
enables much more accurate rendering and extraction of glosses, word
senses, inflected forms, and pronunciations.  It also makes the system
much easier to maintain.  All this results in much higher extraction
quality and accuracy.

This tool extracts glosses, parts-of-speech, declension/conjugation
information when available, translations for all languages when
available, pronunciations (including audio file links), qualifiers
including usage notes, word forms, links between words including
hypernyms, hyponyms, holonyms, meronyms, related words, derived terms,
compounds, alternative forms, etc.  Links to Wikipedia pages, Wikidata
identifiers, and other such data are also extracted when available.
For many classes of words, a word sense is annotated with specific
information such as what word it is a form of, what is the RGB value
of the color it represents, what is the numeric value of a number,
what SI unit it represents, etc.

This tool extracts information for all languages that have data in the
English wiktionary.  It also extracts translingual data and
information about characters (anything that has an entry in Wiktionary).

This tool reads the ``enwiktionary-<date>-pages-articles.xml.bz2``
dump file and outputs JSON-format dictionaries containing most of the
information in Wiktionary.  The dump files can be downloaded from
https://dumps.wikimedia.org.

This utility will be useful for many natural language processing,
semantic parsing, machine translation, and language generation
applications both in research and industry.

The tool can be used to extract machine translation dictionaries,
language understanding dictionaries, semantically annotated
dictionaries, and morphological dictionaries with
declension/conjugation information (where this information is
gavailable for the target language).  Dozens of languages have
extensive vocabulary in ``enwiktionary``, and several thousand
languages have partial coverage.

The ``wiktwords`` script makes extracting the information for use by
other tools trivial without writing a single line of code.  It
extracts the information specified by command options for languages
specified on the command line, and writes the extracted data to a file
or standard output in JSON format for processing by other tools.

While there are currently no active plans to support parsing
non-English wiktionaries, I'm considering it.  Now that this builds on
[wikitextprocessor](https://github.com/tatuylonen/wikitextprocessor/)
and expands templates and Lua macros, it would be fairly
straightforward to build support for other languages too - and even
make the extraction configurable so that only a configuration file
would need to be created for a processing a Wiktionary in a new
language.

As far as we know, this is the most comprehensive tool available for
extracting information from Wiktionary as of December 2020.

If you find this tool and/or the pre-extracted data helpful, please
give this a star on github!

## Pre-extracted data

For most people, it may be easiest to just download pre-expanded data.
Please see https://kaikki.org/dictionary/.  There is a download link
at the bottom of every page.  You can download all data, data for a
specific language, just a single word, or a list of related words
(e.g., a particular part-of-speech or words relating to a particular
topic or having a particular inflectional form).  All downloads are in
JSON format (each line is a separate JSON object).  The bigger
downloads are also available in compressed form.

Some people have asked for the data as a single JSON object.  I've
decided to keep it as a JSON object per line, because loading all the
data into Python requires 40-50 GB of memory.  It is much easier to
process the data line-by-line, especially if you are only interested
in part of the information.  You can easily read the files using the
following code:
```
import json
...
with open("filename.json", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        ... parse the data for this record
```

If you want to collect all the data into a list, you can read the file
into a list with:
```
import json
...
lst = []
with open("filename.json", "r", encoding="utf-8") as f:
    for line in f:
        data = json.loads(line)
        lst.append(data)
```

You can also easily pretty-print the data into more human-readable form using:
```
print(json.dumps(data, indent=2, sort_keys=True))
```

Here is a pretty-printed example of an extracted word entry for the
word ``thrill`` as an English verb:
```
{
  "categories": [
    "Emotions"
  ],
  "derived": [
    {
      "word": "enthrill"
    }
  ],
  "forms": [
    {
      "form": "thrills",
      "tags": [
        "present",
        "simple",
        "singular",
        "third-person"
      ]
    },
    {
      "form": "thrilling",
      "tags": [
        "present"
      ]
    },
    {
      "form": "thrilled",
      "tags": [
        "participle",
        "past",
        "simple"
      ]
    }
  ],
  "heads": [
    {
      "template_name": "en-verb"
    }
  ],
  "lang": "English",
  "lang_code": "en",
  "pos": "verb",
  "senses": [
    {
      "glosses": [
        "To suddenly excite someone, or to give someone great pleasure; to electrify; to experience such a sensation."
      ],
      "tags": [
        "ergative",
        "figuratively"
      ]
    },
    {
      "glosses": [
        "To (cause something to) tremble or quiver."
      ],
      "tags": [
        "ergative"
      ]
    },
    {
      "glosses": [
        "To perforate by a pointed instrument; to bore; to transfix; to drill."
      ],
      "tags": [
        "obsolete"
      ]
    },
    {
      "glosses": [
        "To hurl; to throw; to cast."
      ],
      "tags": [
        "obsolete"
      ]
    }
  ],
  "sounds": [
    {
      "ipa": "/\u03b8\u0279\u026al/"
    },
    {
      "ipa": "[\u03b8\u027e\u032a\u030a\u026a\u026b]",
      "tags": [
        "UK",
        "US"
      ]
    },
    {
      "ipa": "[\u03b8\u027e\u032a\u030a\u026al]",
      "tags": [
        "Ireland"
      ]
    },
    {
      "ipa": "[t\u032a\u027e\u032a\u030a\u026al]",
      "tags": [
        "Ireland"
      ]
    },
    {
      "rhymes": "-\u026al"
    },
    {
      "audio": "en-us-thrill.ogg",
      "tags": [
        "US"
      ],
      "text": "Audio (US)"
    }
  ],
  "translations": [
    {
      "code": "nl",
      "lang": "Dutch",
      "sense": "suddenly excite someone, or to give someone great pleasure; to electrify",
      "word": "opwinden"
    },
    {
      "code": "fi",
      "lang": "Finnish",
      "sense": "suddenly excite someone, or to give someone great pleasure; to electrify",
      "word": "syk\u00e4hdytt\u00e4\u00e4"
    },
    {
      "code": "fi",
      "lang": "Finnish",
      "sense": "suddenly excite someone, or to give someone great pleasure; to electrify",
      "word": "riemastuttaa"
    },
...
    {
      "code": "tr",
      "lang": "Turkish",
      "sense": "slight quivering of the heart that accompanies a cardiac murmur",
      "word": "\u00e7arp\u0131nt\u0131"
    }
  ],
  "wikipedia": [
    "thrill"
  ],
  "word": "thrill"
}
```

## Getting started

### Installing

Preparation: on Linux (example from Ubuntu 20.04), you may need to
first install the ``build-essential`` and ``python3-dev`` packages
with ``apt update && apt install build-essential python3-dev python3-pip``.

To install ``wiktextract``, use ``pip`` (or ``pip3``, as appropriate):
```
pip3 install wiktextract
```

Alternatively, you can get the latest development version from githup:

```
git clone https://github.com/tatuylonen/wiktextract.git
cd wiktextract && pip3 install -r requirements.txt && pip3 install -e .
```

This will install the ``wiktextract`` package and the ``wiktwords`` script.

This software requires Python 3.

### Running tests

This package includes tests written using the ``unittest`` framework.
They can be run using, for example, ``nose``, which can be installed
using ``pip3 install nose``.

To run the tests, just use the following command in the top-level directory:
```
nosetests
```

(Unfortunately the test suite for ``wiktextract`` is not yet very
comprehensive.  The underlying lower-level toolkit,
``wikitextprocessor``, has much more extensive test coverage.)

### Expected performance

Extracting all data for all languages from English Wiktionary takes
about 1.5 hours on a 128-core dual AMD EPYC 7702 system.  The
performance is expected to be approximately linear with the number of
processor cores, provided you have enough memory (about 8GB/core or
4GB/hyperthread recommended).

You can control the number of parallel processes to use with the
``--num-threads`` option; the default on Linux is to use the number of
available cores/hyperthreads.  On Windows and MacOS, ``--num-threads``
should currently be set to 1 (default on those systems). We don't
really recommend using Windows or Mac for the extraction, because it
will be slow.  Extracting only a few languages or a subset of the data
will be faster.

You can download the full pre-extracted data from
[kaikki.org](https://kaikki.org/dictionary/). The pre-extraction is
updated regularly with the latest Wiktionary dump.  Using the
pre-extracted data may be the easiest option unless you have special
needs or want to modify the code.

## Using the command-line tool

The ``wiktwords`` script is the easiest way to extract data from
Wiktionary.  Just download the data dump file from
[dumps.wikimedia.org](https://dumps.wikimedia.org/enwiktionary/) and
run the script.  The correct dump file the name
``enwiktionary-<date>-pages-articles.xml.bz2``.

An example of a typical invocation for extracting all data would be:
```
wiktwords --all --all-languages --out data.json enwiktionary-20201201-pages-articles.xml.bz2
```

If you wish to modify the code or test processing individual pages,
the following may also be useful:

1. To extract all pages from Wiktionary into separate files under
``pages/`` and to create a cache file that you can use for quickly
processing individual pages:
```
wiktwords --cache-file /tmp/wikt-cache --pages-dir pages enwiktionary-20201201-pages-articles.xml.bz2
```

2. To process a single page, processing a human-readable output file
for debugging:
```
wiktwords --cache-file /tmp/wikt-cache --all --all-languages --out outfile --page pages/Words/di/dictionary.txt
```

The following command-line options can be used to control its operation:

* --out FILE: specifies the name of the file to write (specifying "-" as the file writes to stdout)
* --all-languages: extract words for all available languages
* --language LANGUAGE: extracts the given language (this option may be specified multiple times; by default, English and Translingual words are extracted)
* --list-languages: prints a list of supported language names
* --all: causes all data to be captured for the selected languages
* --translations: causes translations to be captured
* --pronunciation: causes pronunciation information to be captured
* --linkages: causes linkages (synonyms etc.) to be captured
* --redirects: causes redirects to be extracted
* --pages-dir DIR: save all wiktionary pages under this directory (mostly for debugging)
* --cache CACHE: save/use cache file(s) from this path
* --num-threads THREADS: use this many parallel processes (needs 4GB/process)
* --human-readable: print human-readable JSON with indentation (no longer
machine-readable)
* --override PATH: override a page or Lua module by this file (first line should be TITLE: pagetitle)
* --help: displays help text (with some more options than listed here)

## Calling the library

While this package has been mostly intended to be used using the ``wiktwords``
program, it is also possible to call this as a library.  Underneath, this uses
the ``wikitextprocessor`` module.

This code can be called from an application as follows:

```
from wiktextract import (WiktionaryConfig, parse_wiktionary, parse_page,
                         PARTS_OF_SPEECH)
from wikitextprocessor import Wtp, ALL_LANGUAGES

config = WiktionaryConfig(
             capture_languages=["English", "Translingual"],
             capture_translations=True,
             capture_pronunciation=True,
             capture_linkages=True,
             capture_compounds=True,
             capture_redirects=True)
ctx = Wtp()

def word_cb(data):
    # data is dictionary containing information for one word/redirect
    ... do something with data

parse_wiktionary(ctx, path, config, word_cb)
```

#### def parse_wiktionary(ctx, path, config, word_cb, capture_cb=None, phase1_only=False)

The ``parse_wiktionary`` function will call ``word_cb(data)`` for
words and redirects found in the Wiktionary dump.  ``data`` is
information about a single word and part-of-speech as a dictionary and
may include several word senses.  It may also be a redirect (indicated
by the presence of a "redirect" key in the dictionary).  It is in the same
format as the JSON-formatted dictionaries returned by the
``wiktwords`` tool.

Its arguments are as follows:
* ``ctx`` (Wtp) - a
  [wikitextprocessor](https://github.com/tatuylonen/wikitextprocessor/)
  processing context.  The number of parallel processes to use can be
  given as the ``num_threads`` argument to the constructor, and a cache file
  path can be provided as the ``cache_file`` argument.
* ``path`` (str) - path to a Wiktionary dump file (*-pages-articles.xml.bz2)
* ``config`` (WiktionaryConfig) - a configuration object describing what to
  exctract (see below)
* ``word_cb`` (function) - this function will be called for every word
  extracted from Wiktionary.  The argument is a dictionary.  Typically it
  will be called once for each word form and part-of-speech (each time there
  may be more than one word sense under "senses").  See below for a description
  of the dictionary.
* ``capture_cb`` (function) - this can be ``None`` or a function to be
  called as ``capture_cb(model, title, text)`` for every page before
  extracting any words from it.  It can be used to extract raw pages
  to disk.  The ``model`` argument is ``wikitext`` for normal pages,
  ``Scribunto`` for Lua modules, and ``redirect`` for redirects (other
  values are also possible).  ``title`` is page title and ``text`` is
  page content or page title to redirect to.
* ``phase1_only`` - if this is set to ``True``, then only a cache file will
  be created but no extraction will take place.  In this case the ``Wtp``
  constructor should probably be given the ``cache_file`` argument when
  creating ``ctx``.

This call gathers statistics in ``config``.  This function will automatically
parallelize the extraction.  ``page_cb`` will be called in the parent process,
however.

#### def parse_page(ctx, title, text, config)

This function parses ``text`` as if it was a Wiktionary page with the
title ``title``.  The arguments are:
* ``ctx`` (Wtp) - a ``wikitextprocessor`` context
* ``title`` (str) - the title to use for the page
* ``text`` (str) - contents of the page (wikitext)
* ``config`` (WiktionaryConfig) - specifies what to capture and is also used
  for collecting statistics

#### PARTS_OF_SPEECH

This is a constant set of all part-of-speech values (``pos`` key) that
may occur in the extracted data.  Note that the list is somewhat larger than
what a conventional part-of-speech list would be.

### class WiktionaryConfig(object)

The ``WiktionaryConfig`` object is used for specifying what data to collect
from Wiktionary and is also used for collecting statistics during
extraction.

The constructor is called as:
```
WiktionaryConfig(capture_languages=["English", "Translingual",
                 capture_translations=False,
                 capture_pronunciation=False,
                 capture_linkages=False,
                 capture_compounds=False,
                 capture_redirects=False,
                 capture_examples=False)
```

The arguments are as follows:
* ``capture_languages`` (list/tuple/set of strings) - names of
  languages for which to capture data.  It defaults to ``["English",
  "Translingual"]``.  To capture all languages, one can use
  ``set(x["name"] for x in ALL_LANGUAGES)`` (with ``ALL_LANGUAGES``
  imported from wikitextprocessor).
* ``capture_translations`` (boolean) - set to ``True`` to capture translation
  information for words.  Translation information seems to be most
  widely available for the English language, which has translations into
  other languages.
* ``capture_pronunciation`` (boolean) - set to ``True`` to capture pronunciation
  information for words.  Typically, this includes IPA transcriptions
  and any audio files included in the word entries, along with other
  information.  The type and amount of pronunciation
  information varies widely between languages.
* ``capture_linkages`` (boolean) - set to ``True`` to capture linkages between
  word, such as hypernyms, antonyms, synonyms, etc.
* ``capture_compounds`` (boolean) - set to ``True`` to capture compound words
  containing the word.
* ``capture_redirects`` (boolean) - set to ``True`` to capture
  redirects.  Redirects are not associated with any specific language
  and thus requesting them returns them for all words in all languages.
* ``capture_examples`` (boolean) - set to ``True`` to capture usage examples
  (XXX currently not implemented).

## Format of extracted redirects

Some pages in Wiktionary are redirects.  For these, ``word_cb`` will
be called with data in a special format.  In this case, the dictionary
will have a ``redirect`` key, which will contain the page title that
the entry redirects to.  The ``title`` key contains the word/term that
contains the redirect.  Redirect entries do not have ``pos`` or any of
the other fields.  Redirects also are not associated with any
language, so all redirects are always returned regardless of the
captured languages (if extracting redirects has been requested).

## Format of the extracted word entries

Information returned for each word is a dictionary.  The dictionary has the
following keys (others may also be present or added later):

* ``word`` - the word form
* ``pos`` - part-of-speech, such as "noun", "verb", "adj", "adv", "pron", "determiner", "prep" (preposition), "postp" (postposition), and many others.  The complete list of possible values returned by the package can be found in ``wiktextract.PARTS_OF_SPEECH``.
* ``lang`` - name of the language this word belongs to (e.g., ``English``)
* ``lang_code`` - Wiktionary language code (e.g., ``en``)
* ``senses`` - list of word senses (dictionaries) for this word/part-of-speech (see below)
* ``forms`` - list of inflected or alternative forms specified for the word (e.g., plural, comparative, superlative, roman script version).  This is a list of dictionaries, where each dictionary has a ``word`` key and a ``tags`` key.  The ``tags`` identify what type of form it is.
* ``sounds`` - list of dictionaries containing pronunciation, hyphenation, rhyming, and related information.  Each dictionary may have a ``tags`` key containing tags that clarify what kind of form that entry is.  Different types of information are stored in different fields: ``ipa`` is [IPA](https://en.wikipedia.org/wiki/International_Phonetic_Alphabet) pronunciation, ``enPR`` is [enPR](https://en.wikipedia.org/wiki/Pronunciation_respelling_for_English) pronunciation, ``audio`` is name of sound file in Wikimedia commons.
* ``translations`` - non-disambiguated translation entries (see below)
* ``synonyms`` - non-disambiguated synonym linkages for the word (see below)
* ``antonyms`` - non-disambiguated antonym linkages for the word (see below)
* ``hypernyms`` - non-disambiguated hypernym linkages for the word (see below)
* ``holonyms`` - non-disambiguated linkages indicating being part of something (see below) (not systematically encoded)
* ``meronyms`` - non-disambiguated linkages indicating having a part (see below) (fairly rare)
* ``derived`` - non-disambiguated derived word linkages for the word (see below)
* ``related`` - non-disambiguated related word linkages for the word (see below)
* ``wikidata`` - non-disambiguated Wikidata identifer
* ``wiktionary`` - non-disambiguated page title in Wikipedia (possibly prefixed by language id)
* ``categories`` - list of non-disambiguated categories for the word
* ``topics`` - list of non-disambiguated topics for the word
* ``inflection`` - conjugation and declension entries found for the word, as dictionaries.  These basically capture the language-specific inflection template
for the word.
* ``heads``: part-of-speech specific head tags for the word.  This basically just captures the templates (their name and arguments) as a list of dictionaries.  Most applications may want to ignore this.

There may also be other fields.

Note that several of the field on the word entry level indicate
information that has not been sense-disambiguated.  Such information
may apply to one or more of the senses.  Currently only the most
trivial cases are disambiguated; however, it is anticipated that more
disambiguation may be performed in the future.  It is also possible
for the same key to be provided in a sense and in the word entry; in
that case, the data in the sense has been sense-disambiguated and the
data in the word entry has not (and may not be apply to any particular
sense, regardless of whether the sense has some related
sense-disambiguated information).

### Word senses

Each word entry may have multiple glosses under the ``senses`` key.  Each
sense is a dictionary that may contain the following keys (among others, and more may be added in the future):

* ``glosses`` - list of gloss strings for the word sense (usually only one).  This has been cleaned, and should be straightforward text with no tagging.
* ``nonglosses`` - list of gloss-like strings but that are not traditional glossary entries describing the word's meaning
* ``tags`` - list of qualifiers and tags for the gloss.  This is a list of strings, and may include words such as "archaic", "colloquial", "present", "participle", "plural", "feminine", and many others (new words may appear arbitrarily).  Some effort has been put into trying to canonicalize various sources and styles of annotation into a consistent set of tags, but it is impossible to do an exact job at this.
* ``senseid`` - list of textual identifiers collected for the sense.  If there is a QID for the entry (e.g., Q123), those are stored in the ``wikidata`` field.
* ``wikidata`` - list of QIDs (e.g., Q123) for the sense
* ``wikipedia``- list of Wikipedia page titles (with optional language code prefix)
* ``categories`` - list of category names extracted from (a subset) of the Category links on the page
* ``topics`` - list of topic names (kind of similar to categories but determined differently)
* ``alt_of`` - list of words that his sense is an alternative form of; for example, for an abbreviation, this would typically be set to the full form
* ``form_of`` - list of words that this sense is an inflected form of; for example, a participle form would typically set this to be the base form
* ``translations`` - sense-disambiguated translation entries (see below)
* ``synonyms`` - sense-disambiguated synonym linkages for the word (see below)
* ``antonyms`` - sense-disambiguated antonym linkages for the word (see below)
* ``hypernyms`` - sense-disambiguated hypernym linkages for the word (see below)
* ``holonyms`` - sense-disambiguated linkages indicating being part of something (see below) (not systematically encoded)
* ``meronyms`` - sense-disambiguated linkages indicating having a part (see below) (fairly rare)
* ``derived`` - sense-disambiguated derived word linkages for the word (see below)
* ``related`` - sense-disambiguated related word linkages for the word (see below)

### Linkages to other words

Linkages (``synonyms``, ``antonyms``, ``hypernyms``, ``derived
words``, ``holonyms``, ``meronyms``, ``derived``, ``related``) are
stored in the word's data if not sense-disambiguated, and in the word
sense if sense-disambiguated.  They are lists of dictionaries, where
each dictionary can contain the following keys, among others:

* ``word`` - the word this links to (string).  If this starts with "Thesaurus:", then this entry is a link to a thesaurus page in Wiktionary.  If this starts with "Category:", then this refers to a category page in Wiktionary.
* ``sense`` - text identifying the word sense or context (e.g., ``"to rain very heavily"``).
* ``tags``: qualifiers specified for the sense (e.g., field of study, region, dialect, style).  This is a list of strings.

### Pronunciation

Pronunciation information is stored under the ``sounds`` key.  It is a
list of dictionaries, each of which may contain the following keys,
among others:

* ``ipa`` - pronunciation specifications as IPA strings
* ``enpr`` - pronunciation in English pronunciation respelling
* ``audio`` - name of a sound file in WikiMedia Commons
* ``homophones`` - list of homophones for the word
* ``hyphenation`` - list of hyphenations
* ``tags`` - other labels or context information attached to the sense (e.g., regional variant)

### Translations

Translations are stored under the ``translations`` key in the word's
data (if not sense-disambiguated) or in the word sense (if
sense-disambiguated).  They are stored in a list of dictionaries,
where each dictionary has the following keys (and possibly others):

* ``lang``  the language name that the translation is for
* ``code`` - Wiktionary's 2 or 3-letter language code for the language the translation is for
* ``word`` - the translation in the specified language
* ``sense`` - optional sense for which the translation is (this is a free-text string, and may not match any gloss exactly)
* ``tags`` - optional list of qualifiers for the translations, e.g., gender

## Related packages

The
[wikitextprocessor](https://github.com/tatuylonen/wikitextprocessor)
is a generic module for extracting data from Wiktionary, Wikipedia, and
other WikiMedia dump files.  ``wiktextract`` is built using this module.

The [wiktfinnish](https://github.com/tatuylonen/wiktfinnish) package
can be used to interpret Finnish noun declinations and verb
conjugations and for generating Finnish inflected word forms.

## Related tools

A few other tools also exist for parsing Wiktionaries.  These include
[Dbnary](http://kaiko.getalp.org/about-dbnary/),
[Wikiparse](https://github.com/frankier/wikiparse), and [DKPro
JWKTL](https://dkpro.github.io/dkpro-jwktl/).

## Contributing and reporting bugs

Please report bugs and other issues on github.  I also welcome
suggestions for improvement.

Please email to ``ylo`` at ``clausal.com`` if you wish to contribute
or have patches or suggestions.

## License

Copyright (c) 2018-2020 [Tatu Ylonen](https://ylonen.org).  This
package is free for both commercial and non-commercial use.  It is
licensed under the MIT license.  See the file
[LICENSE](https://github.com/tatuylonen/wiktextract/blob/master/LICENSE)
for details.  (Certain files have different open source licenses)
