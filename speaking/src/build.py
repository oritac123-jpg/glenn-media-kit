"""Builds the two versions of Glenn Cohen's speaker kit.

speaking/index.html         direct version, with Glenn's contact details
speaking/bureau/index.html  bureau-friendly version, no contact details

Edit body.html (content) or base_style.html (shared look from the media kit),
then run:  python3 speaking/src/build.py
"""
from pathlib import Path

SRC = Path(__file__).parent
OUT = SRC.parent
style = (SRC / "base_style.html").read_text().splitlines()
style = "\n".join(l for l in style if not l.startswith("<title>"))
body = (SRC / "body.html").read_text()

CTA_DIRECT = """<footer class="cta">
    <div>
      <h2>Book Glenn Cohen for your next event</h2>
      <p class="sub">Keynotes, fireside chats and workshops, in person or virtual. Happy to tailor the talk to your audience.</p>
    </div>
    <div class="contact">
      <a href="mailto:glenn@gobeyond.team">glenn@gobeyond.team</a>
      <a href="https://wa.me/972506532681">WhatsApp&nbsp;+972&nbsp;50&#8209;653&#8209;2681</a>
      <a href="https://www.glenn-cohen.com">www.glenn-cohen.com</a>
    </div>
  </footer>"""

CTA_BUREAU = """<footer class="cta">
    <div>
      <h2>Book Glenn Cohen for your next event</h2>
      <p class="sub">Keynotes, fireside chats and workshops, in person or virtual. Contact your speakers bureau for fees and availability.</p>
    </div>
  </footer>"""

versions = {
    OUT / "index.html": ("Glenn Cohen | Speaker Kit", CTA_DIRECT),
    OUT / "bureau" / "index.html": ("Glenn Cohen | Keynote Speaker", CTA_BUREAU),
}
for path, (title, cta) in versions.items():
    path.parent.mkdir(parents=True, exist_ok=True)
    html = ("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n"
            f"<title>{title}</title>\n"
            "<meta name=\"description\" content=\"Glenn Cohen, former Mossad Chief Operational Psychologist "
            "and hostage negotiator, keynote speaker on resilience, leadership and performance under pressure.\">\n"
            f"{style}\n</head>\n<body>\n" + body.replace("{{CTA}}", cta) + "\n</body>\n</html>\n")
    if "bureau" in str(path):
        html = html.replace('<a class="watch" href="https://oritac123-jpg.github.io/glenn-media-kit/">Full media kit</a>', "")
    path.write_text(html)
    print("built", path.relative_to(OUT.parent))
