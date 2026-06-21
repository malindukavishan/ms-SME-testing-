import grossprofit
import netprofit

gross=float(grossprofit.grossPROFIT())
addincome=float(netprofit.addiINC())
tot=float(netprofit.Totalexp())

netprofits=(gross+addincome)-tot

filename=input('\nEnter the name that you want to add file:')

report_content=(
    f"{'='*40}\n"
    f"{'Profit/Loss statement':^40}\n"
    f"{'='*40}\n"
    f"|{'Description':<25}|{'Amount(LKR)':>12}|\n"
    f"{'-'*40}\n"
    f"{'Gross profit':<25}|{gross:>12.2f}\n"
    f"{'(+):Additional Income':<25}|{addincome:>12}\n"
    f"{'-'*40}\n"
    f"{'(-)Total expences':<25}|{tot:>12.2f}\n"
    f"{'-'*40}\n"
    f"{'Net profit':<25}|{netprofits:>12.2f}\n"
    f"{'-'*40}\n"
)

print(report_content)

file=open(f"{filename}.txt","a")
file.write(report_content)

print(f"\nReport successfully saved as '{filename}.txt'.\n")