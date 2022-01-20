def find_break_points(processed_small, Sn_ex, processed_big, n_ex):
    #D.sort_values("abspos", inplace = True)

    sub_processed_big = processed_big[processed_big["id"].isin(processed_small["id"])]


    strata_list = sorted([b for b in Sn_ex if Sn_ex[b]!=0])

    N = sum([n_ex[b] for b in strata_list])
    print(N)
    print(strata_list)

    Kuiper_function = sum([(sub_processed_big[b]*Sn_ex[b]-processed_small[b]*n_ex[b])*(n_ex[b])/(Sn_ex[b]*(n_ex[b]-Sn_ex[b])) for b in strata_list])
    Kuiper_function = Kuiper_function/N
    #     for b in strata_list[1:]:
#         print(b)
#         Kuiper_function = Kuiper_function+(new_df_N[b]*Sn[b]-new_df_S[b]*n[b])*n[b]/(Sn[b]*(n[b]-Sn[b]))
    print(Kuiper_function.head())

    mx = max(Kuiper_function)
    mn = min(Kuiper_function)
    amx = Kuiper_function.idxmax()
    print(mn, mx)
    if abs(mx)>abs(mn):
        t = amx
    amn = Kuiper_function.idxmin()
    if abs(mx)<=abs(mn):
        t = amn

    return Kuiper_function,mx,mn,amx,amn, t 
