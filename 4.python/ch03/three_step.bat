echo off
REM ---- 3개 파이썬 프로그램 연속 실행 ----
python step1_merge_files.py
python step2_split_data.py
python step3_fill_temp.py

PAUSE