def f(x):
    return x**2 - 4 * x + 3  # roots = 1, 3


def df_dx(x):
    return 2 * x - 4


def orta_nokta_metodu(f, x1, x2):
    if f(x1) * f(x2) == 0:
        print('Tahminlerinizden birisi denklem kokudur')
    elif f(x1) * f(x2) > 0:
        print('Girdiginiz aralikta tek sayida kok yoktur')
    else:
        xr_comp = x1
        iter = 0
        while True:
            xr = (x1 + x2) / 2
            iter += 1
            if abs(f(xr) - f(xr_comp)) < 0.0001:
                print('Kok bulundu: ', xr, 'iterasyon sayisi:',
                      iter, '(Orta nokta yontemi)')
                return xr, iter
            elif f(x1) * f(xr) < 0:
                x2 = xr
            else:
                x1 = xr
                xr_comp = xr


def x_eksenini_kesen_nokta_ile(f, x1, x2):
    if f(x1) > f(x2):
        x1, x2 = x2, x1
    if f(x1) * f(x2) == 0:
        print('Tahminlerinizden birisi denklem kokudur')
    elif f(x1) * f(x2) > 0:
        print('Girdiginiz aralikta tek sayida kok yoktur')
    else:
        x1_comp = x1
        iter = 0
        while True:
            x1 = (f(x1) * x2 - f(x2) * x1) / (f(x1) - f(x2))
            iter += 1
            if abs(f(x1) - f(x1_comp)) < 0.0001:
                print('Kok bulundu: ', x1, 'iterasyon sayisi:',
                      iter, '(X eksenini kesen nokta yontemi)')
                return x1, iter
            x1_comp = x1


def teget_yardimi_ile(f, f_prime, x):
    iter = 0
    if f(x) != 0:
        while abs(f(x) / f_prime(x)) >= 0.0001:
            iter += 1
            x -= f(x) / f_prime(x)
    print('Kok bulundu: ', x, 'iterasyon sayisi:',
          iter, '(Teget cizme yontemi)')

    return x, iter


def main():
    x1 = int(input('x1 degerini giriniz: '))
    x2 = int(input(
        'x2 degerini giriniz (Teget metodu icin baslangic noktasi sayilacaktir): '))
    orta_nokta_metodu(f, x1, x2)
    x_eksenini_kesen_nokta_ile(f, x1, x2)
    teget_yardimi_ile(f, df_dx, x2)


main()
