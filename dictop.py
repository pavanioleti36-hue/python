myd= {"id":169,"name":"pavani","branch":"cse","section":3 }
use_myd={
    k:v.upper()
    for k, v in myd.items()
    if isinstance(v,str)
}
print(use_myd)