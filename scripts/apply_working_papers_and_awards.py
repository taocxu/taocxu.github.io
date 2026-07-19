#!/usr/bin/env python3
from pathlib import Path


def replace_once(text: str, old: str, new: str, label: str) -> str:
    count = text.count(old)
    if count != 1:
        raise RuntimeError(f"{label}: expected exactly one match, found {count}")
    return text.replace(old, new, 1)


path = Path("index.html")
html = path.read_text(encoding="utf-8")

# Add four current working papers at the beginning of the Working Papers list.
html = replace_once(
    html,
    '''          <h3 class="subsection-title">WORKING PAPERS</h3>
          <ol class="item-list">
            <li class="item">
              <p class="item-title"><a href="https://doi.org/10.21203/rs.3.rs-7374795/v2">‘Why Cities Backfire? High-Speed Railway New Town Planning and Urban Structural Change’</a></p>''',
    '''          <h3 class="subsection-title">WORKING PAPERS</h3>
          <ol class="item-list">
            <li class="item">
              <p class="item-title">‘Confucian Values and Supply-Chain Stability’</p>
              <p class="item-meta">with Weiwei Zhu</p>
            </li>
            <li class="item">
              <p class="item-title">‘Understanding Hierarchically Differentiated Legitimacy Work: Organisational Hierarchy, Rent Governance, and Industrial Policy Practice’</p>
            </li>
            <li class="item">
              <p class="item-title">‘The Political Economy of Critical Minerals and Development: A Review’</p>
            </li>
            <li class="item">
              <p class="item-title">‘Infrastructure Development and Agri-food Supply Chains in the Global South: From Value Capturing to Value Sharing’</p>
              <p class="item-meta">with Li Liu</p>
            </li>
            <li class="item">
              <p class="item-title"><a href="https://doi.org/10.21203/rs.3.rs-7374795/v2">‘Why Cities Backfire? High-Speed Railway New Town Planning and Urban Structural Change’</a></p>''',
    "working-paper insertion",
)

# Add the undergraduate dissertation distinction.
html = replace_once(
    html,
    '''                <p>Dissertation: ‘Towards Sustainable Prosperity? Policy Evaluation of Jiangsu Advanced Manufacturing Clusters’<br>
                  Supervisor:''',
    '''                <p>Dissertation: ‘Towards Sustainable Prosperity? Policy Evaluation of Jiangsu Advanced Manufacturing Clusters’ (Jiangsu Provincial Distinguished UG Dissertation Award 1st Class, 77 1st-class works/over 732k graduates)<br>
                  Supervisor:''',
    "undergraduate dissertation award",
)

# Add the Wuhan University distinction after the course and dates.
html = replace_once(
    html,
    '''            <li>Marxian Political Economy, Adv - <a href="https://en.whu.edu.cn/">Wuhan University</a>, Jul 2023, 2024 · <a href="WHURoP.pdf">[Certificate-Distinguished Paper Award]</a></li>''',
    '''            <li>Marxian Political Economy, Adv - <a href="https://en.whu.edu.cn/">Wuhan University</a>, Jul 2023, 2024 (WHU Outstanding Student &amp; Distinguished Paper Award, 19/~1300) · <a href="WHURoP.pdf">[Certificate-Distinguished Paper Award]</a></li>''',
    "Wuhan University award",
)

path.write_text(html, encoding="utf-8")
