---
name: ascii-art
description: "ASCII art: pyfiglet, cowsay, boxes, image-to-ascii."
version: 4.0.0
author: 0xbyt4, Hermes Agent
license: MIT
dependencies: []
platforms: [linux, macos, windows]
metadata:
  hermes:
    tags: [ASCII, Art, Banners, Creative, Unicode, Text-Art, pyfiglet, figlet, cowsay, boxes]
    related_skills: [excalidraw]

---

# ASCII Art Skill

Multiple tools for different ASCII art needs. All tools are local CLI programs or free REST APIs — no API keys required.

## Tool 1: Text Banners (pyfiglet — local)

Render text as large ASCII art banners. 571 built-in fonts.

### Setup

```bash
pip install pyfiglet --break-system-packages -q
```

### Usage

```bash
python3 -m pyfiglet "YOUR TEXT" -f slant
python3 -m pyfiglet "TEXT" -f doom -w 80    # Set width
python3 -m pyfiglet --list_fonts             # List all 571 fonts
```

### Recommended fonts

| Style | Font | Best for |
|-------|------|----------|
| Clean & modern | `slant` | Project names, headers |
| Bold & blocky | `doom` | Titles, logos |
| Big & readable | `big` | Banners |
| Classic banner | `banner3` | Wide displays |
| Compact | `small` | Subtitles |
| Cyberpunk | `cyberlarge` | Tech themes |
| 3D effect | `3-d` | Splash screens |
| Gothic | `gothic` | Dramatic text |

### Tips

- Preview 2-3 fonts and let the user pick their favorite
- Short text (1-8 chars) works best with detailed fonts like `doom` or `block`
- Long text works better with compact fonts like `small` or `mini`

## Tool 2: Text Banners (asciified API — remote, no install)

Free REST API that converts text to ASCII art. 250+ FIGlet fonts. Returns plain text directly — no parsing needed. Use this when pyfiglet is not installed or as a quick alternative.

### Usage (via terminal curl)

```bash
# Basic text banner (default font)
curl -s "https://asciified.thelicato.io/api/v2/ascii?text=Hello+World"

# With a specific font
curl -s "https://asciified.thelicato.io/api/v2/ascii?text=Hello&font=Slant"
curl -s "https://asciified.thelicato.io/api/v2/ascii?text=Hello&font=Doom"
curl -s "https://asciified.thelicato.io/api/v2/ascii?text=Hello&font=Star+Wars"
curl -s "https://asciified.thelicato.io/api/v2/ascii?text=Hello&font=3-D"
curl -s "https://asciified.thelicato.io/api/v2/ascii?text=Hello&font=Banner3"

# List all available fonts (returns JSON array)
curl -s "https://asciified.thelicato.io/api/v2/fonts"
```

### Tips

- URL-encode spaces as `+` in the text parameter
- The response is plain text ASCII art — no JSON wrapping, ready to display
- Font names are case-sensitive; use the fonts endpoint to get exact names
- Works from any terminal with curl — no Python or pip needed

## Tool 3: Cowsay (Message Art)

Classic tool that wraps text in a speech bubble with an ASCII character.

### Setup

```bash
sudo apt install cowsay -y    # Debian/Ubuntu
# brew install cowsay         # macOS
```

### Usage

```bash
cowsay "Hello World"
cowsay -f tux "Linux rules"       # Tux the penguin
cowsay -f dragon "Rawr!"          # Dragon
cowsay -f stegosaurus "Roar!"     # Stegosaurus
cowthink "Hmm..."                  # Thought bubble
cowsay -l                          # List all characters
```

### Available characters (50+)

`beavis.zen`, `bong`, `bunny`, `cheese`, `daemon`, `default`, `dragon`,
`dragon-and-cow`, `elephant`, `eyes`, `flaming-skull`, `ghostbusters`,
`hellokitty`, `kiss`, `kitty`, `koala`, `luke-koala`, `mech-and-cow`,
`meow`, `moofasa`, `moose`, `ren`, `sheep`, `skeleton`, `small`,
`stegosaurus`, `stimpy`, `supermilker`, `surgery`, `three-eyes`,
`turkey`, `turtle`, `tux`, `udder`, `vader`, `vader-koala`, `www`

### Eye/tongue modifiers

```bash
cowsay -b "Borg"       # =_= eyes
cowsay -d "Dead"       # x_x eyes
cowsay -g "Greedy"     # $_$ eyes
cowsay -p "Paranoid"   # @_@ eyes
cowsay -s "Stoned"     # *_* eyes
cowsay -w "Wired"      # O_O eyes
cowsay -e "OO" "Msg"   # Custom eyes
cowsay -T "U " "Msg"   # Custom tongue
```

## Tool 4: Boxes (Decorative Borders)

Draw decorative ASCII art borders/frames around any text. 70+ built-in designs.

### Setup

