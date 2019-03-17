import re
kunci_jawaban = "selamat datang pada rumah kami"
jawaban = "sselamattdadatang di rumahhh kami"
def pisahKata(kunci_jawaban, jawaban):
    d_index = []
    b_index = []
    
    for i in S_kunci_jawaban:
        index_replace = [(m.start(0)) for m in re.finditer(i,jawaban)]
        d_index += index_replace
    
        index_replace = [(m.end(0)) for m in re.finditer(i,jawaban)]
        b_index += index_replace
    jawaban_list = [x for x in jawaban]
    for d, b in zip(d_index, b_index):
        #print(d,b)
        jawaban_list[d]= " "+jawaban_list[d]
        jawaban_list[b-1]=jawaban_list[b-1]+" "

    jawaban_list = re.sub(r"\s+", " ","".join(jawaban_list).rstrip().strip().lstrip())
    return jawaban_list

pisahKata(kunci_jawaban, jawaban)
