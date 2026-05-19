# Science — Quantum waves & probability (HTML)

This folder contains a **single static web page**, `index.html`, that explains **wave functions**, **probability**, and **interference** — from classical water ripples through the **double-slit experiment** to **Born’s rule** and a gentle introduction to the **Schrödinger equation**.

## What the page covers

- **Symbol index** — Greek symbols (e.g. **ψ** psi, **λ** lambda, **ℏ** h-bar) are named on first use and listed in a table at the top.
- **Classical waves** — travelling-wave equation step by step, **phase φ** (sine vs cosine, interactive + unit circle), worked examples, travelling-wave animation, and **superposition** (interactive).
- **Wave–particle duality** — particle-like detections vs wave-like interference.
- **Water-wave ripple tank** — top-down **Huygens** model: one slit (diffraction fan) and two slits (interference). **Wide green bands** = constructive interference; **slim dark gaps** = near-complete **cancellation** (crest meets trough). Optional **fringe guide** marks bright vs dark zones in the tank.
- **Double-slit experiment** — classical particles, classical waves, and quantum buildup (interactive screen histogram).
- **Feynman sum over paths** — animated sample paths; schematic path-integral idea.
- **de Broglie** matter waves (**λ = h/p**).
- **Wave function ψ** — real and imaginary parts (animated).
- **Born’s rule** — probability vs **probability density**, step-by-step **|ψ₁ + ψ₂|²**, and comparison of with/without interference (interactive).
- **Particle in a box** — **ψₙ** and **|ψₙ|²** for energy levels **n = 1…6**.
- **Schrödinger equation** — time-dependent and time-independent forms (introductory).

The page uses **British English**, **interactive canvas demos**, and simple **SVG figures**; no build step is required to view the page.

## How to view

Open `index.html` in any modern web browser, or publish the folder on **GitHub Pages** and open the site URL.

**iPhone / iPad:** In Safari, tap **Share → Add to Home Screen**. The **apple-touch-icon** (180×180) is used for the home-screen tile; the short name under the icon is **Quantum waves** (`apple-mobile-web-app-title`). The same icon also appears **in the page header** next to the Hal AI by CJF logo.

## Ripple tank controls

| Control | Purpose |
|---------|---------|
| **One slit / Two slits** | Switch diffraction vs interference layout |
| **Animation speed** | 0.4×–4× (default 1×) |
| **Fringe guide** | Labels bright (wide) vs cancelled (slim) bands (two-slit mode) |
| **Pause / Reset** | Freeze or clear the tank and averages |

## Assets in this folder

| File | Purpose |
|------|---------|
| `index.html` | Full guide and interactive demos (GitHub Pages entry) |
| `header-logo.svg` | Standard Hal AI by CJF header logo (canonical copy from `Branding/CJF Hal AI/`) |
| `favicon.svg` | Browser tab icon (ψ motif) |
| `apple-touch-icon.png` | **180×180** — home-screen tile and header companion icon |
| `build_icons.py` | Regenerate `favicon.svg` and `apple-touch-icon.png` |

To rebuild icons:

```bash
python build_icons.py
```

---

*Educational summary only — not a substitute for textbooks or peer-reviewed sources.*
