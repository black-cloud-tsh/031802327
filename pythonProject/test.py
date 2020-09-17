from main import simhash_similarity
def similarity():
    f = open('orig.txt', 'r', encoding='utf-8')
    text1 = f.read()
    similar = simhash_similarity(text1, text1)
    print("orig.txt 与 orig.txt 的相似度为：%.2f" % similar)
    f.close()

    f = open('orig_0.8_add.txt', 'r', encoding='utf-8')
    text2 = f.read()
    similar = simhash_similarity(text1, text2)
    print("orig.txt 与 orig_0.8_add.txt 的相似度为：%.2f" % similar)
    f.close()

    f = open('orig_0.8_del.txt', 'r', encoding='utf-8')
    text2 = f.read()
    similar = simhash_similarity(text1, text2)
    print("orig.txt 与 orig_0.8_del.txt 的相似度为：%.2f" % similar)
    f.close()

    f = open('orig_0.8_dis_1.txt', 'r', encoding='utf-8')
    text2 = f.read()
    similar = simhash_similarity(text1, text2)
    print("orig.txt 与 orig_0.8_dis_1.txt 的相似度为：%.2f" % similar)
    f.close()

    f = open('orig_0.8_dis_3.txt', 'r', encoding='utf-8')
    text2 = f.read()
    similar = simhash_similarity(text1, text2)
    print("orig.txt 与 orig_0.8_dis_3.txt 的相似度为：%.2f" % similar)
    f.close()

    f = open('orig_0.8_dis_7.txt', 'r', encoding='utf-8')
    text2 = f.read()
    similar = simhash_similarity(text1, text2)
    print("orig.txt 与 orig_0.8_dis_7.txt 的相似度为：%.2f" % similar)
    f.close()

    f = open('orig_0.8_dis_10.txt', 'r', encoding='utf-8')
    text2 = f.read()
    similar = simhash_similarity(text1, text2)
    print("orig.txt 与 orig_0.8_dis_10.txt 的相似度为：%.2f" % similar)
    f.close()

    f = open('orig_0.8_dis_15.txt', 'r', encoding='utf-8')
    text2 = f.read()
    similar = simhash_similarity(text1, text2)
    print("orig.txt 与 orig_0.8_dis_15.txt 的相似度为：%.2f" % similar)
    f.close()

    f = open('orig_0.8_mix.txt', 'r', encoding='utf-8')
    text2 = f.read()
    similar = simhash_similarity(text1, text2)
    print("orig.txt 与 orig_0.8_mix.txt 的相似度为：%.2f" % similar)
    f.close()

    f = open('orig_0.8_rep.txt', 'r', encoding='utf-8')
    text2 = f.read()
    similar = simhash_similarity(text1, text2)
    print("orig.txt 与 orig_0.8_rep.txt 的相似度为：%.2f" % similar)
    f.close()

    return 0


similarity()