```bash
sudo apt install boxes -y    # Debian/Ubuntu
# brew install boxes         # macOS
```

### Usage

```bash
echo "Hello World" | boxes                    # Default box
echo "Hello World" | boxes -d stone           # Stone border
echo "Hello World" | boxes -d parchment       # Parchment scroll
echo "Hello World" | boxes -d cat             # Cat border
echo "Hello World" | boxes -d dog             # Dog border
echo "Hello World" | boxes -d unicornsay      # Unicorn
echo "Hello World" | boxes -d diamonds        # Diamond pattern
echo "Hello World" | boxes -d c-cmt           # C-style comment
echo "Hello World" | boxes -d html-cmt        # HTML comment
echo "Hello World" | boxes -a c               # Center text
boxes -l                                       # List all 70+ designs
```

### Combine with pyfiglet or asciified

```bash
python3 -m pyfiglet "HERMES" -f slant | boxes -d stone
# Or without pyfiglet installed:
curl -s "https://asciified.thelicato.io/api/v2/ascii?text=HERMES&font=Slant" | boxes -d stone
```

## Tool 5: TOIlet (Colored Text Art)

Like pyfiglet but with ANSI color effects and visual filters. Great for terminal eye candy.

### Setup

```bash
sudo apt install toilet toilet-fonts -y    # Debian/Ubuntu
# brew install toilet                      # macOS
```

### Usage

```bash
toilet "Hello World"                    # Basic text art
toilet -f bigmono12 "Hello"            # Specific font
toilet --gay "Rainbow!"                 # Rainbow coloring
toilet --metal "Metal!"                 # Metallic effect
toilet -F border "Bordered"             # Add border
toilet -F border --gay "Fancy!"         # Combined effects
toilet -f pagga "Block"                 # Block-style font (unique to toilet)
toilet -F list                          # List available filters
```

### Filters

`crop`, `gay` (rainbow), `metal`, `flip`, `flop`, `180`, `left`, `right`, `border`

**Note**: toilet outputs ANSI escape codes for colors — works in terminals but may not render in all contexts (e.g., plain text files, some chat platforms).

## Tool 6: Image to ASCII Art

Convert images (PNG, JPEG, GIF, WEBP) to ASCII art.

### Option A: ascii-image-converter (recommended, modern)

```bash
# Install
sudo snap install ascii-image-converter
# OR: go install github.com/TheZoraiz/ascii-image-converter@latest
```

```bash
ascii-image-converter image.png                  # Basic
ascii-image-converter image.png -C               # Color output
ascii-image-converter image.png -d 60,30         # Set dimensions
ascii-image-converter image.png -b               # Braille characters
ascii-image-converter image.png -n               # Negative/inverted
ascii-image-converter https://url/image.jpg      # Direct URL
ascii-image-converter image.png --save-txt out   # Save as text
```

### Option B: jp2a (lightweight, JPEG only)

```bash
sudo apt install jp2a -y
jp2a --width=80 image.jpg
jp2a --colors image.jpg              # Colorized
```

## Tool 7: Search Pre-Made ASCII Art

Search curated ASCII art from the web. Use `terminal` with `curl`.

### Source A: ascii.co.uk (recommended for pre-made art)

Large collection of classic ASCII art organized by subject. Art is inside HTML `<pre>` tags. Fetch the page with curl, then extract art with a small Python snippet.

**URL pattern:** `https://ascii.co.uk/art/{subject}`

**Step 1 — Fetch the page:**

```bash
curl -s 'https://ascii.co.uk/art/cat' -o /tmp/ascii_art.html
```

**Step 2 — Extract art from pre tags:**

```python
import re, html
with open('/tmp/ascii_art.html') as f:
    text = f.read()
arts = re.findall(r'<pre[^>]*>(.*?)</pre>', text, re.DOTALL)
for art in arts:
    clean = re.sub(r'<[^>]+>', '', art)
    clean = html.unescape(clean).strip()
    if len(clean) > 30:
        print(clean)
        print('\n---\n')
```

**Available subjects** (use as URL path):
- Animals: `cat`, `dog`, `horse`, `bird`, `fish`, `dragon`, `snake`, `rabbit`, `elephant`, `dolphin`, `butterfly`, `owl`, `wolf`, `bear`, `penguin`, `turtle`
- Objects: `car`, `ship`, `airplane`, `rocket`, `guitar`, `computer`, `coffee`, `beer`, `cake`, `house`, `castle`, `sword`, `crown`, `key`
- Nature: `tree`, `flower`, `sun`, `moon`, `star`, `mountain`, `ocean`, `rainbow`
- Characters: `skull`, `robot`, `angel`, `wizard`, `pirate`, `ninja`, `alien`
- Holidays: `christmas`, `halloween`, `valentine`

**Tips:**
- Preserve artist signatures/initials — important etiquette
- Multiple art pieces per page — pick the best one for the user
- Works reliably via curl, no JavaScript needed

