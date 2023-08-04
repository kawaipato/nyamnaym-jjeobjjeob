import pandas as pd

Y_2009 = pd.read_csv('2009년 건강검진조사.csv',low_memory = False)
Y_2009_col = Y_2009[['age','sex','HE_LDL_drct','HE_HDL_st2','HE_insulin','HE_glu','HE_BMI','HE_wt','HE_wc','HE_chol','HE_TG']]
Y_2009_col.to_csv('Y_2009_col.csv')

Y_2010 = pd.read_csv('2010년 건강검진조사.csv',low_memory = False)
Y_2010_col = Y_2010[['age','sex','HE_LDL_drct','HE_HDL_st2','HE_insulin','HE_glu','HE_BMI','HE_wt','HE_wc','HE_chol','HE_TG']]
Y_2010_col.to_csv('Y_2010_col.csv')