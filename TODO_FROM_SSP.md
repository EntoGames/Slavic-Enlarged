# TODO from Slavic Struggle of Perun (SSP)

Sugestie zmian w Slavic Enlarged wynikajace z pracy nad addonem SSP.
Kazdy wpis oznacza cos, co ulatwi integracje lub poprawi mod bazowy.

---

<!-- Dodawaj wpisy ponizej w formacie: -->
<!-- - [ ] Opis problemu / sugestii (data lub faza SSP) -->

- [x] `wsl_is_slavic_pagan_faith_trigger` brakuje `wsl_slavic_unified` — trigger w `common/scripted_triggers/wsl_triggers.txt` wymienia base/east/west/south, ale pomija zreformowaną wiarę unified. Każdy mod korzystający z tego triggera pominie Wszechsłowiańskich wyznawców. (Faza 1 SSP)
- [x] Placeholder triggery nadal zwracają `always = yes` — `wsl_controls_shared_holy_sites_trigger`, `wsl_controls_regional_holy_sites_trigger`, `wsl_pagan_slavs_threshold_trigger` w `common/scripted_triggers/wsl_triggers.txt` nigdy nie zostały zaimplementowane. Nie blokuje SSP, ale mogłyby być użyteczne w przyszłości. (Faza 1 SSP)
