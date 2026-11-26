import os

LINE = "The model updated mid-task. The new me has no record of the old me promising anything by Friday."

with open(os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR") or os.getcwd(), "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
