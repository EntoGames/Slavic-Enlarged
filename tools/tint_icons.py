"""Generate tinted variants of the vanilla slavic faith icon for CK3."""
from PIL import Image, ImageEnhance
import colorsys
import os

VANILLA_ICON = r"C:\Program Files (x86)\Steam\steamapps\common\Crusader Kings III\game\gfx\interface\icons\faith\slavic.dds"
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.dirname(__file__)), "gfx", "interface", "icons", "faith")

# Tint definitions: (target_hue_degrees, saturation_mult, value_mult)
# Hue: 0=red, 60=yellow, 120=green, 180=cyan, 240=blue, 300=magenta
TINTS = {
    "se_slavic_east":  (100, 1.4, 1.0),   # green
    "se_slavic_west":  (40,  1.3, 1.0),    # gold/amber
    "se_slavic_south": (180, 1.3, 1.0),    # teal/turquoise
}


def tint_image(img: Image.Image, target_hue_deg: float, sat_mult: float, val_mult: float) -> Image.Image:
    """Shift hue of an RGBA image while preserving alpha and luminance structure."""
    target_hue = target_hue_deg / 360.0
    pixels = img.load()
    result = img.copy()
    out = result.load()
    w, h = img.size

    for y in range(h):
        for x in range(w):
            r, g, b, a = pixels[x, y]
            if a == 0:
                continue
            rn, gn, bn = r / 255.0, g / 255.0, b / 255.0
            h_orig, s, v = colorsys.rgb_to_hsv(rn, gn, bn)
            new_s = min(1.0, s * sat_mult)
            new_v = min(1.0, v * val_mult)
            nr, ng, nb = colorsys.hsv_to_rgb(target_hue, new_s, new_v)
            out[x, y] = (int(nr * 255), int(ng * 255), int(nb * 255), a)

    return result


def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    src = Image.open(VANILLA_ICON).convert("RGBA")
    print(f"Source: {VANILLA_ICON} ({src.size[0]}x{src.size[1]} {src.mode})")

    for name, (hue, sat, val) in TINTS.items():
        print(f"Generating {name} (hue={hue}, sat={sat}, val={val})...")
        tinted = tint_image(src, hue, sat, val)
        out_path = os.path.join(OUTPUT_DIR, f"{name}.dds")
        tinted.save(out_path)
        print(f"  Saved: {out_path} ({os.path.getsize(out_path)} bytes)")

    print("Done!")


if __name__ == "__main__":
    main()
