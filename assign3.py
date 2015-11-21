import QSTK.qstkutil.qsdateutil as du
import QSTK.qstkutil.tsutil as tsu
import QSTK.qstkutil.DataAccess as da

import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import math


def simulate( startdate, enddate, ls_symbols, allocation):

    c_dataobj = da.DataAccess('Yahoo')
    ls_keys = ['open', 'high', 'low', 'close', 'volume', 'actual_close']
    ldf_data = c_dataobj.get_data(ldt_timestamps, ls_symbols, ls_keys)
    d_data = dict(zip(ls_keys, ldf_data)) #cria dicionario


    fechamento = d_data['close'].values #preco de fechamento
    fechamento_normalizado = fechamento / fechamento[0, :] #fechamento normalizado


    fechn = fechamento_normalizado.copy()
    tsu.returnize0(fechn)  #daily returns


    media_ret_port = np.sum(fechn * allocation, axis=1)


    print 'Average daily return of the total portfolio'
    port_avg = np.average(media_ret_port)
    print port_avg


    print'Standard deviation of daily returns of the total portfolio'
    port_std= np.std(media_ret_port)
    print port_std



    print 'Sharpe Ratio'
    sharpe = math.sqrt(252)*port_avg/port_std
    print sharpe

    print 'Cumulative Return'
    print np.cumprod(media_ret_port + 1)[-1]

    print math.pow(1+port_avg,252)




    return sharpe


def eh_alloc_valid(i,j,k,l):
    if (i+j+k+l)==10:
        return True



ls_symbols = ['AAPL','GLD','GOOG','XOM']
#ls_symbols =   ['C', 'GS', 'IBM', 'HNZ']
dt_start = dt.datetime(2011, 1, 1)
#dt_start = dt.datetime(2010, 12, 31)
dt_end = dt.datetime(2011, 12, 31)
dt_timeofday = dt.timedelta(hours=16)
ldt_timestamps = du.getNYSEdays(dt_start, dt_end, dt_timeofday)

allocation=[0.4,0.4,0.0,0.2]
'''
max_sharpe = 0.0
max_alloc = []

for i in range(0, 11):
    for j in range(0, 11):
        for k in range(0, 11):
            for l in range(0, 11):
                if eh_alloc_valid(i, j, k, l):
                    alloc = [float(i)/10, float(j)/10, float(k)/10, float(l)/10]
                    si= simulate(dt_start, dt_end, ls_symbols, alloc)
                    if si>max_sharpe:
                        max_sharpe = si
                        max_alloc = alloc

print max_alloc
print max_sharpe
'''
simulate(dt_start, dt_end, ls_symbols, allocation)





