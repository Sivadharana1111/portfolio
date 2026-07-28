import os

js_path = 'js/0i1..nj4jaiqb.js'
with open(js_path, 'r', encoding='utf-8') as f:
    js_content = f.read()

old_str = '["marqueeWords",0,["Product Design","Creative Technology","AI Prototyping","Web Design","Brand Systems","Vibe Coding"]'
new_str = '["marqueeWords",0,["Artificial Intelligence (AI) & Machine Learning","Full Stack Web Development","Data Analytics & Business Intelligence","Internet of Things (IoT)","Computer Vision & Deep Learning Prediction","Healthcare AI","Cloud & Backend Development","Research & Innovation"]'

if old_str in js_content:
    js_content = js_content.replace(old_str, new_str)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    print("JS fixed!")
else:
    print("Old string not found in JS.")
