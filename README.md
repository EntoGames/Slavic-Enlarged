# Slavic Enlarged

> Mod do **Crusader Kings III** rozbudowujący świat słowiański — 35 kultur, 4 odłamy wiary i system nagród za reformację oparty na kontroli miejsc świętych.
> A **Crusader Kings III** mod enriching the Slavic world — 35 cultures, 4 faith branches and a holy-site-driven reformation reward system.

**Wersja / Version:** 1.0.0 · **Gra / Game:** CK3 `1.19.*` · **Tagi / Tags:** Culture · Religion · Events

---

## Spis treści / Table of Contents

- [Polski](#-polski)
- [English](#-english)
- [Języki / Languages](#-języki--languages)
- [Kompatybilność / Compatibility](#-kompatybilność--compatibility)

---

## Polski

### O modzie

**Slavic Enlarged** zastępuje ogólne kultury słowiańskie w podstawce historycznymi plemionami i nadaje słowiańskiemu pogaństwu trójdzielną strukturę regionalną z własną mechaniką reformacji.

---

### Kultury — 31 nowych + 4 korekty waniliowe

#### Wschodnie (heritage_east_slavic)
| Kultura | Obszar | Ethos |
|---|---|---|
| Krivichians | Smolensk, Psków | communal |
| Vyatichi | Górna Oka | communal |
| Drevlyans | Puszcze nad Prypecią | stoic |
| Dregovichs | Błota Prypeckie, Górny Niemen | communal |
| Polyans | Kijów, Perejasław | courtly |
| Ulichs | Dolny Dniepr, Południowy Bug | bellicose |
| Radimichs | Dorzecze Soży | communal |
| Polochans | Księstwo Połockie | courtly |
| Severian | Czernihów, dorzecze Desny | stoic |
| Tivertsi | Dorzecze Dniestru | stoic |
| Ilmenian | Nowogród, Jezioro Ilmen | communal |

#### Południowe (heritage_south_slavic)
| Kultura | Obszar | Ethos |
|---|---|---|
| Travunians | Trebinje | stoic |
| Docleani | Duklja, Czarnogóra | stoic |
| Timocani | Dolina Timoku | stoic |
| Branicevci | Branicevo | stoic |
| Smolyani | Rodopy | stoic |
| Pannonian Slavs | Balatonu, Zalavár | bureaucratic |
| Draguvites | Macedonia, Strymon | communal |

#### Zachodnie i Połabskie (heritage_west_slavic)
| Kultura | Obszar | Ethos |
|---|---|---|
| Polans | Wielkopolska | courtly |
| Goplans | Okolice Gopła | communal |
| Mazovians | Mazowsze | communal |
| Kashubians | Gdańsk Pomorze | communal |
| Nitrianians | Nitra | spiritual |
| Hevelli | Dolina Haweli | courtly |
| Wagrians | Wagria, Holstein | stoic |
| Obodrites | Meklenburgia | bellicose |
| Lutici | Wolgast, Prenzlau | bellicose |
| Rani | Wyspa Rugia | bellicose |
| Sorbian | Miśnia, Łużyce | communal |
| Drevani | Wendland, Altmarka | stoic |

#### Korekty waniliowe (+4)
- **Vistulan** — Kraków, Małopolska (reassignment z polskiej)
- **Silesian** — Górny i Dolny Śląsk (reassignment z polskiej)
- **Pommeranian** — korekta tradycji (hussar → stand_and_fight)
- **Croatian / Serbian / Carantanian** — korekty tradycji i języka

---

### Religia — 4 wiary słowiańskie

Wszyscy słowiańscy poganie w 867 startują w jednym z **trzech odłamów regionalnych**. Czwarta wiara — **pradawna** (`se_slavic_base`) — reprezentuje wspólny korzeń wszystkich odłamów, łączy wszystkie 15 miejsc świętych, ale w 867 nikt jej nie wyznaje. Wszystkie cztery wiary są **niezreformowane** — każdą można zreformować waniliowym przyciskiem.

#### Odłamy i ich unikalne tenety
| Wiara | Region | Unikalne tenety |
|---|---|---|
| **Wschodnia** `se_slavic_east` | Ruś, Połocie | ancestor worship · ritual celebrations · sanctity of nature |
| **Zachodnia** `se_slavic_west` | Połabie, Polska, Czechy | warmonger · ritual celebrations · sanctity of nature |
| **Południowa** `se_slavic_south` | Bałkany | false conversion sanction · ritual celebrations · sanctity of nature |
| **Pradawna** `se_slavic_base` | (wspólny korzeń — nikt nie startuje) | ancestor worship · sanctity of nature · communal identity |

Wszystkie wiary są **politeistyczne, egalitarne** (gender_equal), bez głowy Kościoła, ze szkołą klerycką wolną od celibatu. Kremacja, tolerancja dla czarów i zboczenia — standard słowiańskiego pogaństwa.

---

### 15 Miejsc Świętych

#### Wschodnie
| Miejsce | County | Bonus |
|---|---|---|
| Kijów | c_kiev | +8% piety, +5% prestige/mc |
| Lwów | c_lviv | +5% piety/mc |
| Mińsk | c_minsk | +5% piety/mc |
| Nowogród | c_novgorod | +6% piety, +3% prestige/mc |
| Połock | c_polotsk | +5% piety/mc |

#### Zachodnie
| Miejsce | County | Bonus |
|---|---|---|
| Arkona (Rugia) | c_rugen | +8% piety, +5% prestige/mc |
| Płock | c_plocka | +5% piety, +3% prestige/mc |
| Praga | c_praha | +5% piety, +3% prestige/mc |
| Legnica | c_legnica | +5% piety/mc |
| Retra (Meklenburgia) | c_mecklenburg | +6% piety/mc |

#### Południowe
| Miejsce | County | Bonus |
|---|---|---|
| Velbazhd | c_velbazhd | +5% piety, +3% prestige/mc |
| Tolna | c_tolna | +4% piety/mc |
| Ston (Zachlumia) | c_zachlumia | +4% piety, +2% prestige/mc |
| Barlad | c_barlad | +4% piety/mc |
| Szerem | c_szerem | +5% piety/mc |

---

### Mechanika Reformacji

Odłamy reformują się **standardowym wanilowym przyciskiem** w menu religii. Gdy reformacja dochodzi do skutku, mod sprawdza ile z 15 słowiańskich miejsc świętych kontrolujesz — i przyznaje stosowną nagrodę lub karę.

#### Trzy progi

| Kontrolujesz | Event | Efekt |
|---|---|---|
| **≥ 9 z 15** | *Święta Ziemia Odpowiedziała* | +500 pobożności, +250 prestiżu · modifier **Wielki Reformator** na 30 lat (+10% piety/mc, +20 opinii u wyznawców) |
| **6 – 8 z 15** | *Wiara Zreformowana* | brak nagrody i kary — stan zerowy |
| **< 6 z 15** | *Wiara Zreformowana w Pośpiechu* | −300 pobożności · modifier **Pochopna Reformacja** na 15 lat (−15% piety/mc, −5% prestige/mc) |

#### Decyzja „Zbadaj Słowiańskie Miejsca Święte"

W zakładce **Decyzje** dostępna jest czysto informacyjna decyzja — bez efektu, bez kosztu. Widoczna tylko dla wyznawców wiary pradawnej (`se_slavic_base`). Kliknij ją przed reformacją, żeby sprawdzić do którego progu należysz. Znaczniki ✅ / ❌ pokazują twój aktualny stan.

---

### Instalacja

1. Subskrybuj mod w **Warsztacie Steam** / **Paradox Mods** lub umieść folder w `Documents/Paradox Interactive/Crusader Kings III/mod/`
2. Włącz **Slavic Enlarged** w launcherze CK3
3. Zalecany start: **867 n.e.**

### Zgłaszanie błędów

Znalazłeś błąd, literówkę lub masz pomysł? **Zostaw komentarz** — czytam wszystkie zgłoszenia. Pomocne informacje: data startu, zaangażowane kultury/wiary, zrzut ekranu lub fragment `error.log`.

### Spodobał się mod?

Zostaw ocenę i podziel się ze znajomymi — to najlepsza motywacja do dalszego rozwoju!

---

## English

### About

**Slavic Enlarged** replaces the base game's broad Slavic cultures with historical tribes and gives Slavic paganism a three-branch regional structure with a holy-site-driven reformation system.

---

### Cultures — 31 new + 4 vanilla corrections

#### Eastern (heritage_east_slavic)
| Culture | Area | Ethos |
|---|---|---|
| Krivichians | Smolensk, Pskov | communal |
| Vyatichi | Upper Oka | communal |
| Drevlyans | Pripyat forests | stoic |
| Dregovichs | Pripyat marshes, Upper Neman | communal |
| Polyans | Kyiv, Pereyaslavl | courtly |
| Ulichs | Lower Dnieper, Southern Bug | bellicose |
| Radimichs | Sozh river basin | communal |
| Polochans | Polotsk principality | courtly |
| Severian | Chernigov, Desna basin | stoic |
| Tivertsi | Dniester basin | stoic |
| Ilmenian | Novgorod, Lake Ilmen | communal |

#### Southern (heritage_south_slavic)
| Culture | Area | Ethos |
|---|---|---|
| Travunians | Trebinje | stoic |
| Docleani | Duklja, Montenegro | stoic |
| Timocani | Timok valley | stoic |
| Branicevci | Branicevo | stoic |
| Smolyani | Rhodopes | stoic |
| Pannonian Slavs | Balaton, Zalavár | bureaucratic |
| Draguvites | Macedonia, Strymon | communal |

#### Western & Polabian (heritage_west_slavic)
| Culture | Area | Ethos |
|---|---|---|
| Polans | Wielkopolska | courtly |
| Goplans | Lake Gopło area | communal |
| Mazovians | Mazovia | communal |
| Kashubians | Gdańsk Pomerania | communal |
| Nitrianians | Nitra | spiritual |
| Hevelli | Havel valley | courtly |
| Wagrians | Wagria, Holstein | stoic |
| Obodrites | Mecklenburg | bellicose |
| Lutici | Wolgast, Prenzlau | bellicose |
| Rani | Rügen island | bellicose |
| Sorbian | Meissen, Lusatia | communal |
| Drevani | Wendland, Altmark | stoic |

#### Vanilla corrections (+4)
- **Vistulan** — Kraków, Lesser Poland (reassigned from Polish)
- **Silesian** — Upper & Lower Silesia (reassigned from Polish)
- **Pommeranian** — tradition fix (hussar → stand_and_fight)
- **Croatian / Serbian / Carantanian** — tradition and language corrections

---

### Religion — 4 Slavic Faiths

All Slavic pagans in 867 start in one of **three regional branches**. A fourth faith — **Ancient** (`se_slavic_base`) — represents the common root of all branches and holds all 15 holy sites, but no character follows it in 867. All four faiths are **unreformed** and can be reformed via the vanilla button.

#### Branches and their unique tenets
| Faith | Region | Unique tenets |
|---|---|---|
| **Eastern** `se_slavic_east` | Ruthenia, Polotia | ancestor worship · ritual celebrations · sanctity of nature |
| **Western** `se_slavic_west` | Polabia, Poland, Bohemia | warmonger · ritual celebrations · sanctity of nature |
| **Southern** `se_slavic_south` | Balkans | false conversion sanction · ritual celebrations · sanctity of nature |
| **Ancient** `se_slavic_base` | (common root — no starting characters) | ancestor worship · sanctity of nature · communal identity |

All faiths are **polytheist, gender-equal**, headless, with married clergy. Cremation, tolerance for witchcraft and deviancy — standard Slavic paganism.

---

### 15 Holy Sites

#### Eastern
| Site | County | Bonus |
|---|---|---|
| Kyiv | c_kiev | +8% piety, +5% prestige/mo |
| Lviv | c_lviv | +5% piety/mo |
| Minsk | c_minsk | +5% piety/mo |
| Novgorod | c_novgorod | +6% piety, +3% prestige/mo |
| Polotsk | c_polotsk | +5% piety/mo |

#### Western
| Site | County | Bonus |
|---|---|---|
| Arkona (Rügen) | c_rugen | +8% piety, +5% prestige/mo |
| Płock | c_plocka | +5% piety, +3% prestige/mo |
| Prague | c_praha | +5% piety, +3% prestige/mo |
| Legnica | c_legnica | +5% piety/mo |
| Retra (Mecklenburg) | c_mecklenburg | +6% piety/mo |

#### Southern
| Site | County | Bonus |
|---|---|---|
| Velbazhd | c_velbazhd | +5% piety, +3% prestige/mo |
| Tolna | c_tolna | +4% piety/mo |
| Ston (Zachlumia) | c_zachlumia | +4% piety, +2% prestige/mo |
| Barlad | c_barlad | +4% piety/mo |
| Szerem | c_szerem | +5% piety/mo |

---

### Reformation Mechanic

Branches reform via the **standard vanilla button** in the religion menu. When the reformation completes, the mod checks how many of the 15 Slavic holy sites you control and fires the appropriate event.

#### Three tiers

| You control | Event | Effect |
|---|---|---|
| **≥ 9 of 15** | *The Sacred Earth Answered* | +500 piety, +250 prestige · **Great Reformer** modifier for 30 years (+10% piety/mo, +20 same-faith opinion) |
| **6 – 8 of 15** | *A Faith Reformed* | no reward, no penalty — neutral outcome |
| **< 6 of 15** | *A Faith Reformed in Haste* | −300 piety · **Hasty Reformer** modifier for 15 years (−15% piety/mo, −5% prestige/mo) |

#### "Assess the Slavic Holy Sites" decision

A purely **informational decision** available in the Decisions tab — no effect, no cost. Only visible to followers of the Ancient faith (`se_slavic_base`). Click it before reforming to check your current tier. ✅ / ❌ markers show your standing at a glance.

---

### Installation

1. Subscribe on the **Steam Workshop** / **Paradox Mods** or drop the folder into `Documents/Paradox Interactive/Crusader Kings III/mod/`
2. Enable **Slavic Enlarged** in the CK3 launcher
3. Recommended start: **867 AD**

### Bug Reports & Feedback

Found a bug, typo, or have an idea? **Leave a comment** — I read every report. Helpful info: start date, cultures/faiths involved, a screenshot or snippet from `error.log`.

### Enjoying the mod?

Drop a rating and share it with friends — it's the best motivation to keep developing!

---

## Języki / Languages

| Język / Language | Kod / Code | Status |
|---|---|---|
| English | `l_english` | natywne / native |
| Polski | `l_polish` | natywne / native |
| Français | `l_french` | tłumaczenie LLM / LLM translation |
| Deutsch | `l_german` | tłumaczenie LLM / LLM translation |
| Español | `l_spanish` | tłumaczenie LLM / LLM translation |

> ⚠️ Tłumaczenia FR / DE / ES zostały wykonane przy pomocy modelu językowego (LLM) i mogą zawierać niedoskonałości — zwłaszcza w nazwach plemion i terminach religijnych. Poprawki od native speakerów są mile widziane w komentarzach!
>
> ⚠️ The FR / DE / ES translations were produced with a large language model (LLM) and may contain imperfections — especially in tribe names and religious terms. Corrections from native speakers are very welcome in the comments!

W pozostałych językach gry mod wyświetla teksty po angielsku (mechanizm zapasowy CK3). / In other game languages the mod falls back to English text (CK3's built-in fallback).

---

## Kompatybilność / Compatibility

- Wymaga / Requires CK3 **`1.19.*`**
- Nadpisuje kilka kultur waniliowych (chorwacka, serbska, pomorska, karyntyjska) — możliwe konflikty z modami zmieniającymi te same kultury. / Overrides a few vanilla cultures (Croatian, Serbian, Pommeranian, Carantanian) — may conflict with mods editing the same cultures.
- Zawiera kulturę `ilmenian` dla zgodności z innymi modami słowiańskimi. / Includes an `ilmenian` culture for compatibility with other Slavic mods.

---

*Dziękuję za grę! / Thanks for playing!*
