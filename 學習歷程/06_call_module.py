# 載入內建的 sys 模組並取得資訊
import sys
# import module_geometry as geometry 移動到資料夾後改用下面寫法
from module import module_geometry as geometry #from 目錄
print(sys.platform)
print(sys.maxsize)

# 建立 geometyr 模組，載入使用
# result = geometry.distance(1,1,5,5)
# print(result)

# result = geometry.slope(1,2,5,6)
# print(result)

# 調整搜尋模組的路徑
# sys.path.append("modules")
# import module_geometry as geometry #最好還是放在最上面，用 from 的方式
# print(sys.path)

result = geometry.slope(1,2,5,6)
print(result)