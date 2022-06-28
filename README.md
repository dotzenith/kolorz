<h2 align="center"> ━━━━━━  ❖  ━━━━━━ </h2>

<!-- BADGES -->
<div align="center">
   <p></p>
   
   <img src="https://img.shields.io/github/stars/dotzenith/kolorz?color=F8BD96&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/forks/dotzenith/kolorz?color=DDB6F2&labelColor=302D41&style=for-the-badge">   

   <img src="https://img.shields.io/github/repo-size/dotzenith/kolorz?color=ABE9B3&labelColor=302D41&style=for-the-badge">
   
   <img src="https://badges.pufler.dev/visits/dotzenith/kolorz?style=for-the-badge&color=96CDFB&logoColor=white&labelColor=302D41"/>
   <br>
</div>

<p/>

---

### ❖ Information 

  kolorz is a simple, fast, and extensible python library to facilitate printing colors to terminals that support true color  

  <img src="https://github.com/dotzenith/dotzenith/blob/main/assets/kolorz/kolorz.png" alt="kolorz">

---

### ❖ Installation

> Install from pip
```sh
pip3 install kolorz
```

> Install from source
- First, install [poetry](https://python-poetry.org/)
```sh
git clone https://github.com/dotzenith/kolorz.git
cd kolorz
poetry build
pip3 install ./dist/kolorz-0.2.0.tar.gz
```

### ❖ Usage 

Using the kolorz CLI endpoint to print out all available colorschemes:  

```
$ kolorz
Supported colorschemes: 

catppuccin latte
catppuccin frappe
catppuccin macchiato
catppuccin mocha
dracula
nord
gruvbox
onedark
tokyonight
ayu
palenight
gogh
```

Using the kolorz python interface to print colored output:

```python
from kolorz import make_kolorz

kl = make_kolorz()

print(f"{kl.blue}This is some{kl.end} {kl.orange}output{kl.end}")
```

The following colors are available, but more can be added (more on that later):
```
red
purple
blue
green
orange
yellow
white
```

By default, the colorscheme is set to `catppuccin mocha` but that can be changed to any of the colorschemes listed by `kolorz`. For example:

```python
from kolorz import make_kolorz

kl = make_kolorz("nord")

print(f"{kl.blue}This is some{kl.end} {kl.orange}output{kl.end}")
```

Users can also define their own colorschemes:

```python
from kolorz import kolorz

new_colors = {
    "red": (210, 15, 57),
    "purple": (136, 57, 239),
    "blue": (30, 102, 245),
    "green": (64, 160, 43),
    "orange": (254, 100, 11),
    "yellow": (223, 142, 29),
    "white": (204, 208, 218),
}

kl = make_kolorz(custom=new_colors)

print(f"{kl.blue}This is some{kl.end} {kl.orange}output{kl.end}")
```

> When adding a custom colorscheme, the user is not restricted to just seven colors. The user can define as many colors as they'd like in the dict structure

Adding or overriding a color

```python
from kolorz import make_kolorz, make_kolor

kl = make_kolorz()

# Adding
kl.rosewater = make_kolor((245, 224, 220))

# Overriding
kl.blue = make_kolor((137, 220, 235))

print(f"{kl.rosewater}This is some{kl.end} {kl.blue}output{kl.end}")
```

---

### ❖ What's New? 
0.2.0 - Now using `dotwiz` instead of a custom class

---

<div align="center">

   <img src="https://img.shields.io/static/v1.svg?label=License&message=MIT&color=F5E0DC&labelColor=302D41&style=for-the-badge">

</div>
