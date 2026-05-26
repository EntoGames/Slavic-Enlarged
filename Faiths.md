# Wiara słowiańska — Slavic Enlarged

Rozpiska religii i wszystkich odłamów wiary słowiańskiej (`wsl_slavic`) dodanych przez mod **Slavic Enlarged**.

---

## 🌍 Religia: `wsl_slavic` — Wiara Słowiańska

Główna religia rodzimowiercza, należąca do rodziny `rf_pagan` (religie pogańskie z możliwością reformy).

### Charakterystyka ogólna

| Cecha | Wartość |
|---|---|
| **Rodzina** | `rf_pagan` (pogańska, z reformą) |
| **Pagan roots** | ✅ tak |
| **Hostility** | `pagan_hostility_doctrine` |
| **Grafika** | `pagan_gfx` |

### Cnoty i grzechy

| Cnoty | Grzechy |
|---|---|
| just (sprawiedliwy) | arbitrary (samowolny) |
| gregarious (towarzyski) | shy (nieśmiały) |
| honest (uczciwy) | deceitful (kłamliwy) |

### Hierarchia duchowna i panteon

| Element | Nazwa |
|---|---|
| **Najwyższy bóg** | Perun |
| **Bóg śmierci** | Morana |
| **Bóg czarów** | Weles |
| **Kapłan** | wołchw (l.mn. wołchwowie) |
| **Głowa religii** | Naczelny Wołchw |
| **Pozaświat (dobry)** | Wyraj, Wiecznie Zielone Pola, Kraina Przodków |
| **Pozaświat (zły)** | Nawia, Mroczna Kraina, Zaświaty |

### Zakony rycerskie

| Zakon | Charakter |
|---|---|
| Wojownicy Peruna (`holy_order_warriors_of_perun`) | bojowy, kult Peruna |
| Strażnicy Welesa (`holy_order_guardians_of_veles`) | tajemny, kult Welesa |

Główny typ jednostek zakonów: **konni łucznicy** (`horse_archers`).

---

## 🕊️ Doktryny ogólne religii

Wszystkie 5 odłamów dziedziczy poniższe doktryny:

### Teologia
- `doctrine_polytheist` — politeizm
- `doctrine_no_head` — brak jednej głowy religii (przed reformą)
- `doctrine_gender_equal` — równouprawnienie płci
- `doctrine_pluralism_righteous` — pluralizm sprawiedliwy
- `doctrine_theocracy_temporal` — teokracja świecka

### Małżeństwo i obyczaje
- `doctrine_monogamy` — monogamia
- `doctrine_divorce_allowed` — rozwód dozwolony
- `doctrine_bastardry_none` — brak konceptu bękartów
- `doctrine_consanguinity_unrestricted` — brak ograniczeń pokrewieństwa

### Moralność
- `doctrine_homosexuality_accepted` — homoseksualizm akceptowany
- `doctrine_adultery_men_shunned` / `_women_shunned` — cudzołóstwo potępiane
- `doctrine_kinslaying_close_kin_crime` — zabójstwo bliskich krewnych jest zbrodnią
- `doctrine_deviancy_accepted` — odstępstwa akceptowane
- `doctrine_witchcraft_accepted` — czarostwo akceptowane

### Kapłaństwo
- `doctrine_clerical_function_recruitment` — kapłani rekrutują żołnierzy
- `doctrine_clerical_gender_either` — obie płcie kapłańskie
- `doctrine_clerical_marriage_allowed` — kapłani mogą zawierać małżeństwa
- `doctrine_clerical_succession_temporal_appointment` — wybór kapłana przez władcę

### Rytuały
- `doctrine_pilgrimage_encouraged` — pielgrzymki zalecane
- `doctrine_funeral_cremation` — kremacja
- `doctrine_no_anointment` — brak namaszczenia

---

## ⛪ Odłamy (faiths)

Religia `wsl_slavic` dzieli się na **5 odłamów**:

### 🟢 1. `wsl_slavic_base` — Wiara Słowiańska (bazowa)

> Pierwotna wiara słowiańska, wspólna dla wszystkich Słowian przed regionalnym rozdzieleniem. Oparta na wielkiej trójcy Peruna, Wełesa i Dadźboga.

| Cecha | Wartość |
|---|---|
| **Kolor** | RGB(0.55, 0.70, 0.30) — oliwkowo-zielony |
| **Ikona** | `slavic` |
| **Ikona po reformie** | `slavic_reformed` |
| **Status** | `unreformed_faith_doctrine` |
| **Występowanie w 867** | ❌ **NIE pojawia się na mapie w 867** (rozdzielona między 3 odłamy regionalne) |

**Doktryny szczegółowe:**
- `tenet_ancestor_worship` — kult przodków
- `tenet_sanctity_of_nature` — świętość natury
- `tenet_communal_identity` — tożsamość wspólnoty

