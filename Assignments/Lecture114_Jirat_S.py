from tkinter import *
import tkinter.ttk as ttk
from forex_python.converter import CurrencyRates
from datetime import datetime
from datetime import timedelta
import matplotlib.pyplot as plt


c = CurrencyRates()
rate = c.get_rates('USD')
list_currency = []
for currency_unit in rate:
    list_currency.append(currency_unit)


def click_button(button):
    t = [button]
    now = datetime.now()
    list_day = [now.date()]
    list_rates = [c.get_rate(combobox1.get(), combobox2.get(), now)]
    if t[0] == 'Convert':
        get_rate = c.get_rate(combobox1.get(), combobox2.get(), now)
        convert = (get_rate * float(text_get.get())).__format__(".2f")
        result.configure(text=convert)
    else:
        if t[0] == 'Last week':
            for i in range(6):
                date_range = timedelta(days=-1)
                date_minus = now.__add__(date_range)
                list_day.append(date_minus.date())
                list_rates.append(c.get_rate(combobox1.get(), combobox2.get(), date_minus.date()))
                now = date_minus
        elif t[0] == 'Last month':
            for i in range(6):
                date_range = timedelta(days=-5)
                date_minus = now.__add__(date_range)
                list_day.append(date_minus.date())
                list_rates.append(c.get_rate(combobox1.get(), combobox2.get(), date_minus.date()))
                now = date_minus
        elif t[0] == 'Last year':
            for i in range(12):
                date_range = timedelta(days=-31)
                date_minus = now.__add__(date_range)
                list_day.append(date_minus.date())
                list_rates.append(c.get_rate(combobox1.get(), combobox2.get(), date_minus.date()))
                now = date_minus
        elif t[0] == 'Last 3 year':
            for i in range(36):
                date_range = timedelta(days=-31)
                date_minus = now.__add__(date_range)
                list_day.append(date_minus.date())
                list_rates.append(c.get_rate(combobox1.get(), combobox2.get(), date_minus.date()))
                now = date_minus
        elif t[0] == 'Last 5 year':
            for i in range(60):
                date_range = timedelta(days=-31)
                date_minus = now.__add__(date_range)
                list_day.append(date_minus.date())
                list_rates.append(c.get_rate(combobox1.get(), combobox2.get(), date_minus.date()))
                now = date_minus
        elif t[0] == 'Last 10 year':
            for i in range(120):
                date_range = timedelta(days=-31)
                date_minus = now.__add__(date_range)
                list_day.append(date_minus.date())
                list_rates.append(c.get_rate(combobox1.get(), combobox2.get(), date_minus.date()))
                now = date_minus
        # plot graph
        plt.title(f"Exchange 1 {combobox1.get()} to {combobox2.get()} ")
        plt.xlabel('Date')
        plt.ylabel('Exchange rate')
        plt.plot(list_day, list_rates)
        plt.show()


#หน้าต่าง GUI
main_window = Tk()
main_window.title("Convert")
main_window.configure(bg='#00FA9A')
convert_title = LabelFrame(text="โปรแกรมคำนวณค่าเงิน", font=("Helvetica", 18))
convert_title.grid(row=0, columnspan=5)
convert_title.configure(bg='#00FA9A')
combobox1 = ttk.Combobox(convert_title, value=list_currency, width=5)
combobox1.grid(row=1, column=1)
combobox2 = ttk.Combobox(convert_title, value=list_currency, width=5)
combobox2.grid(row=1, column=3)
text_get = Entry(convert_title)
text_get.grid(row=1, column=0)
text1 = Label(convert_title, text="to", bg='#00FA9A')
text1.grid(row=1, column=2)
result = Label(convert_title, text="Result", bg='#00FA9A')
result.grid(row=2, column=1)
button_convert = Button(convert_title, text="Convert", command=lambda: click_button("Convert"))
button_convert.grid(row=2, column=0, padx=10, pady=10)
graph_title = LabelFrame(text="กราฟแสดงค่าเงิน(โปรดเลือกหน่วยก่อนเลือกแสดงค่าเงิน)")
graph_title.grid(row=3, columnspan=5)
graph_title.configure(bg='#00BFFF')
button_last_week = Button(graph_title, text="Last week", command=lambda: click_button("Last week"))
button_last_week.grid(row=4, column=0, padx=10)
button_last_month = Button(graph_title, text="Last month", command=lambda: click_button("Last month"))
button_last_month.grid(row=4, column=1, padx=10)
button_last_year = Button(graph_title, text="Last year", command=lambda: click_button("Last year"))
button_last_year.grid(row=4, column=2, padx=10)
button_last_3_year = Button(graph_title, text="Last 3 year", command=lambda: click_button("Last 3 year"))
button_last_3_year.grid(row=5, column=0, padx=10)
button_last_5_year = Button(graph_title, text="Last 5 year", command=lambda: click_button("Last 5 year"))
button_last_5_year.grid(row=5, column=1, padx=10)
button_last_10_year = Button(graph_title, text="Last 10 year", command=lambda: click_button("Last 10 year"))
button_last_10_year.grid(row=5, column=2, padx=10)

main_window.mainloop()





