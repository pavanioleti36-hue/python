<<<<<<< HEAD
myd= {"id":169,"name":"pavani","branch":"cse","section":3 }
use_myd={
    k:v.upper()
    for k, v in myd.items()
    if isinstance(v,str)
}
=======
myd= {"id":169,"name":"pavani","branch":"cse","section":3 }
use_myd={
    k:v.upper()
    for k, v in myd.items()
    if isinstance(v,str)
}
>>>>>>> cc9c058bde5fd6ced8fb6651372cb99cdb3da7a2
print(use_myd)