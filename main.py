import pre_deal as rc
import sub_variable as sv
import check_it as cc
import  requests
import xlrd

varsub_method = {
    0:'进行变量代换',
    1:'不进行变量代换'
}
match_method = {
    0:'LCS',
    1:'Levenshtein',
    2:'LCS-nlogn'
}
# ('../test_code/测试题/A0.c++.txt', '../test_code/测试题/B0.c++.txt', False, [], 1, 1, 0.88)
compare_method = {
    0:'LCS',
    1:'Levenshtein',
    2:'hungarain',
    3:'dinic',
}
#

def do_check(code1:str,code2:str,is_sub:bool,Filter:list,
             match_key:int,compare_key:int,parms:float):

    if is_sub:
        code1,code2 = sv.sub_var_main(code1,code2)
    else:
        code1,code2 = rc.format_code_main(code1),rc.format_code_main(code2)

    if compare_key == 0 or compare_key == 1:
        similar_matrix = cc.get_similarMatrix(
                code_1=code1,code_2=code2,is_ad=False,parms=parms,match_method=match_key)
    else:
        similar_matrix = cc.get_similarMatrix(
                code_1=code1,code_2=code2,is_ad=True, parms=parms,match_method=match_key)

    if compare_key==0:
        check_rate = cc.lcs_matrix_optimize(matrix=similar_matrix)
    elif compare_key==2:
        check_rate = cc.hungarain_matrix(ad_matrix=similar_matrix,row=len(code1),column=len(code2))
    elif compare_key==1:
        check_rate = cc.levenshtein_matrix(matrix=similar_matrix)
    else:
        check_rate = cc.dinic(matrix_ad=similar_matrix,row=len(code1),column=len(code2))
    check_rate*=100

    print('查重比例：%.2f'%check_rate)

if __name__ == '__main__':

    """
    do_check(
        code1_path = code1_path,
        code2_path = code2_path,
        is_sub = isVar_sub,
        Filter = Filter,
        match_key = match_key,
        compare_key = compare_key,
        parms = parms
    )
    """
   



    '''
    for i in range[0:126]:
        use_name=table.cell_value(i,0);
        use_add=table.cell_value(i,1);
        code_path = "https://raw.githubusercontent.com/"+use_add[18:]+"/"+code1+code[0:9]+"/111"
     print(code1_path1)
    '''
    #网页直接读入
'''code1_path1 = "https://raw.githubusercontent.com/031702221/wangzhe/master/map";
    code2_path1 = "https://raw.githubusercontent.com/031702221/wangzhe/master/hero";
    test = requests.get(code1_path1)
    code1 = test.text
    test = requests.get(code2_path1)
    code2 = test.text
'''
 #文件读入方法
code1_path = "./test_code/A0.c++.txt"
code2_path = "./test_code/B1.c++.txt"

with open(code1_path, 'r') as test:
      code1 = test.read();
with open(code2_path, 'r') as test1:
      code2 = test1.read();
do_check(
        code1,
        code2,
        is_sub=True,
        Filter=[1, 1.5, 1.5],
        match_key=2,
        compare_key=3,
        parms=0.9
    )