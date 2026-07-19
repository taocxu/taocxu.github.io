from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected one match, found {count}")
    return text.replace(old, new, 1)


index_path = Path("index.html")
css_path = Path("site-v2.css")
index = index_path.read_text(encoding="utf-8")
css = css_path.read_text(encoding="utf-8")

index = replace_once(
    index,
    '''        <div class="section-body">
          <p class="lead">My research interests include:</p>
          <!-- Edit or add research interests by changing the list items below. -->
          <ul class="research-interest-list">''',
    '''        <div class="section-body">
          <!-- Edit or add research interests by changing the list items below. -->
          <ul class="research-interest-list">''',
    "remove research introduction",
)

css = replace_once(
    css,
    '''.portrait-frame img {
  width: 100%;
  aspect-ratio: 1 / 1;
  object-fit: cover;
  object-position: center;
}''',
    '''.portrait-frame img {
  width: 100%;
  height: auto;
  object-fit: contain;
  object-position: center;
}''',
    "preserve full PNG portrait",
)

css = replace_once(
    css,
    '''.research-interest-list {
  display: grid;
  grid-template-columns: repeat(3, minmax(0, 1fr));
  gap: 14px 34px;
  margin: 26px 0 0;
  padding-left: 1.2rem;
}

.research-interest-list li {
  padding-left: 0.2rem;
  break-inside: avoid;
}

.research-interest-list li::marker { color: #111111; font-size: 0.82em; }''',
    '''.research-interest-list {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  gap: 13px 48px;
  margin: 0;
  padding: 0;
  list-style: none;
}

.research-interest-list li {
  position: relative;
  min-width: 0;
  padding-left: 1.15rem;
  line-height: 1.48;
  break-inside: avoid;
}

.research-interest-list li::before {
  content: "•";
  position: absolute;
  left: 0;
  top: 0;
  color: #303134;
  font-size: 0.92em;
}''',
    "refine research grid",
)

css = replace_once(
    css,
    '  .research-interest-list { grid-template-columns: repeat(2, minmax(0, 1fr)); }',
    '  .research-interest-list { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 12px 34px; }',
    "refine tablet research grid",
)

css = replace_once(
    css,
    '  .research-interest-list { grid-template-columns: 1fr; gap: 9px; }',
    '  .research-interest-list { grid-template-columns: 1fr; gap: 10px; }',
    "refine mobile research grid",
)

index_path.write_text(index, encoding="utf-8")
css_path.write_text(css, encoding="utf-8")
