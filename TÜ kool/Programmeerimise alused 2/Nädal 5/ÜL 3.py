import pandas as pd

df = pd.DataFrame()


def raamatukogud(f_sisend):
    f_open = pd.read_csv(f_sisend, delimiter=';', index_col=" ")
    taiendus = taienda_tabelit(f_open)
    uus_f_nimi = f_sisend.replace(".csv", "_uus.csv")
    taiendus.to_csv(uus_f_nimi, sep=';', encoding='utf-8')


def taienda_tabelit(pandas_dataframe):
    pandas_dataframe.pop("2012")
    pandas_dataframe["Keskmine"] = pandas_dataframe.mean(axis=1)

    return pandas_dataframe


#taienda_tabelit("test")

raamatukogud("raamatukogud.csv")