**Miejsca święte (5):** Kijów, Arkona, Lwów, Nowogród, Praga

> **Uwaga:** Mimo że bazowa wiara nie pojawia się w dacie startu, jej definicja pozostaje w mocy. Wykorzystywana jest jako historyczny punkt wyjścia i może wystąpić w późniejszych zdarzeniach.

---

### 🔴 2. `wsl_slavic_east` — Wschodnia Wiara Słowiańska

> Wiara wschodniosłowiańskich ludów, gdzie Perun Gromowładny sprawuje najwyższą władzę. Ukształtowana przez stepowe pogranicze i kulturę wojowniczej drużyny.

| Cecha | Wartość |
|---|---|
| **Kolor** | RGB(0.70, 0.25, 0.20) — krwistoczerwony |
| **Ikona** | `wsl_slavic_east` |
| **Status** | `unreformed_faith_doctrine` |
| **Przypisanie 867** | wszystkie hrabstwa `religion:slavic_religion` w `world_europe_east` z pillarem `heritage_east_slavic` |

**Doktryny szczegółowe:**
- `tenet_communal_identity` — tożsamość wspólnoty
- `tenet_ritual_celebrations` — uroczystości rytualne
- `tenet_sanctity_of_nature` — świętość natury

**Miejsca święte (5):** Lwów, Kijów, Mińsk, Nowogród, Połock

---

### 🔵 3. `wsl_slavic_west` — Zachodnia Wiara Słowiańska

> Wiara zachodniosłowiańskich ludów, gdzie Świętowit z Arkony panuje niepodzielnie. Wyróżnia ją niezwykły stopień organizacji kapłańskiej.

| Cecha | Wartość |
|---|---|
| **Kolor** | RGB(0.25, 0.45, 0.75) — niebieski |
| **Ikona** | `wsl_slavic_west` |
| **Status** | `unreformed_faith_doctrine` |
| **Przypisanie 867** | hrabstwa w `world_europe_west_germania` (Połabie, Pomorze) oraz z pillarem `heritage_west_slavic` w `world_europe_east` (Polska, Czechy) |

**Doktryny szczegółowe:**
- `tenet_ancestor_worship` — kult przodków
- `tenet_ritual_celebrations` — uroczystości rytualne
- `tenet_sanctity_of_nature` — świętość natury

**Miejsca święte (5):** Arkona, Płock, Praga, Legnica, Retra

---

### 🟠 4. `wsl_slavic_south` — Południowa Wiara Słowiańska

> Wiara południowosłowiańskich ludów, ukształtowana przez góry i cień Bizancjum. Zadruga jest zarazem rodziną i kongregacją.

| Cecha | Wartość |
|---|---|
| **Kolor** | RGB(0.80, 0.55, 0.15) — pomarańczowo-żółty |
| **Ikona** | `wsl_slavic_south` |
| **Status** | `unreformed_faith_doctrine` |
| **Przypisanie 867** | wszystkie hrabstwa `religion:slavic_religion` w `world_europe_south_east` |

**Doktryny szczegółowe:**
- `tenet_false_conversion_sanction` — sankcja za fałszywą konwersję (presja bizantyjska)
- `tenet_ritual_celebrations` — uroczystości rytualne
- `tenet_sanctity_of_nature` — świętość natury

**Miejsca święte (5):** Welbażd, Tolna, Ston, Bârlad, Szerem

---

### 🟣 5. `wsl_slavic_unified` — Wszechsłowiańska Wiara (zreformowana)

> Wielka synteza: zjednoczona, zinstytucjonalizowana wiara obejmująca wszystkie trzy odłamy słowiańskiego pogaństwa.

| Cecha | Wartość |
|---|---|
| **Kolor** | RGB(0.45, 0.60, 0.20) — zielony |
| **Ikona** | `slavic_reformed` |
| **Status** | ✅ **ZREFORMOWANA** (brak `unreformed_faith_doctrine`) |
| **Dostęp** | poprzez decyzję `wsl_reform_panslavic_faith` |

**Doktryny szczegółowe:**
- `tenet_ancestor_worship` — kult przodków
- `tenet_sanctity_of_nature` — świętość natury
- `tenet_warmonger` — kult wojny (zastępuje regionalne tenety)

**Miejsca święte (15) — wszystkie miejsca z wszystkich 3 odłamów regionalnych**

#### Warunki reformy panslawistycznej:
- Tytuł co najmniej królestwa (`highest_held_title_tier >= tier_kingdom`)
- Piety ≥ 2000
- Prestige ≥ 1500
- Kontrola wszystkich miejsc świętych dzielonych (wsl_controls_shared_holy_sites_trigger)
- Kontrola wszystkich miejsc świętych regionalnych (wsl_controls_regional_holy_sites_trigger)
- Osiągnięty próg słowiańskich pogan (`wsl_pagan_slavs_threshold_trigger`)

---

## 🛕 Miejsca święte (15 łącznie)

