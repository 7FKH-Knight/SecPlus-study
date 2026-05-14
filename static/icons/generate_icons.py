"""
Run this script once to generate the PWA icon PNGs.
No external dependencies — uses only Python stdlib.

    python3 static/icons/generate_icons.py
"""
import struct
import zlib
import os

HERE = os.path.dirname(os.path.abspath(__file__))

# Theme colours: purple background (#7c5cbf), white text area (#e2e8f0)
BG  = (124, 92, 191)   # #7c5cbf
FG  = (226, 232, 240)  # #e2e8f0
DARK = (15, 17, 23)    # #0f1117


def _png_chunk(tag: bytes, data: bytes) -> bytes:
    c = zlib.crc32(tag + data) & 0xFFFFFFFF
    return struct.pack(">I", len(data)) + tag + data + struct.pack(">I", c)


def make_png(size: int, path: str) -> None:
    """Write a minimal valid PNG: purple bg with a centred white 'S+' block."""
    w = h = size
    s = size  # shorthand

    # Build raw RGBA pixel rows
    rows = []
    for y in range(h):
        row = bytearray()
        for x in range(w):
            # Outer purple background with rounded-feel padding (10% inset)
            pad = s // 10
            in_inner = pad <= x < s - pad and pad <= y < s - pad

            # Central white band — simulate "S+" text as two white rectangles
            cx, cy = s // 2, s // 2

            # Horizontal bar
            bar_h = s // 12
            bar_w = s // 3
            in_h_bar = (cx - bar_w // 2 <= x < cx + bar_w // 2 and
                        cy - bar_h // 2 <= y < cy + bar_h // 2)

            # Vertical stem of S (left side)
            stem_w = s // 18
            top_half = (cx - bar_w // 2 <= x < cx - bar_w // 2 + stem_w and
                        cy - bar_w // 2 <= y < cy)
            bot_half = (cx + bar_w // 2 - stem_w <= x < cx + bar_w // 2 and
                        cy <= y < cy + bar_w // 2)

            # Plus sign
            plus_arm_len = s // 5
            plus_thick  = s // 18
            in_plus_h = (cx + bar_w // 2 + s // 12 <= x < cx + bar_w // 2 + s // 12 + plus_arm_len and
                         cy - plus_thick // 2 <= y < cy + plus_thick // 2)
            in_plus_v = (cx + bar_w // 2 + s // 12 + plus_arm_len // 2 - plus_thick // 2 <= x <
                         cx + bar_w // 2 + s // 12 + plus_arm_len // 2 + plus_thick // 2 and
                         cy - plus_arm_len // 2 <= y < cy + plus_arm_len // 2)

            if in_h_bar or top_half or bot_half or in_plus_h or in_plus_v:
                r, g, b = FG
            elif in_inner:
                r, g, b = BG
            else:
                r, g, b = DARK

            row += bytes([r, g, b, 255])

        # PNG filter byte 0 (None) at the start of each row
        rows.append(b"\x00" + bytes(row))

    raw = b"".join(rows)
    compressed = zlib.compress(raw, 9)

    ihdr_data = struct.pack(">IIBBBBB", w, h, 8, 2, 0, 0, 0)  # 8-bit RGB... wait, we have RGBA
    # Correct: bit depth=8, colour type=6 (RGBA)
    ihdr_data = struct.pack(">II", w, h) + bytes([8, 6, 0, 0, 0])

    with open(path, "wb") as f:
        f.write(b"\x89PNG\r\n\x1a\n")                 # PNG signature
        f.write(_png_chunk(b"IHDR", ihdr_data))
        f.write(_png_chunk(b"IDAT", compressed))
        f.write(_png_chunk(b"IEND", b""))

    print(f"  Created {path} ({size}x{size})")


if __name__ == "__main__":
    for size in (192, 512):
        out = os.path.join(HERE, f"icon-{size}.png")
        make_png(size, out)
    print("Done. Icons are in static/icons/")
