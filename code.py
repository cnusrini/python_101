import pandas as pd
import icd
print(icd)
data = {"person_id":[1,1,1,2,2,3],
         "dx_1":["F11","E40","","F32","C77","G10"],
         "dx_2":["F1P","E400","","F322","C737",""]}
df = pd.DataFrame.from_dict(data)
print(df)
df1 = icd.long_to_short_transformation(df,"person_id",["dx_1","dx_2"])
print(df1)
