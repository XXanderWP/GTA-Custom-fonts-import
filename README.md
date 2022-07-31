# GTA Custom fonts import

A utility that speeds up the connection of third-party fonts in GTA (FiveM, Rage, etc.)

# Usage example

```
python .\run.py Oswald.ttf
```

Oswald - is example font name. You can use any font

# Output file

`Oswald.gfx`

# Import result

FiveM: Move result file to stream folder<br/>
Rage: Understand yourself or go to FiveM

# Use font (FiveM)

```JS
// JS
RegisterFontFile('Oswald');

const OswaldFont = RegisterFontId('Oswald');
```

```LUA
-- LUA
RegisterFontFile('Oswald');
local OswaldFont = RegisterFontId('Oswald');
```
