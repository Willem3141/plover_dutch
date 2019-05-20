# plover_dutch

This is my effort towards constructing a steno system for the Dutch language, using the Ireland layout usually used for writing English. I try to keep this Dutch system as similar as possible to Plover's English system, to minimize confusion between the two. After all, anyone writing in Dutch will probably also have to write in English rather often. However, there are quite a few differences that are necessary to make this system practical.

> **Warning:** this system is not finalized. I am still in the process of finetuning the rules, which also means the description below is permanently out of date. Furthermore, the dictionary is still very small (~1600 entries at the time of writing). I'm adding words as I encounter them, but this is not a very fast process.
>
> If you want to use this system, and you run into problems, feel free to open an issue.


## Vowels

The main vowels are spelt in the same way as in English (that is, vowels that sound the same get the same key).

| Phoneme | Stroke | Remarks |
|:--:|:--:|----|
| a | `A` | short _a_ as in lamp |
| aa | `AE` | long _a_ as in taart, lader |
| e | `E` | short _e_ as in mep |
| ee | `AEU` | long _e_ as in meer, beter |
| i | `EU` | short _i_ as in pit |
| ie | `AOE` | long _i_ as in lied |
| o | `O` | short _o_ as in kop |
| oo | `OE` | long _o_ as in koop, koper |
| u / uu | `U` | short or long _u_, doesn't matter |

Note that, just like in English, this system is phonetic, that is, theoretically the spelling doesn't matter. However, the spelling of Dutch is way more regular than the spelling of English, which makes it easier to be consistent with short and long vowels. In many cases, the choice between long and short is therefore spelling-inspired. For example, the word _planeet_ is stroked with `AE` (long _a_) as `PHRAE/NAEUT`, not with `A` (short _a_), because _pla_ is an open syllable in the spelling (even though in practice, many people say it with a short _a_ anyway. On the other hand, wherever sensible, I do try to put the variants in (in fact, `PHRA/NAEUT` does work as well).

These are the diphtongues:

| Phoneme | Stroke | Remarks |
|:--:|:--:|----|
| au | `AU` | `AU` and `OU` sound the same, and are distinguished by spelling |
| ou | `OU` | |
| ij / ei / aai | `AOEU` | in case of a conflict, the _ei_ spelling gets a `*` |
| oe | `AOU` | |
| oi / ooi / ui | `OEU` | |
| eu | `AO` | also used as a random disambiguator |


## Initial consonants

Mostly the same as in English. The following are different:

| Phoneme | Stroke | Remarks |
|:--:|:--:|----|
| sch | `SH` | |
| schr | `SR` | |
| j | `KWR` | as in jas, not as in jeans |
| ch | `KH` | |
| g | `TKPW` | as in either gas or goal |
| vl | `TPHR` | stroked as _fl_ |
| vr | `TPR` | stroked as _fr_ |
| z | `STKPW` | |


## Final consonants

Here there are some differences. In particular, Dutch has a very common `-en` ending, used for plurals and verb infinitives. This is so common that the `-Z` key is solely used for this ending. So, it is not used for words ending in *-s* or *-z* (the `-S` key is used for those).

Because `-TZ` cannot be stroked (we don't use the Philly shift or stuff like that), as a special rule, we use just `-Z` (for the _-ten_ ending).

| Phoneme | Stroke | Remarks |
|:--:|:--:|----|
| -en | `-Z` | |
| -ten | `-Z` | not `-TZ` because that cannot be done |

Here is an incomplete list of other interesting endings:

| Phoneme | Stroke | Remarks |
|:--:|:--:|----|
| ch / g | `-G` | |
| ng / nk | `-PBG` | in case of a conflict, _nk_ gets a `*` |
| tie / sie | `-GS` | like in actie; this is just for consistency with English |


## Briefs

### Pronominal adverbs

To write [pronominal adverbs](https://en.wikipedia.org/wiki/Pronominal_adverb) in a single stroke, the following system is used.

| | daar- | er- | hier- | waar- | - (suffix) |
|---:|:--:|:--:|:--:|:--:|:--:|
| **-aan** | `DR-N` | `R-N` | `HR-N` | `WR-N` | `-N` | `AEN` |
| **-achter** ||||| `ARG` |
| **-af** ||||| `AF` |
| **-bij** | `DR-B` | `R-B` | `HR-B` | `WR-B` | `-B` | `BAOI` |
| **-binnen** ||||| `BIN` |
| **-boven** ||||| `BOEF` |
| **-buiten** ||||| `BOIN` |
| **-door** | `DR-D` | `R-D` | `HR-D` | `WR-D` | `-D` | `DOER` |
| **-heen** ||||| `HAIN` |
| **-in** | `DR-*N` | `R-*N` | `HR-*N` | `WR-*N` | `-*N` | `N-` |
| **-langs** ||||| `LANGS` |
| **-mee** | `DR-*M` | `R-*M` | `HR-*M` | `WR-*M` | `-*M` | `MAI` |
| **-na** ||||| `NAE` |
| **-naar** | `DR-R` | `R-R` | `HR-R` | `WR-R` | `-R` | `NAER` |
| **-naartoe** | `DR-RT` | `R-RT` | `HR-RT` | `WR-RT` | `-RT` | `NAOU` |
| **-naast** ||||| `NAEFT` |
| **-om** | `DR-M` | `R-M` | `HR-M` | `WR-M` | `-M` | `OM` |
| **-onder** ||||| `N-N` |
| **-op** | `DR-P` | `R-P` | `HR-P` | `WR-P` | `-P` | `OP` |
| **-over** | `DR-*FR` | `R-*FR` | `HR-*FR` | `WR-*FR` | `-*FR` | `OEFR` |
| **-overheen** ||||| `OEFRN` |
| **-tegen** | `DR-G` | `R-G` | `HR-G` | `WR-G` | `-G` | `TAIG` |
| **-tegenover** ||||| `TAIFRG` |
| **-toe** | `DR-T` | `R-T` | `HR-T` | `WR-T` | `-T` | `TAOU` |
| **-tussen** ||||| `TUN` |
| **-tussenuit** ||||| `TOINT` |
| **-uit** ||||| `OIT` |
| **-van** | `DR-FN` | `R-FN` | `HR-FN` | `WR-FN` | `-FN` | `V-` |
| **-vandaan** ||||| `VAND` |
| **-voor** | `DR-FR` | `R-FR` | `HR-FR` | `WR-FR` | `-FR` | `VOER` |
