# plover_dutch

This is my effort towards constructing a steno system for the Dutch language, using the Ireland layout usually used for writing English. I try to keep this Dutch system as similar as possible to Plover's English system, to minimize confusion between the two. After all, anyone writing in Dutch will probably also have to write in English rather often. However, quite a few differences are unavoidable to make this system practical.

> **Warning:** this system is not finalized. I am still in the process of finetuning the rules, which also means the description below is permanently out of date. Furthermore, the dictionary is still pretty small (~7500 entries at the time of writing). I'm adding words as I encounter them, but this is not a very fast process.
>
> If you want to use this system, and you run into problems, feel free to open an issue.


## Installation

To install the plugin, open Plover's built-in Plugins Manager (_Tools > Plugins Manager_). Then click the Git button (the small button to the right of the Install/Update button), in the resulting dialog fill out the repository link `https://github.com/Willem3141/plover_dutch` and click OK.

To switch Plover to the Dutch system, open the settings dialog, and in the _System_ tab change the system to _Dutch Stenotype_. (Tip: you can use the [plover_system_switcher](https://github.com/nsmarkop/plover_system_switcher) plugin to define strokes to switch between Dutch and English. I use `"TK*UFP": {PLOVER:SWITCH_SYSTEM:Dutch Stenotype}"` and `"TKPWHR*EURB": "{PLOVER:SWITCH_SYSTEM:English Stenotype}"` for this purpose.)

You will initially end up with an empty list of dictionaries for the Dutch system. To fix this, download `nl.json` (which takes the place of the original English `main.json`) from this repository and add it to the dictionary list. You can also make a new empty user dictionary to take the place of the English `user.json` (I called mine `nl-user.json`). Any other dictionaries you may be using with the English system (such as `commands.json`) you can also add to the list. The key assignment of the Dutch system is compatible with the English one (see below for details), so these dictionaries should usually just work, unless they happen to conflict with some Dutch strokes.


### For developers

This paragraph is relevant only if you would like to make changes to the Dutch system plugin. In that case, instead of using the Plugins Manager, use the instructions [here](https://plover.readthedocs.io/en/latest/plugin-dev/setup.html#installation) to install the plugin from a local Git clone. In short: clone this repository, `cd` into it, and run `<path_to_plover> -s plover_plugins install -e .`. This way, you can test changes locally.


## Layout

The steno layout is almost identical to the English layout, with the addition of an (optional) no-space key `^` as the upper half of `S-`. Furthermore, the `-Z` key is actually used for the _-en_ ending instead of _-z_, but we'll still refer to this key as `-Z`. More details below.

![image](https://user-images.githubusercontent.com/7533280/123835365-b8e65280-d908-11eb-8068-5969de48b109.png)

*Layout drawing by [Kaoffie](https://github.com/Kaoffie/steno_diags).*


## Vowels

The vowels are assigned like in English by matching pronunciation, not spelling. For example, we stroke Dutch long _ee_ as `AEU` because it sounds like English long _a_ (which is also stroked as `AEU`).


### Pure vowels

| Phoneme | Stroke | Remarks |
|:--:|:--:|----|
| a | `A` | short _a_ as in _lamp_ |
| aa | `AE` | long _a_ as in _taart_, _lader_ |
| e | `E` | short _e_ as in _mep_ |
| ee | `AEU` | long _e_ as in _meer_, _beter_ |
| i | `EU` | short _i_ as in _pit_ |
| ie | `AOE` | long _i_ as in _lied_ |
| o | `O` | short _o_ as in _kop_ |
| oo | `OE` | long _o_ as in _koop_, _koper_ |
| u / uu | `U` | short or long _u_ as in _hut_, _nu_, _huur_ |

Note that, just like in English, this system is phonetic, that is, theoretically the spelling doesn't matter. For English loans, we generally prefer to use the English strokes, so *hacken* is written with `A`, not `E` (in this case, plus `*` to avoid conflict with *hakken*). The spelling of Dutch has precise rules regarding short and long vowels, but the pronunciation is often not so clear, especially in unstressed syllables. For example, the word _planeet_ ‘should’ be stroked with `AE` (long _a_), not with `A` (short _a_), because the _a_ is long according to the spelling because _pla_ is an open syllable in the spelling. In practice, however, the pronunciation with a short _a_ is common as well, so in these cases, I try to put both the short and long variants in the dictionary.


### Diphthongs

| Phoneme | Stroke | Remarks |
|:--:|:--:|----|
| ui | `AU` | as in _huis_ |
| ou | `OU` | as in _auto_, _hout_ |
| ij / ei / aai | `AOEU` | as in _baai_, _rijk_, _reis_, in case of conflicts usually the _ei / aai_ spelling gets the `*` |
| oe | `AOU` | as in _hoed_ |
| oi / oei / ooi | `OEU` | as in _hoi_, _mooi_, _roei_, in case of conflicts usually the _oei / ooi_ spelling gets the `*` |
| eu | `AO` | as in _keus_ |


### Some extra rules

* In Dutch an *-r* sound after a vowel tends to ‘color’ that vowel to sound slightly different. We ignore this effect when determining which vowel keys to stroke a word with, rather just following the spelling. So _deur_ is written with `AO`, even though it may sound more like `U`.

* If a word ends in *-ij* we often stroke it as a short _i_ (`EU`) instead of `AOEU`. This corresponds to the English system using `EU` for words that end in *-y*, and helps work around several conflicts (e.g., *mij* with `EU`, *mei* with `AOEU`, and *maai* with `AO*EU`).

* `AO` is used pretty consistently for prefix strokes (see below).


## Initial consonants

As these are mostly the same as in English, we'll just describe the differences:

| Phoneme | Stroke | Remarks |
|:--:|:--:|----|
| ch | `KH` | |
| sch | `SKH` | |
| schr | `SKHR` | |
| j | `KWR` | for the default Dutch _j-_ sound, which sounds like English _y-_; `SKWR` is still used for loans like _jeans_ |
| g | `TKPW` | as in either _gas_ or _goal_ |
| vl | `TPHR` | stroked as _fl_ |
| vr | `TPR` | stroked as _fr_ |
| z | `STKPW` | not `S*` like in English, as that results in many conflicts |
| zw | `SW` | stroked as _sw_ |


## Final consonants

Here there are some differences. In particular, Dutch has a very common `-en` ending, used for plurals and verb infinitives. This is so common that the `-Z` key is solely used for this ending. So, it is not used for words ending in *-s* or *-z* (the `-S` key is used for those).

Because `-TZ` cannot be easily stroked, we use just `-Z` (for the _-ten_ ending). Similarly, because `-SD` cannot be easily stroked (for words ending on _-ds_), we use `-TS` instead.

| Phoneme | Stroke | Remarks |
|:--:|:--:|----|
| -en | `-Z` | |
| -ten | `-Z` | not `-TZ` |
| -ds | `-TS` | not `-SD` |

Like in English, we use `-F` as a substitute for `-S` if required, so words on _-st_ generally use `-FT` (or sometimes `*S` in the case of a conflict like _lift_ / _list_). When adding _-en_ to such a word, `-F` stays even though we drop `-T`: _kost_ `KOFT`, _kosten_ `KOFZ` (not `KOSZ`).

Here is an incomplete list of other interesting endings:

| Phoneme | Stroke | Remarks |
|:--:|:--:|----|
| ch / g | `-G` | in case of conflicts usually the _ch_ spelling gets the `*` |
| lijk / ling / lig | `-LG` | see suffixes below for details |
| ng / nk | `-PBG` | in case of a conflict, _nk_ gets a `*`, or we use `-PG` instead for _nk_; see suffixes below for details |
| tie / sie | `-GS` | like in actie; this is just for consistency with English |
| je / tje / pje / kje | `-PG` | |
| w | `-FRPB` | after _u_, such as _duw_, _eeuw_, _lauw_ |


## Prefixes and suffixes

### Prefixes with `AO`

To make prefixes, replace the vowel with `AO`. This works for almost all prepositions. There are a few special cases, such as _in-_ `IN` (because _in_ `N-`, again, like in English). Also note the conflict _door-_ `DAOR` / _deur_ `DAO*R`.


### _-e_ for adjectives

For almost all adjectives, adding `*` results in the conjugated _-e_ form. So _mooi_ `MOI`, _mooie_ `MO*I`. This gives rise to some conflicts (_bange_ / _bank_), and in these cases we usually moved the word with _-nk_ to `-PG` instead. So _bang_ `BANG`, _bange_ `BA*NG`, _bank_ `BAPG`. This also works for past participles used as adjectives. For nouns ending in _-e_ (such as _schede_), the `*` is also often used.


### The _ge-_ prefix

The prefix for past participles _ge-_ is very common, so for many verbs we allow adding _ge-_ by just adding `G-` (= `TKPW-`) if possible, so _gehad_ `GHAD`. If `TKPW-`is already occupied, you can often just add `K-` to indicate _ge-_, so _geweest_ `KWAIFT`. If the verb starts with _s-_ or _z-_, we generally use `SK-`. All of these can cause conflicts however, for example _geleden_ / _gleden_. In case of doubt, just use the `GE-` prefix as a separate stroke.

Another common pattern is that in the case of separable verbs, the separable prefix gets placed in front of _ge-_, for example _uitglijden_ becomes _uitgegleden_. It would be inconvenient to have to write _uit- ge- gleden_ as three separate strokes. Therefore for all separable verb prefixes, it is possible to add `-G` on the right side to make variants with _-ge_ attached, so we would write _uitgegleden_ as _uitge- gleden_ `AOGT/GLAIDZ`.


### Diminutives

`-PG` adds _-(t/p/k)je_ to make diminuties. For some very common diminutives we allow folding that in (_eentje_ `AIPG`).


### The `-LG` suffix

`-LG` is primarily used for _-lijk_ (_gevaarlijk_ `KWAERLG`), but also for _-ling_ (_leerling_ `LAIRLG`) and _-lig_ (_woelig_ `WAOULG`).


## Connecting words

Compound nouns can in principle be created arbitrarily in Dutch, so it is impossible to put them all in the dictionary. The standard way to connect two words together is `TK-LS` (_brandweer_ `BRAND/TK-LS/WAEUR`), but this is not very stroke-efficient. Therefore the top half of the `S-` key is named `^` and it serves to remove the space before the currently stroked word (so _brandweer_ `BRAND/^WAEUR`).

You may be used to using the top half of `S-` for the _s-_ sound already. Also, Plover currently does not officially support prefix keys, which makes it necessary to use [nimble0's branch](https://github.com/openstenoproject/plover/issues/974). Therefore, the `^` key is an optional feature.
