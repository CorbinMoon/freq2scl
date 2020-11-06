import freq2scl
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('data.csv')
    f = df["freq"].to_numpy()
    v = df["amp"].to_numpy()

    f2scl = freq2scl.Freq2Scl()
    f2scl.calc_dis(f, v, n=100000)
    f2scl.write_to_scl('test1.scl')