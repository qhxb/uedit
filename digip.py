import os,re

def dig(domain,targetfile):
    ip=os.popen('dig '+domain).readlines()
    try:
        s=ip.index(';; ANSWER SECTION:\n')
        e=ip.index('\n',s)
        fi=open(targetfile,'a+')
        for i in range(e-s-2):
            try:
                ips=re.findall(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b",ip[s+2+i])[0]
                fi.writelines(ips+'\r')
            except:
                print('dig error')
        fi.close()
    except:
        print(domain+' error')
def digscan(sourcefile,targetfile):
    fo=open(sourcefile,'r')
    for i in fo.readlines():
        print(i)
        dig(i.strip(),targetfile)


digscan('sourcedomain','targetip')
