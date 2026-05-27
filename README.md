# Projekt 2 – Bulls & Cows

Implementace zadání ze souboru `2 (z wordu).pdf`. Program je jednoduchá
konzolová hra, ve které počítač vygeneruje tajné čtyřciferné číslo a hráč
postupně hádá správnou kombinaci.

Po každém pokusu aplikace vrátí:

- `bull(s)` – správná číslice na správné pozici,
- `cow(s)` – správná číslice na špatné pozici.

## Soubory

- `main.py` – kompletní implementace hry
- `README.md` – dokumentace ke spuštění a chování
- `2 (z wordu).pdf` – čitelnější varianta zadání

> Pozn.: Vlastní řešení zůstává v jediném souboru `main.py`, aby odpovídalo
> omezení zadání.

## Požadavky

- Python 3.10+
- bez externích knihoven

## Spuštění

```bash
cd /root/projekty/powerbi/2
python3 main.py
```

## Pravidla hry

- tajné číslo má přesně 4 číslice,
- číslice jsou unikátní,
- první číslice není nula,
- nula se může objevit na jiné než první pozici,
- hráč zadává tipy tak dlouho, dokud číslo neuhodne.

## Validace vstupu

Program po každém tipu kontroluje:

- správnou délku 4,
- že vstup obsahuje pouze číslice,
- že nezačíná nulou,
- že neobsahuje duplicitní číslice.

Při chybě vypíše přehlednou hlášku a vyžádá si nový tip místo ukončení hry.

## Ukázka hry

Příklad z PDF s tajným číslem `2017`:

```text
Hi there!
-----------------------------------------------
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
-----------------------------------------------
Enter a number:
-----------------------------------------------
>>> 1234
0 bulls, 2 cows
-----------------------------------------------
>>> 6147
1 bull, 1 cow
-----------------------------------------------
>>> 2417
3 bulls, 0 cows
-----------------------------------------------
>>> 2017
Correct, you've guessed the right number
in 4 guesses!
-----------------------------------------------
That's amazing!
```

## Struktura řešení

`main.py` je rozdělený do menších funkcí s jedním jasným úkolem:

- `generate_secret()` – vygeneruje tajné číslo bez duplicit a bez nuly na začátku,
- `validate_guess()` – vrátí chybovou zprávu nebo `None`,
- `count_bulls_cows()` – spočítá bulls a cows bez dvojího započítání bulls,
- `word()` – zajistí správné jednotné a množné číslo,
- `print_intro()` – vypíše úvodní text hry,
- `main()` – řídí herní smyčku a ukončení po úspěšném uhodnutí.

## Omezení zadání

- zdrojový kód aplikace zůstává v `main.py`,
- `2/main.py` má 84 řádků, takže splňuje limit max 150 řádků,
- hra se nespouští při importu modulu, pouze při přímém spuštění přes
  `if __name__ == "__main__":`.

## Ověření

Automatické regresní ověření je v kořenovém souboru
`tests/test_project_2_main.py`.

```bash
cd /root/projekty/powerbi
pytest tests/test_project_2_main.py -q
```
