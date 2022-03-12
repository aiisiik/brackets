# "Success"  =>  ")())())"
ti=input().upper()
to=""
for a in ti:
    if ti.count(a)==1:
        to+="("
    else:
        to+=")"
print(to)
