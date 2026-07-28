import re

html_path = 'index.html'
js_path = 'js/11cz13r8bk.28.js'

with open(html_path, 'r', encoding='utf-8') as f:
    html_content = f.read()

with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

new_words = [
    "Artificial Intelligence (AI) & Machine Learning",
    "Full Stack Web Development",
    "Data Analytics & Business Intelligence",
    "Internet of Things (IoT)",
    "Computer Vision & Deep Learning Prediction",
    "Healthcare AI",
    "Cloud & Backend Development",
    "Research & Innovation"
]

# 1. Update JS
# e.s(["marqueeWords",0,["Product Design","Creative Technology","AI Prototyping","Web Design","Brand Systems","Vibe Coding"],
# We match ["marqueeWords",0,[...],
pattern_js = r'\["marqueeWords",0,\[.*?\]'
replacement_js = '["marqueeWords",0,[' + ','.join(f'"{w}"' for w in new_words) + ']'
js_updated = re.sub(pattern_js, replacement_js, js_content)

with open(js_path, 'w', encoding='utf-8') as f:
    f.write(js_updated)


# 2. Update HTML
# The HTML contains two identical <div class="marquee-group flex shrink-0 items-center gap-8 pr-8"> blocks.
# We will construct the new inner HTML for them.
def make_span(word):
    return f'<span class="flex items-center gap-8"><span class="font-blinker text-[clamp(28px,5vw,64px)] leading-none tracking-tight">{word}</span><span class="text-[clamp(20px,3vw,40px)]" style="color:var(--accent)">✳</span></span>'

new_inner_html = ''.join(make_span(w) for w in new_words)

# Regex to replace the inner content of marquee-group
pattern_html = r'(<div class="marquee-group flex shrink-0 items-center gap-8 pr-8">)(.*?)(</div>)'
html_updated = re.sub(pattern_html, r'\g<1>' + new_inner_html + r'\g<3>', html_content)

with open(html_path, 'w', encoding='utf-8') as f:
    f.write(html_updated)

print("Updated JS and HTML successfully.")
