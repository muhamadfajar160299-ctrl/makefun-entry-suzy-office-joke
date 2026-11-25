"""Write the one-line office joke entry to the output directory.

Stdlib only. The entry text is fixed in this file so the grader's run
reproduces entry.txt byte for byte.
"""
import os
import sys

ENTRY = "The shared drive's newest file is FINAL_v2_FINAL(3)_USE_THIS_ONE.docx, and nobody dares open it."

def main():
    if not ENTRY.strip():
        print("error: entry text is empty", file=sys.stderr)
        return 1
    try:
        out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(ENTRY)
    except OSError as exc:
        print(f"error: cannot write entry: {exc}", file=sys.stderr)
        return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
