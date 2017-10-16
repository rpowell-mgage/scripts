import sys
s=sys.stdin.read().strip()
s=s.replace('\\"','"')
s=s.replace('\\/','/')
s=s.replace('\\n',"\n")
print s