### Source B: GitHub Octocat API (fun easter egg)

Returns a random GitHub Octocat with a wise quote. No auth needed.

```bash
curl -s https://api.github.com/octocat
```

## Tool 8: Fun ASCII Utilities (via curl)

These free services return ASCII art directly — great for fun extras.

### QR Codes as ASCII Art

```bash
curl -s "qrenco.de/Hello+World"
curl -s "qrenco.de/https://example.com"
```

### Weather as ASCII Art

```bash
curl -s "wttr.in/London"          # Full weather report with ASCII graphics
curl -s "wttr.in/Moon"            # Moon phase in ASCII art
curl -s "v2.wttr.in/London"       # Detailed version
```

## Tool 7: ASCII Video (absorbed from `ascii-video`)

Convert video/audio files to colored ASCII MP4/GIF animations.

### Installation

```bash
# Primary: gif-for-cli (uses ffmpeg + ImageMagick)
pip install gif-for-cli

# Alternative: ascii-video (Node.js)
npm install -g ascii-video
```

### Usage (gif-for-cli)

```bash
# Convert video to ASCII GIF
gif-for-cli input.mp4 --output output.gif

# Set dimensions and FPS
gif-for-cli input.mp4 -W 120 -H 40 --fps 10 --output output.gif

# Color output (requires terminal with true color support)
gif-for-cli input.mp4 --color --output output.gif

# Audio-only: convert to waveform visualization
gif-for-cli input.mp3 --color --output audio_viz.gif
```

### Usage (ascii-video Node.js)

```bash
# Basic conversion
ascii-video input.mp4 -o output.gif

# Custom size and speed
ascii-video input.mp4 -w 100 -h 30 -s 2.0 -o output.gif

# Color mode
ascii-video input.mp4 -c -o output.gif
```

### Key Parameters

| Parameter | gif-for-cli | ascii-video | Description |
|-----------|-------------|-------------|-------------|
| Width | `-W`, `--width` | `-w` | Character columns |
| Height | `-H`, `--height` | `-h` | Character rows |
| FPS | `--fps` | (auto) | Frames per second |
| Speed | N/A | `-s` | Playback speed multiplier |
| Color | `--color` | `-c` | Enable ANSI color |
| Dither | `--dither` | N/A | Dithering algorithm |

### Performance Notes

- **gif-for-cli**: Python-based, uses ffmpeg for frame extraction + ImageMagick for conversion. Slower but higher quality color.
- **ascii-video**: Node.js-based, faster for simple conversions, less color fidelity.
- **Output size**: A 10s clip at 120x40 @ 10fps ≈ 2-5MB GIF.
- **Terminal playback**: Use `catimg` or `timg` to preview in terminal, or open GIF in browser.

### Common Pitfalls

1. **ffmpeg/ImageMagick not installed** — both tools need system dependencies
2. **Terminal color support** — ASCII color only works in true-color terminals (most modern)
3. **Large files** — long videos produce huge GIFs; trim with ffmpeg first: `ffmpeg -i in.mp4 -t 10 -c copy clip.mp4`
4. **Aspect ratio** — terminal chars are ~2:1 (w:h); use `-W 120 -H 30` for 16:9 content

---

**Tool 8: LLM-Generated Custom Art (Fallback)**

When tools above don't have what's needed, generate ASCII art directly using these Unicode characters:

### Character Palette

**Box Drawing:** `╔ ╗ ╚ ╝ ║ ═ ╠ ╣ ╦ ╩ ╬ ┌ ┐ └ ┘ │ ─ ├ ┤ ┬ ┴ ┼ ╭ ╮ ╰ ╯`

**Block Elements:** `░ ▒ ▓ █ ▄ ▀ ▌ ▐ ▖ ▗ ▘ ▝ ▚ ▞`

**Geometric & Symbols:** `◆ ◇ ◈ ● ○ ◉ ■ □ ▲ △ ▼ ▽ ★ ☆ ✦ ✧ ◀ ▶ ◁ ▷ ⬡ ⬢ ⌂`

### Rules

- Max width: 60 characters per line (terminal-safe)
- Max height: 15 lines for banners, 25 for scenes
- Monospace only: output must render correctly in fixed-width fonts

## Decision Flow

1. **Text as a banner** → pyfiglet if installed, otherwise asciified API via curl
2. **Wrap a message in fun character art** → cowsay
3. **Add decorative border/frame** → boxes (can combine with pyfiglet/asciified)
4. **Art of a specific thing** (cat, rocket, dragon) → ascii.co.uk via curl + parsing
5. **Convert an image to ASCII** → ascii-image-converter or jp2a
6. **QR code** → qrenco.de via curl
7. **Weather/moon art** → wttr.in via curl
8. **Something custom/creative** → LLM generation with Unicode palette
9. **Any tool not installed** → install it, or fall back to next option