### 🔴 Wschodnie (5)
| Klucz | Hrabstwo | Bonus modyfikatorów |
|---|---|---|
| `wsl_site_lviv` | c_lviv (Lwów) | +5% pobożność |
| `wsl_site_kyiv` | c_kiev (Kijów) | **+8% pobożność, +5% prestiż** |
| `wsl_site_minsk` | c_minsk (Mińsk) | +5% pobożność |
| `wsl_site_novgorod` | c_novgorod (Nowogród) | +6% pobożność, +3% prestiż |
| `wsl_site_polotsk` | c_polotsk (Połock) | +5% pobożność |

### 🔵 Zachodnie (5)
| Klucz | Hrabstwo | Bonus modyfikatorów |
|---|---|---|
| `wsl_site_arkona` | c_rugen (Rugia) | **+8% pobożność, +5% prestiż** |
| `wsl_site_plocka` | c_plocka (Płock) | +5% pobożność, +3% prestiż |
| `wsl_site_praha` | c_praha (Praga) | +5% pobożność, +3% prestiż |
| `wsl_site_legnica` | c_legnica (Legnica) | +5% pobożność |
| `wsl_site_retra` | c_mecklenburg (Retra) | +6% pobożność |

### 🟠 Południowe (5)
| Klucz | Hrabstwo | Bonus modyfikatorów |
|---|---|---|
| `wsl_site_velbazhd` | c_velbazhd (Welbażd) | +5% pobożność, +3% prestiż |
| `wsl_site_tolna` | c_tolna (Tolna) | +4% pobożność |
| `wsl_site_ston` | c_zachlumia (Ston) | +4% pobożność, +2% prestiż |
| `wsl_site_barlad` | c_barlad (Bârlad) | +4% pobożność |
| `wsl_site_szerem` | c_szerem (Szerem/Srem) | +5% pobożność |

**Najświętsze miejsca:** Kijów i Arkona (oba +8% pobożność, +5% prestiż).

---

## 📋 Logika startu (867)

Skrypt `wsl_assign_starting_faiths_effect` rozdziela wszystkie hrabstwa `religion:slavic_religion` w 4 krokach:

| Krok | Reguła | Wynik |
|---|---|---|
| 1a | hrabstwa w `world_europe_west_germania` | → `wsl_slavic_west` |
| 1b | hrabstwa w `world_europe_south_east` | → `wsl_slavic_south` |
| 1c | hrabstwa w `world_europe_east` z pillarem zachodnim | → `wsl_slavic_west` |
| 1d | reszta hrabstw w `world_europe_east` | → `wsl_slavic_east` |
| 2 | końcowe zabezpieczenie: pozostałe hrabstwa wg pillara, fallback → east | |
| 3 | władcy słowiańscy: wiara ze stolicy (`capital_county.title_province.faith`) | |
| 4 | postacie bezziemne wciąż mające `wsl_slavic_base` → konwersja wg pillara | |

**Efekt:** w dacie 867 wiara `wsl_slavic_base` **NIE pojawia się** ani na mapie ani u postaci.

---

## 🎨 Tabela porównawcza odłamów

| Cecha | base | east | west | south | unified |
|---|---|---|---|---|---|
| **Kolor** | 🟢 oliwka | 🔴 czerwień | 🔵 niebieski | 🟠 pomarańcz | 🟣 zieleń |
| **Zreformowana** | ❌ | ❌ | ❌ | ❌ | ✅ |
| **Miejsc świętych** | 5 | 5 | 5 | 5 | **15** |
| **W 867 na mapie** | ❌ | ✅ | ✅ | ✅ | ❌ |
| **Tenet 1** | ancestor_worship | communal_identity | ancestor_worship | false_conversion_sanction | ancestor_worship |
| **Tenet 2** | sanctity_of_nature | ritual_celebrations | ritual_celebrations | ritual_celebrations | sanctity_of_nature |
| **Tenet 3** | communal_identity | sanctity_of_nature | sanctity_of_nature | sanctity_of_nature | warmonger |

---

## 📁 Lokalizacja plików

| Plik | Co zawiera |
|---|---|
| `common/religion/religion_types/wsl_slavic_faiths.txt` | Definicja religii `wsl_slavic` i 5 odłamów |
| `common/religion/holy_site_types/wsl_holy_sites.txt` | Definicje 15 miejsc świętych |
| `common/scripted_effects/wsl_startup_effects.txt` | Logika rozdziału wiar w 867 |
| `common/decisions/wsl_religious_decisions.txt` | Decyzja `wsl_reform_panslavic_faith` |
| `common/modifiers/wsl_modifiers.txt` | Modyfikator dynastyczny `wsl_modifier_unifier_of_faiths` |
| `localization/polish/wsl_faiths_l_polish.yml` | Tłumaczenia PL |
| `localization/english/wsl_faiths_l_english.yml` | Tłumaczenia EN |
