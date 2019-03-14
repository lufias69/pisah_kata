import re
kunci_jawaban = "selamat datang pada rumah kami"
jawaban = "sselamattdadatang di rumahhh kami"
def pisahKata(kunci_jawaban, jawaban):
    kunci_jawaban_split = kunci_jawaban.split()
    jawaban_split       = jawaban.split()
    n_jawaban = []
    for kj in kunci_jawaban_split:
        for key, j in enumerate(jawaban_split):
            if re.search(kj, j):
                start = re.search(kj, j).start()
                end   = re.search(kj, j).end()
                if start != 0 and end != len(j):
                    j_ = [x for x in j]
                    j_[start] = " "+j_[start]
                    
                    j_[end] = " "+j_[end-1]
                    #print(j_)
                    #print(end)
                    j = "".join(j_)
                    jawaban_split[key]=j
                    #print(j)
                
                elif start != 0 and end == len(j):
                    j_ = [x for x in j]
                    j_[start] = " "+j_[start]
                    
                    #j_[end] = " "+j_[end-1]
                    #print(j_)
                    #print(end)
                    j = "".join(j_)
                    jawaban_split[key]=j
                    #print(j)
                    #pass
                elif start == 0 and end != len(j):
                    j_ = [x for x in j]
                    j_[start] = " "+j_[start]
                    
                    j_[end] = " "+j_[end-1]
                    #print(j_)
                    #print(end)
                    j = "".join(j_)
                    jawaban_split[key]=j
                    #print(j)
                    
                else:
                    #print("ini else", j)
                    pass
            #n_jawaban.append(j)
    return " ".join(jawaban_split)

pisahKata(kunci_jawaban, jawaban)
