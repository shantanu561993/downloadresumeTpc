import wget
import sys
def foo():
    fin=open(sys.argv[1],'r')
    for line in fin:
        a,b=line.strip().rstrip('\n').split(',')
        c=b.strip('"')+'_'+a.strip('"')+'.pdf'
        makeurl='http://www.tpcuiet.com/resume_upload/cannot_find_it_haha/{}'.format(c)
        wget.download(makeurl)
if __name__ == '__main__':
    foo()
