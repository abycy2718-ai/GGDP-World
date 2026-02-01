# -*- coding: utf-8 -*-
"""
Copy GGDP visualizations to docs/ for GitHub Pages and generate index.html.
Run: python prepare_github.py
Then push the repo and enable GitHub Pages (Settings -> Pages -> Source: main, /docs).
"""
from pathlib import Path
import shutil

OUT_DIR = Path(__file__).resolve().parent
DOCS = OUT_DIR / "docs"

# Files to copy (picture + interactive)
VIS_FILES = [
    "GGDP_Global_Heatmap.png",
    "GGDP_Global_Heatmap.html",
    "GGDP_Global_GDP_vs_GGDP_Bar.png",
    "GGDP_Global_Y_vs_GGDP_Scatter.png",
    "GGDP_Global_Ranking_Bar.png",
    "GGDP_China_Province_Heatmap.png",
    "GGDP_China_Province_Heatmap.html",
    "GGDP_China_Province_Bar.png",
    "GGDP_China_Province_GDP_vs_GGDP.png",
]

INDEX_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Green GDP (GGDP) Visualizations</title>
  <style>
    body { font-family: system-ui, sans-serif; max-width: 1000px; margin: 0 auto; padding: 1.5rem; background: #fafafa; }
    h1 { color: #006d2c; }
    h2 { margin-top: 2rem; color: #00441b; }
    section { margin: 1.5rem 0; }
    figure { margin: 1rem 0; }
    img { max-width: 100%; height: auto; border: 1px solid #ddd; border-radius: 4px; }
    a { color: #006d2c; }
    .caption { font-size: 0.9rem; color: #555; margin-top: 0.25rem; }
    .link { margin-left: 0.5rem; }
  </style>
</head>
<body>
  <h1>Green GDP (GGDP) Visualizations</h1>
  <p>GGDP = Y [1 + αẼI + βẼA − γẼC]. Year: 2020. White = no data.</p>

  <h2>Global</h2>
  <section>
    <figure>
      <img src="GGDP_Global_Heatmap.png" alt="World GGDP heatmap" width="1200">
      <figcaption class="caption">World map: GGDP by country (picture). <a href="GGDP_Global_Heatmap.html" class="link">Interactive</a></figcaption>
    </figure>
    <figure>
      <img src="GGDP_Global_GDP_vs_GGDP_Bar.png" alt="Top 25 GDP vs GGDP">
      <figcaption class="caption">Top 25 countries: GDP vs GGDP</figcaption>
    </figure>
    <figure>
      <img src="GGDP_Global_Y_vs_GGDP_Scatter.png" alt="GDP vs GGDP scatter">
      <figcaption class="caption">GDP vs GGDP (color = ẼC, size = ẼA)</figcaption>
    </figure>
    <figure>
      <img src="GGDP_Global_Ranking_Bar.png" alt="Global GGDP ranking">
      <figcaption class="caption">Global GGDP ranking (top 50)</figcaption>
    </figure>
  </section>

  <h2>China (provinces)</h2>
  <section>
    <figure>
      <img src="GGDP_China_Province_Heatmap.png" alt="China province GGDP heatmap" width="1000">
      <figcaption class="caption">China province GGDP (picture). <a href="GGDP_China_Province_Heatmap.html" class="link">Interactive</a></figcaption>
    </figure>
    <figure>
      <img src="GGDP_China_Province_Bar.png" alt="China province GGDP bar">
      <figcaption class="caption">China province GGDP ranking (万亿元)</figcaption>
    </figure>
    <figure>
      <img src="GGDP_China_Province_GDP_vs_GGDP.png" alt="China GDP vs GGDP">
      <figcaption class="caption">China provinces: GDP vs GGDP (万亿元)</figcaption>
    </figure>
  </section>

  <p style="margin-top: 2rem; font-size: 0.9rem; color: #666;">Data: World Bank / Our World in Data (global); China Statistical Yearbook (provinces).</p>
</body>
</html>
"""


def main():
    DOCS.mkdir(exist_ok=True)
    for f in VIS_FILES:
        src = OUT_DIR / f
        if src.exists():
            shutil.copy2(src, DOCS / f)
            print("Copied:", f)
        else:
            print("Skip (not found):", f)
    (DOCS / "index.html").write_text(INDEX_HTML, encoding="utf-8")
    print("Written: docs/index.html")
    print("Done. Push repo and enable GitHub Pages (Source: main, /docs) to publish.")


if __name__ == "__main__":
    main()
