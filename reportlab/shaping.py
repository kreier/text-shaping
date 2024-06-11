#!/bin/env python
import uharfbuzz as hb

if False:
    import sys
    fontfile = sys.argv[1]
    text = sys.argv[2]
else:
    # fontfile = '/home/robin/devel/reportlab/REPOS/reportlab/tmp/NotoSansKhmer/NotoSansKhmer-Regular.ttf'
    fontfile = "../fonts/NotoKhmer.ttf"
    # fontfile = "../fonts/Khmer-Regular.ttf"
    #1786 Khmer Letter Cha
    #17D2 Khmer Sign Coeng
    #1793 Khmer Letter No
    #17B6 Khmer Vowel Sign Aa
    #17C6 Khmer Sign Nikahit
    text = '\u1786\u17D2\u1793\u17B6\u17C6'
    # strings:    years,  alone,    1st year, sword,  fork
    teststrings = ["ឆ្នាំ", "ម្នាក់ ឯង", "ឆ្នាំទី១", "ដង្កាវ", "ង្គ្រា", "\u1786\u17d2\u1789\u17B6\u17c6", "\u1786\u17D2\u1793\u17B6\u17C6"]

blob = hb.Blob.from_file_path(fontfile)
face = hb.Face(blob)
font = hb.Font(face)

buf = hb.Buffer()
buf.add_str(text)
buf.guess_segment_properties()

features = {"kern": True, "liga": True}
hb.shape(font, buf, features)

infos = buf.glyph_infos
positions = buf.glyph_positions

for info, pos in zip(infos, positions):
    gid = info.codepoint
    glyph_name = font.glyph_to_string(gid)
    cluster = info.cluster
    x_advance = pos.x_advance
    x_offset = pos.x_offset
    y_offset = pos.y_offset
    # print(f"{glyph_name} gid{gid}={cluster}@{x_advance},{y_offset}+{x_advance}")
    print(f"{glyph_name} \t gid{gid}={cluster} \t advanceWidth: {x_advance} \t offset x:{x_offset} y:{y_offset}")
