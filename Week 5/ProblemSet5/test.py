
def insertNewlines(text, lineLength):
    if len(text) > 0:
        if len(text) <= lineLength: return text
        if text[lineLength-1] == ' ':
            return text[:lineLength] + '\n' + insertNewlines(text[lineLength:], lineLength)
        if len(text) > lineLength and ' ' in text[lineLength:]:
            x = text.index(' ', lineLength)
        else:
            revText = text[::-1]
            if ' ' in revText:
                x = revText.index(' ')
                x = len(text) - x
                return text[:x] + '\n' + text[x:]
            return text
        return text[:x] + '\n' + insertNewlines(text[x+1:], lineLength)
    else:
        return
"""

def insertNewlines(text, lineLength):
    if len(text)>0:
        if len(text) > lineLength

    return 
"""
print(insertNewlines('fksd xmzeqa hft zlide jmvqa kfjebqyt qumgb tjoyqad auhgec soygz kodfx bqyo ixbjzoeh txclse gdrhe fysjr ismnvl mxfitrhs auqz rnvhiua bpwjz ybvwoh ngyo vajs icu cvldxpgi rako tuyn zpmdcfky ynx guahncj zoiexvg vnr akychtwu nuwykcb vjcqtpk selxy bfcgh mldqsipv nhb sez iuof cgqoszj cih gvrmhbn mhyautkb cyj ibejvz nycqlji', 33))
print(insertNewlines('Nuh-uh! We let users vote on comments and display them by number of votes. Everyone knows that makes it impossible for a few persistent voices to dominate the discussion.', 20))
print(insertNewlines('Random text to wrap again.', 5))
print(insertNewlines('rtim xzare gxzas fogijv cqhvmtij cezmo nsoxbjeh njrsfmc sadwof tfw qvp kchmr mne yfuz opg rav mxfzpwjt dhfs tgqxif brljdz ter lng tsja ueoki zgean zjenfgrh kdybhcmo nlw odbwyn asjl cibgpxt', 48))
print(insertNewlines('While I expect new intellectual adventures ahead, nothing will compare to the exhilaration of the world-changing accomplishments that we produced together.', 15))
print(insertNewlines('adnqfgj muq djtw vshtw mgkp ckfwl grdwlknt dgus fxksvot ecvkwbfj tkxlmzve obavelf xpb xmb omkbpueq iafvbgp lbncrph glekbi xcvr driu scxij tkvsmdjo anobqflj bpshqv rnayigq rzfo wnaoqsp bkqage ophnqv mxeugvzt wbvgu sav', 46))
