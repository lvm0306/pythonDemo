from gensim.models import word2vec
import pymysql

with open('./people_seg.txt','r',encoding='utf-8') as f:
    word_dic=set(f.read().split(' '))
model=word2vec.Word2Vec.load('./1.txt')

def tobinary(wordlist):
    binarylist=[]
    zhengshu=0
    fushu=0
    zhengavg=0
    fuavg=0
    zhengc=0
    fuc=0
    for n in wordlist:
        if n>0:
            zhengshu+=n
            zhengc+=1
        else:
            fushu+=n
            fuc+=1
    zhengavg=zhengshu/zhengc

    fuavg=fushu/fuc

    for n in wordlist:
        if n>=zhengavg:
            binarylist.append(int(0))
            binarylist.append(int(1))
        elif n<=fuavg:
            binarylist.append(int(1))
            binarylist.append(int(0))
        else:
            binarylist.append(int(0))
            binarylist.append(int(0))
    return binarylist

# db=pymysql.connect(host='localhost',user='root',password='19941202',db='python',port=3306)
# cur=db.cursor()


try:
    for word in word_dic:
        v=tobinary(model.wv[word])
        print(v[0])
        sql_insert="""insert into word_binary(word,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13,v14,v15,v16,v17,v18,v19,v20,v21,v22,v23,v24,v25,v26,v27,v28,v29,v30,v31,v32,v33,v34,v35,v36,v37,v38,v39,v40,v41,v42,v43,v44,v45,v46,v47,v48,v49,v50,v51,v52,v53,v54,v55,v56,v57,v58,v59,v60,v61,v62,v63,v64,v65,v66,v67,v68,v69,v70,v71,v72,v73,v74,v75,v76,v77,v78,v79,v80,v81,v82,v83,v84,v85,v86,v87,v88,v89,v90,v91,v92,v93,v94,v95,v96,v97,v98,v99,v100) values (word,v[0],v[1],v[2],v[3],v[4],v[5],v[6],v[7],v[8],v[9],v[10],v[11],v[12],v[13],v[14],v[15],v[16],v[17],v[18],v[19],v[20],v[21],v[22],v[23],v[24],v[25],v[26],v[27],v[28],v[29],v[30],v[31],v[32],v[33],v[34],v[35],v[36],v[37],v[38],v[39],v[40],v[41],v[42],v[43],v[44],v[45],v[46],v[47],v[48],v[49],v[50],v[51],v[52],v[53],v[54],v[55],v[56],v[57],v[58],v[59],v[60],v[61],v[62],v[63],v[64],v[65],v[66],v[67],v[68],v[69],v[70],v[71],v[72],v[73],v[74],v[75],v[76],v[77],v[78],v[79],v[80],v[81],v[82],v[83],v[84],v[85],v[86],v[87],v[88],v[89],v[90],v[91],v[92],v[93],v[94],v[95],v[96],v[97],v[98],v[99])"""

        # cur.execute(sql_insert)
        # db.commit()
        # print(sql_insert)
        # cur.execute(sql_insert)
        # db.commit()
except Exception as e:
    # db.rollback()
    print(e)
finally:
    print()
    # db.close()

