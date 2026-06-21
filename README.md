# mr.SME — Profit calculation scripts 
🔺Disclaimer: THIS README FILE (only readme.md file) WAS WRITTEN BY USING AI 🔻

This folder contains three small Python scripts to calculate gross profit, total expenses and net profit and to produce a simple profit/loss report.

**Files**
- `grossprofit.py`: collects sales, sales returns, purchases, purchase returns, opening and closing stock to compute gross profit.
- `netprofit.py`: collects additional incomes and several expense categories (transport, administration, financial, other) and returns totals used to compute net profit.
- `main.py`: runs the interactive flows in `grossprofit.py` and `netprofit.py`, computes net profit, prints a formatted Profit/Loss statement and appends it to a text file.

**How it works (high level)**
- `grossprofit.grossPROFIT()` — prompts for sales and purchase flows and starting/ending stock, returns gross profit (float).
- `netprofit.addiINC()` and `netprofit.Totalexp()` — prompt for additional incomes and expense items; `Totalexp()` calls expense functions and returns total expenses (float).
- `main.py` — imports the above modules, calls them, computes `netprofit = (gross + additional_income) - total_expenses`, prints the report and saves it to `<filename>.txt`.

**Usage**
1. From the workspace root run:

```powershell
python mr.SME\\main.py
```

Or change into the `mr.SME` directory and run:

```powershell
cd "mr.SME"
python main.py
```

2. Follow the interactive prompts. Input `0` to stop each loop of numeric entries.
   # enter the data one by one
Example (interactive flow shortened):
- Enter sales values (enter 0 when done): 1000, 500, 0
- Any sales returns? (yes=1 or no=0): 0
- Enter purchases: 400, 600, 0
- Any purchase returns? 0
- Starting stock: 100
- Final stock: 50
- Enter additional incomes: 200, 0
- Enter transport costs: 50, 0
- Enter administration costs: 30, 0
- Enter financial costs: 20, 0
- Enter other costs: 10, 0

The script will print a formatted Profit/Loss statement and save it as the filename you specify (appending to `<filename>.txt`).

**Notes & caveats**
- These scripts are interactive and expect numeric input; invalid input (non-numeric) will raise exceptions.
- The code uses global variables and simple input loops — suitable for quick demos but not for production use.
- `main.py` opens the output file with mode `a` (append). Running multiple times with the same filename will append multiple reports.

**Suggested improvements**
- Add input validation and error handling.
- Replace global variables with function-local variables or a small class to avoid state leakage between runs.
- Add a `--non-interactive` mode (CLI args or reading a CSV) for automated runs.
- Add unit tests for computation functions.

**Contact / maintainer**
This README was generated to document the current scripts in this folder.  
