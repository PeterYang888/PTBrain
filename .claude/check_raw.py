"""
PTBrain hook: 掃描 raw/ 有無尚未 ingest 的檔案，提醒使用者。
輸出 JSON additionalContext 給 Claude Code UserPromptSubmit hook 使用。
"""
import os, sys, json, re

ROOT = "C:/Users/user/Desktop/PTBrain/PTBrain"
RAW_DIRS = ["raw/articles", "raw/papers", "raw/notes", "raw/transcripts"]
SOURCES_DIR = "wiki/sources"

def key_segments(filename):
    stem = os.path.splitext(filename)[0].lower()
    parts = re.split(r"[\s_\-\u2014]+", stem)
    result = set()
    for part in parts:
        # split on ASCII\u2194CJK transitions (e.g. 'apple\u7522\u54c1\u7b56\u7565' \u2192 ['apple','\u7522\u54c1\u7b56\u7565'])
        sub = re.split(r'(?<=[a-z0-9])(?=[\u4e00-\u9fff])|(?<=[\u4e00-\u9fff])(?=[a-z0-9])', part)
        for s in sub:
            has_cjk = bool(re.search(r'[\u4e00-\u9fff]', s))
            # CJK segments: allow len >= 2; ASCII/digit segments: require len >= 4
            if (has_cjk and len(s) >= 2) or (not has_cjk and len(s) >= 4):
                result.add(s)
    return result

src_path = os.path.join(ROOT, SOURCES_DIR)
src_names = []
if os.path.exists(src_path):
    src_names = [f for f in os.listdir(src_path) if f.endswith(".md")]

def is_processed(filename):
    segs = key_segments(filename)
    for src in src_names:
        src_segs = key_segments(src)
        if segs & src_segs:
            return True
    return False

unprocessed = []
for raw_dir in RAW_DIRS:
    full_dir = os.path.join(ROOT, raw_dir)
    if not os.path.exists(full_dir):
        continue
    for f in sorted(os.listdir(full_dir)):
        if f.startswith(".") or f.startswith("~"):
            continue
        if not (f.endswith(".md") or f.endswith(".pdf")):
            continue
        if not is_processed(f):
            unprocessed.append(f"{raw_dir}/{f}")

if unprocessed:
    files = "\n".join(f"  - {f}" for f in unprocessed)
    out = {
        "hookSpecificOutput": {
            "hookEventName": "UserPromptSubmit",
            "additionalContext": (
                f"[PTBrain] 發現 {len(unprocessed)} 個 raw 檔案尚未 ingest：\n"
                f"{files}\n"
                f"如需處理，請在對話中說「ingest」。"
            )
        }
    }
    sys.stdout.buffer.write(json.dumps(out, ensure_ascii=False).encode("utf-8"))
