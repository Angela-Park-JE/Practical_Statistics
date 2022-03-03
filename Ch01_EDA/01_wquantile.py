# 가중 중간값 구하기

# wquantiles 라는 패키지가 !pip install로 안깔리길래 순망치한으로 직접 만들어본 함수인다.

def wquantile(dataframe, column_name, weight):
    # please write the column_name with ''
    import numpy as pd
    
    dataframe[column_name].sort_values()
    dataframe.reindex()
    
    cut = round((dataframe[column_name].count()) * weight)
    #cut = round((dataframe[column_name].count()) / weight)
    df = dataframe[cut:-cut]
    
    return np.median(df[column_name])   

# 결과는 틀렸다. 웨이트값을 직접 주는 것으로 (trim=0.1)을 차용하려고 했으나 원래 실습에서의 정답과 다른 답이 나왔다. 
# 틀린 이유는 sort하는 컬럼과 구하는 값이 같아서 문제에서 원하는 답이 안나왔던 것이다.
# 다시 짜보기로 했다. 

def wquant(dataframe, weight_column_name, value_column_name, weight):
    # please write the column_name with ''
    import numpy as pd
    
    dataframe[weight_column_name].sort_values()
    dataframe.reindex()
    
    cut = round((dataframe[weight_column_name].count()) * weight)
    #cut = round((dataframe[column_name].count()) / weight)
    df = dataframe[cut:-cut]
    
    return np.median(df[value_column_name])   

# 생각을 바꾸었다고 생각했는데 그게 아니었나보다 이전과 값이 같아서, 또 틀렸다.

# weight_column_name 의 문제이거나 dataframe을 df로 만드는 과정에 문제가 있을 지도 모르겠는데...
