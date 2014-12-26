'''
Created on Dec 25, 2014

@author: mmagdy
'''
import codecs

from eventUtils import getTokens
def evaluate(collFolder,k):
    evalres = []
    for j in range(k):
        
        fn = collFolder+str(j)+'.txt'
        f = codecs.open(fn, encoding='utf-8')
        ftext = f.read()
        text =  getTokens(ftext)
        if 'shoot' in text or 'shooter' in text or 'shooting' in text:
            if 'fsu' in text:
                evalres.append(1)
            elif 'florida' in text and 'state' in text and 'university' in text:
                evalres.append(1)
            else:
                evalres.append(0)
        else:
            evalres.append(0)
        f.close()
    return evalres
if __name__ == '__main__':
    for i in range(3):
        #i=0
        collFiles = '/Users/mmagdy/Dropbox/FC results/500/crawler-without ?/event-'+str(i)+'/event-webpages/'
        #collFiles = '/Users/mmagdy/Dropbox/FC results/500/crawler-without ?/base-'+str(i)+'/base-webpages/'
        res = evaluate(collFiles,500)
        f = open(collFiles+'evaluationRes_Words-?.txt','w')
        f.write('\n'.join([str(r) for r in res]))
        f.close()
        print sum(res)